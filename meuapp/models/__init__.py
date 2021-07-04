from .Classificacao import *
from .ContaPagar import *
from .ContaReceber import *

# Notar que não foi inserido o import para "pessoa"
# Neste caso, quando for fazer a referência é necessário colocar o caminho completo do módulo/arquivo que contém a classe.
# Ex em views.py: from .models.pessoa import Pessoa