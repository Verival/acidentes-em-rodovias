# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

# ESSA CLASSE NÃO PODE FICAR AQUI, DEVE SER NA MODELS.PY
class Pessoa():
	def __init__(self, nome, idade, sexo):
		self.nome = nome
		self.idade = idade
		self.sexo = sexo

	def __str__(self):
		return "Nome = {0}, Idade = {1}, Sexo = {2}".format(self.nome, self.idade, self.sexo)

def index(request):
	# Lógica
    return render_to_response("index.html", {'param1' : 30, 'param2' : Pessoa("Matheus", 21, "M")}, context_instance=RequestContext(request))