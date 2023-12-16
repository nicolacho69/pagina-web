from django.http import HttpResponse


def welcome(request):
    return HttpResponse("WELCOME TO THE JUNGLE. =)")


def welcomeRed(request):
    return HttpResponse("<p style =`color: red;`>WELCOME TO THE JUNGLE. ;)</p>")
