from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'keepsakes/index.html')

def preview(request):
    # This will be implemented later to handle image preview
    return JsonResponse({'status': 'preview not implemented yet'})

def buy(request):
    # This will be implemented later to handle purchase
    return JsonResponse({'status': 'buy not implemented yet'})