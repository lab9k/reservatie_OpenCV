from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import camera
import check
import recognize
import face_detection

def index(request):
    return render(request, 'reservatie_open_cv/index.html')


def data(request):
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/data.html')
    if request.method == "POST":
        time_data = request.POST.get('date_value')
        return render(request, 'reservatie_open_cv/loading.html', {'selected_date': time_data})
    return render(request, 'reservatie_open_cv/data.html')


def loading(request):
    # checking if there is some space left.
    # yes: going to loading screen
    # no: return to index with alert message that all spaces are already booked on that day
    if check.searchSpace(0):
        return render(request, 'reservatie_open_cv/loading.html')
    else:
        return render(request, 'reservatie_open_cv/noRooms.html')


def confirmation(request):
    file = open("founded.txt", "r")
    name = file.read()

    #hier nog de zaal dan definitief boeken + de zaal ook tonen!
    return render(request, 'reservatie_open_cv/confirmation.html', {'name': name})


@csrf_exempt
def error(request):
    return render(request, 'reservatie_open_cv/error.html')


@csrf_exempt
def noRoom(request):
    return render(request, 'reservatie_open_cv/noRooms.html')



@csrf_exempt
def camerafunction(request):
    # do something with the your data
    datacam = face_detection.take_picture()
    #datacam = camera.testfunctie()

    return JsonResponse(datacam)


@csrf_exempt
def facerec(request):
    name = recognize.recon(request.POST.get('Time'), request.POST.get('Coord'))
    #name = request.POST.get('Coord')
    file = open("founded.txt", "w")
    file.write(name)
    file.close()

    return JsonResponse(name,safe=False)

