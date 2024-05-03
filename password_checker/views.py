from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .checker import evaluate_password_strength
from .models import PasswordLogger

def index(request):
    return render(request, 'password_checker.html')

def check_password(request):
    if request.method == 'POST' and request.headers.get('X_Requested_With') == 'XMLHttpRequest':
        password = request.POST.get('password')
        # Call password checking function
        strength = evaluate_password_strength(password)

        # Log the password attempt
        success = strength == "Strong"  # Determine if attempt was successful
        attempt = PasswordLogger(password=password, success=success)
        attempt.save()

        return JsonResponse({'strength': strength})
    else:
        return JsonResponse({'error': 'Invalid request'})