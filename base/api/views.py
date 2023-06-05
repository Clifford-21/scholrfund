from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from applier.models import Learner, Address, Application
from .serializers import LearnerSerializer, AddressSerializer, ApplicationSerializer

import dropbox
from dropbox.exceptions import ApiError, AuthError
from django.http import JsonResponse


#------------- LEARNERS ---------------------#
@api_view(["GET", "POST"])
def show_learners(request):
    if request.method == "GET":
        learner = Learner.objects.all()
        serialized_data = LearnerSerializer(learner, many = True)
        return Response(serialized_data.data)
    else:
        # Dropbox authentication and backup
        ACCESS_TOKEN = 'sl.Bfowj2mqGb1zqxMkUlyKatKV0IhHjrIFEPeFeUtYpD1XLlRNgxhv9Z1tXqt6pPJw_FPxNchm08OfynjJ-atFp2f5qW9EvL2uFmVz-4aPMniLXH8TKKnJt14SG4cae2BZSEL6_f0p'
        BACKUP_FOLDER = '/backup'

        dbx = dropbox.Dropbox(ACCESS_TOKEN)
        dbx.users_get_current_account()


        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        physical_address = request.POST.get('physical_address')
        password = request.POST.get('password')
        cellphone = request.POST.get('Cellphone')
        id_copy = request.FILES.get('id_copy')
        matric_certificate = request.FILES.get('matric_certificate')
        proof_of_income = request.FILES.get('proof_of_income')

        # Upload files to Dropbox
        id_path = f'{BACKUP_FOLDER}/{first_name + last_name + "-"}'
        dbx.files_upload(id_copy.read(), id_path)

        matric_cert_path = f'{BACKUP_FOLDER}/{first_name + last_name}'
        dbx.files_upload(matric_certificate.read(), matric_cert_path)

        POI_path = f'{BACKUP_FOLDER}/{first_name + last_name}'
        dbx.files_upload(proof_of_income.read(), POI_path)

        data = request.data
        serialized_data = LearnerSerializer(data = data)
        #serialized_data.save()

        if serialized_data.is_valid():
            print("Data is valid")
            serialized_data.save()
            print("Data saved")
        return Response(serialized_data.data)
    
@api_view(["GET", "PUT", "DELETE"])
def show_learner(request, id):
    if request.method == "GET":
        learner = Learner.objects.get(id = id)
        serialized_data = LearnerSerializer(learner, many = False)

        return Response(serialized_data.data)
    elif request.method == "PUT":
        learner = Learner.objects.get(id = id)
        data = request.data
        serialized_data = LearnerSerializer(instance = learner, data= data)

        if serialized_data.is_valid():
            serialized_data.save()
        return Response(serialized_data.data)

    else:

        learner = Learner.objects.get(id = id)
        learner.delete()
        return HttpResponse("learner deleted")
    

#------ MAKE API RESTful, delete below ---------
    
"""
@api_view(["POST"])
def create_learner(request):
    serialized_data = LearnerSerializer(data = request.data)

    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)

    

@api_view(["GET"])
def show_learners(request):
    data = Learner.objects.all()
    serialized_data = LearnerSerializer(data, many = True)
    return Response(serialized_data.data)
   

@api_view(["GET"])
def learner_details(request, id):
    data = Learner.objects.get(pk = id)
    serialized_data = LearnerSerializer(data)
    return Response(serialized_data.data)
    

@api_view(["PUT"])
def edit_learner(request, id):
    project = Learner.objects.get(id = id)
    data = Learner.objects.get(id = id)
    serialized_data = LearnerSerializer(instance = project, data = request.data)

    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)


@api_view(["DELETE"])
def delete_learner(request, id):
    data = Learner.objects.get(pk = id)
    data.delete()
    return HttpResponse("Learner deleted")
"""