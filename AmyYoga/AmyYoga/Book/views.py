from django.shortcuts import render
from Database import models
import datetime
from Tools.SessionManager import SessionManager
from django.contrib import messages

# Create your views here.
def CustomerBook (request):
    courselist=models.Course.objects.all()
    trainerlist=models.Customer.objects.filter(identitySignal=2)
    Authority = 'Customer'
    # if request.method == 'POST':
    #     if request.POST.get('Submit'):#如果是Submit传来的请求
    #         username = request.POST.get('vipname')
    #         course_name = request.POST.get('coursename')
    #         if course_name=='all':
    #             if username=='all':
    #                 user_list = models.CourseUsedRecord.objects.all()
    #                 used_times = 0
    #             else:
    #                 user_list = models.CourseUsedRecord.objects.filter(username=username)
    #                 used_times = 0
    #         else:
    #             if username=='all':
    #                 user_list = models.CourseUsedRecord.objects.filter(coursename=course_name)
    #                 used_times = 0
    #             else:
    #                 user_list = models.CourseUsedRecord.objects.filter(username=username,coursename=course_name)
    #                 used_times= models.CourseUsedRecord.objects.filter(username=username,coursename=course_name).count()
    #     else:
    #         if request.POST.get('newlyRecord'):#如果是newlyRecord传来的请求
    #             username = request.POST.get('vipname')
    #             course_name = request.POST.get('coursename')
    #             flags=models.Customer.objects.filter(username=username).exists()
    #             if username==''or username=='all' or course_name=='' or course_name=='all'or flags==False:#用户名为空
    #                 messages.warning(request, "输入错误！")
    #                 return render(request, 'CourseUsed.html', locals())#跳转
    #             else:#在username,course_name新建一条数据库记录，自动生成一个id作为主键
    #                 year=datetime.datetime.now().year
    #                 month=datetime.datetime.now().month
    #                 day = datetime.datetime.now().day
    #                 hour=datetime.datetime.now().hour
    #                 minute=datetime.datetime.now().minute
    #                 second=datetime.datetime.now().second
    #                 microsecond=datetime.datetime.now().microsecond
    #
    #                 timeid=str(year)+fixformats(month)+fixformats(day)+fixformats(hour)+fixformats(minute)+fixformats(second)+fixformats(microsecond)
    #                 models.CourseUsedRecord.objects.create(timeid=timeid, username=username, coursename=course_name)
    #                 return render(request, 'CourseUsed.html', locals())
    return render(request, 'customerbook.html', locals())

def ManagerBook (request):
    Authority = 'Admin'
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
        customernumber = request.POST.get('maxnumber')  # 人数限制
        timeid = bookdate+booktime+trainername+coursename+customernumber# id关键字
        models.TrainerPublish.objects.create(timeid=timeid, username=trainername,
                                             coursename=coursename,bookdate=bookdate,
                                             booktime=booktime,customernumber=customernumber)
    return render(request, 'trainerpublish.html', locals())
def TrainerPublished (request):
    Authority = 'Trainer'
    allpublish=models.TrainerPublish.objects.all()
    return render(request, 'trainerpublished.html', locals())