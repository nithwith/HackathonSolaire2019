from django.shortcuts import render
from django.http import HttpResponse
import urllib.request, json
import pprint
from jinja2 import Template
from app.models import MyForm

# Create your views here.
def index(request):

    #Get data from Grappe.io

    url_base = "https://grappe.io/data/api/5cc62d808dcde8003322d1e6-result_nantes_metro_hackathon"

    # with urllib.request.urlopen(url_base) as url:
    #     data = json.loads(url.read().decode())
    #     print(data)

    # Get data from local json data

    with open('/home/theo/Perso/Projet/Laplusgrosse/app/5cc4c9a488d5c0002f81b12c-result_nantes_metro_hackathon.json') as json_file:
        data = json.load(json_file)

    i=1
    for ville in data:
        ville["rang"]=i
        if ville["note"]:
            ville["note"] = int(ville["note"])

        if ville["prod_indiv"]:
            ville["prod_indiv"] = int(ville["prod_indiv"])
        i=i+1

    win = data[0]["nom_commune"]
    return render(request, 'city-list.html', {'data': data,'win': win})


def city_detail(request):
    data={}
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            data["prod_photovoltaique"] = float(data["prod_photovoltaique"])
            data["prod_eolien"] = float(data["prod_eolien"])
            data["total_prod"] = float(data["total_prod"])
            data["prod_bioenergie"] = float(data["prod_bioenergie"])
            data["prod_cogénération"] = float(data["prod_cogénération"])





    return render(request, 'city-detail.html', {'data': data})

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    with open(
            '/home/theo/Perso/Projet/Laplusgrosse/app/5cc4c9a488d5c0002f81b12c-result_nantes_metro_hackathon.json') as json_file:
        data = json.load(json_file)
    data_top = []
    i = 1
    for ville in data:
        ville["rang"] = i
        if ville["note"]:
            ville["note"] = int(ville["note"])
        if i < 11:
            data_top.append(ville)
        i = i + 1
    return render(request, 'blog-detail.html', {'data': data_top})

def citizen_projects(request):
    return render(request, 'citizen-projects.html')

