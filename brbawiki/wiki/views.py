from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import requests
import json
import importlib

from .forms import SearchBar

# Auxiliary functions

def array_to_string(array):
    string = ""
    if not isinstance(array, type(list())):
        return array + "."
    for index in range(len(array)):
            if index + 1 != len(array):
                print(array[index])
                string += array[index] + ", "
            else:
                print(array[index])
                string += array[index] + "."
    
    return string

# Create your views here.



api_url = 'https://tarea-1-breaking-bad.herokuapp.com/api/'

def character_search(request):
    search_string = request.POST['search_string'].replace(" ","+")
    offset = 0
    search_url = f'{api_url}characters?name={search_string}&limit=10&offset={offset}'

    response_size = 10
    search_results = []
    while response_size == 10:
        response = requests.get(search_url).json()
        for character in response:
            print(character)
            character['occupation'] = array_to_string(character['occupation'])
            character['category'] = array_to_string(character['category'])
        search_results += response
        response_size = len(response)
        offset += 10
        search_url = f'{api_url}characters?name={search_string}&limit=10&offset={offset}'
        
    context = {'search_results': search_results}
    return render(request, 'wiki/character_search.html', context)

def index(request):
    url_brba = f'{api_url}episodes?series=Breaking+Bad'
    url_bcs = f'{api_url}episodes?series=Better+Call+Saul'
    brba_episodes = requests.get(url_brba).json()
    brba_seasons = []
    bcs_episodes = requests.get(url_bcs).json()
    bcs_seasons = []


    for episode in brba_episodes:
        if episode['season'] not in brba_seasons:
            brba_seasons.append(episode['season'])
    for episode in bcs_episodes:
        if episode['season'] not in bcs_seasons:
            bcs_seasons.append(episode['season'])
    context = {
        "brba_episodes": brba_episodes,
        "brba_seasons": brba_seasons,
        "bcs_episodes": bcs_episodes,
        "bcs_seasons": bcs_seasons
        }
    return render(request, 'wiki/index.html', context)

def brba_seasons(request, question_id):
    url = f'{api_url}episodes?series=Breaking+Bad'
    brba_episodes = requests.get(url).json()
    season_episodes = []
    for episode in brba_episodes:
        if episode['season'] == str(question_id):
            season_episodes.append(episode)
    
    context = {
        "season_episodes": season_episodes,
        "series": "Breaking Bad",
        "season": question_id
        }
    return render(request, 'wiki/season.html', context)

def bcs_seasons(request, question_id):
    url = f'{api_url}episodes?series=Better+Call+Saul'
    bcs_episodes = requests.get(url).json()
    season_episodes = []
    for episode in bcs_episodes:

        if episode['season'] == str(question_id):
            season_episodes.append(episode)

    context = {
        "season_episodes": season_episodes,
        "series": "Better Call Saul",
        "season": question_id
        }
    return render(request, 'wiki/season.html', context)


def episode(request, question_id):
    url_episode = f'{api_url}episodes/{question_id}/'
    episode = requests.get(url_episode).json()[0]
    
    episode['air_date'] = episode['air_date'][8:10] + "-"+ episode['air_date'][5:7] + "-" +episode['air_date'][:4] 

    character_names = episode['characters']
    for index in range(len(character_names)):
        url_character = f'{api_url}characters?name={character_names[index].replace(" ","+")}' 
        character_id = requests.get(url_character).json()[0]['char_id']
        episode['characters'][index] = [character_names[index], character_id]


    context = {"episode": episode}
    return render(request, 'wiki/episode.html', context)

def character(request, question_id):
    url = f'{api_url}characters/{question_id}/'
    response = requests.get(url).json()[0]
    print("." + response["name"].replace(" ","+") + ".")
    url_quotes = f'{api_url}quote?author={response["name"].replace(" ","+")}'
    quotes = requests.get(url_quotes).json()
    
    response['occupation'] = array_to_string(response['occupation'])
    response['category'] = array_to_string(response['category'])
    
    context = {
        "character": response,
        "quotes": quotes
        }
    return render(request, 'wiki/character.html', context)

def characters(request):
    url = f'{api_url}characters/'
    response = requests.get(url).json()
    context = {"characters": response}
    return render(request, 'wiki/characters.html', context)

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