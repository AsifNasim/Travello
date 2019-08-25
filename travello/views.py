from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):

    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City that never sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer =  False

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.img = 'destination_2.jpg'
    # dest2.desc = 'The city of Nizams'
    # dest2.price= 800
    # dest2.offer =  True

    # dest3 = Destination()
    # dest3.name = 'New delhi'
    # dest3.img = 'destination_3.jpg'
    # dest3.desc = 'The city of Beautiful people'
    # dest3.price= 900
    # dest3.offer =  True

    # dests = [dest1, dest2, dest3]
    
    # return render(request,'index.html', {'dest1':dest1,'dest2':dest2,'dest3':dest3})