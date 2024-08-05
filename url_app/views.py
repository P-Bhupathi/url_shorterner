from django.shortcuts import render, HttpResponse, redirect
from .models import Url_db
import json,secrets,hashlib
from datetime import datetime, timedelta

# Create your views here.

def home(req):
    return render(req,'home.html')

def sort_url(req):
    data = Url_db.objects.filter()

    for i in data:
        vut = i.valid_upto
        vut=datetime.strptime(vut, "%Y-%m-%d %H:%M:%S")
        if datetime.now() >= vut:
            i.delete()
    source_url = req.POST['source_url']

    hex_string = format(secrets.randbits(16), '08x')
    while Url_db.objects.filter(short_url=hex_string):
        hex_string = format(secrets.randbits(16), '08x')

    new_data = Url_db(
        source_url = source_url,
        short_url = hex_string,
        valid_upto = (datetime.now()+timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
    )
    new_data.save()
    dtp={ 'sorted_url': f'https://bhupathi504.pythonanywhere.com/short/{hex_string}' }
    return render(req,'home.html',dtp)

def short(req,id):
    try:
        data = Url_db.objects.filter()

        for i in data:
            vut = i.valid_upto
            vut=datetime.strptime(vut, "%Y-%m-%d %H:%M:%S")
            if datetime.now() >= vut:
                i.delete()
        # print(id)
        data = Url_db.objects.filter(short_url=id)
        for i in data:
            surl=i.source_url
            # print(surl)

        # print(surl)
        return redirect(surl)

    except Exception as e:
        return HttpResponse("<h2>Invalid URL</h2>")