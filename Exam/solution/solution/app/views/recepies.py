from django.shortcuts import render, redirect
from app.forms.recepies import RecipeForm, DeleteRecipeForm
from app.models import Recipe

def create_recepie(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)

def details_recepie(request, pk):
    recepie = Recipe.objects.get(pk=pk)
    ingredients_list = recepie.ingredients.split(',')
    context = {
        'recepie': recepie,
        'ingredients_list': ingredients_list,
        'form': RecipeForm(instance=recepie),
    }
    return render(request, 'details.html', context)

def edit_recepie(request, pk):
    recepie = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recepie': recepie,
            'form': RecipeForm(instance=recepie),
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recepie)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'recepie': recepie,
            'form': form,
        }
        return render(request, 'edit.html', context)

def delete_recepie(request, pk):
    recepie = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recepie': recepie,
            'form': DeleteRecipeForm(instance=recepie),
        }
        return render(request, 'delete.html', context)
    else:
        recepie.delete()
        return redirect('index')
