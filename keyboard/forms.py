from dataclasses import field, fields
from django import forms
from .models import *


class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = "__all__"
