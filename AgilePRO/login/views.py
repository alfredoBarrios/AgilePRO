from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def logout_page(request):
    """Metodo que Cierra Sesion."""
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    """Redirecciona al Modulo correspondiente."""
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin')
    else:
        return render_to_response('home.html',{ 'user': request.user })