from django.shortcuts import render

from logs.models import Log
# Create your views here.

def saveLog(msg, type):
    try:
        Log.objects.create(
            msg=msg,
            type=type
        )
    except Exception as e:
        saveLog(msg=str(e), type='Error')
    
