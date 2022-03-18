from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super_types
from super_types.serializers import Super_typesSerializer


@api_view(['GET,PUT,POST,DELETE'])
def super_type_list(request):
    if request.method == 'GET':
        queryset =Super_types.objects.all()
        serializer = Super_typesSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Super_typesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@api_view(['GET'])
def super_types_detail(request,id):
    try:
        super = Super_types.objects.get(id=id)
        serializer = Super_typesSerializer(super)
        return Response(serializer.data)

    except Super_types.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)