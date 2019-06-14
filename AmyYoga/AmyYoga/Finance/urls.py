from django.urls import path

from . import views
urlpatterns = {
    path('addrecord/', views.AddRecord),
    #path('user/',views.UserCourseUsed),
    #path('trainer/',views.TrainerCourseUsed),
    #path('<username>',views.moremessage_username),
    #path('<coursename>',views.moremessage_coursename),
}