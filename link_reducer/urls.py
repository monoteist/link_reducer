from django.urls import path

from .views import create_short_link

app_name = 'link_reducer'

urlpatterns = [
    path("", create_short_link, name='create_short_link'),
]
