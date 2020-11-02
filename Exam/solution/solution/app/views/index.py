from django.shortcuts import render
from app.models import Recipe


def index(request):
    if Recipe.objects.exists():
        recepies = Recipe.objects.all()
        context = {
            'recepies': recepies,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
