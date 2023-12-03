from rest_framework import serializers
from .models import Artist, Work, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'firstname', 'lastname',
                  'link', 'work_type', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class WorkSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()

    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type', 'artist']


class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'
