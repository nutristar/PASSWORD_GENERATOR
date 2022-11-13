from django.shortcuts import render
from .date_now import datetime2
import random
x=datetime2()

# Create your views here.
def about(request):
    return render(request, "about2.html")


def index(request):
    return render(request, "index.html",{"datetoday":x})


def news(request):
    return render(request, "news.html")
def home(request):
    return render(request, "home.html", {"password":" "})

def password2(request):
    thepassword = ""                     #"mir ne zloy prosto ty durachek"
    char=list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("uppercaser"):
        char.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))
    if request.GET.get("numbers"):
        char.extend(list("0987654321"))
    if request.GET.get("specials"):
        char.extend(list(",./:;~!@#$%^&*()_-=+,,,"))

    len=int(request.GET.get("lenth",12))
    for n in range(len):
        thepassword+=random.choice(char)


    return render(request, "passwordhere.html", {"password": thepassword})

def bars(request):
    # ryb=request.GET.get("")
    return render(request, "my.html")

def mycatest(request):
    ryb=request.GET.get("ryba")
    quantityoffish=request.GET.get("quantityoffish")
    wiskas=request.GET.get("wiskas")
    quantityofwiskas=request.GET.get("quantityofwiskas")
    cucumber = request.GET.get("cucumber")
    quantityofcucumbers =request.GET.get("quantityofcucumbers")

    if ryb=="on":
        ryb="Рыба"
    else:
        ryb = " "
    if wiskas=="on":
        wiskas="Вискас"
    else:
        wiskas = " "
    if cucumber=="on":
        cucumber="Огурец???!!!! осторожнее хозяин я не ем огрурцы могу и отомстить ночью на кровать"
    else:
        cucumber = " "


    return render(request, "barsest.html", {"ryba": ryb, "quantityoffish":quantityoffish,"wiskas":wiskas, "quantityofwiskas":quantityofwiskas, "cucumber":cucumber,"quantityofcucumbers":quantityofcucumbers })


