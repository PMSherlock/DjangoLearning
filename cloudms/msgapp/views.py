from django.shortcuts import render

# Create your views here.
def msgproc(request):
    # if request.method == 'POST':
    return render(request,'index.html')