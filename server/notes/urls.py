from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'notes.views.home', name='notesHome'),
    url(r'^(\d+)/$', 'notes.views.home', name='notesHome'),
    url(r'^delNote/(\d+)/$', 'notes.views.delNote', name='notesDelNote'),
    url(r'^newNote/$', 'notes.views.newNote', name='notesNewNote'),
    url(r'^note/(\d+)/$', 'notes.views.note', name='notesNote'),
    url(r'^restoreNote/(\d+)/$', 'notes.views.restoreNote', name='notesRestoreNote'),
    url(r'^trash/$$', 'notes.views.trash', name='notesTrash'),
)
