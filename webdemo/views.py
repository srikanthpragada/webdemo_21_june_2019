from django.http import HttpResponse


# Function View
def hello(request):
    return HttpResponse("<h1 style='color:red'>Hello Django</h1>")
