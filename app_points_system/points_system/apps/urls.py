from django.urls import path
from .views import (
    admin_dashboard,
    add_app,
    delete_app,
    user_dashboard,
    upload_screenshot,
    home
)

urlpatterns = [
    # Admin URLs
    #path('', home, name='home'),
    path('admin/', admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('admin/add/', add_app, name='add_app'),              # Add new app
    path('admin/delete/<int:app_id>/', delete_app, name='delete_app'),  # Delete app

    # User URLs
    path('dashboard/', user_dashboard, name='user_dashboard'),  # User dashboard
    path('upload_screenshot/<int:app_id>/', upload_screenshot, name='upload_screenshot'),  # Upload screenshot
]
