from django.shortcuts import render, redirect
from .models import Event, emails
from datetime import datetime
from django.utils import timezone


def index(request):
    event = Event.objects.first()
    if event:
        end_time = event.endtime.replace(tzinfo=None)  # Remove timezone to make it naive
        request.session['end_time'] = end_time.strftime('%Y-%m-%dT%H:%M:%S')  # Store in session
    return render(request, 'index.html')




def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        event = emails.objects.create(email=email)
        event.save()
        return redirect('index')  # Redirect back to the index page after successful submission

    return redirect('index')  # Redirect to the index page if the request is not a POST request
