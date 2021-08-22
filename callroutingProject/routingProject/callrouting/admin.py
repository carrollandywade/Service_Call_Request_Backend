from django.contrib import admin
from .models import (Customer, ContractedCopier, Manager, FieldTechnician, CopierTraining, ServiceRequest,
                     ServiceResponse)


# Register your models here.

admin.site.register(Customer)
admin.site.register(ContractedCopier)
admin.site.register(Manager)
admin.site.register(FieldTechnician)
admin.site.register(CopierTraining)
admin.site.register(ServiceRequest)
admin.site.register(ServiceResponse)
