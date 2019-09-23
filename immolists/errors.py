from django.conf import settings
from django.shortcuts import render


def error404(request,exception):
    context={}
    context={'project_name':settings.PROJECT_NAME}
    return render(request,'site/404.html',context)
