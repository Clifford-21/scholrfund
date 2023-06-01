from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from applier.models import Learner, Address, Application
from .serializers import LearnerSerializer, AddressSerializer, ApplicationSerializer


#------------- LEARNERS ---------------------#
@api_view(["GET", "POST"])
def show_learners(request):
    if request.method == "GET":
        learner = Learner.objects.all()
        serialized_data = LearnerSerializer(learner, many = True)
        return Response(serialized_data.data)
    else:
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