from django.urls import path
from challenge2.views import AntMoverView

urlpatterns = [
    path('', AntMoverView.as_view())
]