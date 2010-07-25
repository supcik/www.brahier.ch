from django.shortcuts import render_to_response
from django.template import RequestContext

def static(request, file):
    return render_to_response(file, None,
        context_instance=RequestContext(request))

