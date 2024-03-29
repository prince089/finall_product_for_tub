from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth


def index(request):
    if request.method == 'POST':
        sbid = request.POST['id']
        password = request.POST['psd']

        user = auth.authenticate(username=sbid,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home/")
        else:
            messages.info(request,'Username or password invalid')
            return redirect("/")

    else:
        return render(request,'index.html')


def home(request):
    equepmentdata = EquepmentMaster.objects.all()
    return render(request,'home.html',{'edt':equepmentdata})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect("/")


def addclient(request):
    if request.method == 'POST':
        name = request.POST['name']
        compnyname = request.POST['compenyName']
        email = request.POST['email']
        contect_number = request.POST['number']
        address = request.POST['address']
        county = request.POST['country']
        #country = request.POST['country']
        city = request.POST['city']
        try:
            client = Client(clientname=name,compenyname=compnyname,email=email,phone=contect_number,address=address,clientcity = city,clientcountry=county)
            client.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request,'addClient.html')
        messages.info(request, 'data saved sucess')
        return render(request, 'addClient.html')


    else:
        return render(request, 'addClient.html')


def registerequipment(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            redata = Equepmentdetails2(equepmentname=name)
            redata.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addregisterEquipment.html')
        messages.info(request, 'data saved !!!')
        return render(request, 'addregisterEquipment.html')


    else:
        return render(request,'addregisterEquipment.html')


def addequepment(request):
    # plant = Project.objects.all()
    eq  = Equepmentdetails2.objects.all()
    warehouse = Warehouse.objects.all()
    # citi = Client.objects.all()

    if request.method == 'POST':
        serialnumber = request.POST['serialnumber']
        name = Equepmentdetails2.objects.get(equepmentid=request.POST['idname'])
        # cityid = request.POST['cityid']
        # plantid= Project.objects.get(projectid=request.POST['plantid'])
        status = 0

        descripation = request.POST['descripation']
        dimension = request.POST['dimension']
        ware =Warehouse.objects.get(warehouseid= request.POST['warehouse'])

        # ed = Equepmentdetails(equepmentname=name)
        # ed.save()

        try:
            equepment = EquepmentMaster(equepmentid=name, equepmentSerialNumbeer=serialnumber, details=descripation,
                                            dimension=dimension, warehouseid=ware,status=status)
            equepment.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addequepment.html',{'eq':eq,'wh':warehouse})
        messages.info(request, 'data saved sucess')
        return render(request,'addequepment.html',{'eq':eq,'wh':warehouse})
    else:
        return render(request, 'addequepment.html',{'eq':eq,'wh':warehouse})


def addplant(request):
    cliid = Site.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        clientid = Site.objects.get(siteid=request.POST['cid'])
        city = request.POST['city']
        try:
            plantdata = Plant(title=title,city=city,siteid=clientid)
            plantdata.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addplant.html',{'clid':cliid})
        messages.info(request, 'data saved sucess')
        return render(request,'addplant.html',{'clid':cliid})
    else:

        return render(request, 'addplant.html',{'clid':cliid})


def addproject(request):
    cliid = Plant.objects.all()
    #sidata = Site.objects.all()
    if request.method == 'POST':
        title = request.POST['projecttitle']
        clientid = Plant.objects.get(plantid=request.POST['cid'])
        #print(clientid)
        address = request.POST['address']
        projecctCity = request.POST['projectcity']
        projectcountry = request.POST['projectcountry']
        phonenumber = request.POST['contectnumber']
        status = request.POST['status']
        if status == "inactive":
            status = 0
        elif status == "active":
            status = 1
        elif status == "deleted":
            status = 2
        else:
            status = 0
        try:
            prodata = Project(projecttitle=title, plantid=clientid, address=address, projectcity=projecctCity,
                              projectcountry=projectcountry,contecnumber=phonenumber, state=status)
            prodata.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addproject.html', {'clid': cliid})
        messages.info(request, 'data saved sucess')
        return render(request,'addproject.html',{'clid':cliid})
    else:
        return render(request, 'addproject.html',{'clid':cliid})


def addwherehouse(request):
    if request.method == 'POST':
        name = request.POST['whname']
        address = request.POST['address']
        city = request.POST['cityid']
        try:
            werehousedata = Warehouse(warehousename=name,address=address,werehousecity=city)
            werehousedata.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addwherehouse.html')
        messages.info(request, 'data saved sucess')
        return render(request,'addwherehouse.html')
    else:
        return render(request, 'addwherehouse.html')


def vclient(request):
    if request.method == 'POST':
        # role1 = role.objects.all()
        # print(role1)
        return render(request,'vclient.html')
    else:
        role1 = Client.objects.all()
        #print(role1)
        return render(request, 'vclient.html',{'role1': role1})


def vequepment(request):
    equepmentdata = EquepmentMaster.objects.all()
    if request.method == 'POST':
        t = Equepmentdetails2.objects.get(equepmentid=request.POST['search'])
        fatch =EquepmentMaster.objects.filter(equepmentid=t)
        return render(request,'vequepment.html',{'ed':equepmentdata,'edt':fatch})
    else:
        #e1 = EquepmentMaster.objects.all()

        return render(request, 'vequepment.html',{'ed':equepmentdata,'edt':equepmentdata})


def vplant(request):
    if request.method == 'POST':
        return render(request,'vplant.html')
    else:
        plantdata = Plant.objects.all()
        return render(request, 'vplant.html',{'pd':plantdata})


def vproject(request):
    if request.method == 'POST':
        return render(request,'vproject.html')
    else:
        projectdata = Project.objects.all()
        return render(request, 'vproject.html',{'pd':projectdata})


def vwherehouse(request):
    if request.method == 'POST':
        return render(request,'vwherehouse.html')
    else:
        werehousedata = Warehouse.objects.all()
        return render(request,'vwherehouse.html',{'wh':werehousedata})


def returnequipmant(request):
    eq = EquepmentMaster.objects.filter(status=1)
    wh = Warehouse.objects.all()
    if request.method == 'POST':
        srno = request.POST['equipment_details']
        #city = request.POST['city']
        ware = Warehouse.objects.get(warehouseid=request.POST['warehouse_details'])
        t = EquepmentMaster.objects.get(equepmentSerialNumbeer=srno)
        try:
            #t.equepmentcity = city
            t.warehouseid = ware
            t.status = 0
            #t.plantid = None
            t.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'returnEquipment.html')
        messages.info(request, 'update sucess')
        return render(request, 'returnEquipment.html',{'eq':eq,'wh':wh})
    else:
        return render(request, 'returnEquipment.html',{'eq':eq,'wh':wh})


def assign(request):
    avalibe_eq = EquepmentMaster.objects.filter(status=0)
    city = Project.objects.all()

    if request.method == 'POST':
        srno = request.POST['equipment_details']
        pland_id = Project.objects.get(projectid = request.POST['city'])
        #status = 1

        t = EquepmentMaster.objects.get(equepmentSerialNumbeer=srno)
        t.status=1
        t.warehouseid = Warehouse.objects.get(warehouseid = 8)
        t.save()
        assigndata = Assignedequipment(projectid=pland_id,subequipmentsr=srno)
        assigndata.save()




        return render(request, 'assigenEquipment.html',{{'ae':avalibe_eq,'city':city}})
    else:
        return render(request, 'assigenEquipment.html',{'ae':avalibe_eq,'city':city})


def addsite(request):
    cldata = Client.objects.all()
    if request.method == 'POST':
        clientid = Client.objects.get(clientid= request.POST['cid'])
        city = request.POST['city']
        country = request.POST['country']
        try:
            sd = Site(clientid=clientid, sitecity=city, sitecountry=country)
            sd.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addsite.html',{'cldata': cldata})
        messages.info(request, 'data saved sucess')
    return render(request, 'addsite.html', {'cldata': cldata})



