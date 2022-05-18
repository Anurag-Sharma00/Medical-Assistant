from django.shortcuts import render
from . import Pool
import datetime
from datetime import date
from django.http import JsonResponse


def doctorlogin(request):
   return render(request,"Doctorlogin.html")


def doctorpatients(request):
         try:
            db, cmd = Pool.ConnectionPooling()
            email = request.POST['email']
            q="select * from doctorregistration where emailaddress='{0}'".format(email)
            print(q)
            cmd.execute(q)

            result = cmd.fetchone()

            request.session['doctor'] = [result['doctorname'],result['doctorid'],result['specialization'],result['mobileno'],result['emailaddress']]
            if(result):

               q = "select UD.*,(select U.username from userregistration U where U.usernum=UD.mobileno) as username from userdoctor UD where UD.doctorid={0}".format(result['doctorid'])

               cmd.execute(q)
               data=cmd.fetchall()
               print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
               print(data)

               if(data):
                 return render(request,"DoctorPatients.html",{'data':data ,'doctorname':request.session['doctor'][0], 'doctorid':request.session['doctor'][1], 'docspl':request.session['doctor'][2]})
            else:
               return render(request,"Doctorlogin.html")
         except Exception as e:
            print(e)



def getpatientscore(request):
  try:
   docid = request.GET['docid']
   userdoctorid = request.GET['userdoctorid']

   print("docid and userdoctorid",docid,userdoctorid)
   return JsonResponse({'msg':True})
  except Exception as e:
     print(e)


def showpatientscore(request):
   try:
      userdoctorid = request.GET['userdoctorid']
      docspl = request.GET['docspl']
      db, cmd = Pool.ConnectionPooling()
      q="select questionno,totalscore from userdiagnose where userdoctorid = '{0}'".format(userdoctorid)
      print(q)
      cmd.execute(q)
      result = cmd.fetchall()
      q="select q.*,group_concat(s.subquestion separator'#') as subquestions from medassist.questions q, subquestions s where q.questionnumber=s.questionid and q.specializationid='{0}' group by q.questionnumber".format(docspl)
      cmd.execute(q)
      questions  = cmd.fetchall()
      db.close()
      return JsonResponse({'result': result , 'questions': questions})
   except Exception as e:
      print(e)
      return JsonResponse({'msg':'False'})


def prescription(request):
   db, cmd = Pool.ConnectionPooling()
   q = "select specialization from specialization where specializationid = '{0}'".format(request.session['doctor'][2])
   cmd.execute(q)
   spl = cmd.fetchone()
   username = request.POST['username']
   usermob = request.POST['usermob']
   userdate = request.POST['userdate']
   usertime = request.POST['usertime']

   return render(request,"Prescription.html",{'username':username, 'mobileno':usermob,'userdate':userdate,'usertime':usertime,'docname':request.session['doctor'][0], 'docmob':request.session['doctor'][3],'docemail':request.session['doctor'][4],'docspl':spl['specialization']})

def add_prescription(request):
 try:
   prescription = request.GET['prescription']
   remark = request.GET['remark']
   timemed = request.GET['timemed']
   db, cmd = Pool.ConnectionPooling()

   today = date.today()

   q = "insert into prescription(doctorid,mobileno,prescription,remark,timemed,currentdate)values({},'{}','{}','{}','{}','{}')".format(
      request.session['doctor'][1],request.session['user'][1], prescription,remark,timemed, today)
   print(request.session['doctor'])
   print(q)
   cmd.execute(q)
   db.commit()
   db.close()
   return JsonResponse({'result': True})
 except Exception as e:
   print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
   print(e)
   return JsonResponse({'result': False})
