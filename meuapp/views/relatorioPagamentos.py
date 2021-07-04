from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from meuapp.models import ContaPagar

def pay_bills_report(request: HttpRequest):
  pay_bills = None
  if request.method == 'POST':
    data = request.POST
    _due_date = data['validade']
    pay_bills = ContaPagar.objects.all().filter(due_date__lte=_due_date)
    return render(request, 'report/pay_bills.html', { 'pay_bills': pay_bills })
  else:
    return render(request, 'report/pay_bills.html', { 'pay_bills': pay_bills })