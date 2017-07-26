from django.shortcuts import render


# Create your views here.

def index(request):
    random_tekst = "hallo ik ben Jef"
    return render(request, 'reservatie_open_cv/index.html', {'test': random_tekst})


def data(request):
    if request.method == "GET":
        return render(request, 'reservatie_open_cv/data.html', {'var_test': "var_test"})
    if request.method == "POST":
        # TODO do something
        pass
    return render(request, 'reservatie_open_cv/data.html', {'var_test': "var_test"})


def loading(request):
    return render(request, 'reservatie_open_cv/loading.html')


def confirmation(request):
    return render(request, 'reservatie_open_cv/confirmation.html')

