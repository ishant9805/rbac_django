from rest_framework import permissions

class IsSchoolUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'school'
        return request.user.is_authenticated

class IsParentOrStudentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        
        if request.user.role == 'school':
            return True
        elif request.user.role == 'student':
            return obj.student.id == request.user.id
        elif request.user.role == 'parent':
            return obj.student.id == request.user.linked_student_id
        return False