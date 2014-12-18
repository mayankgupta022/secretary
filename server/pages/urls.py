from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home', name='pagesHome'),
    url(r'^(\d+)/$', 'pages.views.home', name='pagesHome'),
    url(r'^delNotebook/(\d+)/$', 'pages.views.delNotebook', name='pagesDelNotebook'),
    url(r'^delPage/(\d+)/$', 'pages.views.delPage', name='pagesDelPage'),
    url(r'^delStack/(\d+)/$', 'pages.views.delStack', name='pagesDelStack'),
    url(r'^makeDefaultNotebook/(\d+)/$', 'pages.views.makeDefaultNotebook', name='pagesMakeDefaultNotebook'),
    url(r'^newNotebook/$', 'pages.views.newNotebook', name='pagesNewNotebook'),
    url(r'^newPage/$', 'pages.views.newPage', name='pagesNewPage'),
    url(r'^newStack/$', 'pages.views.newStack', name='pagesNewStack'),
    url(r'^notebook/(\d+)/$', 'pages.views.notebook', name='pagesNotebook'),
    url(r'^notebooks/$', 'pages.views.notebooks', name='pagesNotebooks'),
    url(r'^page/(\d+)/$', 'pages.views.page', name='pagesPage'),
    url(r'^stack/(\d+)/$', 'pages.views.stack', name='pagesStack'),
    url(r'^stacks/$', 'pages.views.stacks', name='pagesStacks'),
    url(r'^restorePage/(\d+)/$', 'pages.views.restorePage', name='pagesRestorePage'),
    url(r'^trash/$$', 'notes.views.trash', name='notesTrash'),
)
