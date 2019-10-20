from django.shortcuts import render,get_object_or_404
from .models import Music

def alltracks(request):
    tracklist=Music.objects
    return render(request,'music/alltracks.html',{'tracks':tracklist})

def track(request,track_id):
    soundtrack=get_object_or_404(Music, pk=track_id)
    return render(request,'music/play',{'track':soundtrack})