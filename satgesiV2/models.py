from django.db import models

class Stage (models.Model):  
    anne_univ =  models.DateField
    theme = models.CharField(max_length=15)
    document = models.FileField()
    statut = models.CharField(max_length=10)
    note = models.FloatField(max_length=4)
 

class Encadreur(models.Model):
    Nomncadreur  =models.CharField(max_length=50)
    PrenomEncadreur  =models.CharField(max_length=50)
    Telephone = models.IntegerField()
    Mail = models.EmailField()
    grade  =models.CharField(max_length=50)
    domaineInteret  =models.CharField(max_length=50)

class OrganismeAcceuil(models.Model):
    nomOrganisme = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    RaisonSocial = models.CharField(max_length=50)
    Service = models.CharField(max_length=50)
    Departement = models.CharField(max_length=50)

class Type(Stage):
    Type_Stage = models.CharField(max_length=4)
    # code_Stage = models.ForeignKey("Stage",on_delete=models.CASCADE,null=True)
    DateDebut = models.DateField()
    DateFin = models.DateField()
    NbreStagiare = models.IntegerField()
    idfGroupe = models.ForeignKey("GroupeStagiaire",on_delete=models.SET_NULL,null=True,related_name='+',blank=True) 
    unique_together = ('Type_Stage','code_Stage')

class GroupeStagiaire (models.Model):
    FicheDemande = models.FileField()
    idfEncadreur = models.ForeignKey("Encadreur",on_delete=models.SET_NULL,null=True,blank=True)
    idfpromoteur = models.ForeignKey("Promoteur",on_delete=models.SET_NULL,null=True,blank=True)


class Promoteur(models.Model):
    NomPromoteur = models.CharField(max_length=50)
    PrenomPromoteur = models.CharField(max_length=50)
    telephone =models.IntegerField()
    email = models.EmailField()
    FonctionOccupée =models.CharField(max_length=50)
    domainIntérêt =models.CharField(max_length=50)
    idfOrganisme =  models.ForeignKey("OrganismeAcceuil",on_delete=models.SET_NULL,null=True,blank=True)
    idfGroupe =  models.ForeignKey("GroupeStagiaire",on_delete=models.SET_NULL,null=True,related_name='+',blank=True)

class Stagiere (models.Model):
    matricule = models.IntegerField()
    NomStagiere = models.CharField(max_length=50)
    PrenomStagiere = models.CharField(max_length=50)
    niveau = models.IntegerField()
    DateNaissance = models.DateField()
    idf_Groupe = models.ForeignKey("GroupeStagiaire", on_delete=models.SET_NULL,null=True,blank=True)

class SeDeroule(models.Model):
    TypeStage =  models.ForeignKey("Type",on_delete=models.SET_NULL,null=True,blank=True)
    idfOrganisme =  models.ForeignKey("OrganismeAcceuil",on_delete=models.SET_NULL,null=True,blank=True)
    unique_together = ('Type_Stage','idfOrgranisme')

class Sinscrit(models.Model):
    TypeStage =  models.ForeignKey("Type",on_delete=models.SET_NULL,null=True,blank=True)
    idfGroupe =  models.ForeignKey("GroupeStagiaire",on_delete=models.SET_NULL,null=True,blank=True)
    unique_together = ('Type_Stage','idfGroupe')

