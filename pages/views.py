from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings_display
from realtors.models import Agents
from listings.choices import bedrooms_choices,price_choices,state_choices
# Create your views here.
def index(request):
    listings = Listings_display.objects.order_by('-pub_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedrooms_choices': bedrooms_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request,'pages/index.html',context)
def about(request):
    realtors = Agents.objects.order_by('-hire_date')
    mvp_agent = Agents.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_agent': mvp_agent
    }
    return render(request,'pages/about.html',context)