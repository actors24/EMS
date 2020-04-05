from django.urls import path

from manage.views import main, add_employee, confirm_add, delete,update,confirm_update

app_name = 'manage'

urlpatterns = [
    path('main/', main, name='main'),
    path('add/', add_employee, name='add'),
    path('confirm_add/', confirm_add, name='confirm_add'),
    path('delete/', delete, name='delete'),
    path('update/', update, name='update'),
    path('confirm_update/', confirm_update, name='confrim_update')
]
