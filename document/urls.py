from django.urls import path
from . import views


urlpatterns = [
    path("docs/", views.document_list_view),
    path("docs/<str:id>/", views.document_detail_view),
    path("companies/", views.company_list_view),
    path("companies/<str:name>/", views.company_detail_view),
    path("companies/<str:name>/docs/", views.company_documents_list_view),
]

