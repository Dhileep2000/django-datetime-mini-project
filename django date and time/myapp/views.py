from django.shortcuts import render
from datetime import datetime



def greets(request):

    date=datetime.now()
    #print(data)

    msg = "Hello Guest !!! Very Good"

    h = int(date.strftime("%H"))

    if h<12:
        msg += "morning !!!"
    elif h<16:
        msg += "afternoon !!"
    else:
        msg += "evening !"

    return render (request,'greet.html',{'data':msg,"date":date})
