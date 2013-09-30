import json

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

from . import signals


def settings_js(request, extra_context=None):
    mimetype = 'text/javascript'

    context = RequestContext(request)
    if extra_context is not None:
        context.update(extra_context)

    jssettings = getattr(context, 'settings', {})
    if hasattr(settings, 'SETTINGS_JS'):
        jssettings.update(settings.SETTINGS_JS)

    signals.collect_settings.send(
        sender=settings_js,
        jssettings=jssettings,
        request=request
    )

    context.update({
        'settings': jssettings,
        'jssettings': json.dumps(jssettings)
    })

    return render_to_response('settingsjs/settings.js', context, mimetype=mimetype)
