from django.shortcuts import render,redirect
from proj1.settings import covid19_path
import json
from app1.middleware import data_loading
from django.http import HttpResponse

def showIndex(req):
    data = json.loads(open(covid19_path).read())
    x = [x for x in data]
    x.pop(0)
    return render(req,"index.html",{'data':x})

def state_info(req):
    state = req.GET.get('state')
    data = json.loads(open(covid19_path).read())
    for x,y in data[state].items():
        print(x,"----->",y)
        for i in y:
            print(i,"-->")
    return render(req,'state.html',{'state':state,'data':data[state]})


def total(req):
    data = json.loads(open(covid19_path).read())
    for x in data:
        #z=[i for i in y.active]
        print(x)

def refresh(req):
    data_loading()
    dict_data = json.loads(open(covid19_path).read())
    return render(req,'index.html',{'data':dict_data})