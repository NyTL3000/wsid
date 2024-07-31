"""
WSGI config for python_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import certifi
import ssl
from mongoengine import connect
from pymongo import MongoClient
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_web.settings')

# # Kết nối tới MongoDB
# def check_mongodb_connection(): 
#     try:
#         # Attempt to connect to MongoDB
#         connect(host='mongodb+srv://nguyen:l5K9LyqcGPLCAuBx@cluster0.zwea0ao.mongodb.net/')
        
        
#         print("Successfully connected to MongoDB!")
#     except Exception as e: 
#         print(f"Failed to connect to MongoDB. Error: {e}")

# # Call the function to check the connection
# check_mongodb_connection()

application = get_wsgi_application()

app = application

