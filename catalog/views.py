from django.shortcuts import render, redirect
from datetime import datetime
from .forms import PublisherForm
import requests
import sqlite3


# Create your views here.

def index(request):
    return render(request,
                  'index.html',  # template
                  {'now': str(datetime.now())}  # Context
                  )


def country_info(request):
    if 'code' in request.POST:
        # get info about country and send info to template
        code = request.POST['code']
        resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
        if resp.status_code == 200:
            info = resp.json()
            return render(request, 'country.html',
                          {'info': info, 'code': code})
        else:
            return render(request, 'country.html',
                          {'error': 'Country not found!', 'code': code})
    else:
        return render(request, 'country.html')


def add_publisher(request):
    if request.method == "GET":
        form = PublisherForm() # Unbound form
        return render(request, 'add_publisher.html', {'form': form})
    else:  # POST request
        form = PublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            contact = form.cleaned_data["contact"]

            con = sqlite3.connect(r"e:\classroom\python\june21\catalog.db")
            cur = con.cursor()
            cur.execute("insert into publishers (name,email,contact) values(?,?,?)",
                        (name, email, contact))
            con.commit()
            cur.close()
            con.close()
            return redirect("/catalog/add_publisher/")
        else:  # input errors, so redisplay form
            return render(request, 'add_publisher.html', {'form': form})


def list_publishers(request):
    con = sqlite3.connect(r"e:\classroom\python\june21\catalog.db")
    cur = con.cursor()
    cur.execute("select * from publishers order by id")
    rows = cur.fetchall()
    cur.close()
    con.close()
    return render(request, 'list_publishers.html', {'publishers': rows})
