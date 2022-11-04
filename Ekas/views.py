from .models import LoanApplication
from .forms import LoanApplicationForm
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Home')


def apply(request):
    if request.method == 'GET':
        form = LoanApplicationForm()
        context = {
            'form': form
        }
        return render(request, 'apply.html', context)

    elif request.method == 'POST':
        form = LoanApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'form_submit_success.html')
        else:
            context = {'form': form}
            return render(request, 'form_submit_failed.html', context)
