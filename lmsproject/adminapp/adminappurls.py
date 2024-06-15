from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('viewcomplain/',views.viewcomplain,name='viewcomplain'),
    path('addbook/',views.addbook,name='addbook'),
    path('viewbook/',views.viewbook,name='viewbook'),
    path('deletebook/<bookid>',views.deletebook,name='deletebook'),
    path('issuebook/',views.issuebook,name='issuebook'),
    path('issuebookui/<bookid>',views.issuebookui,name='issuebookui'),
    path('issue/',views.issue,name='issue'),
    path('viewissuedbook/',views.viewissuedbook,name='viewissuedbook'),
    path('ret/<id>',views.ret,name='ret'),
    path('returnbook/',views.returnbook,name='returnbook'),

]