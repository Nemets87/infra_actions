from django.urls import path

from infra_project.infra_app import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second_page', views.second_page, name='second_page'),

]
