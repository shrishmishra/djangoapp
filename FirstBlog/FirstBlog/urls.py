from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^boot$', 'blog.views.boot', name='boot'),
    url(r'^blog$', 'blog.views.blog', name='blog'),
    url(r'^savePost$', 'blog.views.savePost', name='savePost'),
    url(r'^likePost$', 'blog.views.likePost', name=''),
    url(r'^deletePost$', 'blog.views.deletePost', name='savvfveePost'),
    url(r'^login$', 'blog.views.login', name='login'),
    url(r'^logout$','blog.views.logout',name='logout'),
    # url(r'^FirstBlog/', include('FirstBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    url(r'^404$','blog.views.not_found'),
)
