from django.urls import path

import infra_project.infra_app

app_name = 'infra_app'

urlpatterns = {
    path('', infra_project.infra_app.views.index, name='index'),
    path('second_page',
         infra_project.infra_app.views.second_page, name='second_page'),

}
