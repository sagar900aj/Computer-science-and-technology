from django.http import HttpResponse
from django.template import loader
from .models import Bloguser

def blog_users(request):
    return HttpResponse("Hello world!")

def members(request):
    myusers = Bloguser.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {'myusers': myusers}
    return HttpResponse(template.render(context, request))