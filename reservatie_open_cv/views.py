from django.shortcuts import render


# Create your views here.

def index(request):
    random_tekst = "hallo ik ben Jef"
    return render(request, 'reservatie_open_cv/index.html', {'test': random_tekst})


def data(request):
    return render(request, 'reservatie_open_cv/data.html', {'var_test': "var_test"})

