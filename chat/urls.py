from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('answer/', views.answer, name='answer'),
]
