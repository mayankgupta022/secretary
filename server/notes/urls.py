from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'notes.views.home', name='notesHome'),
    url(r'^(\d+)/$', 'notes.views.home', name='notesHome'),
    url(r'^trash/$$', 'notes.views.trash', name='notesTrash'),
    url(r'^newBoard/$', 'notes.views.newBoard', name='notesNewBoard'),
    url(r'^newNote/$', 'notes.views.newNote', name='notesNewNote'),
    url(r'^delBoard/(\d+)/$', 'notes.views.delBoard', name='notesDelBoard'),
    url(r'^delNote/(\d+)/$', 'notes.views.delNote', name='notesDelNote'),
    url(r'^restoreNote/(\d+)/$', 'notes.views.restoreNote', name='notesRestoreNote'),
    url(r'^board/(\d+)/$', 'notes.views.board', name='notesBoard'),
    url(r'^boards/$', 'notes.views.boards', name='notesBoards'),
    url(r'^note/(\d+)/$', 'notes.views.note', name='notesNote'),
    url(r'^makeDefaultBoard/(\d+)/$', 'notes.views.makeDefaultBoard', name='notesMakeDefaultBoard'),
)
