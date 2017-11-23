
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"staticfoldername"), #CSS/JS Static Folder
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "projectname/static_cdn", "static_root") #Project Folder/ Media File Saving Folder

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "projectname/static_cdn", "media_root") #Media File Saving Folder 