from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users

# Create your views here.

def users_list(request):
    context = {'users_list': Users.objects.all()}
    return render(request, "users/users_list.html", context)


def users_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UsersForm()
        else:
            users = Users.objects.get(pk=id)
            form = UsersForm(instance=users)
        return render(request, "users/users_form.html", {'form': form})
    else:
        if id == 0:
            form = UsersForm(request.POST)
        else:
            users = Users.objects.get(pk=id)
            form = UsersForm(request.POST,instance= users)
        if form.is_valid():
            form.save()
        return redirect('/users/list')


def user_delete(request,id):
    users = Users.objects.get(pk=id)
    users.delete()
    return redirect('/users/list')
