from django.urls import path, include
from .views import *

urlpatterns = {
    path('manager/', ManagerBook),
    path('customerbook/',CustomerSearch),
    path('customerbook/mks/',CustomerBook),
    path('customerbooked/',CustomerBooked),
    path('customerbooked/mks/',CustomerDelete),
    path('trainerpublish/', TrainerPublish),
    path('trainerpublished/',TrainerPublished),
    path('trainerpublished/mks/',TrainerDelete),
    #path('<username>',views.moremessage_username),
    #path('<coursename>',views.moremessage_coursename),
}
