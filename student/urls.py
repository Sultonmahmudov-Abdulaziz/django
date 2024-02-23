from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:Category_id>', views.category, name='category'),
]