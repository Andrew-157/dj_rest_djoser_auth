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
        # Register djoser, djangorestframework
        'djoser',
        'rest_framework',
    ]
    ```

In 'your_project.urls.py':
    ```python
    urlpatterns = [
        ...
        # Register urls from djoser
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
    ]
    ```

Add following to the 'your_project.settings.py':
