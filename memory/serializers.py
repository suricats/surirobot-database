from rest_framework import serializers
from .models import Info, User, Encoding, Log, SensorData


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        read_only_fields = ('created', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created', )


class EncodingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encoding
        fields = '__all__'
        read_only_fields = ('created', 'updated')


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
        read_only_fields = ('created', )


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
        read_only_fields = ('created', )
