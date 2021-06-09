import challenges
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(f"{month} Bankai")


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Learn 1 new Skill, to near perfection"

    elif month == "february":
        challenge_text = "Walk 20 minutes everyday, minimum."

    elif month == "march":
        challenge_text = "Practice Django for 30 mins everyday."

    else:
        return HttpResponseNotFound("This month is not in existence!!")

    return HttpResponse(challenge_text)
