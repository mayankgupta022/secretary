from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'notes.views.home', name='notesHome'),
    url(r'^newBoard/', 'notes.views.newBoard', name='notesNewBoard'),
    url(r'^newNote/', 'notes.views.newNote', name='notesNewNote'),
    url(r'^delBoard/(\d+)/$', 'notes.views.delBoard', name='notesDelBoard'),
    url(r'^delNote/(\d+)/$', 'notes.views.delNote', name='notesDelNote'),
    url(r'^board/(\d+)/$', 'notes.views.board', name='notesBoard'),
    url(r'^note/(\d+)/$', 'notes.views.note', name='notesNote'),
)
