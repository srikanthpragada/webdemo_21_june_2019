from django.http import HttpResponse
from datetime import datetime

# Function View
def hello(request):
    return HttpResponse("<h1 style='color:red'>Hello Django</h1>")

def wish(request):
    if 'name' in request.GET:
        user = request.GET['name']
    else:
        user = "Guest"

    hour = datetime.now().hour
    if hour < 12:
        msg = "Good Morning"
    elif hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{user}, {msg}</h1>")