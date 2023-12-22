from django.shortcuts import  render

from credentials.models import Department
# Create your views here.

# def index(request):
#     # obj=Place.objects.all()
#     return render(request,'index.html')

def index(request):
    departments = Department.objects.all()
    print(departments)
    return render(request, 'index.html', {'departments': departments})


        