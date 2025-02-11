from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_test_data(apps, schema_editor):
    User = apps.get_model('users', 'User')  # Replace 'users' with your actual app name
    StudentAchievement = apps.get_model('users', 'StudentAchievement')

    # Create school user
    school = User.objects.create(
        username="abc_school",
        email="school@slate.com",
        password=make_password("123456"),
        role="school",
        first_name="ABC",
        last_name="School"
    )

    # Create student user
    student = User.objects.create(
        username="riya_sharma",
        email="student@slate.com",
        password=make_password("987654"),
        role="student",
        first_name="Riya",
        last_name="Sharma"
    )

    # Create parent user
    parent = User.objects.create(
        username="rahul_gupta",
        email="parent@slate.com",
        password=make_password("654321"),
        role="parent",
        first_name="Rahul",
        last_name="Gupta",
        linked_student_id=student.id  # Link parent to student
    )

    # Create student achievement
    StudentAchievement.objects.create(
        student=student,
        school_name="ABC School",
        achievements="Science Olympiad Winner"
    )

def remove_test_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    StudentAchievement = apps.get_model('users', 'StudentAchievement')
    
    User.objects.filter(email__in=[
        "school@slate.com",
        "parent@slate.com",
        "student@slate.com"
    ]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_user_linked_student_id'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(create_test_data, remove_test_data)
    ]