from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.

# using HttpResponse
def sayHello(request):
    return HttpResponse("<h1 style='font-family: Arial;'>Hello World</h1>")

# using a render

# grab all toDo items
def toDoList(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {"items": results})


# create item handler
def createItem(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)

        # django automatically checks if form is valid!
        if form.is_valid():
            form.save()
            return redirect(toDoList)

    else:
        form = ItemForm()

    return render(request, "item-form.html", {"form": form})


# edit item handler
def editItem(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(toDoList)
    else:
        form = ItemForm(instance=item)

    return render(request, "item-form.html", {"form": form})


# toggle view handler
def toggleStatus(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()

    return redirect(toDoList)