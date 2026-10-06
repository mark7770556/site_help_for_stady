from django.shortcuts import render
from .models import Institution,City


def test_database(request):
    institutions = Institution.objects.all()

    return render(request,"main/test.html",{
        "institutions":institutions
    }) 


def home(request):
    search = request.GET.get("search","")

    if search :
        cities = City.objects.filter(name__icontains = search)
    else:
        cities = City.objects.all()

    return render(request,"main/home.html",{
        "cities":cities,
        "search":search
    })

def city_institution(request,city_id):
    search = request.GET.get("search","")
    institution_type = request.GET.get("type","")

    institutions = Institution.objects.filter(city_id=city_id)

    if search:
        institutions = institutions.filter(name__icontains=search)
    if institution_type:
        institutions= institutions.filter(type__icontains=institution_type)

    return render(request, "main/city.html", {
        "institutions": institutions,
        "search":search,
        "institution_type":institution_type
    })

def institution_detail(request,institution_id):
    institution = Institution.objects.get(id=institution_id)

    return render(request, "main/institution.html", {
        "institution": institution
    })


