from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


challanges = {
    'january':'Drink water',
    'february': 'No meat for the month',
    'march': 'walk 5 kilometers a day',
    'april': 'Learn Djano half an hour a day for the month',
    'may':'Drink water',
    'june': 'No meat for the month',
    'july': 'walk 5 kilometers a day',
    'agust': 'Learn Djano half an hour a day for the month',
    'september':'Drink water',
    'october': 'No meat for the month',
    'november': None,
    'december': 'Learn Djano half an hour a day for the month'
}


def home(request):
    months = list(challanges.keys())
    list_items = ''
    return render(request, 'challanges/index.html', context={'months':months})
    # for month in months:
    #     month_path = reverse('month-challange', args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>" # \ escapes the quotes
    #
    # response_data = f"<ul>{list_items}</ul>"
    #
    # return HttpResponse(response_data)


def monthly_chall_numeric(request, month):
    months = list(challanges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month</h1>')

    challange_text = months[month - 1]
    redirect_path = reverse('month-challange', args=[challange_text])  #challange/january

    return HttpResponseRedirect(redirect_path) # redirect to the path passed to argument


def monthly_challanges(request, month):
    try:
        challange_text = challanges[month]
        # response_data = render_to_string('challanges/challange.html')
        # return HttpResponse(response_data)
        return render(request, 'challanges/challange.html', context={'text': challange_text, 'month': month.capitalize()})
    except:
        return HttpResponseNotFound('<h1>Invalid month entered.</h1>')
