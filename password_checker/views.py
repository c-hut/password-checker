from django.http import JsonResponse, HttpResponse
# Import the program from checker.py
from .checker import evaluate_password_strength
from django.shortcuts import render

def index(request):
    return render(request, 'password_checker.html')

def check_password(request):
    if request.method == 'POST' and request.headers.get('X_Requested_With') == 'XMLHttpRequest':
        password = request.POST.get('password')
        # Call password checking function
        strength = evaluate_password_strength(password)
        return JsonResponse({'strength': strength})
    else:
        return JsonResponse({'error': 'Invalid request'})