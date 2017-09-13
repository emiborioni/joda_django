"""jodas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app_jodas.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    
    url(r'^$', iniciador,name="iniciador"),
    url(r'^ register/', registrar,name="registrar"),
    url(r'^ login/', login,name="login"),
    url(r'^main/', main,name="main"),
    url(r'^(?P<nombre>[0-9]+)/$', main, name='main'),
    url(r'^mkevento/', mkevento, name='mkevento'),
    url(r'^mkasist/(?P<evento_id>\d+)$', mkasist, name='mkasist'),
    url(r'^delete_evento/(?P<evento_id>\d+)$', delete_evento, name='delete_evento'),
    

]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)