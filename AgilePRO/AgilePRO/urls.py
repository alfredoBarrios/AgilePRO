from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import home,logout_page
"""Match de URL's."""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AgilePRO.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^home/admin/', include(admin.site.urls)),
    url(r'^logout/$', logout_page),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    #url(r'^register/success/$', register_success),
    url(r'^home/$', home),
)
