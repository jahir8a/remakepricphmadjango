from django.shortcuts import render
from .models import Slider
# Create your views here.
def post_list(request):
    sliders = Slider.objects.all()
    return render(request, 'slider/slider_list.html', {'sliders': sliders})