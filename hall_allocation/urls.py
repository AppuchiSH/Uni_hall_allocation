"""
URL configuration for hall_allocation project.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views  # Import views, no need for forms if not used

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    
    # Static Pages
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # Custom Login Page
    path(
        'login/',
        LoginView.as_view(
            template_name='app/login.html',  # Ensure this matches your template path
            extra_context={  # Pass additional context to the template
                'title': 'Log in',
                'year': datetime.now().year,
                'roles': [
                    "Administrator", "Club Head", "Faculty In-Charge", "Student",
                    "Principal", "IQAC", "Resource Approval Personnel", "HOD",
                    "Dean of Student Affairs"
                ]
            }
        ),
        name='login'
    ),

    # Logout Page (Redirects to home after logout)
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Admin Panel
    path('admin/', admin.site.urls),
]
