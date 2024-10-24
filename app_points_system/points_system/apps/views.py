from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import App, Task
from .forms import ScreenshotUploadForm  # Create this form to handle file uploads

def home(request):
    return render(request,  'home.html')

# Admin Views
def admin_dashboard(request):
    apps = App.objects.all()
    return render(request, 'admin.html', {'apps': apps})


def add_app(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        points = request.POST.get('points')
        App.objects.create(name=name, points=points)
        return redirect('admin_dashboard')
    return redirect('admin_dashboard')  # Redirect if not POST


def delete_app(request, app_id):
    if request.method == 'POST':
        app = get_object_or_404(App, id=app_id)
        app.delete()
    return redirect('admin_dashboard')


# User Views
@login_required
def user_dashboard(request):
    apps = App.objects.all()
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'user.html', {'apps': apps, 'tasks': tasks})


@login_required
def upload_screenshot(request, app_id):
    app = get_object_or_404(App, id=app_id)

    if request.method == 'POST':
        form = ScreenshotUploadForm(request.POST, request.FILES)
        if form.is_valid():
            Task.objects.create(user=request.user, app=app, screenshot=form.cleaned_data['screenshot'], completed=True)
            return redirect('user_dashboard')
    else:
        form = ScreenshotUploadForm()

    return render(request, 'upload_screenshot.html', {'form': form, 'app': app})

