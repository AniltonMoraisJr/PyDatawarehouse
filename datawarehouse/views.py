from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
import json
from .models import Fornecedor, Produto, Agenda
from datetime import datetime

# Create your views here.
def index (request):
	if request.method == 'POST':
		username = request.POST['user']
		password = request.POST['pass']
		user = authenticate(username = username, password = password)
		if user is not None:
			auth_login(request,user)
			return redirect('administration')
		else:
			return render(request, 'login.html', {'error': 'Usuario e/ou Senha errados !'})
	else:
		return render(request, 'login.html')

def do_logout(request):
	if not request.user.is_authenticated:
		return redirect('error.html')		
	else:
		logout(request)
		return redirect('login')

@login_required(login_url='login')
def administration (request):
	return render(request, 'administration.html')

@login_required(login_url='login')
def fornecedores (request):
	fornecedor_list = Fornecedor.objects.all()
	return render(request, 'fornecedor/fornecedores.html', {'fornecedor_list': fornecedor_list})

@login_required(login_url='login')
def new_fornecedor (request):
	if request.method != 'POST':
		return render(request, 'fornecedor/new_fornecedor.html')
	else:
		f = Fornecedor()
		f.nome = request.POST['nome']
		f.cnpj = request.POST['cnpj']
		f.telefone = request.POST['telefone']
		f.save()
		return redirect('fornecedores')

@login_required(login_url='login')
def produtos (request):
	produto_list = Produto.objects.all()
	return render(request, 'produto/produtos.html', {'produto_list': produto_list})

@login_required(login_url='login')
def new_produto (request):
	if request.method != 'POST':
		fornecedor_list = Fornecedor.objects.all()
		return render(request, 'produto/new_produto.html', {'fornecedor_list': fornecedor_list})
	else:
		p = Produto()
		p.nome = request.POST['nome']
		p.descricao = request.POST['descricao']
		p.foto = request.FILES['foto']
		p.preco = request.POST['preco']
		p.fornecedor = Fornecedor.objects.get(pk=request.POST['fornecedor'])
		p.save()
		return redirect('produtos')
@login_required(login_url='login')
def agenda (request):
	return render(request, 'agenda/agenda.html')
@login_required(login_url='login')
def new_agenda (request):
	if request.method == 'POST':
		a = Agenda()
		a.title = request.POST['title']
		a.start = datetime.strptime(request.POST['inicio'], '%Y/%m/%d %H:%M')
		a.end = datetime.strptime(request.POST['fim'], '%Y/%m/%d %H:%M')
		a.allDay = False
		a.save()
		return redirect('agenda')
	else:
		return render(request, 'agenda/new_agenda.html')
def get_agendas (request):
	agendas_list = Agenda.objects.all()
	events = []
	for a in agendas_list:
		events.append({'title' : a.title, 'start' : str(a.start), 'end' : str(a.end), 'allDay': a.allDay})
	return HttpResponse(json.dumps(events), content_type='application/json')