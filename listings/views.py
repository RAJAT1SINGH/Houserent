from django.shortcuts import get_object_or_404,render
from .models import Listings_display
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import bedrooms_choices,price_choices,state_choices

def index(request):
    listings = Listings_display.objects.order_by('-pub_date').filter(is_published=True)
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {'listings': paged_listing}
    return render(request,'listings/listings.html',context)
def listing(request,listing_id):
    listing = get_object_or_404(Listings_display,pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request,'listings/listing.html',context)
def search(request):
    querySet_list = Listings_display.objects.order_by('-pub_date')
    #Keywords for search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querySet_list = querySet_list.filter(description__icontains=keywords)
    #City for search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
        
            querySet_list = querySet_list.filter(city__iexact=city)
    #State for search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querySet_list = querySet_list.filter(state__iexact=state)
        #Bedrooms for search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querySet_list = querySet_list.filter(bedrooms__iexact=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querySet_list = querySet_list.filter(price__gte=price)
    context = {
        'bedrooms_choices': bedrooms_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': querySet_list ,
        'values': request.GET

    }
    return render(request,'listings/search.html', context)