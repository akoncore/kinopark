from django.shortcuts import render,get_list_or_404
from .models import (User)
from .serializers import UserSerializer


def api(request):
    return render(request,'api.html')
