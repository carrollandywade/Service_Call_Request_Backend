from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('customer/<int:pk>/copier/', views.ContractedCopierList.as_view()),
    path('customer/<int:fk>/copier/<int:pk>/', views.ContractedCopierDetail.as_view()),
    path('service_request/', views.ServiceRequestList.as_view()),
    path('copier/<int:fk>/service_request/', views.ServiceRequestDetail.as_view()),
    path('service_request/<int:fk>/service_response/', views.ServiceResponseDetail.as_view()),
    path('technician/', views.FieldTechnicianList.as_view()),
    path('technician/<int:pk>/', views.FieldTechnicianDetail.as_view()),
    path('copiertraining/', views.CopierTrainingList.as_view()),
    path('copiertraining/<int:pk>/', views.CopierTrainingDetail.as_view()),
    path('manager/', views.ManagerList.as_view()),
    path('manager/<int:pk>/', views.ManagerDetail.as_view()),
]
