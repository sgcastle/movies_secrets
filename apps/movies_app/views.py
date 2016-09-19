from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,
	'movies_app/index.html')

def show(request):
	print (request.method)
	return render(request,
	'movies.app/show_users.html')
