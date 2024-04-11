from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    ordering = '-created_at'  # Исправлено на "created_at", так как поле "name" отсутствует в модели
    template_name = 'news_list.html'  # Исправлено имя шаблона
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'



