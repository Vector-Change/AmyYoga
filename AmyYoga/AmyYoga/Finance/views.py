from django.shortcuts import render
from Database import models
import datetime
from Tools.SessionManager import SessionManager
from django.contrib import messages
def AddRecord(request):
    Authority='Admin'
    if request.method == 'POST':
        if request.POST.get('allRecord'):#如果是搜索按钮传来的请求
            allrecord=models.FinanceRecord.objects.all().order_by('date')#获取全部记录
            profit=0
            for item in allrecord:
                profit=profit+int(item.getNumber())
            if profit>0:
                flag='盈利'
            else:
                flag='亏损'
        else:
            if request.POST.get('newlyRecord'):#新建记录
                remarks=request.POST.get('remarks')
                number=request.POST.get('pay')
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                day = datetime.datetime.now().day
                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute
                second = datetime.datetime.now().second
                date=str(year) + fixformats(month) + fixformats(day)
                timeid = date + fixformats(hour) + fixformats(minute) + fixformats(second)
                models.FinanceRecord.objects.create(timeid=timeid, date=date, remarks=remarks, number=number)
    return render(request, 'addrecord.html', locals())

def fixformats(date):
    if date//10==0:
        return '0'+str(date)
    else:
        return str(date)