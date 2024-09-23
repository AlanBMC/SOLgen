from django.shortcuts import render, redirect
import pdfplumber
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import time
import pyperclip
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

