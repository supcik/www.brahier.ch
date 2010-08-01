from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

from brahier.account.forms import RegistrationForm

def profile(request):
    return render_to_response("registration/profile.html", None,
        context_instance=RequestContext(request))
    
def new(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistrationForm()

    return render_to_response('registration/new.html', {
            'form': form,
        },
        context_instance=RequestContext(request)
    )
