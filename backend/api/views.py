import json
from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product
from product.serializers import ProductSerializer
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

# ---------- Normal Django API View ---------------
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}

#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title"]) 
#     return JsonResponse(data)


# ---------------- DRF API VIEW ---------------------
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    return Response(data)


@api_view(['POST'])
def api_send(request, *args, **kwargs):
    # Get JSON from request
    data = request.data

    # Pass into serializer for serialization
    # converting object into JSON
    serializer = ProductSerializer(data=data)

    # serializer validates input against defined fields.
    if serializer.is_valid(raise_exception=True):

        # Creation of model instance/object
        # saves to the db if new else updates
        # instance = serializer.save()
        # print(instance)

        # API output JSON-ready format
        return Response(serializer.data)