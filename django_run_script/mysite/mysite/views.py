from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys


def button(request):
    return render(request, "home.html")


def output(request):
    print(f"the result of 1+1 is {1 + 1}")
    result = 1 + 1
    return render(request, 'home.html', {'result': result})


def runscript(request):
    param1 = request.POST.get('param1')
    param2 = request.POST.get('param2')
    output = run(["python", 'C:\\python-new-code\\django_run_script\\mysite\\mysite\\testscript.py', param1, param2], shell=False, stdout=PIPE)
    print(output)
    return render(request, 'home.html', {"data1": output.stdout.decode("utf-8")})

def uploadfile(request):
    if request.method == "POST":
        return render(request, 'home.html', {"output": "upload success"})
