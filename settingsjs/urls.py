from django.conf.urls import patterns, url
urlpatterns = patterns(
    'settingsjs.views',
    url(r'^settings.js$', 'settings_js', name='settings_js'),
)
