from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import camera
from .models import Zaal
import recognize
import face_detection


def index(request):
    return render(request, 'reservatie_open_cv/index.html')


def data(request):
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/data.html')
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
        return render(request, 'reservatie_open_cv/loading.html', {'gekozen_zaal': gekozen_zaal,
                                                                   'datum': date})
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    file = open("founded.txt", "r")
    name = file.read()

    file = open("freeRoom.txt", "r")
    room = file.read()
    file.close()

    # TODO hier nog zaal definitief boeken: via database
    return render(request, 'reservatie_open_cv/confirmation.html', {'name': name, 'room': room})


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
    name = 'Jorg'
    ret = {'naam': name}
    file = open("founded.txt", "w")
    file.write(name)
    file.close()
    return JsonResponse(ret)
