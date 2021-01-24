from django.urls import path
from . import views


urlpatterns = [
        path('', views.registerPage, name="register"),
        path('login/', views.loginPage, name="login"),
        path('logout/', views.logoutUser, name="logout"),
        path('home', views.home, name='home'),
        path('contact', views.contact, name='contact'),
        path('cost',views.cost,name='cost'),
        path('cart', views.cart, name='cart'),

]