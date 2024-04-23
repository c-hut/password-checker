from django.shortcuts import render
from .checker import check_password

def check_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        strength = check_password(password)  # Call password checking function
        return render(request, 'password_checker.html', {'strength': strength})
    else:
        return render(request, 'password_checker.html')