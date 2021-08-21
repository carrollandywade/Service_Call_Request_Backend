from rest_framework import serializers
from .models import (Customer, ContractedCopier, Manager, FieldTechnician, CopierTraining, ServiceRequest)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'business_name', 'address', 'contact_name', 'contact_phone', 'contact_email']


class ContractedCopierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractedCopier
        fields = ['id', 'model_name', 'serial_number', 'service_history', 'customers']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['manager_name', 'manager_email', 'territory_region']


class FieldTechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldTechnician
        fields = ['technician_name', 'technician_manager']


class CopierTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopierTraining
        fields = ['model_name', 'technician']


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['ETA', 'dispatch_time', 'arrive_time', 'problem_description', 'special_instructions',
                  'escalate_service', 'contracted_copier', 'assigned_technician', 'manager']
