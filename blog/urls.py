from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .import views

import blog.views as bv

urlpatterns = [
    path('', views.index),
    path('article_page/<int:article_id>/',views.article_page,name='article_page'),
    path('edit/<int:article_id>',views.edit_page,name='edit_page'),
    path('edit/action',views.edit_action,name='edit_action')
]