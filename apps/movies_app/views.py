from django.shortcuts import render, redirect
from .models import Movie, Actor
# Create your views here.
def index(request):
	context = {
		'movies': Movie.objects.all()
	}
	return render(request, 'movies_app/index.html', context)

def actor(request, id):
	context = {
		'actor': Actor.objects.get(id=id),
		'movies': Actor.objects.get(id=id).movies.all()
	}
	return render(request, 'movies_app/actor.html', context)

def movie(request, id):
	context = {
		'movie': Movie.objects.get(id=id),
		'actors': Movie.objects.get(id=id).actors.all()
	}
	return render(request, 'movies_app/movie.html', context)

def addmovie(request):
	if request.method=='POST':
		movie = Movie.objects.create(title=request.POST['title'])
		if 'id' in request.POST:
			movie.actors.add(Actor.objects.get(id=request.POST['id']))
		movie.save()
	return redirect('/')

def addactor(request):
	if request.method=='POST':
		actor = Actor.objects.create(name=request.POST['name'])
		if 'id' in request.POST:
			actor.movies.add(Movie.objects.get(id=request.POST['id']))
		actor.save()
	return redirect('/')
