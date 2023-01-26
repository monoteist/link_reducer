from django.urls import path

from .views import create_short_link, redirect_short_link, statistics
from link_reducer.api.views import CreateShortLinkAPI, StatisticsAPI

app_name = "link_reducer"

urlpatterns = [
    path("", create_short_link, name="create_short_link"),
    path("statistics/", statistics, name="statistics"),
    path("<str:shortened_link>/", redirect_short_link, name="redirect_short_link"),
    path("api/v1/create/", CreateShortLinkAPI.as_view(), name="create_short_link_api"),
    path("api/v1/statistics/", StatisticsAPI.as_view(), name="statistics_api"),
]
