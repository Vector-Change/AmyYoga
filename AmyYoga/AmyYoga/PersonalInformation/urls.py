from django.urls import path, include
from .views import *

adminurlpatterns = {
    path('', viewMemeberList),
    path('<username>/', viewDetails),
}
urlpatterns = {
    path('vip_information/', vipInformation),
    path('admin/', include(adminurlpatterns)),
    path('complete/',completeInformation)
}
