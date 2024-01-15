from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'name', 'phone_num', 'child_name', 'child_birth', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            name=validated_data['name'],
            phone_num=validated_data.get('phone_num', ''),  # 'phone_num'이 없을 경우 기본값은 빈 문자열로 설정
            child_name=validated_data.get('child_name', ''),  # 'child_name'이 없을 경우 기본값은 빈 문자열로 설정
            child_birth=validated_data.get('child_birth', None),  # 'child_birth'이 없을 경우 기본값은 None으로 설정
            password=validated_data['password']
        )
        return user

# 패스워드가 필요없는 다른 테이블에서 사용할 용도
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'nickname', 'name', 'phone_num', 'child_name', 'child_birth')