from django.urls import path
from . import views


urlpatterns = [
    path('', views.show, name='welcome'),  # TODO: Change <-this to welcome view or Register View for Auth Users
    path('edit/<str:room>/', views.edit, name='editable'),  # TODO: either this room does not belong to you or does
    path('room/<str:room>/', views.show, name='showroom'),  # TODO: render code or give nice 404
    path('save', views.save, name='save'),  # TODO: Think good way of safely (from author) saving Room Code
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
]