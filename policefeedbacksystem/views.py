from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import path
from databaseReport.models import displayReport, stateWisePoliceStation

from . import views

def loginpage(request):
    render(request, "Auth/index.html")
    
def reportpage(request):
    if 'user' in request.session:       
        return render(request, "report.html")
    else:
        return redirect('loginpage')

def generateqrcode(request):
    policeStationWiseData = stateWisePoliceStation.objects.raw("SELECT DISTINCT POLICE_STATION, id FROM databasereport_statewisepolicestation")
    stateWiseData = stateWisePoliceStation.objects.raw("SELECT DISTINCT STATE, id FROM databasereport_statewisepolicestation group by state")
    data = {'policeStation': policeStationWiseData, 'stateWiseData' : stateWiseData, 'hidden' : 'hidden' }

    if request.method == 'POST':
        messages.success(request, "Get Method Detected")
        state_name = request.POST.get('state')
        police_name = request.POST.get('sub_police')
        state_name+=police_name
        file_name = str(state_name)
        print(file_name)
        query=f"SELECT id, qr_code from databasereport_statewisepolicestation where qr_code =\'qrCodes/{file_name}.png\'"
        query = stateWisePoliceStation.objects.raw(str(query))
        query = str(query[0].qr_code)
        data = {'policeStation': policeStationWiseData, 'stateWiseData' : stateWiseData, 'query': query, 'hidden' : '' }
        print(query)
        return render(request, "index.html", data)

    return render(request, "index.html", data)


def reportpage(request):
    # displayReportData= displayReport.objects.all()
    policeStationWiseData = stateWisePoliceStation.objects.raw("SELECT DISTINCT POLICE_STATION, id FROM databasereport_statewisepolicestation")
    stateWiseData = stateWisePoliceStation.objects.raw("SELECT DISTINCT STATE, id FROM databasereport_statewisepolicestation group by state")
    data = {'policeStation': policeStationWiseData, 'stateWiseData' : stateWiseData, 'showTable': 'No' }

    if request.method == "POST":
            bydate = request.POST['bydate']
            sorttimetaken = request.POST['sorttimetaken']
            sortdata = request.POST['sortdata']
            state_name = request.POST['state']
            police_station = request.POST['sub_police']


            if police_station != 'None' and state_name != 'None':
                messages.error(request, "Please Select Only  One of Police Station or State Wise")
                data = {'policeStation': policeStationWiseData, 'stateWiseData': stateWiseData, 'showTable': 'No'}
                return render(request, "report.html", data)
            elif police_station == 'None' and state_name == 'None':
                messages.warning(request, "Please Select Any One From Police Station or State Wise")
                data = {'policeStation': policeStationWiseData, 'stateWiseData': stateWiseData,
                        'showTable': 'No'}
                return render(request, "report.html", data)
            else:
                bydate = 'date' if bydate == 'select' else 'date = \''+str(bydate)+'\''
                if sortdata == 'default' :
                    sortdata = 'order by id'
                elif sortdata == 'ascending':
                    sortdata = 'order by rating asc'
                elif sortdata == 'descending':
                    sortdata = 'order by rating desc'
                state_name ='state = 0' if state_name == 'None' else 'state= \''+str(state_name)+'\''
                police_station = 'police_station = 0' if police_station == 'None' else 'police_station= \'' + str(police_station) + '\''
                sqlQuery = "select * from databasereport_displayreport where "+str(police_station) +" and " + str(state_name) + " and " + str(bydate)+" "+ str(sortdata)
                displayReportData = displayReport.objects.raw(str(sqlQuery))
                try:
                    displayReportData[0].id
                except:
                    messages.error(request, "No Data Found")
                    data = {'policeStation': policeStationWiseData, 'stateWiseData': stateWiseData,
                        'showTable': 'no', "displayReportData" : displayReportData }
                    return render(request, "report.html", data)

                data = {'policeStation': policeStationWiseData, 'stateWiseData': stateWiseData,
                        'showTable': 'yes', "displayReportData" : displayReportData }
                return render(request, "report.html", data)
    # data = {'displayReportData': displayReportData, 'showTable': 'yes'}
    return render(request, "report.html", data)

def saveData(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        state_name = request.POST.get('state_name')
        police_station = request.POST.get('police_station')
        name = request.POST.get('name')
        how_come = request.POST.get('how_come')
        time_taken = request.POST.get('time_taken')
        feedback = request.POST.get('feedback')
        stars = request.POST.get('stars')
        print(phone_number, state_name,police_station, name, how_come, time_taken, feedback, stars)
        sqlData = displayReport(name = name, state = state_name, police_station = police_station, how_come = how_come, time_taken = time_taken, feedback = feedback, number = phone_number, rating =  stars)
        sqlData.save()
        messages.success(request, "Feedback Taken SucessFully")
        return redirect('loginpage')

def feedback_form(request,name):
    name = name.split("-")
    state_name = name[0]
    police_name = name[1]
    data = {'state_name' : state_name, 'police_name' : police_name}
    if request.method == 'POST':
        phone_number = request.POST.get('number')
        print(phone_number)
        print(state_name)
        print(police_name)
        data = {'state_name' : state_name, 'police_name' : police_name, 'phone_number':phone_number}
        return render(request, "feedbackform.html",data)

    return render (request, "optAuth.html", data)



def generateqrcode(request):
    if 'user' in request.session:       
        return render(request, "generate_qrcode.html")
    else:
        return redirect('loginpage')

    def visualrepresentation(request):
        if 'user' in request.session:
            return render(request, "visualrepresentation.html")
        else:
            return redirect('loginpage')

def visualrepresentation(request):

    policeStationWiseData = stateWisePoliceStation.objects.raw("SELECT DISTINCT POLICE_STATION, id FROM databasereport_statewisepolicestation")
    stateWiseData = stateWisePoliceStation.objects.raw("SELECT DISTINCT STATE, id FROM databasereport_statewisepolicestation group by state")
    data = {'stateWiseData' : stateWiseData, 'policeStationWiseData': policeStationWiseData}
    if request.method == "POST":
        state_name=request.POST['state']
        police_station = request.POST['sub_police']
        visualRepresentationQuery = None
        if state_name != "None" and police_station == "None":
            visualRepresentationQuery = stateWisePoliceStation.objects.raw(f"SELECT id, police_station as 'Iteam',count(police_station) as number FROM databasereport_displayreport where state = '{state_name}' GROUP BY police_station")
            data = {'stateWiseData' : stateWiseData, 'policeStationWiseData': policeStationWiseData, 'visualRepresentationQuery': visualRepresentationQuery , 'allowed' : 'yes'}
            return render(request,"visualrepresentation.html",data)

        elif state_name == "None" and police_station != "None":
            visualRepresentationQuery = stateWisePoliceStation.objects.raw("SELECT id,police_station as 'Iteam', count(*) as number FROM databasereport_displayreport GROUP BY police_station")
            data = {'stateWiseData' : stateWiseData, 'policeStationWiseData': policeStationWiseData, 'visualRepresentationQuery': visualRepresentationQuery , 'allowed' : 'yes'}
            return render(request,"visualrepresentation.html",data)

        elif state_name != "None" and police_station != "None":
            messages.error (request, "Enter in Only One of Field")
            data = {'stateWiseData' : stateWiseData, 'policeStationWiseData': policeStationWiseData,'allowed' : 'yes'}

            return render(request,"visualrepresentation.html",data)

        else:
            messages.warning(request, "Select one of the Options before Submiting")
            data = {'stateWiseData' : stateWiseData, 'policeStationWiseData': policeStationWiseData,'allowed' : 'yes'}
            return render(request,"visualrepresentation.html",data)

    return render(request,"visualrepresentation.html",data)