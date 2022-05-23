from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
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


class BadRequestException(APIException):
    status_code = 400
    default_detail = "Bad Request"
    default_code = "bad_request"


class UnauthorizedException(APIException):
    status_code = 401
    default_detail = "Unauthorized"
    default_code = "unauthorized"

class DummyLoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        password = self.request.query_params.get("password") or None
        if not password:
            raise BadRequestException("Missing password")
        email = self.kwargs["email"];
        obj = get_object_or_404(queryset, email=email)
        if obj.password == password:
            return obj
        raise UnauthorizedException("Incorrect password")


dummy_login_view = DummyLoginView.as_view()
user_documents_view = UserDocumentsView.as_view()
user_list_view = UserView.as_view()
user_detail_view = UserDetailView.as_view()
