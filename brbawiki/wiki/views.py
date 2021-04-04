from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.

api_url = 'https://tarea-1-breaking-bad.herokuapp.com/api/'

def index(request):
    context = {'test_var':'TEST VARIABLE FROM CONTEXT'}
    return render(request, 'wiki/index.html', context)

def episode(request, question_id):
    url = f'{api_url}episodes/{question_id}/'
    response = requests.get(url).json()
    context = {"response": response}
    return render(request, 'wiki/episode.html', context)

def episodes(request):
    url = f'{api_url}episodes/'
    response = requests.get(url).json()
    context = {"episodes": response}
    return render(request, 'wiki/episodes.html', context)

def character(request, question_id):
    url = f'{api_url}characters/'
    response = requests.get(url).json()
    context = {"character": response}
    return render(request, 'wiki/character.html', context)

def characters(request):
    url = f'{api_url}characters/'
    response = requests.get(url).json()
    context = {"characters": response}
    return render(request, 'wiki/characters.html', context)
