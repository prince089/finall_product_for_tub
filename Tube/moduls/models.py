from django.db import models

#from django.db import

STATUS_CHOICES = (
    (0, 'inactive'),
    (1, 'active'),
    (2, 'deleted'),
)


class role(models.Model):
    roleid = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    roleid = models.ForeignKey(role,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
# #
# class Country(models.Model):
#     countryid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     lititude = models.CharField(max_length=22)
#     lonigtude = models.CharField(max_length=22)
#     created = models.DateTimeField(auto_now_add=True)
#     modify = models.DateTimeField(auto_now=True)
#
#
# class Region(models.Model):
#     regionid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     countryid = models.ForeignKey(Country,on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     modify = models.DateTimeField(auto_now=True)
#
#
# class City(models.Model):
#     cityid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     countryid = models.ForeignKey(Country,on_delete=models.CASCADE)
#     regionid = models.ForeignKey(Region,on_delete=models.CASCADE)
#     lititude = models.CharField(max_length=22)
#     lonigtude = models.CharField(max_length=22)
#     created = models.DateTimeField(auto_now_add=True)
#     modify = models.DateTimeField(auto_now=True)


class Client(models.Model):
    clientid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=50)
    compenyname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    #cityid = models.ForeignKey(to='cities_light.City',on_delete=models.CASCADE)
    clientcity = models.CharField(max_length=40)
    clientcountry = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)


class Site(models.Model):
    siteid = models.AutoField(primary_key=True)
    clientid = models.ForeignKey(Client,on_delete=models.CASCADE)
    #disp_siteid = models.CharField(max_length=20)
    sitecity = models.CharField(max_length=50),
    sitecountry = models.CharField(max_length=50)


class Project(models.Model):
    projectid =  models.AutoField(primary_key=True)
    projecttitle = models.CharField(max_length=100)
    siteid = models.ForeignKey(Site,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    projectcity = models.CharField(max_length=40)
    projectcountry = models.CharField(max_length=30)
    #cityid = models.ForeignKey(to='cities_light.City', on_delete=models.CASCADE)
    contecnumber = models.IntegerField()
    state = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)


class Plant(models.Model):
    plantid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    #change client to project and add city
    city = models.CharField(max_length=50,null=True)
    projectid = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)

# class EquepmentMaster(models.Model):
#     equepmentSerialNumbeer = models.CharField(max_length=50)
#     equepmentname = models.CharField(max_length=50,null=True)
#     equepmentid = models.AutoField(primary_key=True)
#     equepmentcity = models.CharField(max_length=100)
#     #cityid = models.ForeignKey(to='cities_light.City', on_delete=models.CASCADE)
#     plantid = models.ForeignKey(Plant,on_delete=models.CASCADE)
#     status = models.IntegerField(choices=STATUS_CHOICES)
#     created = models.DateTimeField(auto_now_add=True)
#     modify = models.DateTimeField(auto_now=True)
#     details = models.CharField(max_length=200)
#     dimension = models.CharField(max_length=50)


class Equepmentdetails2(models.Model):
    equepmentid = models.AutoField(primary_key=True)
    equepmentname = models.CharField(max_length=50)


class Warehouse(models.Model):
    warehouseid = models.AutoField(primary_key=True)
    warehousename = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    werehousecity = models.CharField(max_length=100)
    #cityid = models.ForeignKey(to='cities_light.City', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)


class EquepmentMaster(models.Model):
    equepmentid = models.ForeignKey(Equepmentdetails2,on_delete=models.CASCADE)
    equepmentSerialNumbeer = models.CharField(max_length=50,unique=True)
    equepmentcity = models.CharField(max_length=100,default="in ware house")
    #cityid = models.ForeignKey(to='cities_light.City', on_delete=models.CASCADE)
    plantid = models.ForeignKey(Plant,on_delete=models.CASCADE,null=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    details = models.CharField(max_length=200)
    dimension = models.CharField(max_length=50)
    warehouseid =models.ForeignKey(Warehouse,on_delete=models.CASCADE)






















