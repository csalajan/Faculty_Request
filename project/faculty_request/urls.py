from django.conf.urls import patterns, include, url
from rest_framework import routers
from faculty_request import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#router =routers.DefaultRouter()
#router.register(r'admin',views.admin_view)
#router.register(r'labtech',views.labtech_view)
#router.register(r'faculty',views.faculty_view)
#urlpatterns=router.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),
   # url(r'^',include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    #url(r'^faculty/$',views.faculty_view.as_view()),
    url(r'^derp/$', views.request_save),
    url(r'^requests/',views.admin_view),
    #url(r'^labtech/$',views.labtech_view.as_view()),
    
)
