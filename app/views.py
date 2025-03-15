"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
# views.py
from django.contrib.auth import login
from .forms import RegistrationForm

#faculty in charge
def view_schedule(request):
    # Your view logic here
    return render(request, 'schedule.html')

def manage_venues(request):
    # Your code here
    pass

def approve_bookings(request):
    # Your logic here
    return render(request, 'approve_bookings.html')
#-------------------------------


def system_settings(request):
    # Your logic here
    return render(request, 'system_settings.html')


def approve_requests(request):
    # Your logic here
    return render(request, 'approve_requests.html')


def manage_users(request):
    return render(request, 'app/manage_users.html')

def manage_events(request):
    # Your code for managing events
    return render(request, 'app/manage_events.html')

def allocate_resources(request):
    # Your code for allocating resources
    return render(request, 'app/allocate_resources.html')

def view_reports(request):
    # Your code for viewing reports
    return render(request, 'app/view_reports.html')

def logout_view(request):
    # Your code for logging out
    # You can use Django's built-in logout function:
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')  

def monitor_quality(request):
    # Add logic for the monitor_quality view here
    return render(request, 'monitor_quality.html')  # Replace with your template

def view_reports(request):
    # Logic to display reports
    return render(request, 'app/view_reports.html')  # Use your actual template

def allocate_resources(request):
    # Logic to allocate resources
    return render(request, 'app/allocate_resources.html')  # Use your actual template

def manage_events(request):
    # Add the logic to manage events here
    return render(request, 'app/manage_events.html')  # Replace with your actual template


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )

def custom_login(request):
    """Handles login and redirects based on the selected role."""
    roles = [
        "Administrator", "Club Head", "Faculty In-Charge", "Student",
        "Principal", "IQAC", "Resource Approval Personnel", "HOD",
        "Dean of Student Affairs"
    ]

    if request.method == "POST":
        role = request.POST.get("role")
        if role:
            role_url = role.replace(" ", "_").lower() + "_dashboard"
            return redirect(role_url)  # Redirects to the respective dashboard
    
    return render(request, 'app/login.html', {
        'title': 'Log in',
        'year': datetime.now().year,
        'roles': roles
    })

# Dashboard Views for Different Roles
def admin_dashboard(request):
    """Renders the Administrator dashboard."""
    return render(request, 'app/administrator_dashboard.html', {'title': 'Administrator Dashboard'})

def club_head_dashboard(request):
    """Renders the Club Head dashboard."""
    return render(request, 'app/club_head_dashboard.html', {'title': 'Club Head Dashboard'})

def faculty_dashboard(request):
    """Renders the Faculty In-Charge dashboard."""
    return render(request, 'app/faculty_dashboard.html', {'title': 'Faculty In-Charge Dashboard'})

def student_dashboard(request):
    """Renders the Student dashboard."""
    return render(request, 'app/student_dashboard.html', {'title': 'Student Dashboard'})

def principal_dashboard(request):
    """Renders the Principal dashboard."""
    return render(request, 'app/principal_dashboard.html', {'title': 'Principal Dashboard'})

def iqac_dashboard(request):
    """Renders the IQAC dashboard."""
    return render(request, 'app/iqac_dashboard.html', {'title': 'IQAC Dashboard'})

def resource_dashboard(request):
    """Renders the Resource Approval Personnel dashboard."""
    return render(request, 'app/resource_dashboard.html', {'title': 'Resource Approval Personnel Dashboard'})

def hod_dashboard(request):
    """Renders the HOD dashboard."""
    return render(request, 'app/hod_dashboard.html', {'title': 'HOD Dashboard'})

def dean_dashboard(request):
    """Renders the Dean of Student Affairs dashboard."""
    return render(request, 'app/dean_dashboard.html', {'title': 'Dean of Student Affairs Dashboard'})

##principal

def manage_faculty(request):
    # Your view logic here
    return render(request, 'manage_faculty.html')

def approve_leaves(request):
    # Your logic here
    return render(request, 'approve_leaves.html')

def monitor_performance(request):
    # Your logic here
    return render(request, 'monitor_performance.html')

def departmental_meetings(request):
    # Your view logic here
    return render(request, 'departmental_meetings.html')

def budget_allocation(request):
    # Your view logic here
    return render(request, 'budget_allocation.html')

def staff_appointments(request):
    # Your logic here
    return render(request, 'staff_appointments.html')

#IQAC
def submit_reports(request):
    # Your view logic here
    return render(request, 'app/submit_reports.html', {'title': 'Submit Reports'})

def accreditation_status(request):
    return HttpResponse("Accreditation status page")

# Add a simple function to test import
def test_import(request):
    return HttpResponse("Views module imported successfully")

# app/views.py
from django.shortcuts import render

def manage_feedback(request):
    # Your logic here
    return render(request, 'manage_feedback.html')

def organize_workshops(request):
    # Your logic here
    return render(request, 'organize_workshops.html')

def review_policies(request):
    # Your logic here
    return render(request, 'review_policies.html')

#HOD

def manage_courses(request):
    # Your logic here
    return render(request, 'manage_courses.html')

#DEAN
def dean_dashboard(request):
    # Sample event data (replace with actual database data)
    events = [
        {"name": "Annual Tech Fest", "status": "Pending", "sub_tasks": ["Budget Approval", "Venue Confirmation"]},
        {"name": "Cultural Fest", "status": "Approved", "sub_tasks": ["Artist Invitation", "Logistics Arrangement"]},
    ]
    
    return render(request, "app/dean_dashboard.html", {"events": events})


#REGISTER


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm  # Ensure RegistrationForm exists

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')  # Ensure 'index' is a valid URL name
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})
