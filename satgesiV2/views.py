from webbrowser import get
from django.shortcuts import render ,redirect
from .models import Encadreur, Stagiere ,Promoteur,OrganismeAcceuil,GroupeStagiaire,Type
from satgesiV2.formEtud import  StagieresForm
from  satgesiV2.formEncadreur import EncadreurForm
from  satgesiV2.formPromoteur import PromoteurForm
from satgesiV2.formOrganisme import OrganismeAcceuilForm
from satgesiV2.formGroupeStagiaire import GroupeStagiaireFrom
from  satgesiV2.formTypeS import TypeForm
# Create your views here.
def pageone (request):
 return render(request,'Firstpage.html')

def pagetwo (request):
 return render(request,'Secondpage.html')

def pagethree (request):
  return render(request,'thirdPage-GStage.html')

def pageacc (request):
    return render(request,'accept.html')

def pagefour (request):
    if request.method == "POST":
       form = StagieresForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formulaire = StagieresForm()
        return render(request,'fourthpage.html',{"formEtud":formulaire})

def pagefive (request):
    if request.method == "POST":
       form = PromoteurForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        form = PromoteurForm()
        return render(request,'FivePage.html',{"formPromoteur":form})

def pagesix (request):
    if request.method == "POST":
       form = EncadreurForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formul = EncadreurForm()
        return render(request,'SixPage.html',{"formEncadreur":formul})


def pageseven(request):
    if request.method == "POST":
       form =  OrganismeAcceuilForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formula = OrganismeAcceuilForm()
        return render(request,'SevenPage.html',{"formOrganisme":formula})


def pageeight(request):
    if request.method == "POST":
       form =  OrganismeAcceuilForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formulair = GroupeStagiaireFrom()
        return render(request,'eightPage.html',{"formGroupeStagiaire":formulair})

def pagenine(request):
    if request.method == "POST":
       form = TypeForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect("accept")
    else:
        formlaire = TypeForm()
        return render(request,'NinePage.html',{"formTypeS":formlaire})

def mod (request, pk):
   Encad  = Encadreur.objects.get(id=pk)
   form = EncadreurForm(instance=Encad)
   if request.method == "POST":
       form = EncadreurForm(data=request.POST,instance=Encad)
       if form.is_valid():
           form.save()
           return redirect("accept")
   
   return render(request,'SixPage.html',{"formEncadreur":form}) 

def sup (request, pk):
    Encad  = Encadreur.objects.get(id=pk)
    if request.method =="POST":
     Encad.delete()
     return redirect("GE")

    return render(request,'sup.html' ,{'item':Encad})  
  


def boxstage (request):
 return render(request,'boxStage.html')

def Gencadreur (request): 
    Encadreurss = Encadreur.objects.all()
    return render(request,'Gencadreur.html', {'Ec':Encadreurss })

def boxstage2 (request):
 return render(request,'box2-Etudiant.html')

def Gstage (request):
 return render(request,'GStage.html')

def Gprom (request):
    Promoteurs = Promoteur.objects.all()
    return render(request,'Gpromoteur.html', {'PR':Promoteurs})

def Gstag (request):
    Stagiares =Stagiere.objects.all()
    return render(request,'Gstagiare.html', {'SG':Stagiares})

def GGstag (request):
    Gstage = GroupeStagiaire.objects.all()
    return render(request,'GGstagiare.html', {'GSG':Gstage})

def Gtype (request):
    GTstage = Type.objects.all()
    return render(request,'Gtypestage.html',{'TS':GTstage})
 
def Gorgan (request):
    Organisme = OrganismeAcceuil.objects.all()
    return render(request,'Gorganime.html', {'or':Organisme})

def stats (request):
 return render(request,'stat.html')
