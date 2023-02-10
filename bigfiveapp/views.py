# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


#import models

rf = joblib.load('./savedModels/vak1model.joblib')
clf = joblib.load('./savedModels/newmodel.joblib')


def predictor(request):
    return render(request, 'home.html')

def mbti(request):
    return render(request, 'mbti.html')

def big5(request):
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
    lis = []
    
    lis.append(request.GET['EXT1'])
    lis.append(request.GET['EXT3'])
    lis.append(request.GET['EXT4'])
    lis.append(request.GET['EXT5'])
    lis.append(request.GET['EXT6'])
    lis.append(request.GET['EXT9'])
    lis.append(request.GET['EXT10'])

    lis.append(request.GET['EST1'])
    lis.append(request.GET['EST2'])
    lis.append(request.GET['EST4'])
    lis.append(request.GET['EST5'])
    lis.append(request.GET['EST6'])
    lis.append(request.GET['EST7'])
    lis.append(request.GET['EST9'])

    lis.append(request.GET['AGR2'])
    lis.append(request.GET['AGR3'])
    lis.append(request.GET['AGR4'])
    lis.append(request.GET['AGR5'])
    lis.append(request.GET['AGR6'])
    lis.append(request.GET['AGR8'])
    lis.append(request.GET['AGR10'])

    lis.append(request.GET['CSN1'])
    lis.append(request.GET['CSN3'])
    lis.append(request.GET['CSN4'])
    lis.append(request.GET['CSN5'])
    lis.append(request.GET['CSN6'])
    lis.append(request.GET['CSN9'])
    lis.append(request.GET['CSN10'])

    lis.append(request.GET['OPN1'])
    lis.append(request.GET['OPN2'])
    lis.append(request.GET['OPN3'])
    lis.append(request.GET['OPN5'])
    lis.append(request.GET['OPN7'])
    lis.append(request.GET['OPN8'])
    lis.append(request.GET['OPN9'])
    
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

def vakpredictor(request):
    if request.method == 'POST':
        q1 = request.POST['q1']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']
        q7 = request.POST['q7']
        q8 = request.POST['q8']
        q9 = request.POST['q9']
        q10 = request.POST['q10']
        q11 = request.POST['q11']
        q12 = request.POST['q12']
        q13 = request.POST['q13']
        q14 = request.POST['q14']
        q15 = request.POST['q15']
        q16 = request.POST['q16']
        q17 = request.POST['q17']

        y_pred = rf.predict([[q1,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17]])
       
        V=int(q3)+int(q4)+int(q5)+int(q6)+int(q7)
        A=int(q8)+int(q9)+int(q10)+int(q11)+int(q12)
        K=int(q13)+int(q14)+int(q15)+int(q16)+int(q17)
        
       
        if y_pred[0] == 0:
            y_pred = 'Visual'
            des = 'by seeing new information'
            tip= 'Lean into the visual side of class'
            tip1= 'Create your own designs and diagrams for data'
            tip2= 'Minimize visual distractions during class'
            tip3= 'Takes engaging notes'
        elif y_pred[0] == 2:
            y_pred = 'Auditary'
            tip= 'Turn up volume'
            des= 'by listening and reading out loud'
            tip1= 'Use headphones for virtual classes'
            tip2= 'Listen to lectures with the screen turned off'
            tip3= 'Read material out loud'
        elif y_pred[0] == 1:
            y_pred = 'Kinesthetics'
            tip= 'Incorporate activity into classes'
            des= 'through hands-on experience'
            tip1= 'Listen to lectures while walking'
            tip2= 'Use a standing or walking desk at home'
            tip3= 'Keep a fidget toy'
        else:
            y_pred='not found'
        return render(request, 'vakresult.html', {'result' : y_pred, 'des':des,'tip':tip, 'tip1' : tip1, 'tip2':tip2, 'tip3': tip3, 'V':V, 'A':A, 'K': K})
    return render(request, 'vak.html')

def radar_chart(request):
    return render(request, 'vakresult.html')

def take_test(request):
  questions = [
        {'question': '1.At a party do you:', 'a': 'Interact with many, including strangers', 'b': 'Interact with a few, known to you'},
        {'question': '2.Are you more:' ,'a': 'Realistic than speculative', 'b': 'Speculative than realistic'},
        {'question': '3.Is it worse to:', 'a': 'Have your “head in the clouds”', 'b': 'Be “in a rut”'},
        {'question': '4.Are you more impressed by:', 'a':'Principles', 'b': 'Emotions'},
        {'question': '5.Are more drawn toward the:', 'a': 'Convincing', 'b': 'Touching'},
        {'question': '6.Do you prefer to work:' ,'a': 'To deadlines', 'b': 'Just “whenever”'},
        {'question': '7.Do you tend to choose:', 'a': 'Rather carefully', 'b': 'Somewhat impulsively'},
        {'question': '8.At parties do you:', 'a': 'Stay late, with increasing energy', 'b': 'Leave early with decreased energy'},
        {'question': '9.Are you more attracted to:', 'a': 'Sensible people', 'b': 'Imaginative people'},
        {'question': '10.Are you more interested in:', 'a': 'What is actual', 'b': 'What is possible'},
        {'question': '11.In judging others are you more swayed by:', 'a': 'Laws than circumstances', 'b': 'Circumstances than laws'},
        {
        'question': '12.In approaching others is your inclination to be somewhat:',
        'a': 'Objective',
        'b': 'Personal'
        },
        {
        'question': '13.Are you more:',
        'a': 'Punctual',
        'b': 'Leisurely'
        },
        {
        'question': '14.Does it bother you more having things:',
        'a': 'Incomplete',
        'b': 'Completed'
        },
        {
        'question': '15.In your social groups do you:',
        'a': 'Keep abreast of other’s happenings',
        'b': 'Get behind on the news'
        },
        {
        'question': '16.In doing ordinary things are you more likely to:',
        'a': 'Do it the usual way',
        'b': 'Do it your own way'
        },
        {
        'question': '17.Writers should:',
        'a': '“Say what they mean and mean what they say”',
        'b': 'Express things more by use of analogy'
        },
        {
        'question': '18.Which appeals to you more:',
        'a': 'Consistency of thought',
        'b': 'Harmonious human relationships'
        },
        {
        'question': '19.Are you more comfortable in making:',
        'a': 'Logical judgments',
        'b': 'Value judgments'
        },
        {
        'question': '20.Do you want things:',
        'a': 'Settled and decided',
        'b': 'Unsettled and undecided'
        },
        {'question': '21.Would you say you are more:', 'a': 'Serious and determined', 'b': 'Easy-going'},
        {'question': '22.In phoning do you:', 'a': 'Rarely question that it will all be said', 'b': 'Rehearse what you’ll say'},
        {'question': '23. Facts:', 'a': '“Speak for themselves”', 'b': 'Illustrate principles'},
        {'question': '24.Are visionaries:', 'a': 'somewhat annoying', 'b': 'rather fascinating'},
        {'question': '25. Are you more often:', 'a': 'a cool-headed person', 'b': 'a warm-hearted person'},
        {'question': '26. Is it worse to be:', 'a': 'unjust', 'b': 'merciless'},
        {'question': '27. Should one usually let events occur:', 'a': 'by careful selection and choice', 'b': 'randomly and by chance'},
        {'question': '28. Do you feel better about:', 'a': 'having purchased', 'b': 'having the option to buy'},
        {'question': '29. In company do you:', 'a': 'initiate conversation', 'b': 'wait to be approached'},
        {'question': '30. Common sense is:', 'a': 'rarely questionable', 'b': 'frequently questionable'},
        {'question': '31. Children often do not:', 'a': 'make themselves useful enough', 'b': 'exercise their fantasy enough'},
        {'question': '32. In making decisions do you feel more comfortable with:', 'a': 'standards', 'b': 'feelings'},
        {'question': '33. Are you more:', 'a': 'firm than gentle', 'b': 'gentle than firm'},
        {'question': '34. Which is more admirable:', 'a': 'the ability to organize and be methodical', 'b': 'the ability to adapt and make do'},
        {'question': '35. Do you put more value on:', 'a': 'infinite', 'b': 'open-minded'},
        {'question': '36. Does new and non-routine interaction with others:', 'a': 'stimulate and energize you', 'b': 'tax your reserves'},
        {'question': '37. Are you more frequently:', 'a': 'a practical sort of person', 'b': 'a fanciful sort of person'},
        {'question': '38. Are you more likely to:', 'a': 'see how others are useful', 'b': 'see how others see'},
        {'question': '39. Which is more satisfying:', 'a': 'to discuss an issue thoroughly', 'b': 'to arrive at agreement on an issue'},
        {'question': '40. Which rules you more:', 'a': 'your head', 'b': 'your heart'},
        {'question': '41. Are you more comfortable with work that is:', 'a': 'contracted', 'b': 'done on a casual basis'},
        {'question': '42. Do you tend to look for:', 'a': 'the orderly', 'b': 'whatever turns up'},
        {'question': '43. Do you prefer:', 'a': 'many friends with brief contact', 'b': 'a few friends with more lengthy contact'},
        {'question': '44. Do you go more by:', 'a': 'facts', 'b': 'principles'},
        {'question': '45. Are you more interested in:', 'a': 'production and distribution', 'b': 'design and research'},
        {'question': '46. Which is more of a compliment:', 'a': '“There is a very logical person.”', 'b': '“There is a very sentimental person.”'},
        {'question': '47. Do you value in yourself more that you are:', 'a': 'unwavering', 'b': 'devoted'},
        {'question': '48. Do you more often prefer the:', 'a': 'final and unalterable statement', 'b': 'tentative and preliminary statement'},
        {'question': '49. Are you more comfortable:', 'a': 'after a decision', 'b': 'before a decision'},
        {'question': '50. Do you:', 'a': 'speak easily and at length with strangers', 'b': 'find little to say to strangers'},
        {'question': '51. Are you more likely to trust your:', 'a': 'experience', 'b': 'hunch'},
        {'question': '52. Do you feel:', 'a': 'more practical than ingenious', 'b': 'more ingenious than practical'},
        {'question': '53. Which person is more to be complimented one of:', 'a': 'clear reason', 'b': 'strong feeling'},
        {'question': '54. Are you inclined more to be:', 'a': 'fair-minded', 'b': 'sympathetic'},
        {'question': '55. Is it preferable mostly to:', 'a': 'make sure things are arranged', 'b': 'just let things happen'},
        {'question': '56. In relationships should most things be:', 'a': 're-negotiable', 'b': 'random and circumstantial'},
        {'question': '57. When the phone rings do you:', 'a': 'hasten to get to it first', 'b': 'hope someone else will answer'},
        {'question': '58. Do you prize more in yourself:', 'a': 'a strong sense of reality', 'b': 'a vivid imagination'},
        {'question': '59. Are you drawn more to:', 'a': 'fundamentals', 'b': 'overtones'},
        {'question': '60. Which seems the greater error:', 'a': 'to be too passionate', 'b': 'to be too objective'},
        {'question': '61. Do you see yourself as basically:', 'a': 'hard-headed', 'b': 'soft-hearted'},
        {'question': '62. Which situation appeals to you more:', 'a': 'the structured and scheduled', 'b': 'the unstructured and unscheduled'},
        {'question': '63. Are you a person that is more:', 'a': 'Routinized than whimsical', 'b': 'Whimsical than routinized'},
        {'question': '64. Are you more inclined to be:', 'a': 'Easy to approach', 'b': 'Somewhat reserved'},
        {'question': '65. In writings do you prefer:', 'a': 'The more literal', 'b': 'The more figurative'},
        {'question': '66. Is it harder for you to:', 'a': 'Identify with others', 'b': 'Utilize others'},
        {'question': '67. Which do you wish more for yourself:', 'a': 'Clarity of reason', 'b': 'Strength of compassion'},
        {'question': '68. Which is the greater fault:', 'a': 'Being indiscriminate', 'b': 'Being critical'},
        {'question': '69. Do you prefer the:', 'a': 'Planned event', 'b': 'Unplanned event'},
        {'question': '70. Do you tend to be more:', 'a': 'Deliberate than spontaneous', 'b': 'Spontaneous than deliberate'},
 ]

  count_of_as = 0
  count_of_bs = 0
  personality = ''

  if request.method == 'POST':
        answers = []
        for key, value in request.POST.items():
                    if key != 'csrfmiddlewaretoken':
                        answers.append(( value))
    
        
        for answer in answers:
            if answer == 'a':
                count_of_as += 1
            elif answer == 'b':
                count_of_bs += 1
            else:
                return HttpResponse("Wrong input")

        if count_of_as > count_of_bs:
             personality += 'E '
        else:
             personality += 'I '
        
        count_of_as = 0
        count_of_bs = 0

        for i in range(1, len(questions), 2):
            if answers[i] == 'a':
                count_of_as += 1
            elif answers[i] == 'b':
                count_of_bs += 1
        
        if count_of_as > count_of_bs:
            personality += 'S '
        else:
            personality += 'N '
        
        count_of_as = 0
        count_of_bs = 0

        for i in range(2, len(questions), 2):
            if answers[i] == 'a':
                count_of_as += 1
            elif answers[i] == 'b':
                count_of_bs += 1
        
        if count_of_as > count_of_bs:
            personality += 'T '
        else:
            personality += 'F '
        
        count_of_as = 0
        count_of_bs = 0

        for i in range(3, len(questions), 2):
            if answers[i] == 'a':
                count_of_as += 1
            elif answers[i] == 'b':
                count_of_bs += 1
        
        if count_of_as > count_of_bs:
            personality += 'J '
        else:
            personality += 'P '
        return render(request, 'mbtiresult.html', {'personality': personality})
  return render(request, 'test.html', {'questions': questions})
   