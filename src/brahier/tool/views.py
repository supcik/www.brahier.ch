import urllib
import json
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from xml.sax import make_parser
from xml.sax.handler import ContentHandler 

class CitiesHandler(ContentHandler):

    def __init__ (self):
        self.list = []

    def startElement(self, name, attrs):
        if name == 'city':
            txt = attrs.get('name',"")
            self.list.append({
                'id': txt,
                'label': txt,
                'value' : txt
            })

def cities(request):
    f = urllib.urlopen("http://extapi.local.ch/0/cities.xml?%s" %
                       urllib.urlencode({'q' : request.GET['term']}))

    parser = make_parser()
    curHandler = CitiesHandler() 
    parser.setContentHandler(curHandler)
    parser.parse(f)

    return HttpResponse(json.dumps(curHandler.list), mimetype="text/plain")
                                                                