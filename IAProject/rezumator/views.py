from django.shortcuts import render
from django.http import HttpResponse
from . import modul_2


# Create your views here.
def index(request) :
    return render(request, 'rezumator/index.html')

def processed(request):
    if request.method == 'POST':
        text = request.POST['text']
        procent = request.POST['procent']
        if text == "":
            return render(request, 'rezumator/process.html',{'text': "Introduceti un text!", 'procent': procent})
        return render(request, 'rezumator/process.html', {'text': modul_2.reconstruire_text(text,procent), 'procent': procent})
    else:
        return render(request, 'rezumator/process.html', {'text': "Trebuie sa introduceti textul in formular!"})