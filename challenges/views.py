from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })

    except Exception as e:
        return HttpResponseNotFound("<h1>This month is not in existence!</h1>")
