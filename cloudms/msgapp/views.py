from django.shortcuts import render
from datetime import datetime
# import os

# Create your views here.
def msgproc(request):
    datalist = []

    if request.method == 'POST':
        userA = request.POST.get('userA', None)
        userB = request.POST.get('userB', None)
        msg = request.POST.get('msg', None)
        time = datetime.now()

        with open('data.txt', 'a+') as f:
            f.write('{}--{}--{}--{}\n'.format(userA, userB, msg, time.strftime('%Y-%m-%d %H:%M:%S')))

    if request.method == 'GET':
        userC = request.GET.get('userC', None)

        if userC != None:
            with open('data.txt', 'r', errors='ignore') as f:
                for line in f:
                    linedata = line.split('--')
                    if userC == linedata[1]:
                        d = {'userA': linedata[0], 'msg': linedata[2], 'time': linedata[3]}
                        datalist.append(d)

    return render(request,'msgapp.html',{'data':datalist})

def index(request):
    return render(request,'index.html')