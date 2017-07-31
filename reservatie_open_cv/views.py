from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import camera
from datetime import datetime
from subprocess import call
from .models import Zaal, User, Reservatie
import recognize
import face_detection
import json
import mailgun
from django.http import HttpResponse


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
        response.set_cookie(key='datum', value=timestamp)
        return response
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    date = request.COOKIES.get('datum')
    room = request.COOKIES.get('gekozen_zaal')
    name = request.COOKIES.get('naam')

    return render(request, 'reservatie_open_cv/confirmation.html', {'name': name, 'room': room, 'date': date})


@csrf_exempt
def accept(request):
    # gebruiker accepteerde het voorstel dus moet nu gemaild en geboekt worden

    # TODO hier nog zaal definitief boeken + mailen
    mailAddress = request.COOKIES.get('mail')
    date = request.COOKIES.get('datum')
    room = request.COOKIES.get('gekozen_zaal')
    name = request.COOKIES.get('naam')
    text = 'Beste ' + name +  ',\nVolgende zaal: ' + room + 'werd voor u gereserveerd op ' + date + '.\n\nMet vriendelijke groeten,\nLab9000'
    mailgun.send_async_message('postmaster@mail.lab9k.gent', mailAddress, 'zaalboeking', "")

    zaal = request.COOKIES.get('gekozen_zaal')
    cookie_datum = request.COOKIES.get('datum')
    date = datetime.fromtimestamp(cookie_datum / 1e3)

    db_zaal = Zaal.objects.filter(naam=zaal).first()
    reservatie = Reservatie(zaal=db_zaal, date=date)
    reservatie.save()

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
    datacam = face_detection.take_picture()
    # datacam = camera.testfunctie()
    return JsonResponse(datacam)


@csrf_exempt
def facerec(request):
    # do something with the your data

    x = request.POST.get('Coords[x]')
    y = request.POST.get('Coords[y]')
    h = request.POST.get('Coords[h]')
    w = request.POST.get('Coords[w]')
    face_id = recognize.recon(request.POST.get('Time'), (x, y, h, w))
    if face_id == "Unknown":
        return render(request, 'reservatie_open_cv/noPerson.html')
    else:
        # cause images in the trainer.yml needed to have an integer as id
        face_id = int(face_id)
        user = User.objects.filter(face_id=face_id)
        ret = {'naam': user.first_name}
        print(request.POST)

        response = JsonResponse(ret)
        response.set_cookie(key='naam', value=user.first_name)
        response.set_cookie(key='mail', value=user.email)
        return response
