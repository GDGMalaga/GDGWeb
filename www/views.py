from django.shortcuts import render


def home(request):
	"""
	Displays the homepage.
	"""
	return render(request, 'home.html')

def calendario(request):
    '''
    Displays the calendar
    '''
    return render(request, 'calendario.html')
