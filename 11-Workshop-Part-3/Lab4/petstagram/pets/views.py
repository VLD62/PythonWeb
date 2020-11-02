from django.shortcuts import render, redirect

from .forms.comment_form import CommentForm
from .forms.pet_form import PetForm
from .models import Like, Pet, Comment


# Create your views here.
def list_pets(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pets/pet_list.html', context)

def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        pet.likes_count = pet.like_set.count()
        context = {
            'pet': pet,
            'form': CommentForm(),
        }
        return render(request, 'pets/pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text = form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)
        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pets/pet_detail.html', context)

def persist_pet(request, pet, template_name):
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'pets/{template_name}.html', context)
    else:
        form = PetForm(
            request.POST,
            instance=pet
        )
        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'pets/{template_name}.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit')


def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')

def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(request, 'pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet details or comment', pk)

