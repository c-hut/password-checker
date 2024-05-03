from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .checker import evaluate_password_strength
from django.contrib.auth.hashers import make_password
from .models import PasswordLogger

def index(request):
    return render(request, 'password_checker.html')

def check_password(request):
    if request.method == 'POST' and request.headers.get('X_Requested_With') == 'XMLHttpRequest':
        password = request.POST.get('password')
        # Call password checking function
        strength = evaluate_password_strength(password)
        # Log the password attempt
        success = strength == "Strong"
        # Hash the password before logging it
        hashed_password = make_password(password)
        #Save the password attempt in the database
        attempt = PasswordLogger(password=hashed_password, success=success)
        attempt.save()

        return JsonResponse({'strength': strength})
    else:
        return JsonResponse({'error': 'Invalid request'})