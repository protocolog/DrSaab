from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from DiseaseApi.prediction import disease_prediction
from DiseaseApi.models import PatientDetails
from django import forms

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "POST":
        symptoms = request.POST.get("symptoms")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        patientdetails = PatientDetails(name=name, phone=phone, email=email, symptoms=symptoms)
        patientdetails.save()
        disease = disease_prediction(symptoms)
        return JsonResponse({'Predicted Disease':disease})
    if request.method == "GET":
        return HttpResponse('Welcome msg')


