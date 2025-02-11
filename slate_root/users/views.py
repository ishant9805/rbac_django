from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import StudentAchievement
from .permission import IsParentOrStudentUser, IsSchoolUser
from .serializers import LoginSerializer, StudentAchievementSerializer, UserSerializer
from django.contrib.auth import login
from rest_framework import viewsets, permissions



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"] # type: ignore
            login(request, user)  

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        role = request.user.role
        if role == 'school':
            return Response({
                "dashboard": "school",
                "message": f"Welcome to {request.user.first_name + request.user.last_name} School Dashboard",
                "features": ["Manage student achievements", "Admin controls"]
            })
        elif role == 'parent':
            return Response({
                "dashboard": "parent",
                "message": f"Welcome back, {request.user.first_name} {request.user.last_name} sir!",
                "features": ["View child's achievements"]
            })
        elif role == 'student':
            return Response({
                "dashboard": "student",
                "message": f"Hello, {request.user.first_name}!",
                "features": ["View personal achievements"]
            })

class StudentAchievementViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAchievementSerializer
    permission_classes = [permissions.IsAuthenticated, IsParentOrStudentUser, IsSchoolUser]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'school':
            return StudentAchievement.objects.all()
        elif user.role == 'student':
            return StudentAchievement.objects.filter(student=user)
        elif user.role == 'parent':
            return StudentAchievement.objects.filter(student_id=user.linked_student_id)
        return StudentAchievement.objects.none()
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)