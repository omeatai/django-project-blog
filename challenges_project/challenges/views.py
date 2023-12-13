from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def index(request):
    """
    This function handles the index page of the challenges app.
    It returns a simple HTTP response with a message.
    """

    months = list(monthly_challenges.keys())
    context = {
        "months": months
    }
    return render(request, "challenges/index.html", context)


def monthly_challenge_by_number(request, month):
    """
    This function handles the monthly_challenge_by_number page of the challenges app.
    It returns a simple HTTP response with a message.
    """

    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=(redirect_month,))
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    """
    This function handles the monthly_challenge page of the challenges app.
    It returns a simple HTTP response with a message.
    """

    try:
        challenge_text = monthly_challenges[month]
        context = {
            "text": challenge_text,
            "month_name": month.capitalize()
        }
        return render(request, "challenges/challenge.html", context)
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    except Exception as e:
        return HttpResponse(f"<h1>Error: {str(e)}</h1>")
