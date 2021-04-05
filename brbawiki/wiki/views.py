from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.

api_url = 'https://tarea-1-breaking-bad.herokuapp.com/api/'

def index(request):
    url = f'{api_url}episodes/'
    response = requests.get(url).json()
    brba_episodes = []
    brba_seasons = []
    bcs_episodes = []
    bcs_seasons = []


    for episode in response:
        if episode['series'] == "Breaking Bad":
            brba_episodes.append(episode)
            if episode['season'] not in brba_seasons:
                brba_seasons.append(episode['season'])
        else:
            bcs_episodes.append(episode)
            if episode['season'] not in bcs_seasons:
                bcs_seasons.append(episode['season'])
    context = {
        "brba_episodes": brba_episodes,
        "brba_seasons": brba_seasons,
        "bcs_episodes": bcs_episodes,
        "bcs_seasons": bcs_seasons
        }
    return render(request, 'wiki/index.html', context)

def episode(request, question_id):
    url = f'{api_url}episodes/{question_id}/'
    response = requests.get(url).json()
    context = {"response": response}
    return render(request, 'wiki/episode.html', context)

def episodes(request):
    url = f'{api_url}episodes/'
    response = requests.get(url).json()
    brba_episodes = []
    bcs_episodes = []
    for episode in response:
        if episode['series'] == "Breaking Bad":
            brba_episodes.append(episode)
        else:
            bcs_episodes.append(episode)
    context = {"brba_episodes": brba_episodes, "bcs_episodes": bcs_episodes}
    return render(request, 'wiki/episodes.html', context)

def character(request, question_id):
    url = f'{api_url}characters/{question_id}/'
    print(url)
    response = requests.get(url).json()
    context = {"character": response}
    return render(request, 'wiki/character.html', context)

def characters(request):
    url = f'{api_url}characters/'
    response = requests.get(url).json()
    context = {"characters": response}
    return render(request, 'wiki/characters.html', context)
