from rest_framework import viewsets
from clp_api.models.ClpEntity import ClpInformation
from clp_api.SerializerClp import ClpInformationSerializer
from django.shortcuts import render



def form(request):
    clp_information_object = ClpInformation.objects.last()  # Obtém o último objeto ClpInformation do banco de dados
    serialized_data = ClpInformationSerializer(clp_information_object).data  # Serializa o objeto para poder passar para o template
    return render(request, 'form.html', {'clp_information': serialized_data})

class ClpInformationViewSet(viewsets.ModelViewSet):
    queryset = ClpInformation.objects.all()
    serializer_class = ClpInformationSerializer