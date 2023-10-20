from django.shortcuts import render, redirect, HttpResponse, resolve_url
from .models import URL

# Create your views here.
def redirect(request, *args, **kwargs):
    print('kwargs: ', kwargs['short_url'])
    redirectObj = URL.objects.filter(short_url=kwargs['short_url']).values()
    print('redirectObj: ', str(redirectObj))
    returnUrl = str(redirectObj[0]['long_url'])
    response = HttpResponse()
    response.status_code = 302
    response['Location'] = returnUrl
    return response