from django.shortcuts import render
from FormDaftar_app_1174043.forms import NewUserForm
from django.views.generic import CreateView
# Create your views here.

def index(request):
    return render(request, 'FormDaftar_1174043/index_1174043.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'FormDaftar_1174043/users_1174043.html',{'form':form})