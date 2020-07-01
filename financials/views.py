from django.shortcuts import render

# Create your views here.
def balance(request):
    return render(request, 'servers.html')


def cashflow(request):
    return render(request, 'servers.html')


def income(request):
    return render(request, 'servers.html')
