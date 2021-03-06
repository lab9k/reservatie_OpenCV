from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import camera
from datetime import datetime
from subprocess import call
from .models import Zaal, User, Reservatie, FaceUser
import recognize
import face_detection
import json
import mailgun
from django.http import HttpResponse
import time


def index(request):
    # open the index page
    return render(request, 'reservatie_open_cv/index.html')


def data(request):
    # open the data page
    return render(request, 'reservatie_open_cv/data.html')


def loading(request):
    # this methode check get called twice,
    # first time to check if there is a room free if not back to time and date
    # second time to proceed(so free room) and go to the imagetaker
    if request.method == "POST":
        timestamp = float(request.POST.get('date_value'))
        date = datetime.fromtimestamp(timestamp / 1e3)
        alle_zalen = Zaal.objects.all()
        gekozen_zaal = None
        for zaal in alle_zalen:
            if zaal.is_vrij_op_datum(date):
                gekozen_zaal = zaal
                break
        if gekozen_zaal is None:
            return render(request, "reservatie_open_cv/noRooms.html")
        response = render(request, 'reservatie_open_cv/loading.html')
        response.set_cookie(key='gekozen_zaal', value=gekozen_zaal.naam)
        response.set_cookie(key='datum', value=timestamp)
        return response
    # TODO: mag misschien weg herbekijken
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    # person data is alright now all we need is his confirmation
    # send page where we display the data and some buttons
    date = datetime.fromtimestamp(float(request.COOKIES.get('datum')) / 1e3)
    room = request.COOKIES.get('gekozen_zaal')
    name = request.COOKIES.get('naam')
    return render(request, 'reservatie_open_cv/confirmation.html',
                  {'name': name, 'room': room, 'date': date})


@csrf_exempt
def accept(request):
    # user confirmed so mail and save the reservation

    # TODO hier + mailen
    mailAddress = request.COOKIES.get('mail')
    date = request.COOKIES.get('datum')
    room = request.COOKIES.get('gekozen_zaal')
    name = request.COOKIES.get('naam')

    text = 'Beste ' + name + ',\nVolgende zaal: ' + room + 'werd voor u gereserveerd op ' + date + '.\n\nMet vriendelijke groeten,\nLab9000'
    mailgun.send_async_message('postmaster@mail.lab9k.gent', mailAddress,
                               'zaalboeking', "")

    zaal = request.COOKIES.get('gekozen_zaal')
    date = datetime.fromtimestamp(float(request.COOKIES.get('datum')) / 1e3)

    db_zaal = Zaal.objects.filter(naam=zaal).first()
    db_user = FaceUser.objects.filter(first_name=name).first()
    reservatie = Reservatie(for_zaal=db_zaal, date=date, face_user=db_user)
    reservatie.save()

    response = render(request, 'reservatie_open_cv/index.html')
    response.delete_cookie('datum')
    response.delete_cookie('gekozen_zaal')
    response.delete_cookie('naam')
    response.delete_cookie('mail')

    return response


@csrf_exempt
def error(request):
    # get called when a error occurs or unable to detect face
    return render(request, 'reservatie_open_cv/error.html')


@csrf_exempt
def noRoom(request):
    # no space available
    return render(request, 'reservatie_open_cv/noRooms.html')


@csrf_exempt
def noPerson(request):
    # person not recognized
    return render(request, 'reservatie_open_cv/noPerson.html')


@csrf_exempt
def camerafunction(request):
    # call methode for detecting face
    datacam = face_detection.take_picture()
    return JsonResponse(datacam)


@csrf_exempt
def facerec(request):
    # turn out their is a face on the image, so we have to detect whose face
    # it is

    x = request.POST.get('Coords[x]')
    y = request.POST.get('Coords[y]')
    h = request.POST.get('Coords[h]')
    w = request.POST.get('Coords[w]')
    face_id = recognize.recon(request.POST.get('Time'), (x, y, h, w))
    # if we detect one we can proceed else persoon not found
    if face_id == "Unknown":
        ret = {'naam': "None"}

        response = JsonResponse(ret)
        response.set_cookie(key='naam', value="None")
        response.set_cookie(key='mail', value="None")
        return response
    else:
        # cause images in the trainer.yml need an integer as id
        face_id = int(face_id)
        user = FaceUser.objects.get(face_id=face_id)
        ret = {'naam': user.first_name}

        response = JsonResponse(ret)
        response.set_cookie(key='naam', value=user.first_name)
        response.set_cookie(key='mail', value=user.email)
        return response
