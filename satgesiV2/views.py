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

def modpr (request, pk):
   pro = Promoteur.objects.get(id=pk)
   form = PromoteurForm(instance=pro)
   if request.method == "POST":
       form = PromoteurForm(data=request.POST,instance=pro)
       if form.is_valid():
           form.save()
           return redirect("accept")
   
   return render(request,'FivePage.html',{"formPromoteur":form}) 
def modpO (request, pk):
   org = OrganismeAcceuil.objects.get(id=pk)
   form = OrganismeAcceuilForm(instance=org)
   if request.method == "POST":
       form =OrganismeAcceuilForm(data=request.POST,instance=org)
       if form.is_valid():
           form.save()
           return redirect("accept")
   
   return render(request,'SevenPage.html',{"formOrganisme":form}) 
def modpGS (request, pk):
   gs = GroupeStagiaire.objects.get(id=pk)
   form =GroupeStagiaireFrom(instance=gs)
   if request.method == "POST":
       form = GroupeStagiaireFrom(data=request.POST,instance=gs)
       if form.is_valid():
           form.save()
           return redirect("accept")
   
   return render(request,'eightPage.html',{"formGroupeStagiaire":form}) 
def modTS (request, pk):
   ts = Type.objects.get(id=pk)
   form = TypeForm(instance=ts)
   if request.method == "POST":
       form = TypeForm(data=request.POST,instance=ts)
       if form.is_valid():
           form.save()
           return redirect("accept")
   
   return render(request,'NinePage.html',{"formTypeS":form}) 
def modS (request, pk):
   s = Stagiere.objects.get(id=pk)
   form = StagieresForm(instance=s)
   if request.method == "POST":
       form = StagieresForm(data=request.POST,instance=s)
       if form.is_valid():
           form.save()
           return redirect("accept")
   
   return render(request,'fourthpage.html',{"formEtud":form}) 
def sups (request, pk):
    s  = Stagiere.objects.get(id=pk)
    if request.method =="POST":
     s.delete()
     return redirect("GSR")

    return render(request,'sups.html' ,{'item':s})  

def supP (request, pk):
    pro  = Promoteur.objects.get(id=pk)
    if request.method =="POST":
     pro.delete()
     return redirect("GP")

    return render(request,'supp.html' ,{'item':pro})  
def sup (request, pk):
    Encad  = Encadreur.objects.get(id=pk)
    if request.method =="POST":
     Encad.delete()
     return redirect("GE")

    return render(request,'sup.html' ,{'item':Encad}) 
def supo (request, pk):
    org  = OrganismeAcceuil.objects.get(id=pk)
    if request.method =="POST":
     org.delete()
     return redirect("GO")

    return render(request,'supo.html' ,{'item':org}) 
def supt (request, pk):
    ts  = Type.objects.get(id=pk)
    if request.method =="POST":
     ts.delete()
     return redirect("GT")

    return render(request,'supt.html' ,{'item':ts}) 
def supgs (request, pk):
    gs =GroupeStagiaire.objects.get(id=pk)
    if request.method =="POST":
     gs.delete()
     return redirect("GGSR")

    return render(request,'supt.html' ,{'item':gs}) 
def rech (request):
 if request.method =="POST":
     q = request.POST['q']
     Encad  = Encadreur.objects.filter(Nomncadreur__contains= q) 
     return render(request,'rech.html',{'Encad':Encad}) 
 else:
  text = "Aucun resultat"
  return render(request,'rech.html',{'text': text}) 
 
def rechs (request):
 if request.method =="POST":
     q = request.POST['q']
     s  = Stagiere.objects.filter(NomStagiere__contains= q) 
     return render(request,'rechs.html',{'s':s}) 
 else:
  text = "Aucun resultat"
  return render(request,'rechs.html',{'text': text}) 
def rechp (request):
 if request.method =="POST":
     q = request.POST['q']
     pro  = Promoteur.objects.filter(NomPromoteur__contains= q) 
     return render(request,'rechp.html',{'pro':pro}) 
 else:
  text = "Aucun resultat"
  return render(request,'rech.html',{'text': text}) 
def recho (request):
 if request.method =="POST":
     q = request.POST['q']
     org  = OrganismeAcceuil.objects.filter(nomOrganisme__contains= q) 
     return render(request,'recho.html',{'org':org}) 
 else:
  text = "Aucun resultat"
  return render(request,'recho.html',{'text': text}) 
def recht (request):
 if request.method =="POST":
     q = request.POST['q']
     ts  = Type.objects.filter(Type_Stage__contains= q) 
     return render(request,'recht.html',{'ts':ts}) 
 else:
  text = "Aucun resultat"
  return render(request,'recht.html',{'text': text}) 
def rechgs (request):
 if request.method =="POST":
     q = request.POST['q']
     gs  = GroupeStagiaire.objects.filter(id__contains= q) 
     return render(request,'rechgs.html',{'gs':gs}) 
 else:
  text = "Aucun resultat"
  return render(request,'rechgs.html',{'text': text}) 

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
