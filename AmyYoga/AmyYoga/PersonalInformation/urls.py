from django.urls import path, include
from .views import *

adminurlpatterns = {
    path('', viewMemeberList),
    path('<username>/', viewDetails),
}

trainerurlpatterns = {
    path('', vipInformation),
    path('<username>/', vipDetails),
}
urlpatterns = {
    path('vip_information/', include(trainerurlpatterns)),
    path('admin/', include(adminurlpatterns)),
    path('complete/',completeInformation)
}
