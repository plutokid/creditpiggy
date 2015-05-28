from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'creditpiggy.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', 	include(admin.site.urls)),
	url(r'^api/', 		include('creditpiggy.api.urls')),
	url('', 			include('creditpiggy.frontend.urls')),

    # - Social Auth ---
    url('', include('social.apps.django_app.urls', namespace='social'))
    # -----------------

)
