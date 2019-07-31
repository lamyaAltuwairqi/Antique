from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.urls import reverse
from .models import Category, Items
from .forms import UserForm, ProfileForm, LoginForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView
# Create your views here.



def index(request):
    if request.user.is_authenticated:
        items= Items.objects.filter(user = request.user)
    else:
        items= []
    data = {
        'items': items
    }
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    category =Category.objects.all()
    data = {
        'category':category
    }
    return render(request, 'category.html', data)

def register(request):
    userForm = UserForm()
    profileForm = ProfileForm()

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('login'))
    data = {'userForm':userForm, 'profileForm':profileForm}
    return render (request, 'register.html', data)
    
def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request,'user is not active')
            else:
                messages.error(request, 'invalid username or password')
    data = {'form': form}
    return render(request, 'login.html', data)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def add(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user=request.user

            if 'image' in request.FILES:
                item.image = request.FILES['image']
            item.save()
            messages.success(request, 'your Item have been added successfully')
            return HttpResponseRedirect(reverse('home'))
    
    data = {
        'form':form
    }
    return render(request, 'add.html', data)




def detail(request, pk):
    item = Items.objects.get(pk=pk)
    status=False
    if request.user ==item.user:
        status = True
    else:
        status = False

    data = {
        'item': item,
        'owner': status
    }
    return render(request, 'detail.html', data)

def catdetail(request, pk):
    bb = Category.objects.get(pk=pk)
    items = Items.objects.filter(category=bb)

    data = {
        'items':items,
    }
    return render(request, 'catdetail.html', data)

def delete_item(request, pk):
    items = get_object_or_404(Items, pk=pk)
    if items:
        items.delete()
    return HttpResponseRedirect(reverse('home'))

class ItemUpdate(UpdateView):
    model = Items
    fields = '__all__'
    template_name = 'ItemUpdate.html'