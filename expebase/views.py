from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import re
from django.template.defaultfilters import slugify

# Create your views here.

def index(request):
    return HttpResponse("Welcome visit our page")

def dashboard(request):

    # client = MongoClient("localhost", 27017)
    # client = MongoClient("mongodb://localhost:27017/")
    client = MongoClient()
    db = client["mydb"]
    coll = db["Information"]
    # document = {"street": "1225 North King Street", "city": "Wilmington", "state": "Delaware",
    #             "country": "United States"}
    # coll.insert(document)
    

    solution = {'Virtual Mailroom','Virtual Business Address','Mail & Packaging Forward'}
    location = {'Wilmington, Delaware','Marysville, California'}

    if 'solution_select' in request.POST:
        result_solution = request.POST['solution_select']
    else :
        result_solution = "Empty"
    if 'location_select' in request.POST:
        result_location = request.POST['location_select']
    else :
        result_location = "Empty"

    results = ""
    result_location_arr = result_location.split(",")
    
    if len(result_location_arr) > 1:
        city = result_location_arr[0].strip()
        state = result_location_arr[1].strip()
        be_regx = "^"+state
        regx = re.compile(be_regx)
        results = db.Information.find({"solution" : result_solution, "city" : city , "state" : regx })
        #results = db.Information.find({"state" : regx })
    formlink = "expebase/"+slugify(result_location)+"/"+slugify(result_solution)
    return render(request, 'expebase/dashboard.html',{'solution' : solution, 'location': location,'result_solution' : result_solution , 'result_location' : result_location, "results":results, "formlink" : formlink})

def result(request):
    location =  request.POST['location_select']
    solution = request.POST['solution_select']
    return render(request, "expebase/result.html",{'location': location, 'solution' : solution})

