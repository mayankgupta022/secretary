from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'diary.views.home', name='diaryHome'),
    url(r'^(\d+)/$', 'diary.views.home', name='diaryHome'),
    url(r'^day/(\d+)/$', 'diary.views.day', name='diaryDay'),
    url(r'^delDay/(\d+)/$', 'diary.views.delDay', name='diaryDelDay'),
    url(r'^delCalender/(\d+)/$', 'diary.views.delCalender', name='diaryDelCalender'),
    url(r'^delEvent/(\d+)/$', 'diary.views.delEvent', name='diaryDelEvent'),
    url(r'^makeDefaultCalender/(\d+)/$', 'diary.views.makeDefaultCalender', name='diaryMakeDefaultCalender'),
    url(r'^newDay/$', 'diary.views.newDay', name='diaryNewDay'),
    url(r'^newCalender/$', 'diary.views.newCalender', name='diaryNewCalender'),
    url(r'^newEvent/$', 'diary.views.newEvent', name='diaryNewEvent'),
    url(r'^event/(\d+)/$', 'diary.views.event', name='diaryEvent'),
    url(r'^calender/(\d+)/$', 'diary.views.calender', name='diaryCalender'),
    url(r'^calenders/$', 'diary.views.calenders', name='diaryCalenders'),
    url(r'^restoreEvent/(\d+)/$', 'diary.views.restoreEvent', name='diaryRestoreEvent'),
    url(r'^trash/$$', 'diary.views.trash', name='diaryTrash'),
)
