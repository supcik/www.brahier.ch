from django.shortcuts import render_to_response
from django.template import RequestContext

def profile(request):
    return render_to_response("registration/profile.html", None,
        context_instance=RequestContext(request))