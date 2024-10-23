from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

def names(request):
    dict={"name":"ahmed"}
    js=json.dumps(dict)
    return HttpResponse (js,content_type='application/json')


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


# Get all items or create a new one (POST/GET)
@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Item.objects.all()
        print(items[1].price)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get, update or delete an item by ID (GET/PUT/DELETE)
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        print("uyem",item)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
