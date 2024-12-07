import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render


def projecthomepage(request):
    return render(request, 'adminapp/projecthomepage.html')


# Create your views here.




from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, Order2Form


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/Tasksprogram.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


def loginpagecall(request):
    return render(request, 'adminapp/loginpage.html')


def registerpagecall(request):
    return render(request, 'adminapp/registerform.html')


import datetime
from datetime import datetime
from datetime import timedelta


def dateandtimepagecall(request):
    return render(request, 'adminapp/datetimeexample.html')



from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def registerpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        if password != confirmpassword:
            return render(request, 'adminapp/registerfailed.html')

        if User.objects.filter(username=username).exists():
            return render(request,  'adminapp/registerfailed.html')

        if User.objects.filter(email=email).exists():
            return render(request, 'adminapp/registerfailed.html')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        return render(request, 'adminapp/projecthomepage.html', {'success_message': 'Account created successfully!'})

    return render(request, 'adminapp/registerform.html')

from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect

def loginpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:studenthomepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:facultyhomepage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from .forms import StudentForm
from .models import StudentList


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/addfarmer.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/studentlist.html', {'students': students})

def teammatespagecall(request):
    return render(request, 'adminapp/teammates.html')
def teammatespagelogic(request):
    return render(request, 'adminapp/teammates.html')


# views.py
import requests
from django.shortcuts import render


def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed']
            }
        else:
            weather_data = {
                'error': 'City not found. Please try again.'
            }

        return render(request, 'adminapp/weather.html', {'weather_data': weather_data})

    return render(request, 'adminapp/weather.html')

#
#def ratingpagecall(request):
#    return render(request, 'adminapp/rating.html')
#def ratingpagelogic(request):
#    return render(request, 'adminapp/rating.html')

def ratingthankyou(request):
    return render(request, 'adminapp/ratingthankyou.html')

from django.shortcuts import render, redirect
from .forms import RatingForm

def rate_service(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ratingthankyou')  # Redirect to a thank-you page after submission
    else:
        form = RatingForm()

    return render(request, 'adminapp/rating.html', {'form': form})


def externalcsspagecall(request):
    return render(request, 'adminapp/student_details.html')
def externalpagelogic(request):
    return render(request, 'adminapp/student_details.html')


def uitrailpagecall(request):
    return render(request, 'adminapp/uitrail.html')


def uitrailpagelogic(request):
    return render(request, 'adminapp/uitrail.html')


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text


@csrf_exempt
def assistant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session_id = data.get('session_id', None)
        command = data.get('command', '').lower()

        # Response to handle invalid or missing commands
        if not command:
            return JsonResponse({'response': 'Please provide a valid command.'})

        # Process the command
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)
            response = f'Playing {song} on YouTube.'
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            response = talk(f'Current time is {time}')
        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            info = wikipedia.summary(person, sentences=1)
            response = talk(info)
        elif 'joke' in command:
            response = talk(pyjokes.get_joke())
        elif 'date' in command:
            response = talk('Sorry, I have a headache')
        elif 'what is this project' in command:
            response = talk('This project is about an e-commerce platform for agriculture.')
        elif 'what is your name?' in command:
            response = talk('My name is Bhanu.')
        elif 'who developed you?' in command:
            response = talk('I was developed by Bhanu Vamsi.')
        elif 'are you single' in command:
            response = talk('I am in a relationship with Wi-Fi.')
        elif 'weather in' in command:
            city = command.replace('weather in', '').strip()
            api_key = '9c0dce6c68794ff4309c5bdb5fa78008'
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            try:
                weather_data = requests.get(url).json()
                if weather_data.get('cod') == 200:
                    temp = weather_data['main']['temp']
                    description = weather_data['weather'][0]['description']
                    response = talk(f'The temperature in {city} is {temp}°C with {description}.')
                else:
                    response = talk('City not found.')
            except Exception as e:
                response = talk('Error fetching weather data.')
        else:
            response = talk('I did not understand. Please say it again.')

        # Return response for the current command
        return JsonResponse({'response': response, 'continue': True})

    return JsonResponse({'response': 'Invalid request method.'})


def assistantpagecall(request):
    return render(request, 'adminapp/assistant.html')


from django.shortcuts import render, redirect
from .forms import OrderForm
from django.shortcuts import render, redirect
from .forms import OrderForm

def order_confirmation(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'adminapp/order_confirmation.html')

def order_success(request):
    return render(request, 'adminapp/order_success.html')

from django.shortcuts import render, redirect
from .forms import Order2Form

def order_confirmation2(request):
    if request.method == 'POST':
        form = Order2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'adminapp/order_confirmation.html')


def cropsuggestions(request):
    return render(request, 'adminapp/cropsuggestions.html')