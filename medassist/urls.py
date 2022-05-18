"""medassist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Specialization
from . import Dregistration
from . import Questions
from . import SubQuestions
from . import AdminLogin
from . import UserRegistration
from . import DoctorPatient
urlpatterns = [
    path('admin/', admin.site.urls),
    path('specialization/',Specialization.SpecializationInterface),
    path('specializationsubmit',Specialization.SpecializationSubmit),
    path('specializationdisplayall/',Specialization.SpecializationDisplayAll),
    path('specializationdisplayallJSON/',Specialization.SpecializationDisplayAllJSON),
    path('updatespecialization/', Specialization.UpdateSpecialization),
    path('deletespecialization/', Specialization.DeleteSpecialization),
    path('editspecializationpicture', Specialization.EditSpecializationPicture),

    #for doctors

    path('dregistration/', Dregistration.RegistrationInterface),
    path('dregistrationsubmit', Dregistration.RegistrationSubmit),
    path('dregistrationdisplayall/', Dregistration.RegistrationDisplayALL),
    path('updatedregistration/', Dregistration.UpdateRegistration),
    path('deletedregistration/', Dregistration.DeleteRegistration),
    path('editdregistrationpicture', Dregistration.EditDregistrationPicture),

    #Questions..
    path('questions/', Questions.QuestionInterface),
    path('questionsubmit/', Questions.QuestionSubmit),
    path('questionjson/', Questions.QuestionJSON),


    #Sub-Questions
    path('subquestions/', SubQuestions.SubQuestionInterface),
    path('subquestionsubmit/', SubQuestions.SubQuestionSubmit),

#Admin....................
    path('adminlogin/', AdminLogin.AdminLogin),
    path('adminlogout/', AdminLogin.AdminLogout),

    path('dashboard', AdminLogin.CheckAdminLogin),

    # User Details------------------------
    # User Details------------------------
    path('userregistration/', UserRegistration.UserRegistrationInterface),
    path('loginpage/', UserRegistration.UserLogin),
    path('otppage', UserRegistration.OtpPage),
    path('userregistrationsubmit', UserRegistration.UserRegistrationSubmit),
    path('userregistrationdisplayall/', UserRegistration.UserRegistrationDisplayAll),
    path('userlogininterface/', UserRegistration.UserLoginInterface),
    path('womacform/', UserRegistration.WomacForm),
    path('surveyinterface', UserRegistration.SurveyInterface),
    path('userquestions/', UserRegistration.UserQuestions),
    path('userquestion', UserRegistration.UserQuestionInterface),

    path('checkotp', UserRegistration.ChkOtp),
    path('emaillogin/', UserRegistration.EmailLogin),
    path('forgetpassword/', UserRegistration.ForgetPassword),
    path('checkemailidandpasswd', UserRegistration.CheckEmailIdAndPasswd),
    path('submitscore/', UserRegistration.SubmitScore),

    path('helpuserquestion/', UserRegistration.HelpUserQuestion),
    path('callhelpuserquestion/', UserRegistration.CallHelpUserQuestion),

#DoctorPatient
    path('doctorlogin/',DoctorPatient.doctorlogin),
    path('doctorpatients',DoctorPatient.doctorpatients),
    path('getpatientscore/',DoctorPatient.getpatientscore),
    path('getuserscore/',DoctorPatient.showpatientscore),
    path('prescription',DoctorPatient.prescription),
    path('add_prescription/',DoctorPatient.add_prescription),



]
