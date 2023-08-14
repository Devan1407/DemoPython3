
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    # path('details',views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update, name='update'),
    path('gohome/',views.Tasklistview.as_view(),name='gohome'),
    path('godetail/<int:pk>/',views.Tasklistview.as_view(),name='godetail'),
    path('goupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='goupdate'),


]