from setuptools import setup, find_packages

from settingsjs import get_version
setup(
    name='django-settingsjs',
    packages=find_packages(),
    include_package_data=True,
    version=get_version(),
    description='Configurable Javascript settings in Django.',
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='http://github.com/incuna/django-settingsjs/',
)
