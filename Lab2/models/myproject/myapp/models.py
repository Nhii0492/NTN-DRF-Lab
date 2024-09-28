from django.db import models

from django.utils.text import slugify


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.instrument})"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return f"{self.name} by {self.artist}"


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

    # Set the default shirt size to "M" (Medium)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default="M")

    @property
    def full_name(self):
        """Returns the person's full name."""
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        """Returns the URL for the person instance."""
        from django.urls import reverse
        return reverse('person_detail', args=[str(self.id)])

    def __str__(self):
        """Returns a string representation of the person."""
        return self.full_name


class Runner(models.Model):
    class MedalType(models.TextChoices):
        GOLD = "GOLD", "Gold"
        SILVER = "SILVER", "Silver"
        BRONZE = "BRONZE", "Bronze"

    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

    def __str__(self):
        return f"{self.name} - {self.medal if self.medal else 'No Medal'}"


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.model_name} ({self.year})"


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping, related_name='pizzas')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.person.full_name} in {self.group.name}"


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, **kwargs):
        # Generate slug from the name
        self.slug = slugify(self.name)

        # Prevent saving for a specific blog name
        if self.name == "Yoko Ono's blog":
            return  # Prevent saving

        # Ensure slug is included in update_fields if name is being updated
        if (update_fields := kwargs.get("update_fields")) is not None and "name" in update_fields:
            kwargs["update_fields"] = {"slug"}.union(update_fields)

        # Call the superclass save method
        super().save(**kwargs)

    def __str__(self):
        return f"{self.name} - {self.tagline[:20]}..."  # Show first 20 chars of tagline


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ["name"]


class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False


class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass


class OtherModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Base(models.Model):
    m2m = models.ManyToManyField(
        OtherModel,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True

class ChildA(Base):
    description = models.TextField()

    def __str__(self):
        return f"ChildA: {self.description}"

class ChildB(Base):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"ChildB: {self.title}"

# E
#
# xample usage (as shown previously)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class ParentModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']  # Default ordering for ParentModel


class ChildModel(ParentModel):
    # Define additional fields or methods specific to ChildModel here
    description = models.TextField()

    class Meta:
        # Remove parent's ordering effect
        ordering = []  # No default ordering for ChildModel

