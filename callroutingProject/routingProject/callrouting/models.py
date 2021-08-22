from django.db import models


class Customer(models.Model):
    business_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)


class ContractedCopier(models.Model):
    model_name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    # service_history = models.CharField(max_length=50)
    customers = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)


class ServiceHistory(models.Model):
    work_performed = models.CharField(max_length=150, null=True, default=None)
    copier = models.ForeignKey(ContractedCopier, null=True, default=None, on_delete=models.CASCADE)


class Manager(models.Model):
    manager_name = models.CharField(max_length=50)
    manager_email = models.EmailField(null=True)
    territory_region = models.CharField(max_length=50)


class FieldTechnician(models.Model):
    technician_name = models.CharField(max_length=50)
    technician_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)


class CopierTraining(models.Model):
    model_name = models.CharField(max_length=50)
    technician = models.ForeignKey(FieldTechnician, on_delete=models.CASCADE)


class ServiceRequest(models.Model):
    problem_description = models.CharField(max_length=150)
    special_instructions = models.CharField(max_length=150, null=True, default=None, blank=True)
    escalate_service = models.CharField(max_length=150, null=True, default=None, blank=True)
    contracted_copier = models.ForeignKey(ContractedCopier, on_delete=models.CASCADE)
    # assigned_technician = models.ForeignKey(FieldTechnician, on_delete=models.CASCADE, default=None, null=True,
    # blank=True)
    # manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, default=None, blank=True)


class ServiceResponse(models.Model):
    ETA = models.DateTimeField(null=True, default=None, blank=True)
    dispatch_time = models.DateTimeField(null=True, default=None, blank=True)
    arrive_time = models.DateTimeField(null=True, default=None, blank=True)
    completion_time = models.DateTimeField(null=True, default=None, blank=True)
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
