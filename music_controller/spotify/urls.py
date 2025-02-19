from .views import *
from django.urls import path

urlpatterns = [
    path('get-auth-url',AuthURL.as_view()),
    path('redirect',spotify_callback),
    path('is-authenticated',isAuthenticated.as_view()),
    path('current-song',CurrentSong.as_view()),
    path('pause',PauseSong.as_view()),
    path('play',PlaySong.as_view()),
    path('skip',SkipSong.as_view()),
    path('get-playback-token', GetPlaybackToken.as_view()),
    path('api/lyrics', get_lyrics, name='get-lyrics'),
    ]
