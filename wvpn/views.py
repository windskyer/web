from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
from django.template import loader
from django.urls import NoReverseMatch, reverse

from django.views.decorators.cache import never_cache
from django.shortcuts import HttpResponseRedirect, render_to_response
from django.contrib import auth
from django.template.response import TemplateResponse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.translation import ugettext as _, ugettext_lazy




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

def login(request, extra_context=None):
    """
        Displays the login form for the given HttpRequest.
    """
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

    from django.contrib.auth.views import login
    # Since this module gets imported in the application's root package,
    # it cannot import models from other applications at the module level,
    # and django.contrib.admin.forms eventually imports User.
    from django.contrib.admin.forms import AdminAuthenticationForm
    context = dict(
        #    self.each_context(request),
        title=_('Log in'),
        app_path=request.get_full_path(),
        username=request.user.get_username(),
    )
    if (REDIRECT_FIELD_NAME not in request.GET and
        REDIRECT_FIELD_NAME not in request.POST):
        context[REDIRECT_FIELD_NAME] = reverse('wvpn:index', current_app='wvpn')
    context.update(extra_context or {})

    defaults = {
        'extra_context': context,
        'authentication_form': AdminAuthenticationForm,
        'template_name': 'login.html',
    }
    request.current_app = "wvpn"
    return login(request, **defaults)
