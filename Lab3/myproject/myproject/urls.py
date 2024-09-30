"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp.views import my_async_view, safe_view, non_cache_view, async_view_using_sync_function

urlpatterns = [
    path('', my_async_view, name='my_async_view'),
    path('safe/', safe_view, name='safe_view'),
    path('non-cache/', non_cache_view, name='non_cache_view'),
    path('async-sync/', async_view_using_sync_function, name='async_sync_view'),
]