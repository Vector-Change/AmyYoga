from django.db import models


# Create your models here.


class CommonUsername(models.Model):
    username = models.CharField(primary_key=True, max_length=20)

    class Meta:
        abstract = True


class SecurityQA(CommonUsername):
    securityQ1 = models.CharField(max_length=50)
    securityA1 = models.CharField(max_length=50)
    securityQ2 = models.CharField(max_length=50)
    securityA2 = models.CharField(max_length=50)
    securityQ3 = models.CharField(max_length=50)
    securityA3 = models.CharField(max_length=50)

    def checkSecurityQA(self, Qnum, Ans):
        if self.securityQ1 == Qnum:
            if self.securityA1 == Ans:
                return True
            else:
                return False
        if self.securityQ2 == Qnum:
            if self.securityA2 == Ans:
                return True
            else:
                return False
        if self.securityQ3 == Qnum:
            if self.securityA3 == Ans:
                return True
            else:
                return False

    def getSecurityQuestion(self, p):
        if p == 1:
            return self.securityQ1
        elif p == 2:
            return self.securityQ2
        elif p == 3:
            return self.securityQ3


class Customer(CommonUsername):  # 用户类（管理员和客户合并到同一个类，用authoritySignal区分）
    authoritySignal = models.BooleanField(default=False)  # 身份标志，False为客户，True为管理员
    password = models.CharField(max_length=20)  # 密码

    def checkAuthority(self, uncheckPassword):  # 身份认证函数，以后如果需要加入数据库内密码加密，可在该函数内添加加密解密函数
        if self.password == uncheckPassword:
            return True
        else:
            return False

    def isAdministrator(self):
        if self.authoritySignal:
            return True
        else:
            return False

    def setPassword(self, password):
        self.password = password
        self.save()


class PersonalInformation(CommonUsername):  # 个人信息类
    phoneNumber = models.CharField(max_length=20, default="")  # 电话号码
    name = models.CharField(max_length=20, default="")  # 客户姓名
    age = models.IntegerField(default=0)
    birthday = models.DateField(default='1970-01-01')
    profession = models.CharField(max_length=20)
    sex = models.BooleanField(default=False)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    bust = models.FloatField(default=0)
    waistline = models.FloatField(default=0)
    hipline = models.FloatField(default=0)
    shoulderwidth = models.FloatField(default=0)

    def setPhoneNumber(self, p):
        self.phoneNumber = p
        self.save()

    def getPhoneNumber(self):
        return self.phoneNumber

    def setName(self, p):
        self.name = p
        self.save()

    def getName(self):
        return self.name

    def setAge(self, p):
        self.age = p
        self.save()

    def getAge(self):
        return self.age

    def setBirthday(self, p):
        self.birthday = p
        self.save()

    def getBirthday(self):
        return self.birthday

    def setProfession(self, p):
        self.profession = p
        self.save()

    def getProfession(self):
        return self.profession

    def setSex(self, p):
        self.sex = p
        self.save()

    def getSex(self):
        return self.sex

    def setHeight(self, p):
        self.height = p
        self.save()

    def getHeight(self):
        return self.height

    def setWeight(self, p):
        self.weight = p
        self.save()

    def getWeight(self):
        return self.weight

    def setBust(self, p):
        self.bust = p
        self.save()

    def getBust(self):
        return self.bust

    def setWaistline(self, p):
        self.waistline = p
        self.save()

    def getWaistline(self):
        return self.waistline

    def setHipline(self, p):
        self.hipline = p
        self.save()

    def getHipline(self):
        return self.hipline

    def setShoulderwidth(self, p):
        self.shoulderwidth = p
        self.save()

    def getShoulderwidth(self):
        return self.shoulderwidth


class Course(models.Model):  # 课程信息
    coursename = models.CharField(primary_key=True, max_length=20)  # 课程名
    courseintroduction = models.CharField(max_length=100, default="")  # 课程介绍
    courseprice = models.IntegerField(max_length=10, default=0)  # 课程价格

    def setCourseName(self, p):
        self.coursename = p
        self.save()

    def getCourseName(self):
        return self.coursename

    def setCourseIntroduction(self, p):
        self.courseintroduction = p
        self.save()

    def getCourseIntroduction(self):
        return self.courseintroduction

    def setCoursePrice(self, p):
        self.courseprice = p
        self.save()

    def getCoursePrice(self):
        return self.courseprice


class PhysicalAssessment(models.Model):
    number = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=20)
    date = models.DateField()
    caption = models.CharField(max_length=50)
    text = models.TextField()

    def getNumber(self):
        return self.number

    def setNumber(self, p):
        self.number = p
        self.save()

    def getCustomer(self):
        return self.customer

    def setCustomer(self, p):
        self.customer = p
        self.save()

    def getDate(self):
        return self.date

    def setDate(self, p):
        self.date = p
        self.save()

    def getCaption(self):
        return self.caption

    def setCaption(self, p):
        self.caption = p
        self.save()

    def getText(self):
        return self.text

    def setText(self, p):
        self.text = p
        self.save()
