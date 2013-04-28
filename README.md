Red File Browser Extensions
==================

Crop FileBrowser is an extension to FileBrowser <https://github.com/sehmaschine/django-filebrowser/>` that allows you to use JCrop <http://deepliquid.com/content/Jcrop.html> to create custom crops for your image versions:

Requirements
------------
Working with upstream releases:

* FileBrowser 3.5.2
* Django 1.5 (http://www.djangoproject.com)
* Grappelli 2.4.4 (https://github.com/sehmaschine/django-grappelli)
* PIL (http://www.pythonware.com/products/pil/)

Installation
------------

python setup.py install

Open settings.py and add crop_filebrowser to your INSTALLED_APPS if you want access to the filebrowser management commands you should include it as well:

    INSTALLED_APPS = (
        'grappelli',
        'crop_filebrowser',
        'filebrowser',
        'django.contrib.admin',
    )

In your url.py import the default CropFileBrowser site:

from crop_filebrowser.sites import site
and add the following URL-patterns (before any admin-urls):

urlpatterns = patterns('',
   url(r'^admin/filebrowser/', include(site.urls)),
)
