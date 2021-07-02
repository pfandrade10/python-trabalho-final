from django.db import models
from . import Departamento, Telefone

class PessoaManager(models.Manager):
	def obter_pessoa_id(self, idpessoa):
		return self.get(id=idpessoa)

	def obter_todas_pessoas(self):
		return self.all()

	def obter_m_18(self):
		pessoas = self.all()
		return pessoas

	def create_pessoa(self, nome_completo):
		_nome_completo = nome_completo.split(" ")
		pessoa = self.create(nome=_nome_completo[0],
							 sobrenome=_nome_completo[1])
		return pessoa

class Pessoa(models.Model):
	SEXO_CHOICES = [('M','Masculino'),
					('F','Feminino')]

	nome = models.CharField(max_length=50)
	sobrenome = models.CharField(max_length=50,
							null=True)
	idade = models.IntegerField(default=0)
	sexo = models.CharField(max_length=10,
			choices=SEXO_CHOICES,
			default='M')
	dataNascimento = models.DateField(null=True)
	departamento = models.ForeignKey(Departamento,
							on_delete=models.SET_NULL,
							null=True)
	telefones = models.ManyToManyField(Telefone)

	objects = PessoaManager()

	def __str__(self):
		return f"{self.nome} {self.sobrenome}"