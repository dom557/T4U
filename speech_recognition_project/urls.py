"""
URL configuration for speech_recognition_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# speech_recognition_project/urls.py

from django.contrib import admin
from django.urls import path
from speech_recognition_app.views import speech_recognition_view, index , features

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # the feature page
    path('features/' , features, name='features'),
    path('recognize/', speech_recognition_view, name='recognize_speech'),
]
