from meuapp.views import pay_bills_report
from meuapp.views.pagamentos import create_pay_bills
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('classificacao/criar', views.create_category, name='create_category'),
    path('pagamento/criar', views.create_pay_bills, name='create_pay_bills'),
    path('pagamento/relatorio', views.pay_bills_report, name='pay_bills_report'),
    path('recebimento/criar', views.create_receive_bills, name='create_receive_bills'),
    path('recebimento/relatorio', views.receive_bills_report, name='receive_bills_report'),
    path('caixa', views.cash_flow, name='cash_flow'),
]