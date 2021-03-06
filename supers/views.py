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
        super_type = request.query_params.get('super_type_id')
        print(super_type)
        queryset = Supers.objects.all()
        if super_type:
            queryset = queryset.filter(super__type=super_type)
        serializer = SupersSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT','DELETE'])
def supers_detail(request, pk):
    if request.method == 'GET':
        super = get_object_or_404(super, pk=pk)
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == "PUT":
        super = get_object_or_404(super, pk=pk)
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        super = get_object_or_404(super, pk=pk)
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
    