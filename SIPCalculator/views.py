from django.shortcuts import render, redirect
from .forms import SIPCalculatorForm
from django.http import HttpResponse



def sip_calculator(request):
    if request.method == 'POST':
        form = SIPCalculatorForm(request.POST)
        if form.is_valid():
            sip_calculator = form.save(commit=False)
            sip_calculator_result = sip_calculator.calculate_future_value()
            sip_calculator.save()
            return render(request, 'sip_calculator/result.html', {'result': sip_calculator_result})
    else:
        form = SIPCalculatorForm()

    return render(request, 'sip_calculator/sip_calculator.html', {'form': form})

def home(request):
    return HttpResponse("Welcome, click here: http://localhost:8000/sip_calculator/")
    # return HttpResponse("Welcome to the SIP Calculator App!")