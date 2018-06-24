from django.http import HttpResponse

def homepage(request):
    return HttpResponse('HomePage( add new things for git)....')