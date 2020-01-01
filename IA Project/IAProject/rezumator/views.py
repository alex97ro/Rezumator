from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request) :
    return render(request, 'rezumator/index.html')

def processed(request):
    if request.method == 'POST':
        text = request.POST['text']
        procent = request.POST['procent']
        return render(request, 'rezumator/process.html', {'text': text, 'procent': procent})
    else:
        return render(request, 'rezumator/process.html', {'text': "Trebuie sa introduceti textul in formular!"})