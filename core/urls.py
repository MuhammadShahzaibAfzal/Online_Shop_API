from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('products/',views.ProductView.as_view()),
    path('products/<str:pk>/',views.SingleProductView.as_view())
]