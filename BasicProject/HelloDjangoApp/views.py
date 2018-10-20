
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#def index(request):
#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body><br/>"
#    typeOfOneAsString=str(type(html_content))
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X") + "<br/>"   + typeOfOneAsString
#    html_content += "</body></html>"

#    print(type(now))
#    print(type(html_content))
#    print(typeOfOneAsString)
   

#    return HttpResponse(html_content)


## Create your views here.

#def index(request):
#    return HttpResponse("Hello, Django!")


def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )