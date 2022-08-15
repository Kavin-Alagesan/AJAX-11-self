from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('work/',views.work,name='work'),
    path('create_task/',views.create_task,name='create_task'),
    path('post/<int:id>/',views.post,name='post'),
    path('edit_and_update/<int:id>/',views.edit_and_update,name='edit_and_update'),
    path('delete_task/<int:id>/',views.delete_task,name='delete_task'),
    path('delete_task/',views.delete_task,name='delete_task'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout,name='logout'),
]
