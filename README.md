# AUTHENTICATING IN DJANGO-REST-FRAMEWORK BACKEND USING DJOSER

## Apply Token-Based authentication in DRF project using djoser, djangorestframework-simplejwt

Packages to install:
```
    django
    djangorestframework
    djoser
    djangorestframework_simplejwt
```

Start project using command:
```
    django-admin startproject <your_project>
```

In 'your_project.settings.py':
```python
INSTALLED_APPS = [
    ...
    #Register djoser and djangorestframework
    'djoser',
    'rest_framework',
]
```

In 'your_project.urls.py':
```python
urlpatterns = [
    ...
    #Register djoser's urls
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
```

Add following to 'your_project.settings.py':
```python
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

Djoser provides the following endpoints:
```
    /users/
    /users/me/
    /users/confirm/
    /users/resend_activation/
    /users/set_password/
    /users/reset_password/
    /users/reset_password_confirm/
    /users/set_username/
    /users/reset_username/
    /users/reset_username_confirm/
    /jwt/create/
    /jwt/refresh/
    /jwt/verify
```

To be recognized as an authenticated user, generated token should be provided in request header like this(With Modheader extension, for example):
![Authorization](docs/images/Authorization.png)

In case you need to change default behavior of Djoser serializers, you need to do the following:
 - Start app with command:
    ```
    python manage.py startapp <your_app>
    ```
    - Register 'your_app' in 'your_project.settings.py':
        ```python
        INSTALLED_APPS = [
            ...
            'your_app',
        ]
        ```
 - Create file 'your_app.serializers.py' and define the desired behavior of serializers
    through inheritance:
    ```python
    from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,\
    UserSerializer as BaseUserSerializer


    class UserCreateSerializer(BaseUserCreateSerializer):
        ...
        class Meta(BaseUserCreateSerializer.Meta):
            fields = [
                ...
            ]


    class UserSerializer(BaseUserSerializer):
        ...
        class Meta(BaseUserSerializer.Meta):
            fields = [
                ...
            ]

    ```
 - Add the following to 'your_project.settings.py':
    ```python
    DJOSER = {
    'SERIALIZERS': {
        'user_create': 'account.serializers.UserCreateSerializer',
        'current_user': 'account.serializers.UserSerializer',
        }
    }
    ```