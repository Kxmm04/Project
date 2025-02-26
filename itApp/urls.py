from django.contrib import admin
from django.urls import path
from itApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('showMassage', views.showMessages, name='showMessages'),
    path('computerList/', views.computerList, name='computerList'),
    path('computerOne/<id>', views.computerOne, name='computerOne'), 
    path('accessoriesList',views.accessoriesList,name='accessoriesList'),
    path('accessoriesOne/<id>', views.accessoriesOne, name='accessoriesOne'),
    path('storageList', views.storageList, name='storageList'),
    path('storageOne/<id>', views.storageOne, name='storageOne'),
]