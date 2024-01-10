from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": 'Start Running!',
    "february": 'Eat no meat!',
    "march": 'Learn Django!',
    "april": 'Eat more vegetables!',
    "may": "Eat less carbs!",
    "june": 'Learn Python!',
    "july": 'Learn Java!',
    "august": 'Learn C!',
    "september": 'Learn C++!',
    "october": 'Learn C#!',
    "november": 'Learn Ruby!',
    "december": 'Stop Running!'
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
 

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

                        
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
