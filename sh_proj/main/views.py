from django.shortcuts import render
from .models import Lesson
# Create your views here.

def main_render(request):
    lessons = Lesson.objects.all().order_by('day_of_week', 'time')
    return render(request, 'main/main.html', {'lessons': lessons})