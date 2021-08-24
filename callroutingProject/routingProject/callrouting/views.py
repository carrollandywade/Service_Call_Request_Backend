from .models import Customer, ContractedCopier, Manager, FieldTechnician, CopierTraining, ServiceRequest, \
    ServiceResponse, ServiceHistory
from .serializers import CustomerSerializer, ContractedCopierSerializer, ManagerSerializer, FieldTechnicianSerializer,\
    CopierTrainingSerializer, ServiceRequestSerializer, ServiceResponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import render


class CustomerList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    def get_Customer(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_Customer(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_Customer(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_Customer(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContractedCopierList(APIView):
    def get(self, request, pk):
        copier = ContractedCopier.objects.filter(customers_id=pk)
        serializer = ContractedCopierSerializer(copier, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContractedCopierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractedCopierDetail(APIView):
    def get_ContractedCopier(self, fk):
        try:
            return ContractedCopier.objects.filter(customers_id=fk)
        except ContractedCopier.DoesNotExist:
            raise Http404

    def get(self, request, fk, pk):
        copier = ContractedCopier.objects.get(customers_id=fk, id=pk)
        serializer = ContractedCopierSerializer(copier)
        return Response(serializer.data)

    def delete(self, request, pk, fk):
        copier = ContractedCopier.objects.get(customers_id=fk, id=pk)
        copier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceRequestList(APIView):
    def get(self, request):
        servicerequest = ServiceRequest.objects.all()
        serializer = ServiceRequestSerializer(servicerequest, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceRequestDetail(APIView):
    def get_ServiceRequest(self, fk):
        try:
            return ServiceRequest.objects.filter(contracted_copier=fk)
        except ServiceRequest.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        copier = ServiceRequest.objects.get(contracted_copier=fk)
        serializer = ServiceRequestSerializer(copier)
        return Response(serializer.data)

    def delete(self, request, fk):
        copier = ServiceRequest.objects.get(contracted_copier=fk)
        copier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceResponseDetail(APIView):
    def get_ServiceResponse(self, fk):
        try:
            return ServiceResponse.objects.filter(service_request_id=fk)
        except ServiceResponse.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        servresponse = ServiceResponse.objects.get(service_request_id=fk)
        serializer = ServiceResponseSerializer(servresponse)
        return Response(serializer.data)

    def post(self, request, fk):
        serializer = ServiceResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, fk):
        servresponse = ServiceResponse.objects.get(service_request_id=fk)
        serializer = ServiceResponseSerializer(servresponse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fk):
        servresponse = ServiceResponse.objects.get(service_request_id=fk)
        servresponse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FieldTechnicianList(APIView):
    def get(self, request):
        technician = FieldTechnician.objects.all()
        serializer = FieldTechnicianSerializer(technician, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FieldTechnicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FieldTechnicianDetail(APIView):
    def get_FieldTechnician(self, pk):
        try:
            return FieldTechnician.objects.get(pk=pk)
        except FieldTechnician.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        technician = self.get_FieldTechnician(pk)
        serializer = FieldTechnicianSerializer(technician)
        return Response(serializer.data)

    def put(self, request, pk):
        technician = self.get_FieldTechnician(pk)
        serializer = FieldTechnicianSerializer(technician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        technician = self.get_FieldTechnician(pk)
        technician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CopierTrainingList(APIView):
    def get(self, request):
        training = CopierTraining.objects.all()
        serializer = CopierTrainingSerializer(training, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CopierTrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CopierTrainingDetail(APIView):
    def get_CopierTraining(self, pk):
        try:
            return CopierTraining.objects.get(pk=pk)
        except CopierTraining.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        training = self.get_CopierTraining(pk)
        serializer = CopierTrainingSerializer(training)
        return Response(serializer.data)

    def put(self, request, pk):
        training = self.get_CopierTraining(pk)
        serializer = CopierTrainingSerializer(training, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        training = self.get_CopierTraining(pk)
        training.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagerList(APIView):
    def get(self, request):
        training = Manager.objects.all()
        serializer = ManagerSerializer(training, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerDetail(APIView):
    def get_Manager(self, pk):
        try:
            return Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        boss = self.get_Manager(pk)
        serializer = ManagerSerializer(boss)
        return Response(serializer.data)

    def put(self, request, pk):
        boss = self.get_Manager(pk)
        serializer = ManagerSerializer(boss, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        boss = self.get_Manager(pk)
        boss.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

