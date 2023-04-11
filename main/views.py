from django.shortcuts import render
from .models import Category, Words

# Create your views here.
def main(request):
    objs = Category.objects.all().order_by("id")
    print(objs)
    context = {
        'objs':objs
    }
    return render(request, 'main.html', context)

def onpage(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    words = Words.objects.filter(category=category)
    context = {
        "words":words,
        "categories":categories,
    }
    return render(request, 'index.html', context)