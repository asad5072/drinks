from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserilizer
from django.shortcuts import render

def drink_list(request):
    #get all the drinks
    # serialize them
    # return json
    drinks = Drink.objects.all()
    serializer = Drinkserilizer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)
    
def index(request):
    return render(request, 'index.html')