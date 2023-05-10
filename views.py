from django.shortcuts import render

# Create your views here.


from .models import CareerDetails
from .models import Skills
from .models import Testimonial

# def index(request):
    
#     return render(request,"index.html")

def index(request):
    objC = CareerDetails.objects.all()
    objS = Skills.objects.all()
    objT = Testimonial.objects.all()
    return render(request,"index.html",{'objCar':objC,'objSkill': objS,'objtm':objT})
