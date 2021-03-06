from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from datetime import datetime

from dashboard.forms import UserForm, UserProfileInfoForm
from dashboard.models import Requirements
from dashboard.models import PmaDemand
from dashboard.models import PmaPartner
from dashboard.models import SelfPlaced
from dashboard.models import ActiveDrives
from dashboard.models import DrivesReport
import csv
from django.utils.encoding import smart_str

def index(request):
    return render(request, 'dashboard/index.html')

def requirements(request):
    return render(request, 'dashboard/requirements.html')

def selfPlaced(request):
    selfPlacedStudents = None
    return render(request, 'dashboard/selfPlaced.html', {'selfPlacedStudents' : selfPlacedStudents})

def getSelfPlaced(request):
    batchID = request.POST.get('batch ID')
    print(batchID)
    selfPlacedStudents = SelfPlaced.objects.raw(
        'SELECT firstName, lastName, batch, id, skill, selfPlacedWith, email, mobile, '
        'lastGradYear, collegeName from pma_trainee where selfPlacedWith IS NOT NULL '
        'AND selfPlacedWith NOT LIKE \"\"'
        ' AND batch = \'' + batchID + '\';'
    )
    return render(request, 'dashboard/selfPlaced.html', {'selfPlacedStudents' : selfPlacedStudents})

def activeDrives(request):
    activeDrives = ActiveDrives.objects.raw(
        'SELECT drive_fk as id, @a := @a + 1 slno, name, date FROM pma_selection_round '
        'INNER JOIN pma_drive ON drive_fk = pma_drive.id, (select @a := 0) '
        'as a where roundNumber = 0;'
    )
    for drive in activeDrives:
        print(drive.slno)
    return render(request, 'dashboard/activeDrives.html', {'activeDrives' : activeDrives})

def drivesReport(request):
    drives = None
    return render(request, 'dashboard/drivesReport.html', {'drives' : drives})

def getDrivesReport(request):
    startdate = request.POST.get('startDate')
    enddate = request.POST.get('endDate')
    print(startdate)
    startdate = datetime.strptime(startdate, "%Y-%m-%d").strftime("%d-%m-%Y")
    enddate = datetime.strptime(enddate , "%Y-%m-%d").strftime("%d-%m-%Y")
    print('SELECT pma_selection_round.id, date, pma_drive.name, roundNumber, skills, numberOfPositions, '
        'compensation,rounds FROM pma_selection_round INNER JOIN pma_drive '
        'ON drive_fk = pma_drive.id INNER JOIN pma_demand_skills ON demand_fk '
        '= demand_id INNER JOIN pma_demand ON demand_fk = pma_demand.id '
        'INNER JOIN pma_drive_rounds on roundNumber = round_num AND '
        'drive_id = drive_fk WHERE row(drive_fk,roundNumber) IN '
        '(SELECT drive_fk,max(roundNumber) FROM pma_selection_round GROUP BY '
        'drive_fk) AND date between \'' + startdate + '\' AND \'' + enddate + '\';')
    drives = DrivesReport.objects.raw(
        'SELECT pma_selection_round.id, date, pma_drive.name, roundNumber, skills, numberOfPositions, '
        'compensation,rounds FROM pma_selection_round INNER JOIN pma_drive '
        'ON drive_fk = pma_drive.id INNER JOIN pma_demand_skills ON demand_fk '
        '= demand_id INNER JOIN pma_demand ON demand_fk = pma_demand.id '
        'INNER JOIN pma_drive_rounds on roundNumber = round_num AND '
        'drive_id = drive_fk WHERE row(drive_fk,roundNumber) IN '
        '(SELECT drive_fk,max(roundNumber) FROM pma_selection_round GROUP BY '
        'drive_fk) AND date between \'' + startdate + '\' AND \'' + enddate + '\';'
    )

    for drive in drives:
        print(drive.rounds)
    return render(request, 'dashboard/drivesReport.html', {'drives' : drives})

def getfile(request):
    startdate = request.POST.get('startDate')
    enddate = request.POST.get('endDate')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="requirements.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
		smart_str(u"Sl No"),
		smart_str(u"Date of requirement"),
        smart_str(u"Partner"),
		smart_str(u"Job Title"),
        smart_str(u"Skills"),
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
    requirements = Requirements.objects.raw(
            'SELECT d.id, created, p.name, jobTitle, skills, gender, certification, lastGradYear, '
            'marksPG, marksUG, marks10, marks12, numberOfPositions, bondDetails, bondDuration, '
            'compensation, d.location, constraintLocation from pma_demand as d '
            'INNER JOIN pma_partner as p on partner_fk = p.id INNER JOIN pma_demand_skills on demand_id = d.id '
            'WHERE created BETWEEN \'' + startdate + ' \' AND \'' + enddate + '\';'
    )
    for req in requirements:
        writer.writerow([
		    smart_str(req.id),
		    smart_str(req.created),
            smart_str(req.name),
		    smart_str(req.jobTitle),
            smart_str(req.skills),
            smart_str(req.gender),
            smart_str(req.certification),
            smart_str(req.lastGradYear),
            smart_str(req.marksPG),
            smart_str(req.marksUG),
            smart_str(req.marks12),
            smart_str(req.marks10),
            smart_str(req.numberOfPositions),
            smart_str(req.bondDetails),
            smart_str(req.bondDuration),
            smart_str(req.compensation),
            smart_str(req.location),
            smart_str(req.constraintLocation),
	    ])
    return response

@login_required
def special(request):
    return HttpResponse('You are logged in.')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

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