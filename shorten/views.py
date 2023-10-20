from django.shortcuts import render, redirect, HttpResponse, resolve_url
from django.views.generic import TemplateView
from .models import URL
from django.db.models import F
from .forms import IndexForm
import secrets

# Create your views here.
def redirect(request, *args, **kwargs):
    print('kwargs: ', kwargs['short_url'])
    
    redirectObj = URL.objects.get(pk=kwargs['short_url']).long_url
    updateVisits = URL.objects.filter(pk=kwargs['short_url']).update(visits=F('visits') + 1)
    print('redirectObj: ', str(redirectObj))
    response = HttpResponse()
    response.status_code = 302
    response['Location'] = redirectObj
    return response
    

def IndexView(request):
    if request.method == 'POST':
        print('request.POST: ', request.POST)
        form  = IndexForm(request.POST)
        if form.is_valid():
            print('form.cleaned_data: ', form.cleaned_data)
            long_url = form.cleaned_data['long_url']
            short_url = secrets.token_urlsafe(4)
            print('short_url: ', short_url)
            url = URL(long_url=long_url, short_url=short_url, visits=0)
            url.save()
            shortLinks = URL.objects.all()
            template = 'index.html'
            context = {'shortLinks': shortLinks}
            return render(request, template, context)
    else:
        shortLinks = URL.objects.all()
        template = 'index.html'
        context = {'shortLinks': shortLinks}
        return render(request, template, context)