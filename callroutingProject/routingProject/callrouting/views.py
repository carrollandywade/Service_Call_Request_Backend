from django.shortcuts import render
from .models import (Customer, ContractedCopier, Manager, FieldTechnician, CopierTraining, ServiceRequest)
from .serializers import (CustomerSerializer, ContractedCopierSerializer, ManagerSerializer, FieldTechnicianSerializer,
                          CopierTrainingSerializer, ServiceRequestSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CustomerList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
