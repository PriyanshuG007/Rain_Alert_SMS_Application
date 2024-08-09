# Rain_Alert_SMS_Application

# Overview

The Rain Alert SMS System is a Python application designed to help you stay prepared for rainy weather. By leveraging the OpenWeather API and Twilio API, this application checks the weather forecast for the next 12 hours and sends you an SMS alert if rain is expected, so you never leave home without an umbrella!

# Features

1. Real-Time Weather Monitoring: Fetches weather data for the next 12 hours using the OpenWeather API.
2. SMS Notifications: Automatically sends an SMS alert if rain is detected within the specified timeframe.
3. Customizable Location: Set your preferred location by configuring the latitude and longitude.
4. Twilio Integration: Uses Twilio's reliable service to send SMS alerts directly to your phone.
5. Automatable: Easily set up to run daily on a schedule using PythonAnywhere.

# Technologies Used

1. Python: Core programming language used.
2. Twilio API: Sends SMS notifications.
3. OpenWeather API: Provides weather data.

# Automate with PythonAnywhere
To automate this application and have it run daily, you can use PythonAnywhere:

1. Create an Account: Sign up for a free account on PythonAnywhere.
2. Upload Your Script: Upload your rain_alert.py script to your PythonAnywhere account.
3. Set Up a Scheduled Task:
   - Navigate to the "Tasks" section in PythonAnywhere.
   - Set up a new scheduled task to run your script at a specific time every day.
   - This will automatically execute your Python script daily, ensuring you receive timely rain alerts.

# Acknowledgments

1. Twilio for the SMS API.
2. OpenWeather for the weather data.
3. PythonAnywhere for the easy-to-use cloud-based Python development environment
