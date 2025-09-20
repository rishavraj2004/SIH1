from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .decorators import role_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Role-based redirection
            if user.role == 'Admin':
                return redirect('admin_dashboard')
            elif user.role == 'Dept_Head':
                return redirect('dept_dashboard')
            elif user.role == 'Scheduler':
                return redirect('scheduler_dashboard')
            else:
                messages.error(request, 'Invalid user role.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

@login_required
def custom_logout(request):
    """
    Custom logout that redirects back to login page
    but preserves the user's intended destination
    """
    # Store the user's role-based dashboard URL before logout
    user_role = request.user.role
    
    # Logout the user
    logout(request)
    
    # Add a success message
    messages.success(request, 'You have been successfully logged out.')
    
    # Redirect to login page
    return redirect('login')

@login_required
@role_required('Admin')
def admin_dashboard(request):
    context = {
        'user': request.user,
        'role': 'Admin'
    }
    return render(request, 'dashboard_admin.html', context)

@login_required
@role_required('Dept_Head')
def dept_dashboard(request):
    context = {
        'user': request.user,
        'role': 'Department Head',
        'department': request.user.department
    }
    return render(request, 'dashboard_dept.html', context)

@login_required
@role_required('Scheduler')
def scheduler_dashboard(request):
    context = {
        'user': request.user,
        'role': 'Scheduler',
        'department': request.user.department
    }
    return render(request, 'dashboard_scheduler.html', context)