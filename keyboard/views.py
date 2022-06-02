from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from .models import Keyboard, Switche, Keycap
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.list import ListView
from .forms import KeyboardForm


class KeyboardView(generic.ListView):
    template_name = 'keyboard/keyboard.html'
    model = Keyboard

    def get_queryset(self):
        return Keyboard.objects.all()


class KeycapView(generic.ListView):
    template_name = "keyboard/keycap.html"
    model = Keycap

    def get_queryset(self):
        return Keycap.objects.all()


class SwitcheView(generic.ListView):
    template_name = "keyboard/switche_detail.html"
    model = Switche

    def get_queryset(self):
        return Switche.objects.all()


def KeyboardFormView(request):
    form = KeyboardForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'keyboard/keyboardform.html', context)
