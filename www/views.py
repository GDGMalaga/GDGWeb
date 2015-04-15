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
    return render(request, "calendario.html")

def grupos(request):
    '''
    Displays the groups
    '''
    return render(request, "grupos.html")

def accede(request):
    '''
    Displays the access
    '''
    return render(request,"accede.html")
