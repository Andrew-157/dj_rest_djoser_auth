AUTHENTICATING IN DJANGO-REST-FRAMEWORK BACKEND USING DJOSER

Apply Token-Based authentication in DRF project using djoser, djangorestframework-simplejwt

Packages to install:
    django,
    djangorestframework,
    djangorestframework_simplejwt,
    djoser

Start project using command:
    django-admin startproject <your_project>


In 'your_project.settings.py':
    ```
    INSTALLED_APPS = [
    ...
    'rest_framework',
    'djoser',
    ]
    ```


In 'your_project.urls.py':
    ```
    urlpatterns = [
        ...
        # Register urls from djoser
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
    ]
    ```

Add following to the 'your_project.settings.py':

    ```
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            ),
        }

        SIMPLE_JWT = {
            'AUTH_HEADER_TYPES': ('JWT', ),
            'ACCESS_TOKEN_LIFETIME': timedelta(hours=3)
        }
    ```
