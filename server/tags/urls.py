from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^allTags/(\w+)/$', 'tags.views.allTags', name='tagsAllTags'),#all tags
    url(r'^newTag/(\w+)/$', 'tags.views.newTag', name='tagsNewTag'),#new tag
    url(r'^delTag/(\w+)/(\d+)/$', 'tags.views.delTag', name='tagsDelTag'),#delete tag
    url(r'^entities/(\w+)/(\d+)/$', 'tags.views.entities', name='tagsEntities'),#all objects in a tag
    url(r'^tags/(\w+)/(\d+)/$', 'tags.views.tags', name='tagsTags'),#all tags of an object
    url(r'^tag/(\w+)/(\d+)/(\d+)/$', 'tags.views.tag', name='tagsTag'),#set tag with id for object with id
)
