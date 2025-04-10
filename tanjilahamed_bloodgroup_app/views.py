from django.shortcuts import redirect, render
from . models import blooddonation

# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def add(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        address = request.POST['address']
        bloodgroup = request.POST['bloodgroup']
        donationdate = request.POST['donationdate']

        new_add = blooddonation(name=name, number=number, address=address, bloodgroup=bloodgroup, donationdate=donationdate)
        new_add.save()
        return redirect('view')
        
    else:
        return render(request, 'registration.html')


def display(request):
    display=blooddonation.objects.all()
    context= {'data': display}
    return render(request, 'alldonor.html', context)