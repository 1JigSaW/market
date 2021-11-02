from django.urls import path, include

from product import views

urlpatterns = [
	path('latest_products/', views.LatestProductsList.as_view()),
]