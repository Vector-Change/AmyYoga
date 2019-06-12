from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from Database import models
import datetime
from Tools.SessionManager import SessionManager
from django.contrib import messages

# Create your views here.
def CustomerSearch (request):
    courselist=models.Course.objects.all()
    trainerlist=models.Customer.objects.filter(identitySignal=2)
    datelist=models.TrainerPublish.objects.values('bookdate').distinct()
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()
    Authority = 'Customer'
    if request.method == 'POST':
        if request.POST.get('search'):#如果是Submit传来的请求
            coursename = request.POST.get('coursename')
            trainername = request.POST.get('trainer')
            date = request.POST.get('date')
            time = request.POST.get('time')
            if coursename == 'all':
                if trainername == 'all':
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.all()
                        else:#time!=all
                            #print("云深不知处")
                            publishlist = models.TrainerPublish.objects.filter(booktime=time)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(bookdate=date)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(bookdate=date,booktime=time)
                else:#trainername!=all
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername)
                        else:#time!=all
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,booktime=time)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,bookdate=date)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,bookdate=date,booktime=time)
            else:#coursename!=all
                if trainername == 'all':
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename)
                        else:#time!=all
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,booktime=time)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,bookdate=date)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,bookdate=date,booktime=time)
                else:#trainername!=all
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername)
                        else:#time!=all
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,booktime=time)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,bookdate=date)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,bookdate=date,booktime=time)
    return render(request, 'customerbook.html', locals())
def CustomerBook (request):#建立预定记录
    if request.method == 'POST':
        sessionManager = SessionManager(request)
        trainername=request.POST.get('trainername')
        #print(trainername)
        username = sessionManager.getUsername()#用户名
        bookdate = request.POST.get('bookdate')
        booktime = request.POST.get('booktime')
        coursename = request.POST.get('coursename')
        trainerprice = '80'
        # 生成id
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        microsecond = datetime.datetime.now().microsecond
        timeid = str(year) + fixformats(month) + fixformats(day) + fixformats(hour) \
                 + fixformats(minute) + fixformats(second)
        models.BookRecord.objects.create(timeid=timeid, trainername=trainername,
                                         username=username, bookdate=bookdate,
                                         booktime=booktime, coursename=coursename,
                                         trainerprice=trainerprice)
        return HttpResponse("预约成功")
    return HttpResponse("预约失败")
def CustomerBooked(request):
    Authority = 'Customer'
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()
    allbook = models.BookRecord.objects.filter(username=username)
    #temp = allbook.count()
    return render(request, 'customerbooked.html', locals())
def CustomerDelete (request):
    if request.method == 'POST':
        timeid = request.POST.get('timeid')
        #print(timeid)
        if timeid:
            models.BookRecord.objects.get(timeid=timeid).delete()
            return HttpResponse("删除成功")
    return HttpResponse("删除失败")
    #return render(request, 'trainerpublished.html', locals())
def ManagerBook (request):
    Authority = 'Admin'
    allbook = models.BookRecord.objects.all().order_by('username')
    allpublish = models.TrainerPublish.objects.all().order_by('trainername')
    return render(request, 'managerbook.html', locals())
def TrainerPublish (request):
    allcourse=models.Course.objects.all()
    Authority = 'Trainer'
    sessionManager = SessionManager(request)
    trainername = sessionManager.getUsername()
    if request.method == 'POST':
        bookdate = request.POST.get('date')
        booktime=request.POST.get('time')
        coursename=request.POST.get('coursename')
        customernumber = request.POST.get('maxnumber')# 人数限制

        #生成id
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        microsecond = datetime.datetime.now().microsecond
        timeid = str(year) + fixformats(month) + fixformats(day) + fixformats(hour) \
                 + fixformats(minute) + fixformats(second)

        models.TrainerPublish.objects.create(timeid=timeid, trainername=trainername,
                                             coursename=coursename,bookdate=bookdate,
                                             booktime=booktime,customernumber=customernumber)
    return render(request, 'trainerpublish.html', locals())
def fixformats(date):
    if date//10==0:
        return '0'+str(date)
    else:
        return str(date)
def TrainerPublished (request):
    Authority = 'Trainer'
    sessionManager = SessionManager(request)
    trainername = sessionManager.getUsername()
    allpublish = models.TrainerPublish.objects.filter(trainername=trainername)
    #allpublish=models.TrainerPublish.objects.filter(trainername=trainername)#本教练当前所有发布
    temp=allpublish.count()
    #allbooked=models.TrainerPublish.objects.filter(trainername=trainername)#本教练本课本时段的预约人数
    #number=models.TrainerPublish.objects.filter(trainername=trainername).count()
    return render(request, 'trainerpublished.html', locals())
def TrainerDelete (request):
    if request.method == 'POST':
        timeid = request.POST.get('timeid')
        print(timeid)
        if timeid:
            models.TrainerPublish.objects.get(timeid=timeid).delete()
            return HttpResponse("删除成功")
    return HttpResponse("删除失败")
    #return render(request, 'trainerpublished.html', locals())