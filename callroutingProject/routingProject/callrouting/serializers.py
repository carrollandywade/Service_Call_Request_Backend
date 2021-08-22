from rest_framework import serializers
from .models import Customer, ContractedCopier, Manager, FieldTechnician, CopierTraining, ServiceRequest,\
    ServiceResponse, ServiceHistory


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'business_name', 'address', 'contact_name', 'contact_phone', 'contact_email']


class ContractedCopierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractedCopier
        fields = ['id', 'model_name', 'serial_number', 'customers']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'manager_name', 'manager_email', 'territory_region']


class FieldTechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldTechnician
        fields = ['id', 'technician_name', 'technician_manager']


class CopierTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopierTraining
        fields = ['id', 'model_name', 'technician']


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['id', 'problem_description', 'special_instructions', 'escalate_service', 'contracted_copier']


class ServiceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceResponse
        fields = ['id', 'ETA', 'dispatch_time', 'arrive_time', 'completion_time', 'service_request']


class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistory
        fields = ['id', 'work_performed', 'copier']
