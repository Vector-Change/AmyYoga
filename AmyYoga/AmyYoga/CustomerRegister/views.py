from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm
from UserLogin.models import Customer as CustomerDB
from UserLogin.models import PersonalInformation as PersonalInformationDB


# Create your views here.
def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)  # 获取表单内容
        if registerForm.is_valid():  # 解析表单
            username = registerForm.cleaned_data['username']  # 获得表单内用户名
            password = registerForm.cleaned_data['password']  # 获得表单内密码
            confirmPassword = registerForm.cleaned_data['confirmPassword']
            phoneNumber = registerForm.cleaned_data['phoneNumber']
            birthday=registerForm.cleaned_data['birthday']
            if confirmPassword != password:  # 检查两次密码是否一致
                errormessage="两次密码不一致"
                return render(request, "registerUI.html", locals())
            user = CustomerDB()  # 创建空用户对象
            try:
                user = CustomerDB.objects.get(username=username)  # 尝试查询该用户
            except ObjectDoesNotExist:  # 用户名不存在，执行创建操作
                CustomerDB.objects.create(username=username,password=password)
                personalInformation=PersonalInformationDB.objects.create(username=username)
                print(personalInformation)
                personalInformation.setPhoneNumber(phoneNumber)
                print(personalInformation)
                personalInformation.setBirthday(birthday)
                print(personalInformation)
                return HttpResponse("successed")  # 如果没查询到，返回可以注册信息
            errormessage="用户名已存在，不可注册"  # 返回用户名存在，不可注册信息
    else:
        registerForm = RegisterForm()
    return render(request, "registerUI.html", locals())  # 正常访问，渲染模板
