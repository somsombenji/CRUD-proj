"""fourth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import funccrud.urls
import funccrud.views
import portfolio.views
#미디어파일 사용할때 import / 외우기
from django.conf import settings
from django.conf.urls.static import static


#import classcrud.urls
#import classcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', funccrud.views.welcome, name="welcome"),
    path('funccrud/', include('funccrud.urls')),
    #path('classcrud/', include(classcrud.urls)),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#외우기
