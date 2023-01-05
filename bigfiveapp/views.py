

# Create your views here.
from django.shortcuts import render
import joblib
import numpy as np

def predictor(request):
    return render(request, 'main.html')


def EXTinfo(request):
    return render(request, 'extabout.html')

def ESTinfo(request):
    return render(request, 'estabout.html')

def AGRinfo(request):
    return render(request, 'agrabout.html')

def CSNinfo(request):
    return render(request, 'csnabout.html')

def OPNinfo(request):
    return render(request, 'opnabout.html')


def formInfo(request):
    clf = joblib.load('./savedModels/model.joblib');
    lis = []
    
    lis.append(request.GET['EXT1'])
    lis.append(request.GET['EXT2'])
    lis.append(request.GET['EXT3'])
    lis.append(request.GET['EXT4'])
    lis.append(request.GET['EXT5'])
    lis.append(request.GET['EXT6'])
    lis.append(request.GET['EXT7'])
    lis.append(request.GET['EXT8'])
    lis.append(request.GET['EXT9'])
    lis.append(request.GET['EXT10'])

    lis.append(request.GET['EST1'])
    lis.append(request.GET['EST2'])
    lis.append(request.GET['EST3'])
    lis.append(request.GET['EST4'])
    lis.append(request.GET['EST5'])
    lis.append(request.GET['EST6'])
    lis.append(request.GET['EST7'])
    lis.append(request.GET['EST8'])
    lis.append(request.GET['EST9'])
    lis.append(request.GET['EST10'])

    lis.append(request.GET['AGR1'])
    lis.append(request.GET['AGR2'])
    lis.append(request.GET['AGR3'])
    lis.append(request.GET['AGR4'])
    lis.append(request.GET['AGR5'])
    lis.append(request.GET['AGR6'])
    lis.append(request.GET['AGR7'])
    lis.append(request.GET['AGR8'])
    lis.append(request.GET['AGR8'])
    lis.append(request.GET['AGR10'])

    lis.append(request.GET['CSN1'])
    lis.append(request.GET['CSN2'])
    lis.append(request.GET['CSN3'])
    lis.append(request.GET['CSN4'])
    lis.append(request.GET['CSN5'])
    lis.append(request.GET['CSN6'])
    lis.append(request.GET['CSN7'])
    lis.append(request.GET['CSN8'])
    lis.append(request.GET['CSN9'])
    lis.append(request.GET['CSN10'])

    lis.append(request.GET['OPN1'])
    lis.append(request.GET['OPN2'])
    lis.append(request.GET['OPN3'])
    lis.append(request.GET['OPN4'])
    lis.append(request.GET['OPN5'])
    lis.append(request.GET['OPN6'])
    lis.append(request.GET['OPN7'])
    lis.append(request.GET['OPN8'])
    lis.append(request.GET['OPN9'])
    lis.append(request.GET['OPN10'])
    
    data_array = np.asarray(lis)
    arr= data_array.reshape(1,-1)
    ans = clf.predict(arr)
    # output = clf.predict([EXT1,EXT2,EXT3,EXT4,EXT5,EXT6,EXT7,EXT8,EXT9,EXT10,
    #                 EST1,EST2,EST3,EST4,EST5,EST6,EST7,EST8,EST9,EST10,
    #                 AGR1,AGR2,AGR3,AGR4,AGR5,AGR6,AGR7,AGR8,AGR9,AGR10,
    #                 CSN1,CSN2,CSN3,CSN4,CSN5,CSN6,CSN7,CSN8,CSN9,CSN10,
    #                 OPN1,OPN2,OPN3,OPN4,OPN5,OPN6,OPN7,OPN8,OPN9,OPN10])
    if ans[0]==0:
        path1='EXTinfo'
        ans = 'Extroversion'
        val1 = 'Engineer'
        val2 = 'Human Resources'
        val3 = 'Sales manager'
        val4 = 'Professor'
        val5 = 'Recruiter'
        val6 = 'Event Planner'
        val7 = 'customer Service'
        val8 = 'Flight Attendent'
        val9 = 'Counselor'
        val10 = 'Therapist'
    elif ans[0]==1:
        path1='ESTinfo'
        ans = 'Neuroticism'
        val1 = 'Forensic Psychologist'
        val2 = 'Dentist'
        val3 = 'Stockbroker'
        val4 = 'Accountant'
        val5 = 'Yoga Instructor'
        val6 = 'Web development'
        val7 = 'Psychiatric Nurse'
        val8 = 'Social Worker'
        val9 = 'Chef'
        val10 = 'Freelance Designer'
    elif ans[0]==2:
        path1='AGRinfo'
        ans = 'Agreeableness'
        val1 = 'counselor'
        val2 = 'Nurse'
        val3 = 'Non-profit Organisor'
        val4 = 'Teacher'
        val5 = 'Judge'
        val6 = 'Customer Service'
        val7 = 'Therapist'
        val8 = 'Religious Leader'
        val9 = 'Kindergarden Teacher'
        val10 = 'special Education Teacher'
    elif ans[0]==3:
        path1='CSNinfo'
        ans = 'Conscientiousness'
        val1 = 'Doctor'
        val2 = 'Actor'
        val3 = 'Freelance Writer'
        val4 = 'Marketing Consultant'
        val5 = 'Business Owner'
        val6 = 'Advertising Executive'
        val7 = 'Politician'
        val8 = 'Surgeon'
        val9 = 'Pilot'
        val10 = 'Data Analyst'
    elif ans[0]==4:
        path1='OPNinfo'
        ans = 'Openness'
        val1 = 'Artist'
        val2 = 'Software Engineer'
        val3 = 'Travel Writer'
        val4 = 'Graphic Designer'
        val5 = 'Entrepreneur'
        val6 = 'Fashion Designer'
        val7 = 'Philosopher'
        val8 = 'Executive'
        val9 = 'Interior Designer'
        val10 = 'Lawyer'
    else:
        ans =  'Error !!! , The data is not entered correctly' 

       
        
    return render(request, 'result.html',{'result' : ans,
    'pred1': val1, 'pred2':val2, 'pred3':val3, 'pred4':val4,
    'pred5':val5, 'pred6':val6, 'pred7':val7, 'pred8':val8, 
    'pred9':val9, 'pred10':val10, 'path_': path1
    })

    