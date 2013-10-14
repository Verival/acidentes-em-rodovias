# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):

	# Lógica
    return render_to_response("index.html", context_instance=RequestContext(request))

