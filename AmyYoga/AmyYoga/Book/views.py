from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from Database import models
import datetime
from Tools.SessionManager import SessionManager
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def CustomerSearch (request):
    trainerlist=models.Customer.objects.filter(identitySignal=2)
    validlist=models.TrainerPublish.objects.filter(pastflag=False)
    datelist=validlist.values('bookdate').distinct()
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()
    Authority = 'Customer'
    buyrecord = models.BuyRecord.objects.filter(username=username)  # 该用户所有购买记录
    buycourse = buyrecord.values('coursename').distinct()
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
                            publishlist = models.TrainerPublish.objects.filter(pastflag=False)
                        else:#time!=all
                            #print("云深不知处")
                            publishlist = models.TrainerPublish.objects.filter(booktime=time,pastflag=False)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(bookdate=date,pastflag=False)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(bookdate=date,booktime=time,pastflag=False)
                else:#trainername!=all
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,pastflag=False)
                        else:#time!=all
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,booktime=time,pastflag=False)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,bookdate=date,pastflag=False)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(trainername=trainername,bookdate=date,booktime=time,pastflag=False)
            else:#coursename!=all
                if trainername == 'all':
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,pastflag=False)
                        else:#time!=all
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,booktime=time,pastflag=False)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,bookdate=date,pastflag=False)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,bookdate=date,booktime=time,pastflag=False)
                else:#trainername!=all
                    if date == 'all':
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,pastflag=False)
                        else:#time!=all
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,booktime=time,pastflag=False)
                    else:#date!=all
                        if time == 'all':
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,bookdate=date,pastflag=False)
                        else:
                            publishlist = models.TrainerPublish.objects.filter(coursename=coursename,trainername=trainername,bookdate=date,booktime=time,pastflag=False)
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
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        nowtime = str(year) + fixformats(month) + fixformats(day)
        try:#是否存在记录
            models.BookRecord.objects.get(username=username,trainername=trainername, bookdate=bookdate,
                                             booktime=booktime, coursename=coursename)

        except ObjectDoesNotExist:
            timeid = nowtime + fixformats(hour) + fixformats(minute) + fixformats(second)
            models.BookRecord.objects.create(timeid=timeid, trainername=trainername,
                                             username=username, bookdate=bookdate,
                                             booktime=booktime, coursename=coursename,
                                             trainerprice=trainerprice, pastflag=False)
            booknumber = models.TrainerPublish.objects.get(trainername=trainername, bookdate=bookdate,
                                                           booktime=booktime, coursename=coursename)
            nownumber = str(int(booknumber.getNowNumber()) + 1)
            booknumber.setNowNumber(nownumber)
            return HttpResponse("预约成功")
        #raise forms.ValidationError('该用户名已存在')
    return HttpResponse("预约失败，存在重复数据")
def CustomerBooked(request):
    Authority = 'Customer'
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    nowdate = str(year) + fixformats(month) + fixformats(day)
    allbook = models.BookRecord.objects.filter(username=username)
    for item in allbook:
        if item.bookdate<nowdate:
            item.setPastflag(True)
    validbook = models.BookRecord.objects.filter(username=username, pastflag=False)
    #temp = allbook.count()
    return render(request, 'customerbooked.html', locals())
def CustomerBookedAll(request):
    Authority = 'Customer'
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()
    allbook = models.BookRecord.objects.filter(username=username)
    return render(request, 'customerbookedall.html', locals())
def CustomerDelete (request):
    if request.method == 'POST':
        timeid = request.POST.get('timeid')
        coursename=request.POST.get('coursename')
        trainername=request.POST.get('trainername')
        bookdate=request.POST.get('bookdate')
        booktime=request.POST.get('booktime')
        #print(timeid)
        if timeid:
            models.BookRecord.objects.get(timeid=timeid).delete()
            pulishdec=models.TrainerPublish.objects.get(coursename=coursename,trainername=trainername,
                                                        bookdate=bookdate,booktime=booktime)
            nownumber=str(int(pulishdec.getNowNumber())-1)
            pulishdec.setNowNumber(nownumber)
            return HttpResponse("删除成功")
    return HttpResponse("删除失败")
    #return render(request, 'trainerpublished.html', locals())
def TrainerPublish (request):
    allcourse=models.Course.objects.all()
    Authority = 'Trainer'
    sessionManager = SessionManager(request)
    trainername = sessionManager.getUsername()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    microsecond = datetime.datetime.now().microsecond
    nowdate=str(year) + fixformats(month) + fixformats(day)
    if request.method == 'POST':
        bookdate = request.POST.get('date')
        booktime=request.POST.get('time')
        coursename=request.POST.get('coursename')
        customernumber = request.POST.get('maxnumber')# 人数限制
        try:#是否存在记录
            models.TrainerPublish.objects.get(trainername=trainername, bookdate=bookdate,
                                             booktime=booktime, coursename=coursename)
        except ObjectDoesNotExist:
            #生成id
            timeid = nowdate + fixformats(hour) + fixformats(minute) + fixformats(second)
            if bookdate < nowdate:
                pastflag = True
            else:
                pastflag=False
                models.TrainerPublish.objects.create(timeid=timeid, trainername=trainername,
                                                    coursename=coursename,bookdate=bookdate,
                                                    booktime=booktime,customernumber=customernumber,
                                                    pastflag=pastflag)
            return HttpResponse("发布成功")
    return render(request, 'trainerpublish.html', locals())
def fixformats(date):
    if date//10==0:
        return '0'+str(date)
    else:
        return str(date)
def TrainerPublished (request):#查看已经发布的时间，下架已经过期的时间，查看已经过期的预约
    Authority = 'Trainer'
    sessionManager = SessionManager(request)
    trainername = sessionManager.getUsername()
    allpublish = models.TrainerPublish.objects.filter(trainername=trainername)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    nowdate = str(year) + fixformats(month) + fixformats(day)
    for item in allpublish:
        if item.bookdate<nowdate:
            item.setPastflag(True)
    validpublish = models.TrainerPublish.objects.filter(trainername=trainername,pastflag=False)
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
def TrainerPublishedAll(request):
    Authority = 'Trainer'
    sessionManager = SessionManager(request)
    trainername = sessionManager.getUsername()
    allpublish = models.TrainerPublish.objects.filter(trainername=trainername)
    return render(request, 'trainerpublishedall.html', locals())
def ManagerBook (request):
    Authority = 'Admin'
    allbook = models.BookRecord.objects.filter(pastflag=False).order_by('username')
    allpublish = models.TrainerPublish.objects.filter(pastflag=False).order_by('trainername')
    return render(request, 'managerbook.html', locals())
def ManagerBookAll (request):
    Authority = 'Admin'
    allbook = models.BookRecord.objects.all().order_by('bookdate')
    allpublish = models.TrainerPublish.objects.all().order_by('bookdate')
    return render(request, 'managerbookall.html', locals())