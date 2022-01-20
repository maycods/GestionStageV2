from django.contrib import admin

from satgesiV2.models import Stage 
from satgesiV2.models import Encadreur
from satgesiV2.models import OrganismeAcceuil
from satgesiV2.models import Type
from satgesiV2.models import GroupeStagiaire
from satgesiV2.models import Promoteur
from satgesiV2.models import Stagiere
from satgesiV2.models import SeDeroule
from satgesiV2.models import Sinscrit

admin.site.register(Stage)
admin.site.register(Encadreur)
admin.site.register(OrganismeAcceuil)
admin.site.register(Type)
admin.site.register(GroupeStagiaire)
admin.site.register(Promoteur)
admin.site.register(Stagiere)
admin.site.register(SeDeroule)
admin.site.register(Sinscrit)
# Register your models here.
