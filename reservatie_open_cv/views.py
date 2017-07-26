from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'reservatie_open_cv/index.html')


def data(request):
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/data.html')
    if request.method == "POST":
        time_data = request.POST.get('date_value')
        return render(request, 'reservatie_open_cv/data.html', {'selected_date': time_data})
    return render(request, 'reservatie_open_cv/data.html')


def loading(request):
    return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    name = "Adriaan Glibert"
    return render(request, 'reservatie_open_cv/confirmation.html', {'name': name})


def error(request):
    return render(request, 'reservatie_open_cv/error.html')
