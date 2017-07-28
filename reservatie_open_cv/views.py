from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import camera
from datetime import datetime
from subprocess import call
from .models import Zaal
<<<<<<< HEAD
import recognize
import face_detection
import json
from django.http import HttpResponse
=======

>>>>>>> 0a1f5fecc65aaae0256225dd49b45d25dc7f3a62

def index(request):

    return render(request, 'reservatie_open_cv/index.html')


def data(request):
    return render(request, 'reservatie_open_cv/data.html')


def loading(request):
    if request.method == "POST":
        timestamp = float(request.POST.get('date_value'))
        date = datetime.fromtimestamp(timestamp / 1e3)
        alle_zalen = Zaal.objects.all()
        gekozen_zaal = None
        for zaal in alle_zalen:
            if zaal.is_vrij_op_datum(date):
                gekozen_zaal = zaal
                break
        response = render(request, 'reservatie_open_cv/loading.html')
        response.set_cookie(key='gekozen_zaal', value=gekozen_zaal)
        response.set_cookie(key='datum', value=date)
        return response
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    date = request.COOKIES.get('datum')
    room = request.COOKIES.get('gekozen_zaal')
    name = request.COOKIES.get('naam')
    mail = request.COOKIES.get('mail')
    # file = open("founded.txt", "r")
    # name = file.read()
    #
    # file = open("freeRoom.txt", "r")
    # room = file.read()
    # file.close()

    return render(request, 'reservatie_open_cv/confirmation.html', {'name': name, 'room': room, 'date': date})


@csrf_exempt
def accept(request):
    #gebruiker accepteerde het voorstel dus moet nu gemaild en geboekt worden

    # TODO hier nog zaal definitief boeken + mailen
    mailAddress = request.COOKIES.get('mail')
    #    call(['bash', 'SendMail.sh', mailAddress, name, date, room])

    response = render(request, 'reservatie_open_cv/index.html')
    response.delete_cookie('datum')
    response.delete_cookie('gekozen_zaal')
    response.delete_cookie('naam')
    response.delete_cookie('mail')

    return response


@csrf_exempt
def error(request):
    return render(request, 'reservatie_open_cv/error.html')


@csrf_exempt
def noRoom(request):
    return render(request, 'reservatie_open_cv/noRooms.html')


@csrf_exempt
def noPerson(request):
    return render(request, 'reservatie_open_cv/noPerson.html')


@csrf_exempt
def camerafunction(request):
    # do something with the your data
    # datacam = camera.testfunctie()
    # {Time:string,success:string,(int,int,int,int)}
    # datacam = face_detection.take_picture()
    datacam = camera.testfunctie()
    return JsonResponse(datacam)


@csrf_exempt
def facerec(request):
    # do something with the your data

    # x = request.POST.get('Coords[x]')
    # y = request.POST.get('Coords[y]')
    # h = request.POST.get('Coords[h]')
    # w = request.POST.get('Coords[w]')
    # name = recognize.recon(request.POST.get('Time'), (x, y, h, w))
    # if(name == "Unknown"):
    #     return render(request, 'reservatie_open_cv/noPerson.html')
    # else:
    #     ret = {'naam': name}
    #     print(request.POST)
    #     file = open("founded.txt", "w")
    #     file.write(name)
    #     file.close()
    #     return JsonResponse(ret)


    # hier dus van bij de persoon die FR teruggeeft ook het mailadres instellen in de cookie
    name = 'Jorg'
    mailaddress = 'test@hotmail.com'
    ret = {'naam': name}
    # file = open("founded.txt", "w")
    # file.write(name)
    # file.close()
    response = JsonResponse(ret)
    response.set_cookie(key='naam', value=name)
    response.set_cookie(key='mail', value=mailaddress)
    return response
