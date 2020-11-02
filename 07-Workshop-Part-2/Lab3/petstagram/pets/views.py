from django.shortcuts import render, redirect
from .models import Pet, Like


# Create your views here.
def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/pet_list.html', context)

def show_pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet_detail.html', context)

def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet details', pk)
