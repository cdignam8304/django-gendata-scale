"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "main" # used for creating custom urls, so don't have to hard code urls

urlpatterns = [
    path("", views.homepage, name="homepage"),
    # path("contacts_update/", views.contacts_update, name="contacts_update"),
    path("generic_update/<schema>/", views.generic_update, name="generic_update"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"), # we use logout_request as their is a django method called logout that we already imported!
    path("login/", views.login_request, name="login"), # use login_request for same reason as above
    path("profile/<username>/", views.get_user_profile, name="username"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)