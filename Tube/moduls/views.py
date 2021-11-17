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
    return render(request,'home.html')


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
        #country = request.POST['country']
        city = request.POST['city']
        try:
            client = Client(clientname=name,compenyname=compnyname,email=email,phone=contect_number,address=address,clientcity = city)
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
    plant = Plant.objects.all()
    eq  = Equepmentdetails2.objects.all()
    # citi = Client.objects.all()

    if request.method == 'POST':
        serialnumber = request.POST['serialnumber']
        name = Equepmentdetails2.objects.get(equepmentid=request.POST['idname'])
        cityid = request.POST['cityid']
        plantid= Plant.objects.get(plantid=request.POST['plantid'])
        status = request.POST['status']
        if status == "inactive":
            status = 0
        elif status == "active":
            status = 1
        elif status == "deleted":
            status = 2
        else:
            status = 0
        descripation = request.POST['descripation']
        dimension = request.POST['dimension']

        # ed = Equepmentdetails(equepmentname=name)
        # ed.save()

        try:
            equepment = EquepmentMaster(equepmentid=name,equepmentSerialNumbeer=serialnumber,equepmentcity=cityid,plantid=plantid,status=status,details=descripation,dimension=dimension)
            equepment.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addequepment.html',{'plant':plant,'eq':eq})
        messages.info(request, 'data saved sucess')
        return render(request,'addequepment.html',{'plant':plant,'eq':eq})
    else:
        return render(request, 'addequepment.html',{'plant':plant,'eq':eq})


def addplant(request):
    cliid = Project.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        clientid = Project.objects.get(projectid=request.POST['cid'])
        try:
            plantdata = Plant(title=title, projectid=clientid)
            plantdata.save()
        except:
            messages.info(request, 'please validat your data')
            return render(request, 'addplant.html',{'clid':cliid})
        messages.info(request, 'data saved sucess')
        return render(request,'addplant.html',{'clid':cliid})
    else:

        return render(request, 'addplant.html',{'clid':cliid})


def addproject(request):
    cliid = Client.objects.all()
    if request.method == 'POST':
        title = request.POST['projecttitle']
        clientid = Client.objects.get(clientid=request.POST['cid'])
        print(clientid)
        address = request.POST['address']
        projecctCity = request.POST['projectcity']
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
            prodata = Project(projecttitle=title, clientid=clientid, address=address, projectcity=projecctCity,
                              contecnumber=phonenumber, state=status)
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

