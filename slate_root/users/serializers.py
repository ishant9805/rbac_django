from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, StudentAchievement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")

        if user.role != role:
            raise serializers.ValidationError("Role does not match.")

        data["user"] = user
        return data

class StudentAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAchievement
        fields = ['id', 'student', 'school_name', 'achievements']