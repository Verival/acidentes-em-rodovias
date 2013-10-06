# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	
    return render_to_response("index.html", {'param1' : 30, 'param2' : Pessoa("Matheus", 21, "M")}, context_instance=RequestContext(request))