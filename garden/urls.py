from django.urls import path

from .views import CreateGardenView, GardenListView, GardenView

urlpatterns = [
	path('', GardenListView.as_view(), name='gardenlistview'),
	path('create',  CreateGardenView.as_view(), name='gardencreate'),
	path('<int:garden_id>/',  GardenView.as_view(), name='gardenview'),
]
