from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import prices_choices, bedroom_choices, county_choices
from .models import Listing

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
    'county_choices': county_choices,
    'price_choices': prices_choices,
    'bedroom_choices': bedroom_choices,
    }

    return render(request, 'listings/search.html', context)
