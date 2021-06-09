import challenges
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls.base import reverse

monthly_challenges = {
    "january": "Learn 1 new Skill, to near perfection",
    "february": "Walk 20 minutes everyday, minimum.",
    "march": "Practice Django for 30 mins everyday.",
    "april": "Make a NextJS Project",
    "may": "Make a React Project",
    "june": "Apply Redux Toolkit and Sagas.",
    "july": "Learn CSS Animation",
    "august": "Rewatch Month! No new anime.",
    "september": "Exercise 40 mins everyday",
    "october": "Hacktober",
    "november": "No Shave November",
    "december": "Lazy to do anything actually"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

    except Exception as e:
        return HttpResponseNotFound("This month is not in existence!!")

    return HttpResponse(challenge_text)
