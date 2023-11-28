from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    HttpResponse('main page')

def products(request):
    return render(request, 'products.html', {})


