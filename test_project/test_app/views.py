from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import TestFormNewRendering

def test_multiwidget_view(request):
    form_new = TestFormNewRendering()
    return render(request, 'test_app/test_multiwidget.html', {
        'form_new': form_new,
    })
