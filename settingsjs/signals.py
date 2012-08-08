from django.dispatch import Signal


collect_settings = Signal(providing_args=["jssettings"])
