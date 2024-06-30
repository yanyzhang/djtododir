from django.shortcuts import render, redirect
from .models import Todolistmdl
from .forms import TodolistForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    todo_items = Todolistmdl.objects.order_by('completed', 'date', 'time')
    form = TodolistForm()
    show_modal = request.session.pop('show_modal', False)  # Retrieve and clear show_modal flag
    context = {
        'todo_items': todo_items,
        'form': form,
        'show_modal': show_modal  # Pass show_modal to template
    }
    return render(request, 'lists/index.html', context)




@require_POST
def addItem(request):
    form=TodolistForm(request.POST)
    if form.is_valid():
        new_todo=Todolistmdl(text=form.cleaned_data['text'], date=form.cleaned_data['date'], time=form.cleaned_data['time'])
        new_todo.save()

    # print(request.POST['text'])
    return redirect('index')


def completedTask(request, todo_id):
    todo=Todolistmdl.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todolistmdl.objects.filter(completed=True).delete()
    return redirect('index')

@require_POST
def deleteAll(request):
    Todolistmdl.objects.all().delete()
    return redirect('index')

def showDeleteAllModal(request):
    request.session['show_modal'] = True
    return redirect('index')