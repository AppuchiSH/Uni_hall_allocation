"""
URL configuration for hall_allocation project.
"""

from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from app import views  # Import views
from django.urls import path
from app.views import administrator_dashboard, custom_login, administrator_dashboard
from django.urls import path
from app import views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin/verify_users/", views.get_pending_users, name="verify_users"),
    # Home Page (Front Page)
    path('', views.home, name='home'),

    # Register and Login Pages
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path("login/", custom_login, name="login"),
    path("administrator-dashboard/", administrator_dashboard, name="administrator_dashboard"),  # Admin dashboard
     path('get_pending_users/', views.get_pending_users, name='get_pending_users'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject_user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('monitor_quality/', views.monitor_quality, name='monitor_quality'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('approve_requests/', views.approve_requests, name='approve_requests'),
    path('system_settings/', views.system_settings, name='system_settings'),
    path('manage_events/', views.manage_events, name='manage_events'),
    path('allocate_resources/', views.allocate_resources, name='allocate_resources'),
    path('view_reports/', views.view_reports, name='view_reports'),

    # Faculty In-Charge
    path('manage_venues/', views.manage_venues, name='manage_venues'),
    path('approve_bookings/', views.approve_bookings, name='approve_bookings'),
    path('view_schedule/', views.view_schedule, name='view_schedule'),

    # Principal
    path('manage_faculty/', views.manage_faculty, name='manage_faculty'),
    path('approve_leaves/', views.approve_leaves, name='approve_leaves'),
    path('monitor_performance/', views.monitor_performance, name='monitor_performance'),
    path('departmental_meetings/', views.departmental_meetings, name='departmental_meetings'),
    path('budget_allocation/', views.budget_allocation, name='budget_allocation'),
    path('staff_appointments/', views.staff_appointments, name='staff_appointments'),

    # IQAC
    path('submit_reports/', views.submit_reports, name='submit_reports'),
    path('accreditation_status/', views.accreditation_status, name='accreditation_status'),
    path('manage_feedback/', views.manage_feedback, name='manage_feedback'),
    path('organize_workshops/', views.organize_workshops, name='organize_workshops'),
    path('review_policies/', views.review_policies, name='review_policies'),

    # HOD
    path('manage_courses/', views.manage_courses, name='manage_courses'),

    # Static Pages
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # Logout Page
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # Role-Based Dashboards
    path('administrator_dashboard/', views.administrator_dashboard, name='admin_dashboard'),
    path('club_head_dashboard/', views.club_head_dashboard, name='club_head_dashboard'),
    path('faculty_in-charge_dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('principal_dashboard/', views.principal_dashboard, name='principal_dashboard'),
    path('iqac_dashboard/', views.iqac_dashboard, name='iqac_dashboard'),
    path('resource_approval_personnel_dashboard/', views.resource_dashboard, name='resource_dashboard'),
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('dean_of_student_affairs_dashboard/', views.dean_dashboard, name='dean_dashboard'),

    #DEAN
    path("dean_dashboard/", views.dean_dashboard, name="dean_dashboard"),
   

]

