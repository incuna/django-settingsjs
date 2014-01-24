# django-settingsjs changelog.

## v0.1.5

Fix deprecated `django.conf.urls.defaults` import.

## v0.1.4

Use `escapejs` to escape JSON rather than assuming it is `safe`. 

## v0.1.3

Update the `settings_js` view to include a `json` encoded version of the settings in the template content.
Removes the dependency on the `json` filter from `django-incuna`.

## v0.1.2

The `request` is now passed to `collect_settings` listeners.
