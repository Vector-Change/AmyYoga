from django.urls import path, include
from .views import *

urlpatterns = {
    path('manager/', ManagerBook),
    path('managered/', ManagerBookAll),
    path('customerbook/',CustomerSearch),
    path('customerbook/mks/',CustomerBook),
    path('customerbooked/',CustomerBooked),
    path('customerbooked/mks/',CustomerDelete),
    path('customerbookedall/',CustomerBookedAll),
    path('trainerpublish/', TrainerPublish),
    path('trainerpublished/',TrainerPublished),
    path('trainerpublished/mks/',TrainerDelete),
    path('trainerpublishedall/',TrainerPublishedAll),
    #path('<username>',views.moremessage_username),
    #path('<coursename>',views.moremessage_coursename),
}
