from django.urls import path
from . import views


urlpatterns = [
    path("", views.user_list_view),
    path("<str:email>/", views.user_detail_view),
    path("id/<int:id>/", views.user_detail_view),
]
