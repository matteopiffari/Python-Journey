from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import CreateNewItem

# Create your views here.
def home(request):
    #return HttpResponse("Hello World!")
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

def ping(request):
    return HttpResponse("Pong!")

def allItems(request):
    return render(request, "items.html", {"items": Item.objects.all()})

def getItem(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, "item_detail.html", {"item": item})

def createItem(request):
    if request.method == "POST":
        form = CreateNewItem(request.POST)
        if form.is_valid():
            item = Item(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"]
            )
            item.save()
            return redirect("/items/")
    else:
        form = CreateNewItem()
    return render(request, "create.html", {"form": form})
