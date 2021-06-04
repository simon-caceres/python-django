from django.http import HttpResponse

#utilities
from datetime import datetime

from django.http.response import JsonResponse

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('quibuopapa, current server time its: {now}'.format(
        now=str(now)
    ))

def sort_int(request):
    #import pdb; pdb.set_trace()
    numbers = map(lambda x: int(x), request.GET['numbers'].split(','))
    return JsonResponse({
        "numbers:":
        sorted(numbers)
    }, json_dumps_params={'indent': 4})

def say_hi(request, name, age):
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)
    else:
        message = 'hello, {}! Welcome to platzigram'.format(name)
    return HttpResponse(message)