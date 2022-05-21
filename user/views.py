from django.shortcuts import get_object_or_404
from rest_framework import generics
from document.models import Doc

from document.serializers import DocumentSerializer
from .models import User
from .serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    multiple_lookup_fields = ("email", "id")

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            if field in self.kwargs:
                print(field)
                filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        return obj


class UserDocumentsView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    multiple_lookup_fields = ("email", "id")

    def get_queryset(self):
        filter = {}
        for field in self.multiple_lookup_fields:
            if field in self.kwargs:
                related_field = f"created_by__{field}"
                filter[related_field] = self.kwargs[field]

        return Doc.objects.filter(**filter, deleted=False)

user_documents_view = UserDocumentsView.as_view()
user_list_view = UserView.as_view()
user_detail_view = UserDetailView.as_view()
