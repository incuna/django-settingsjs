from django.conf.urls.defaults import *
urlpatterns = patterns(
    'settingsjs.views',
    url(r'^settings.js$', 'settings_js', name='settings_js'),
)
