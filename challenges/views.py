from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

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
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
 

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
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        raise Http404()
