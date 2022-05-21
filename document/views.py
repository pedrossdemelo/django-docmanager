from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Doc, Company
from .serializers import DocumentSerializer, CompanySerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer
    multiple_lookup_fields = ("name", "id")

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            if field in self.kwargs:
                filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        return obj


class CompanyDocumentsList(generics.ListAPIView):
    serializer_class = DocumentSerializer
    multiple_lookup_fields = ("name", "id")

    def get_queryset(self):
        filter = {}
        for field in self.multiple_lookup_fields:
            if field in self.kwargs:
                related_field = f"company__{field}"
                filter[related_field] = self.kwargs[field]

        return Doc.objects.filter(**filter, deleted=False)


class DocumentList(generics.ListCreateAPIView):
    queryset = Doc.objects.filter(deleted=False)
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.filter(deleted=False)
    serializer_class = DocumentSerializer
    lookup_field = "id"


company_list_view = CompanyList.as_view()
company_detail_view = CompanyDetail.as_view()
company_documents_list_view = CompanyDocumentsList.as_view()
document_list_view = DocumentList.as_view()
document_detail_view = DocumentDetail.as_view()
