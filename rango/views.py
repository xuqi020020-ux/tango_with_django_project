from django.shortcuts import render

def about(request):
    return render(request, 'rango/about.html', {'boldmessage': "Rango says here is the about page."})
