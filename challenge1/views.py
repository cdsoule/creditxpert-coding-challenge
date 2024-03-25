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
        name = request.data.get('name')
        fa_class = request.data.get('fa_class')
        Shape.objects.create(name=name, fa_class=fa_class)

        return JsonResponse({"name": name, "fa_class": fa_class})

class ColorEndpoint(APIView):

    def get(self, request, id):
        data = ColorScheme.objects.get(id=id)
        serializer = ColorSchemeSerilizer(data)

        return JsonResponse(serializer.data)
    

    def post(self, request):
        color1 = request.data['color1']
        color2 = request.data['color2']
        color3 = request.data['color3']
        color4 = request.data['color4']
        ColorScheme.objects.create(color1=color1, color2=color2, color3=color3, color4=color4)

        return JsonResponse({"color1": color1, 
                             "color2": color2, 
                             "color3": color3, 
                             "color4": color4})