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
from satgesiV2.views import mod, modTS, modpGS, modpO,modpr, recho, rechp, stats4, supP, supgs, supo,supt,rechgs,recht,modS,sups,rechs
from satgesiV2.views import pagetwo
from satgesiV2.views import pagethree,pagederoule
from satgesiV2.views import pagefour,stats4
from satgesiV2.views import pagefive,rech ,stats2,stats3
from satgesiV2.views import pageacc ,sup,pageseven,pageeight,pagenine,mod
from satgesiV2.views import pagesix,boxstage, Gencadreur, boxstage2,Gorgan,GGstag,Gprom,Gtype,Gstage,Gstag,stats,pageSedroul,pageInscrit
from accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('', pageone),
      path('', login_view),
      path('connected/', pagetwo),
      path('formul/',pagethree,name="formul"),
      path('Etudiant/',pagefour,name="create"),
      path('accept/',pageacc,name="accept"),
      path('EncadMod/<str:pk>/',mod,name="modifE"),
      path('ProMod/<str:pk>/',modpr,name="modifP"),
      path('orgMod/<str:pk>/',modpO,name="modifO"),
      path('gsMod/<str:pk>/',modpGS,name="modifGS"),
       path('sMod/<str:pk>/',modS,name="modifS"),
      path('tsMod/<str:pk>/',modTS,name="modifT"),
      path('Encadsup/<str:pk>/',sup,name="supE"),
      path('prosup/<str:pk>/',supP,name="supP"),
      path('orgsup/<str:pk>/',supo,name="supo"),
      path('tssup/<str:pk>/',supt,name="supt"),
      path('gssup/<str:pk>/',supgs,name="supgs"),
      path('ssup/<str:pk>/',sups,name="sups"),
      path('Encadrech/',rech,name="rechE"),
      path('prorech/',rechp,name="rechp"),
      path('orgrech/',recho,name="recho"),
      path('gsrech/',rechgs,name="rechgs"),
      path('tsrech/',recht,name="recht"),
      path('ssrech/',rechs,name="rechs"),
       path('Promoteur/',pagefive,name="createP"),
       path('Encadreur/',pagesix,name="createE"),
       path('Organisme/',pageseven,name="createO"),
       path('SeDeroule/',pageSedroul,name="Sederoul"),
       path('Sinscrit/',pageInscrit,name="Sinscrit"),
       
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
        path('ST/',stats,name="ST"),
        path('ST2/',stats2,name="ST2"),
        path('ST3/',stats3,name="ST3"),
        path('ST4/',stats4,name="ST4"),
        path('DR/',pagederoule,name="DR"),
      ]

