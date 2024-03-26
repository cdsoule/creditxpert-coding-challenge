from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from challenge1.models import Shape, ColorScheme
from challenge1.serializers import ShapeSerializer, ColorSchemeSerilizer

def index(request):
    colors = ColorScheme.objects.all()
    shapes = Shape.objects.all()
    context = {"colors": colors, "shapes": shapes}
    return render(request, template_name='challenge1.html', context=context)

class ShapeEndpoint(APIView):
    def get(self, request, id):
        data = Shape.objects.get(id=id)
        serializer = ShapeSerializer(data)

        return JsonResponse(serializer.data)
    

    def post(self, request):
        serializer = ShapeSerializer(data=request.data)
        if serializer.is_valid():
            Shape.objects.create(**serializer.data)
        else:
            return JsonResponse({"message": "invalid request"})

        return JsonResponse(serializer.data)

class ColorEndpoint(APIView):

    def get(self, request, id):
        data = ColorScheme.objects.get(id=id)
        serializer = ColorSchemeSerilizer(data)

        return JsonResponse(serializer.data)
    

    def post(self, request):
        serializer = ColorSchemeSerilizer(data=request.data)
        if serializer.is_valid():
            ColorScheme.objects.create(**serializer.data)
        else:
            return JsonResponse({"message": "invalid request"})

        return JsonResponse(serializer.data)