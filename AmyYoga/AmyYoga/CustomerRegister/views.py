from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from Database.models import Customer
from Database.models import PersonalInformation
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index_logined, url_login, url_index


def register(request):#用户注册
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():
        return HttpResponseRedirect(url_index_logined)
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data.get('username')
            password = registerForm.cleaned_data.get('password')
            phoneNumber = registerForm.cleaned_data.get('phoneNumber')
            birthday = registerForm.cleaned_data.get('birthday')
            identity = request.POST.get('identity')

            #Customer.objects.create(username=username, password=password)
            if identity == 'customer':
                Customer.objects.create(username=username, password=password,identitySignal=1)
            elif identity == 'trainer':
                Customer.objects.create(username=username, password=password,identitySignal=2)

            personalInformation = PersonalInformation.objects.create(username=username)
            personalInformation.setIdentity(identity)
            personalInformation.setPhoneNumber(phoneNumber)
            personalInformation.setBirthday(birthday)
            return HttpResponseRedirect(url_login)
    else:
        registerForm = RegisterForm()
    return render(request, "RegisterUI.html", {'registerForm': registerForm})
