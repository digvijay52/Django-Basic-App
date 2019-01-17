from django.conf.urls import url
from . import views

app_name= 'task'

urlpatterns = [
    url(r'^update/(?P<taskfinal>.*)/$',views.task_final,name="taskfinal"),
    url(r'^edit/(?P<taskedit>.*)/$',views.task_edit,name="taskupdate"),
    url(r'^delete/(?P<tasktitle>.*)/$',views.task_del,name="taskdelete"),
    url(r'^(?P<subtask>.*)/(?P<task>.*)/$',views.sub_del,name="subdelete"),
    url(r'^$', views.task_views,name="taskview"),
    url(r'^(?P<title>.*)/$',views.sub_add,name="addsub"),
    

]