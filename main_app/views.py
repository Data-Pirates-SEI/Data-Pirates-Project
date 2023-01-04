from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chore, Supply
from .forms import CommentForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def chores_index(request):
  chores=Chore.objects.filter(user=request.user)
  return render(request, 'chores/index.html', {'chores':chores})

@login_required
def chores_detail(request, chore_id):
  chore = Chore.objects.get(id=chore_id)
  id_list = chore.supplies.all().values_list('id')
  supplies_chores_doesnt_have = Supply.objects.exclude(id__in=id_list)
  comment_form = CommentForm()
  return render(request, 'chores/detail.html', {
    'chore': chore, 'comment_form': comment_form,
    'supplies':supplies_chores_doesnt_have
    })

class ChoreCreate(LoginRequiredMixin, CreateView):
  model = Chore
  fields = ['title', 'creator', 'assignedTo', 'details' ]


  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  # success_url = '/chores/'

class ChoreUpdate(LoginRequiredMixin, UpdateView):
  model = Chore
  fields = ['assignedTo', 'details' ]

class ChoreDelete(LoginRequiredMixin, DeleteView):
  model = Chore
  success_url = '/chores/'

@login_required
def add_comment(request, chore_id, user_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.chore_id = chore_id
    new_comment.user_id = user_id
    new_comment.save()
  return redirect('detail', chore_id=chore_id)

class SupplyList(LoginRequiredMixin, ListView):
  model = Supply

class SupplyDetail(LoginRequiredMixin, DetailView):
  model = Supply

class SupplyCreate(LoginRequiredMixin, CreateView):
  model = Supply
  fields = '__all__'

class SupplyUpdate(LoginRequiredMixin, UpdateView):
  model = Supply
  fields = ['name']

class SupplyDelete(LoginRequiredMixin, DeleteView):
  model = Supply
  success_url = '/supplies/'

@login_required
def assoc_supply(request, chore_id, supply_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Chore.objects.get(id=chore_id).supplies.add(supply_id)
  return redirect('detail', chore_id=chore_id)

@login_required
def unassoc_supply(request, chore_id, supply_id):
  chore = Chore.objects.get(id=chore_id)
  chore.supplies.remove(supply_id)
  return redirect('detail', chore_id=chore_id)

def signup(request):
  error_message= ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)    
