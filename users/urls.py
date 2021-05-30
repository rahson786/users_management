from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.users_form, name='user_insert'),                     # get and post req. for insert operation
    path('<int:id>/', views.users_form,name='user_update'),             # get and post req. for update operation
    path('delete/<int:id>/',views.user_delete,name='user_delete'),      # delete a particular user from database
    path('list/',views.users_list,name='users_list')                    # get req. to retrieve and display all records

]