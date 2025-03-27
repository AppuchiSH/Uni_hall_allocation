"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import PendingUser, ClubHead, HOD, FacultyInCharge, ResourceApprovalPerson, Principal, IQAC, DeanOfStudentAffairs

# View to fetch pending users
def get_pending_users(request):
    # Fetch all pending users and return as JSON
    pending_users = list(PendingUser.objects.values('id', 'username','email','position', 'department', 'club_name', 'lab'))
    print(f"Fetched Pending Users: {pending_users}")  # Debugging
    return JsonResponse(pending_users, safe=False)

# View to approve a user
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Add only if CSRF token issues persist during testing
def approve_user(request, user_id):
    if request.method == 'POST':
        # Fetch user from PendingUser table
        user = get_object_or_404(PendingUser, id=user_id)
        print(f"Approving User: {user.username}, Position: {user.position}")  # Debugging

        # Move user to their respective table based on their position
        if user.position == "Club Head":
            ClubHead.objects.create(username=user.username, password=user.password,email=user.email, club=user.club_name)
        elif user.position == "HOD":
            HOD.objects.create(username=user.username, password=user.password,email=user.email, department=user.department)
        elif user.position == "Faculty In-Charge":
            FacultyInCharge.objects.create(username=user.username, password=user.password,email=user.email, department=user.department)
        elif user.position == "Resource Approval Personnel":
            ResourceApprovalPerson.objects.create(username=user.username, password=user.password,email=user.email, lab=user.lab)
        elif user.position == "Principal":
            Principal.objects.create(username=user.username, password=user.password,email=user.email)
        elif user.position == "IQAC":
            IQAC.objects.create(username=user.username, password=user.password,email=user.email)
        elif user.position == "Dean of Student Affairs":
            DeanOfStudentAffairs.objects.create(username=user.username, password=user.password,email=user.email)
        else:
            return JsonResponse({"error": "Invalid position"}, status=400)

        # Remove user from PendingUser table
        user.delete()
        print(f"User {user.username} approved and removed from pending list.")  # Debugging
        return JsonResponse({"message": "User approved successfully."})
    else:
        print("Invalid request method.")  # Debugging
        return JsonResponse({"error": "Invalid request method"}, status=405)

# View to reject a user

def reject_user(request, user_id):
    if request.method == 'POST':
        try:
            # Fetch user from PendingUser table
            user = get_object_or_404(PendingUser, id=user_id)
            print(f"Rejecting User: ID={user.id}, Username={user.username}")  # Debugging

            # Remove user from PendingUser table
            user.delete()
            print(f"User {user.username} rejected and removed from pending list.")  # Debugging
            return JsonResponse({"message": "User rejected successfully."})
        except Exception as e:
            print(f"Error rejecting user: {e}")  # Debugging
            return JsonResponse({"error": "Failed to reject user."}, status=500)
    else:
        print("Invalid request method.")  # Debugging
        return JsonResponse({"error": "Invalid request method"}, status=405)


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

from django.shortcuts import render, redirect
from django.contrib import messages

# Predefined admin credentials
ADMIN_USERNAME = "adminvfl"
ADMIN_PASSWORD = "334766"

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        role = request.POST.get("role")  # Getting the selected role

        if role == "Admin":
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                return redirect("administrator_dashboard")  # Redirect to Admin Dashboard
            else:
                messages.error(request, "Invalid Admin credentials.")
                return redirect("login")  # Reload the login page with an error message
        
        else:
            # Redirecting users to their respective dashboards based on role
            role_redirects = {
                "Club Head": "club_head_dashboard",
                "HOD": "hod_dashboard",
                "Faculty-In-Charge": "faculty_dashboard",
                "IQAC": "iqac_dashboard",
                "Resource Approval Person": "resource_dashboard",
                "Dean of Student Affairs": "dean_dashboard",
                "Principal": "principal_dashboard"
            }

            if role in role_redirects:
                return redirect(role_redirects[role])  # Redirect to respective dashboard
            else:
                messages.error(request, "Invalid role selected.")
                return redirect("login")

    return render(request, "app/login.html")

# Dashboard Views for Different Roles
def administrator_dashboard(request):
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
from .forms import RegistrationForm  # Ensure this is correctly imported

from django.http import JsonResponse
from .models import PendingUser  # Import your model
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from app.models import PendingUser  # Replace `app` with your app name

def register(request):
    if request.method == "POST":
        # Fetch form data
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        position = request.POST.get("position")
        club_name = request.POST.get("club_name", None)
        department = request.POST.get("department", None)
        lab = request.POST.get("lab", None)

        # Debugging form data
        print(f"Form Data: Username={username}, Password=****,email={email}, Position={position}, Department={department}, Club Name={club_name}, Lab={lab}")

        # Validate required fields
        if not username or not password or not email or not position:
            messages.error(request, "All fields are required.")
            return redirect("register")

        # Validate role
        valid_positions = [
            "Club Head", "HOD", "Faculty In-Charge", "Resource Approval Personnel",
            "Principal", "IQAC", "Dean of Student Affairs"
        ]
        if position not in valid_positions:
            messages.error(request, "Invalid position selected.")
            return redirect("register")

        # Save user to PendingUser table
        pending_user = PendingUser.objects.create(
            username=username,
            password=make_password(password),  # Store hashed password
            email=email,
            position=position,
            department=department if position in ["HOD", "Faculty In-Charge"] else None,
            club_name=club_name if position == "Club Head" else None,
            lab=lab if position == "Resource Approval Personnel" else None
        )
        print(f"PendingUser Created: {pending_user}")  # Debugging

        messages.success(request, "Registration successfully sent for verification!")
        return redirect("login")

    # Render registration form for GET requests
    return render(request, 'app/register.html')
