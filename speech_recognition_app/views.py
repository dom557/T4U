# speech_recognition_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .speech_recognition import recognize_speech

def speech_recognition_view(request):
    transcription = recognize_speech()
    return JsonResponse({"transcription": transcription})

def index(request):
    return render(request, 'index.html')

def features(request ):
    return render(request, 'features.html')