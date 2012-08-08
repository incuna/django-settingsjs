from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

from . import signals


def settings_js(request, extra_context=None):
    mimetype = 'text/javascript'

    context = RequestContext(request)
    if extra_context != None:
        context.update(extra_context)

    context['settings'] = getattr(context, 'settings', {})
    if hasattr(settings, 'SETTINGS_JS'):
        context['settings'].update(settings.SETTINGS_JS)

    signals.collect_settings.send(sender=settings_js,
                            jssettings=context['settings'], request=request)

    return render_to_response('settingsjs/settings.js', context, mimetype=mimetype)
