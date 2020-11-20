from django.urls import path

from .views import *    # * - import all


urlpatterns = [
    path('', posts_list)
]

