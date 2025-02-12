from django.urls import path
from.import views
urlpatterns=[
    path("", views.home, name='home.html'),
    path("base",views.base,name='base.html'),
    path("entry", views.entry, name='entry.html'),
    path("report", views.report, name='report.html'),
    path("viewres/<int:id>", views.viewres,name='viewres.html' ),
    path("editres/<int:id>", views.editres,name='editres.html' ),
    path("delres/<int:id>", views.delres,name='delres.html'),

]