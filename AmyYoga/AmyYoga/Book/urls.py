from django.urls import path, include
from .views import *

urlpatterns = {
    path('manager/', ManagerBook),
    path('customer/',CustomerBook),
    path('trainerpublish/', TrainerPublish),
    path('trainerpublished/',TrainerPublished),
    path('trainerpublished/mks/',delete),
    #path('<username>',views.moremessage_username),
    #path('<coursename>',views.moremessage_coursename),
}
