from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chore, Supply
from .forms import CommentForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chores_index(request):
  chores=Chore.objects.all()
  return render(request, 'chores/index.html', {'chores':chores})

def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  id_list = chore.supplies.all().values_list('id')
  supplies_chores_doesnt_have = Supply.objects.exclude(id__in=id_list)
  comment_form = CommentForm()
  return render(request, 'chores/detail.html', {
    'chore': chore, 'comment_form': comment_form,
    'supplies':supplies_chores_doesnt_have
    })

class ChoreCreate(CreateView):
  model = Chore
  fields = ['title', 'creator', 'assignedTo', 'details' ]
  success_url = '/chores/'

class ChoreUpdate(UpdateView):
  model = Chore
  fields = ['assignedTo', 'details' ]

class ChoreDelete(DeleteView):
  model = Chore
  success_url = '/chores/'

def add_comment(request, chore_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.chore_id = chore_id
    new_comment.save()
  return redirect('detail', chore_id=chore_id)

class SupplyList(ListView):
  model = Supply

class SupplyDetail(DetailView):
  model = Supply

class SupplyCreate(CreateView):
  model = Supply
  fields = '__all__'

class SupplyUpdate(UpdateView):
  model = Supply
  fields = ['name']

class SupplyDelete(DeleteView):
  model = Supply
  success_url = '/supplies/'

def assoc_supply(request, chore_id, supply_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Chore.objects.get(id=chore_id).supplies.add(supply_id)
  return redirect('detail', chore_id=chore_id)

def unassoc_supply(request, chore_id, supply_id):
  chore = Chore.objects.get(id=chore_id)
  chore.supplies.remove(supply_id)
  return redirect('detail', chore_id=chore_id)

