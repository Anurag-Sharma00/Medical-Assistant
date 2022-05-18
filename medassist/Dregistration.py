from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def RegistrationInterface(request):
    try:
        admin = request.session['admin']
        print("ADMIN", admin)
        return render(request, "Dregistration.html", {'msg': ''})
    except Exception as e:
        return render(request, "AdminLogin.html", {'msg': ''})



@xframe_options_exempt
def RegistrationDisplayALL(request):
    try:
      db,cmd=Pool.ConnectionPooling()

      q = "Select D.*,(select S.spe" \
          "cialization from specialization S where S.specializationid=D.specialization)" " as tspecialization  From doctorregistration D"
      cmd.execute(q)

      records=cmd.fetchall()

      print(records)
      db.close()
      return render(request, "DisplayAll.html", {'result': records,'msg':''})
    except Exception as e:
        print(e)
        return render(request, "DisplayAll.html", {'result': '','msg':'' })


@xframe_options_exempt
def RegistrationSubmit(request):
    try:
      db,cmd=Pool.ConnectionPooling()

      dname=request.POST['doctorname']
      d = request.POST['dob']
      g = request.POST['gender']
      email= request.POST['emailaddress']
      special =request.POST['specialization']
      mno = request.POST['mobileno']
      iconfile=request.FILES['icon']


      q="insert into doctorregistration (doctorname,dob,gender,emailaddress,specialization,icon,mobileno) values('{0}',{1},'{2}','{3}','{4}','{5}','{6}')".format(dname,d,g,email,special,iconfile.name,mno)
      print(q)
      cmd.execute(q)
      db.commit()
      F=open("g:/doctorregistration/assets/"+iconfile.name,"wb")
      for chunk in iconfile.chunks():
        F.write(chunk)
      F.close()
      db.close()
      return render(request, "Dregistration.html", {'msg': 'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "Dregistration.html", {'msg': 'Fail to submit Record'})
@xframe_options_exempt
def UpdateRegistration(request):
     try:
         db, cmd = Pool.ConnectionPooling()
         doctorid=request.GET['doctorid']
         doctorname = request.GET['doctorname']
         dob = request.GET['dob']
         gender = request.GET['gender']
         emailaddress = request.GET['emailaddress']
         specialization = request.GET['specialization']
         mobileno = request.GET['mobileno']

         q = "update doctorregistration set doctorname='{0}',dob='{1}',gender='{2}',emailaddress='{3}',specialization='{4}',mobileno='{5}' where doctorid={6}".format(doctorname,dob,gender,emailaddress,specialization,mobileno,doctorid)
         cmd.execute(q)
         db.commit()
         db.close()
         return JsonResponse({"result": True, }, safe=False)
     except Exception as e:
         print(e)
         return JsonResponse({"result": False, }, safe=False)

@xframe_options_exempt
def DeleteRegistration(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        doctorid = request.GET['doctorid']
        doctorname = request.GET['doctorname']
        dob = request.GET['dob']
        gender = request.GET['gender']
        emailaddress = request.GET['emailaddress']
        specialization = request.GET['specialization']
        mobileno = request.GET['mobileno']

        q = "delete from doctorregistration where doctorid={0}".format(doctorid)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({"result": True, }, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"result": False, }, safe=False)
@xframe_options_exempt
def EditDregistrationPicture(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        doctorid = request.POST['doctorid']
        iconfile = request.FILES['icon']
        q = "update  doctorregistration set icon='{0}' where doctorid={1}".format(iconfile.name,doctorid)
        cmd.execute(q)
        db.commit()
        F = open("g:/doctorregistration/assets/" + iconfile.name, "wb")
        for chunk in iconfile.chunks():
            F.write(chunk)
        F.close()
        db.close()


        return JsonResponse({"result":True,}, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"result": False, }, safe=False)

        print(e)
        return JsonResponse({"result": False, }, safe=False)







