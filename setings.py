MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

#…
INSTALLED_APPS = [
    #...
    'blog’,
    'rest_framework',
]
#…
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.IsAdminUser’,
    ],
    'PAGE_SIZE': 10
}

INSTALLED_APPS = [
#...
'blog’,
'rest_framework’,
'rest_framework.authtoken', #added
]