from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ParagraphSerializer, SavedSerializer
from .models import Paragraph, Saved

def index(request):
    context = { }
    return render(request, "index.html", context)

class ParagraphView(viewsets.ModelViewSet):
    serializer_class = ParagraphSerializer
    queryset = Paragraph.objects.all()

class SavedView(viewsets.ModelViewSet):
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()