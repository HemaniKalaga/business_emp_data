from django.shortcuts import render
from app.models import *
import csv
from django.http import HttpResponse
# Create your views here.
def insert_emp_data(request):
    with open('C:\\Users\\ASUS\\OneDrive\\Desktop\\django projects\\Hemani\\Scripts\\business_emp_data\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IDO=csv.reader(FO)
        next(IDO)
        for i in IDO:
            sr=i[0]
            p=i[1]
            dv=i[2]
            su=i[3]
            st=i[4]
            un=i[5]
            mag=i[6]
            sub=i[7]
            gro=i[8]
            s1=i[9]
            

            BEDO=BusinessEmpData(Series_reference=sr,Period=p,Data_value=dv,Suppressed=su,STATUS=st,UNITS=un,Magnitude=mag,Subject=sub,Group=gro,Series_title_1=s1)
            BEDO.save()

    return HttpResponse('Data is inserted')