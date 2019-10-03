from django import forms

class TaskInquiryForm(forms.Form):
    email = forms.EmailField(required=True, label="What is your Email? (So we can reach out to you).")
    task = forms.CharField(required=True, widget=forms.Textarea, label="Describe your task below. (Profanities welcomed, and encouraged).")
    duration = forms.CharField(widget=forms.Textarea, required=True, label="How long does this task take you per week? (in hours)")

class WebAppInquiryForm(forms.Form):
    email = forms.EmailField(required=True, label="What is your Email? (So we can reach out to you).")
    app = forms.CharField(required=True, widget=forms.Textarea, label="What are you looking for? What does your dream web app look like?")
