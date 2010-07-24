from django.shortcuts import render_to_response

def static(request, file):
    return render_to_response(file, {})

