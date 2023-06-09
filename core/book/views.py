from django.db.models import F, FloatField
from django.shortcuts import render, HttpResponse
from .models import Book
from django.db.models.functions import Coalesce



# index sehinde yazilanlar
def index_view(request):
    context={
        "text":"Salam necesen?",
        "new":Book.objects.all()
        # "text":Book.objects.all()
    }
    return render(request, "index.html", context)


# create sehifesinde yazilanlar
def create_view(request):
    context={}
    return render(request,"create.html", context)


# list sehifesinde yazilanlar
def list_view(request):
    context={
        "books":Book.objects.all()
    }
    return render(request, "list.html", context)


# detail sehifesinde yazilanlar
def detail_view(request, id):
    bookdetail= Book.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount")
    ).get(id=id)

    context={
        "bookdetail": bookdetail
    }
    return render(request, "detail.html", context)

