# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

class Pessoa():
	def __init__(self, nome, idade, sexo):
		self.nome = nome
		self.idade = idade
		self.sexo = sexo

	def __str__(self):
		return "Nome = {0}, Idade = {1}, Sexo = {2}".format(self.nome, self.idade, self.sexo)
