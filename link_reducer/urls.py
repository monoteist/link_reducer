from django.urls import path

from .views import create_short_link, redirect_short_link

app_name = "link_reducer"

urlpatterns = [
    path("", create_short_link, name="create_short_link"),
    path("<str:shortened_link>/", redirect_short_link, name="redirect_short_link"),
]
