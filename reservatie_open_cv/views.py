from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'reservatie_open_cv/index.html')


def data(request):
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/data.html')
    if request.method == "POST":
        print(request.POST)
        # TODO do something
        pass
    return render(request, 'reservatie_open_cv/data.html')


def loading(request):
    return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    name = "Adriaan Glibert"
    return render(request, 'reservatie_open_cv/confirmation.html', {'name': name})
