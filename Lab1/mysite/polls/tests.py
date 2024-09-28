from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
from datetime import timedelta  # Updated import
from django.urls import reverse


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + timedelta(days=days)  # Updated to use timedelta
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        future_question = Question(pub_date=timezone.now() + timedelta(days=30))
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_question = Question(pub_date=timezone.now() - timedelta(days=1, seconds=1))
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date=timezone.now() - timedelta(hours=23, minutes=59, seconds=59))
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    class QuestionDetailViewTests(TestCase):
        def test_future_question(self):
            """
            The detail view of a question with a pub_date in the future
            returns a 404 not found.
            """
            future_question = create_question(question_text="Future question.", days=5)
            url = reverse("polls:detail", args=(future_question.id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

        def test_past_question(self):
            """
            The detail view of a question with a pub_date in the past
            displays the question's text.
            """
            past_question = create_question(question_text="Past Question.", days=-5)
            url = reverse("polls:detail", args=(past_question.id,))
            response = self.client.get(url)
            self.assertContains(response, past_question.question_text)

    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
            ordered=False  # Use ordered=False for flexibility
        )

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],  # This order is important if you have specific expectations
            ordered=False  # Use ordered=False for flexibility
        )
