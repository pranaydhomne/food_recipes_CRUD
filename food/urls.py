from django.contrib import admin
from django.urls import path ,include
from food.views import *
from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic.base import RedirectView

urlpatterns = [
    # path(r'', RedirectView.as_view(url='food/')),

    path("",food, name='food'),
    path("recipe/",recipe,name='contact'),
    path('delete_recipe/<id>/',delete_recipe,name="delete_recipe"),
    path('update_recipe/<int:id>/',update_recipe,name="update_recipe"),
    path('search/',search,name="search")



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)