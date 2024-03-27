from django.shortcuts import render

def colaborator(request):
    return render(request, "collaborator/collaborator.html")