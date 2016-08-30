from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
from django.template import loader
from django.urls import NoReverseMatch, reverse

from django.views.decorators.cache import never_cache
from django.shortcuts import HttpResponseRedirect, render_to_response
from django.contrib import auth


app_name = 'wvpn'

class WvpnSite(object):

    def has_permission(self, request):
        """
        Returns True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        return request.user.is_active and request.user.is_staff

    @never_cache
    def login(self, request):
        if request.method == 'GET' and not self.has_permission(request):
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        from django.contrib.auth.views import login


    @never_cache
    def index(self, request):
        pass

    @property
    def urls(self):
        return self.get_urls(), 'admin', self.name

def has_permission(request):
    return request.user.is_active and request.user.is_staff

def index(request):
    return HttpResponse(render(request, 'index.html'))
    #return render_to_response('index.html',locals())


def logout(request):
    index_path = '/'
    return HttpResponseRedirect(index_path)
# return HttpResponse("Hello  logout world!")

def login(request):
    if request.method == 'GET' and has_permission(request):
        index_path = reverse('wvpn:index', current_app=app_name)
        return HttpResponseRedirect(index_path)

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        index_path = reverse('wvpn:index', current_app=app_name)
        return HttpResponseRedirect(index_path)
    else:
        return render_to_response('login_register_modal.html')
