from rest_framework import generics
from .models import Doc, Company
from .serializers import DocumentSerializer, CompanySerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer
    lookup_field = "name"


class CompanyDocumentsList(generics.ListAPIView):
    serializer_class = DocumentSerializer
    lookup_field = "name"

    def get_queryset(self):
        return Doc.objects.filter(company__name=self.kwargs["name"], deleted=False)


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
