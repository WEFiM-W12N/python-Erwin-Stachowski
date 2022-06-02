from django.contrib import admin

from .models import Keyboard, Switche, Keycap

admin.site.register(Keycap)
admin.site.register(Switche)
admin.site.register(Keyboard)
