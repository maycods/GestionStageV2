"""GestionStageV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from satgesiV2.views import pageone
from satgesiV2.views import pagetwo
from satgesiV2.views import pagethree
from satgesiV2.views import pagefour
from satgesiV2.views import pagefive
from satgesiV2.views import pageacc ,pageseven,pageeight,pagenine
from satgesiV2.views import pagesix,boxstage, Gencadreur, boxstage2,Gorgan,GGstag,Gprom,Gtype,Gstage,Gstag

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', pageone),
      path('connected/', pagetwo),
      path('formul/',pagethree,name="formul"),
      path('Etudiant/',pagefour,name="create"),
      path('accept/',pageacc,name="accept"),
      path('Encadreur/',pagesix,name="createE"),
       path('Promoteur/',pagefive,name="createP"),
       path('Organisme/',pageseven,name="createO"),
       path('GPStagieres/',pageeight,name="createG"),
       path('TypeStage/',pagenine,name="CreateS"),

        path('GS/',Gstage,name="GS"),
        path('BS/',boxstage,name="BS"),
        path('GE/',Gencadreur,name="GE"),
        path('BS2/',boxstage2,name="BS2"),
        path('GO/',Gorgan,name="GO"),
        path('GP/',Gprom,name="GP"),
        path('GT/' ,Gtype,name="GT"),
        path('GGSR/',GGstag,name="GGSR"),
        path('GSR/',Gstag,name="GSR"),

      ]

