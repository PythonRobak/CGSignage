from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime

# Create your views here.

from webadminpanel.forms import LoginForm, AddUserForm, AddMediaForm, AddGroupForm
from webadminpanel.models import Media, User, Group


class LoginUserView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'webadminpanel/login.html', {'form': form})

    def post(self, request):

        form = LoginForm(request.POST)
        msg = "You have entered an invalid username!"
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                return render(request, 'webadminpanel/logged_in.html', {'form': form, 'msg': msg})

            else:

                msg = "You have entered an invalid password!"

        return render(request, 'webadminpanel/login.html', {'form': form, 'msg': msg})

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'webadminpanel/add-user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                msg = 'Password didnt match!'
                return render(request, 'webadminpanel/add-user.html', {'form': form, 'msg': msg})


            u = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1']

            )

            return redirect('users')

        return render(request, 'webadminpanel/logged_in.html', {'form': form})

class LoggedInView(View):
    def get(self, request):
        return redirect('logged-in')

class UsersView(View):
    def get(self, request):
        users = User.objects.all().order_by('last_name')
        ctx = {
            'users': users
        }
        return render(request, 'webadminpanel/users.html', ctx)


class MediaView(View):
    def get(self, request):
        media = Media.objects.all()
        ctx = {
            'media': media
        }
        return render(request, 'webadminpanel/media.html', ctx)


class AddMediaView(View):
    def get(self, request):
        form = AddMediaForm()
        return render(request, 'webadminpanel/add-media.html', {'form': form})

    def post(self, request):
        form = AddMediaForm(request.POST, request.FILES or None)
        logged_user = request.user
        print("*"*50)
        print(f"User id is: {logged_user.id}")
        user = User.objects.get(pk=logged_user.id)

        if form.is_valid():
            print("add-media form validated")


            try:
                media = Media()
                media.name = form.cleaned_data['name']
                media.file = form.cleaned_data['file']
                media.duration = form.cleaned_data['duration']
                media.added_by = user
                media.save()


                return redirect('media')

            except Exception:
                return HttpResponse("Something went wrong!")

        else:
            print("add-media form not validated!")
            print("Błąd formularza:")
            print(form.errors)
        return render(request, "webadminpanel/media.html", {'form': form})


class EditMediaView(View):
    def get(self, request, media_id):
        media = Media.objects.get(pk=media_id)
        form = AddMediaForm(initial={
            'name': media.name,
            'file': media.filename,
            'duration': media.duration,
        })
        return render(request, 'webadminpanel/edit-media.html', {'form': form})


    def post(self, request, media_id):
        form = AddMediaForm(request.POST, request.FILES or None)

        if form.is_valid():
            print("edit-media form validated")

            try:
                media = Media.objects.get(pk=media_id)
                media.name = form.cleaned_data['name']
                media.file = form.cleaned_data['file']
                media.duration = form.cleaned_data['duration']
                media.last_edited = datetime.now()
                media.save()

                return redirect('media')

            except Exception:
                return HttpResponse("Something went wrong!")

        else:
            print("edit-media form not validated!")
            print("Błąd formularza:")
            print(form.errors)
        return render(request, "webadminpanel/media.html", {'form': form})


class DeleteMediaView(View):
    def get(self, request, media_id):
        media = Media.objects.get(pk=media_id)
        media.delete()
        return redirect('media')


class GroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        ctx = {
            'groups': groups
        }
        return render(request, 'webadminpanel/group.html', ctx)


class AddGroupView(View):
    def get(self, request):
        form = AddGroupForm()
        return render(request, 'webadminpanel/add-group.html', {'form': form})

    def post(self, request):
        form = AddGroupForm(request.POST)
        logged_user = request.user
        print("*"*50)
        print(f"User id is: {logged_user.id}")
        user = User.objects.get(pk=logged_user.id)

        if form.is_valid():
            print("add-group form validated")


            try:
                group = Group()
                group.name = form.cleaned_data['name']
                group.description = form.cleaned_data['description']
                group.added_by = user
                group.save()


                return redirect('group')

            except Exception:
                return HttpResponse("Something went wrong!")

        else:
            print("add-group form not validated!")
            print("Błąd formularza:")
            print(form.errors)
        return render(request, "webadminpanel/group.html", {'form': form})


class EditGroupView(View):
    def get(self, request, group_id):
        group = Group.objects.get(pk=group_id)
        form = AddGroupForm(initial={
            'name': group.name,
            'description': group.description,
        })
        return render(request, 'webadminpanel/edit-group.html', {'form': form})

    def post(self, request, group_id):
        form = AddMediaForm(request.POST)

        if form.is_valid():
            print("edit-group form validated")

            try:
                group = Group.objects.get(pk=group_id)
                group.name = form.cleaned_data['name']
                group.description = form.cleaned_data['description']
                group.last_edited = datetime.now()
                group.save()

                return redirect('group')

            except Exception:
                return HttpResponse("Something went wrong!")

        else:
            print("edit-group form not validated!")
            print("Błąd formularza:")
            print(form.errors)
        return render(request, "webadminpanel/group.html", {'form': form})