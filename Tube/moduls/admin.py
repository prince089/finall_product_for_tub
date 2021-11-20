from django.contrib import admin
from .models import *


class roleAdmin(admin.ModelAdmin):
    list_display = ('roleid','name','created','modify')


admin.site.register(role,roleAdmin)


class userAdmin(admin.ModelAdmin):
    list_display = ('userid', 'roleid', 'name', 'password','email','phone','status','created','modify')


admin.site.register(User,userAdmin)

#
# class userCountry(admin.ModelAdmin):
#     list_display =('countryid', 'name', 'lititude', 'lonigtude', 'created', 'modify')
#
#
# admin.site.register(Country,userCountry)
#
#
# class userRegion(admin.ModelAdmin):
#     list_display = ('regionid','name','countryid','created','modify')
#
#
# admin.site.register(Region,userRegion)
#
#
# class userCity(admin.ModelAdmin):
#     list_display = ('cityid','name','countryid','regionid','lititude','lonigtude','created','modify')
#
#
# admin.site.register(City,userCity)


class userClient(admin.ModelAdmin):
    list_display =('clientid','clientname','compenyname','email','phone','address','clientcity','clientcountry','created','modify')


admin.site.register(Client,userClient)


class userProject(admin.ModelAdmin):
    list_display =('projectid','projecttitle','siteid','address','projectcity','projectcountry','contecnumber','state','created','modify')


admin.site.register(Project,userProject)


class userPlant(admin.ModelAdmin):
    list_display = ('plantid','title','city','projectid','created','modify')


admin.site.register(Plant,userPlant)

class useEquepmentMaster(admin.ModelAdmin):
    list_display = ('equepmentid','equepmentSerialNumbeer','equepmentcity','plantid','status','created','modify','details','dimension','warehouseid')


admin.site.register(EquepmentMaster,useEquepmentMaster)


class userEqEquepmentdetails(admin.ModelAdmin):
    list_display = ('equepmentid','equepmentname')


admin.site.register(Equepmentdetails2,userEqEquepmentdetails)


class userwhWarehouse(admin.ModelAdmin):
    list_display = ('warehouseid','warehousename','address','werehousecity','created','modify')


admin.site.register(Warehouse,userwhWarehouse)


class userSite(admin.ModelAdmin):
    list_display = ('siteid','clientid','sitecity','sitecountry','created','modify')


admin.site.register(Site,userSite)
