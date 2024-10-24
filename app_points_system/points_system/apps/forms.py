from django import forms

class ScreenshotUploadForm(forms.Form):
    screenshot = forms.ImageField()
