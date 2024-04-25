from django.http import JsonResponse
# Import the program from checker.py
from .checker import evaluate_password_strength

def check_password(request):
    if request.method == 'POST' and request.is_ajax():
        password = request.POST.get('password')
        # Call password checking function
        strength = evaluate_password_strength(password)
        return JsonResponse({'strength': strength})
    else:
        return JsonResponse({'error': 'Invalid request'})