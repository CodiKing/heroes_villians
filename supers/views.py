from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from supers.serializers import SupersSerializer
from .models import Supers
# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        queryset =Supers.objects.all()
        serializer = SupersSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def supers_detail(request,pk):
    if request.method == 'GET':
        super = get_object_or_404(super,pk=pk)
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == "PUT":
        super = get_object_or_404(super,pk=pk)
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

   
    