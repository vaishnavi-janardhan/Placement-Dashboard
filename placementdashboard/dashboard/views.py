from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dashboard.forms import UserForm, UserProfileInfoForm 
from dashboard.models import Requirements
from dashboard.models import PmaDemand
from dashboard.models import PmaPartner
import csv
from django.utils.encoding import smart_str

def index(request):
    requirements = Requirements.objects.raw(
        'SELECT d.id, created, p.name, jobTitle, gender, certification, lastGradYear, marksPG, marksUG, marks10, marks12, numberOfPositions, bondDetails, bondDuration, compensation, d.location, constraintLocation from pma_demand as d INNER JOIN pma_partner as p on partner_fk = p.id;'         
    )
    
    print (requirements)
    return render(request, 'dashboard/index.html', {'requirements': requirements})

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="requirements.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
		smart_str(u"Sl No"),
		smart_str(u"Date of requirement"),
		smart_str(u"Job Title"),
		smart_str(u"Gender"),
        smart_str(u"Certification required"),
        smart_str(u"Year of last graduation"),
        smart_str(u"Marks PG"),
        smart_str(u"Marks UG"),
        smart_str(u"Marks XII"),
        smart_str(u"Marks X"),
        smart_str(u"Number of positions"),
        smart_str(u"Bond details"),
        smart_str(u"Bond duration"),
        smart_str(u"Compensation"),
        smart_str(u"Work location"),
        smart_str(u"Constraint location"),
	])
    demands = PmaDemand.objects.all()
    for demand in demands:
        writer.writerow([
		    smart_str(demand.id),
		    smart_str(demand.enddate),
		    smart_str(demand.jobtitle),
            smart_str(demand.gender),
            smart_str(demand.certification),
            smart_str(demand.lastgradyear),
            smart_str(demand.markspg),
            smart_str(demand.marksug),
            smart_str(demand.marks12),
            smart_str(demand.marks10),
            smart_str(demand.numberofpositions),
            smart_str(demand.bonddetails),
            smart_str(demand.bondduration),
            smart_str(demand.compensation),
            smart_str(demand.location),
            smart_str(demand.constraintlocation),
	    ])
    return response    

@login_required
def special(request):
    return HttpResponse('You are logged in.')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) 
            else:
                return HttpResponseRedirect("Your account was inactive")
        else:
            print("Someone tried to login and failed.")
            print("They used username : {} and password : {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dashboard/login.html', {})       