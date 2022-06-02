from django.urls import path
from . import views

app_name = 'keyboard'

urlpatterns = [
    path('keyboard/', views.KeyboardView.as_view(), name='type-list'),
    path('keycaps/', views.KeycapView.as_view(), name='type-list'),
    path('switches/', views.SwitcheView.as_view(), name='type-list'),
    path('keyboard_form/', views.KeyboardFormView),
]
