# Django Static File Handle
In Django, For Static File handling add those line of code in settings.py and urls.py

# settings.py
At the end of setting.py add those lines
```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static_folder_name"),  #CSS/JS Static Files Handle
    
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "project_folder_name/static_cdn", "static_root") #Project Folder/ Media File Saving Folder

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "project_folder_name/static_cdn", "media_root") #Media File Saving Folder 
```
# urls.py
At the beginning of urls.py add those lines
```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin #For Urlpatterns Not For Media Url

urlpatterns = [
    url(r'^admin/', admin.site.urls),

]
```
At the end of urls.py add those lines
```python

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
