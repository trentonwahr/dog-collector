from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('dogs/', views.dog_index, name='dog-index'),
  path('dogs/<int:dog_id>/', views.dog_detail, name='dog-detail'),
  path('dogs/create/', views.DogCreate.as_view(), name='dog-create'),
  path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog-update'),
  path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog-delete'),
  path('dogs/<int:dog_id>/add-nap/', views.add_nap, name='add-nap'),
  path('dogs/<int:dog_id>/assoc-treat/<int:treat_id>/', views.assoc_treat, name='assoc-treat'),
  path('treats/create/', views.TreatCreate.as_view(), name='treat-create'),
  path('treats/<int:pk>/', views.TreatDetail.as_view(), name='treat-detail'),
  path('treats/', views.TreatList.as_view(), name='treat-index'),
  path('treats/<int:pk>/update/', views.TreatUpdate.as_view(), name='treat-update'),
  path('treats/<int:pk>/delete/', views.TreatDelete.as_view(), name='treat-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]