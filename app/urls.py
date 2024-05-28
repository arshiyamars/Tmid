from django.urls import path
from . import views #new

urlpatterns = [
    path('', views.product, name = 'product') ,#new
    path('login/',views.login, name="login"),
    path('form/',views.form, name="form"),

]