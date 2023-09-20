from django.shortcuts import render, get_object_or_404
from galery.models import Photography

def index(request):
    photographs = Photography.objects.order_by("photo_date").filter(published=True)
    return render(request, 'galery/index.html', {'cards': photographs})

def image(request, photographs_id):
    photo = get_object_or_404(Photography, pk=photographs_id)
    return render(request, 'galery/image.html', {"photo": photo})

def search(request):
    photographs = Photography.objects.order_by("photo_date").filter(published=True)

    if "search" in request.GET:
        name_search = request.GET['search']
        
        if name_search:
            photographs = photographs.filter(name__icontains=name_search)

    return render (request, 'galery/search.html', {"cards": photographs})

