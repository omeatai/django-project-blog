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
    "december": "Learn Django for at least 20 minutes every day!"
}


def index(request):
    """
    This function handles the index page of the challenges app.
    It returns a simple HTTP response with a message.
    """

    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"""
        <h1>These are the challenges for the year:</h1>
        <ul>
            {list_items}
        </ul>
    """

    return HttpResponse(response_data)



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
        # response_data = f"<h1>{challenge_text}</h1>"

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html")
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    except Exception as e:
        return HttpResponse(f"<h1>Error: {str(e)}</h1>")
