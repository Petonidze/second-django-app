# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import application_user, notes
from .forms import UserCreateForm, UserUpdateForm, UserDeleteForm, NoteDeleteForm, NoteCreateForm, NoteUpdateForm, RegisterUserForm

# Create your views here.

def index(request):
    user_display = application_user.objects.all()
    notes_display = notes.objects.all().order_by("-date")[:20]
    return render(request, 'application/homePage.html', {"application_user":user_display, "notes":notes_display})

class UserUpdate(UpdateView):
    model = application_user
    form_class = UserUpdateForm
    template_name = "application/user_update_form.html"

    def form_valid(self, form):
        
        form.save()
        return redirect("/")

    def success_url(self):
        return redirect("/")


class UserDelete(DeleteView):
    model = application_user
    success_url = reverse_lazy('index')
    form_class = UserDeleteForm
    template_name = "application/user_delete_form.html"

    def form_valid(self, form):
        
        form.save()
        return redirect("/")

    def get_success_url(self):
        if self.success_url:
            return self.success_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")

class NoteCreate(CreateView):
    model = notes
    form_class = NoteCreateForm
    template_name = "application/note_form.html"

    def form_valid(self, form):
        
        form.save()
        return redirect("/add-note/")

    def success_url(self):
        return redirect("/add-note/")

class NoteUpdate(UpdateView):
    model = notes
    form_class = NoteUpdateForm
    template_name = "application/note_update_form.html"

    def form_valid(self, form):
       
        form.save()
        return redirect("/")

    def success_url(self):
        return redirect("/")


class NoteDelete(DeleteView):
    model = notes
    success_url = reverse_lazy('index')
    form_class = NoteDeleteForm
    template_name = "application/note_delete_form.html"

    def form_valid(self, form):
        
        form.save()
        return redirect("/")

    def get_success_url(self):
        if self.success_url:
            return self.success_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")

#---------------------------------------register-------------------------------------------

class RegisterUser(CreateView):
    model = application_user
    form_class = RegisterUserForm
    template_name = "application/user_register.html"
    def success_url(self):
        return redirect("/")

#---------------------------------------auth-----------------------------------------------

