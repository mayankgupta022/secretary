from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home', name='pagesHome'),
    url(r'^(\d+)/$', 'pages.views.home', name='pagesHome'),
    url(r'^trash/$$', 'pages.views.trash', name='pagesTrash'),
    url(r'^newNotebook/$', 'pages.views.newNotebook', name='pagesNewNotebook'),
    url(r'^newPage/$', 'pages.views.newPage', name='pagesNewPage'),
    url(r'^delNotebook/(\d+)/$', 'pages.views.delNotebook', name='pagesDelNotebook'),
    url(r'^delPage/(\d+)/$', 'pages.views.delPage', name='pagesDelPage'),
    url(r'^restorePage/(\d+)/$', 'pages.views.restorePage', name='pagesRestorePage'),
    url(r'^notebook/(\d+)/$', 'pages.views.notebook', name='pagesNotebook'),
    url(r'^notebooks/$', 'pages.views.notebooks', name='pagesNotebooks'),
    url(r'^page/(\d+)/$', 'pages.views.page', name='pagesPage'),
    url(r'^makeDefaultNotebook/(\d+)/$', 'pages.views.makeDefaultNotebook', name='pagesMakeDefaultNotebook'),
)
