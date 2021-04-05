from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('episodes/<int:question_id>/', views.episode, name='episode'),
    path('episodes/', views.episodes, name='episodes'),
    path('characters/<int:question_id>/', views.character, name='character'),
    path('characters/', views.characters, name='characters'),
    # path('episodes/<int:question_id>/', views.episode, name=''),
    # path('episodes/', views.episodes, name='episodes'),
]