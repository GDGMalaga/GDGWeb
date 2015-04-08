from django.shortcuts import render


def home(request):
	"""
	Displays the homepage.
	"""
	return render(request, 'home.html')
