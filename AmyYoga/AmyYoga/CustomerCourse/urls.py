from django.urls import path
from . import  views
urlpatterns = {
    path('', views.uncustomercourse),#显示已支付界面，是默认界面
    path('<number>', views.cancelorder)
}