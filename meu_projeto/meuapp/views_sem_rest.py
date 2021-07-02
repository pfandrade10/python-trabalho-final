from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Telefone
from .models.pessoa import Pessoa
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@require_http_methods(['GET','POST'])
def enviar_json(request):
	payload = json.loads(request.body)

	"""
	{
	    "nome_completo": "Paulo Tavares",
	    "telefone": {
	        "ddd":31,
	        "numero":"987654321"
	    }
	}
	"""

	_nome_completo = payload["nome_completo"]
	_nome = _nome_completo.split(" ")[0]
	_sobrenome = _nome_completo.split(" ")[1]
	_ddd = payload["telefone"]["ddd"]
	_numero = payload["telefone"]["numero"]

	try:
		# Hipoteticamente podem organizar o projeto:
		#    Pessoa.objects.cadastrar_pessoa(_nome,_ddd,_numero)
		#
		# Fazer os métodos para salvar as informações
		pessoa = Pessoa(nome=_nome, sobrenome=_sobrenome)
		pessoa.save()

		tel = Telefone(ddd=_ddd, numero=_numero, temWhatsapp=False)
		tel.save()

		pessoa.telefones.add(tel)

		#mensagem de confirmação
		mensagem = f"Dados de {_nome} cadastrados com sucesso!"
	except Exception as e:
		mensagem = f"Falha ao cadastrar: {e}"
	
	return JsonResponse({"mensagem": mensagem})

@csrf_exempt
@require_http_methods(['GET','POST'])
def listar_com_parametro(request):
	_idade = request.POST['idade']
	pessoas = Pessoa.objects.filter(idade__exact=_idade)
	pessoas_json = []
	for p in pessoas:
		pdic = {
			'nome': p.nome, 'sobrenome':p.sobrenome,
			'idade': p.idade
		}
		pessoas_json.append(pdic)

	payload = {
		'pessoas': pessoas_json
	}

	return JsonResponse(payload)

@csrf_exempt
@require_http_methods(['GET','POST'])
def listar_pessoas(request):
	pessoas = Pessoa.objects.all()
	pessoas_json = []
	for p in pessoas:
		pdic = {
			'nome': p.nome, 'sobrenome':p.sobrenome,
			'idade': p.idade
		}
		pessoas_json.append(pdic)

	payload = {
		'pessoas': pessoas_json
	}

	return JsonResponse(payload)

def detalhar_pessoa(request, idpessoa):
	p = Pessoa.objects.obter_pessoa_id(idpessoa)
	payload = {
		'nome': p.nome,
		'sobrenome': p.sobrenome
	}
	return JsonResponse(payload)

@csrf_exempt
def indice(request):
	response = HttpResponse()

	if request.method == 'GET':
		response.write("Usei o método GET")
	elif request.method == 'POST':
		response.write("Usei o método POST")
	else:
		response.write("Método HTTP não suportado!")

	return response

def detalhar_pessoa2(request, idpessoa):
	# Tratar se os parâmetros são válidos
	try:
		p = Pessoa.objects.obter_pessoa_id(idpessoa)
	except:
		return HttpResponse("Erro ao buscar Pessoa")
	# Manipula da forma como achar conveniente ou necessária

	return HttpResponse(f"Você procurou a pessoa de nome {p.nome}")

def detalhar_pessoa3(request, idpessoa):
	# Tratar se os parâmetros são válidos
	try:
		p = Pessoa.objects.obter_pessoa_id(idpessoa)
		pessoas = Pessoa.objects.all()
	except:
		return HttpResponse("Erro ao buscar Pessoa")

	dados = {'pessoa': p, 'msg': "Uma mensagem qualquer",
		'pessoas': pessoas,
		'valor': 5}
	return render(request, 'pessoa/detalhar2.html', dados)

def listar_pessoas3(request):
	pessoas = Pessoa.objects.all()
	dados = {'pessoas': pessoas,
		'msg': "Esta é uma mensagem fora do modelo"}
	
	return render(request, 'pessoa/listar.html', dados)