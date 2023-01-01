

# Create your views here.
from django.shortcuts import render
import joblib
import numpy as np

def predictor(request):
    return render(request, 'main.html')


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
        ans = 'EXT'
        val1 = 'eg'
        val2 = 'dd'
        val3 = ''
        val4 = ''
        val5 = ''
        val6 = ''
        val7 = ''
        val8 = ''
        val9 = ''
        val10 = ''
    elif ans[0]==1:
        ans = 'EST'
        val1 = 'eg'
        val2 = 'dd'
        val3 = ''
        val4 = ''
        val5 = ''
        val6 = ''
        val7 = ''
        val8 = ''
        val9 = ''
        val10 = ''
    elif ans[0]==2:
        ans = 'AGR'
        val1 = 'eg'
        val2 = 'dd'
        val3 = ''
        val4 = ''
        val5 = ''
        val6 = ''
        val7 = ''
        val8 = ''
        val9 = ''
        val10 = ''
    elif ans[0]==3:
        ans = 'CSN'
        val1 = 'eg'
        val2 = 'dd'
        val3 = ''
        val4 = ''
        val5 = ''
        val6 = ''
        val7 = ''
        val8 = ''
        val9 = ''
        val10 = ''
    elif ans[0]==4:
        ans = 'CSN'
        val1 = 'eg'
        val2 = 'dd'
        val3 = ''
        val4 = ''
        val5 = ''
        val6 = ''
        val7 = ''
        val8 = ''
        val9 = ''
        val10 = ''
    else:
        ans =  'Error !!! , The data is not entered correctly' 

       
        
    return render(request, 'result.html',{'result' : ans,
    'pred1': val1, 'pred2':val2
    })

    