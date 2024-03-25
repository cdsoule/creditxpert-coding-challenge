from django.urls import path
from challenge1.views import index, ShapeEndpoint, ColorEndpoint

urlpatterns = [
    path('', index),
    path('shapes', ShapeEndpoint.as_view()),
    path('shapes/<int:id>', ShapeEndpoint.as_view()),
    path('colors', ColorEndpoint.as_view()),
    path('colors/<int:id>', ColorEndpoint.as_view()),
]