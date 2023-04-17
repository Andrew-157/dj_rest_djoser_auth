from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,\
    UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        # The order in 'fields' variable
        # defines the order of parameters in the Browsable API
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'password'
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        # The order in 'fields' variable
        # defines the order of parameters in the Browsable API
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
        ]
