# Generated by Django 4.2.6 on 2023-12-15 15:37

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Username must consist of @ followed by at least three alphanumericals', regex='^@\\w{3,}$')])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('board_type', models.CharField(choices=[('INVALID', 'Choose Type'), ('Private', 'Private'), ('Team', 'Team')], default='INVALID', max_length=11)),
                ('team_emails', models.TextField(default='Enter team emails here if necessary, seperated by commas.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembershipStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_level', models.IntegerField(choices=[(1, 'Owner'), (2, 'Member'), (3, 'Guest')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='team_member', through='tasks.TeamMembershipStatus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='teammembershipstatus',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.teams'),
        ),
        migrations.AddField(
            model_name='teammembershipstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listName', models.CharField(max_length=50)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.board')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.TextField(max_length=1000)),
                ('due_date', models.DateTimeField()),
                ('task_priority', models.TextField(choices=[('NONE', 'None'), ('LOW', 'Low'), ('MID', 'Mid'), ('HIGH', 'High')], default='NONE')),
                ('assigned_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasklist')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
        migrations.AddField(
            model_name='board',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.teams'),
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_boards_created', models.IntegerField(default=0)),
                ('number_of_boards_deleted', models.IntegerField(default=0)),
                ('number_of_tasks_created', models.IntegerField(default=0)),
                ('number_of_tasks_doing', models.IntegerField(default=0)),
                ('number_of_tasks_completed', models.IntegerField(default=0)),
                ('number_of_logins_completed', models.IntegerField(default=0)),
                ('boards_created_1', models.DateField(blank=True, null=True, verbose_name='1st Board Deleted')),
                ('boards_created_10', models.DateField(blank=True, null=True, verbose_name='10th Board Deleted')),
                ('boards_created_50', models.DateField(blank=True, null=True, verbose_name='50th Board Deleted')),
                ('boards_created_100', models.DateField(blank=True, null=True, verbose_name='100th Board Deleted')),
                ('boards_deleted_1', models.DateField(blank=True, null=True, verbose_name='1st Board Deleted')),
                ('boards_deleted_10', models.DateField(blank=True, null=True, verbose_name='10th Board Deleted')),
                ('boards_deleted_50', models.DateField(blank=True, null=True, verbose_name='50th Board Deleted')),
                ('boards_deleted_100', models.DateField(blank=True, null=True, verbose_name='100th Board Deleted')),
                ('tasks_created_1', models.DateField(blank=True, null=True, verbose_name='1st Board Deleted')),
                ('tasks_created_10', models.DateField(blank=True, null=True, verbose_name='10th Board Deleted')),
                ('tasks_created_50', models.DateField(blank=True, null=True, verbose_name='50th Board Deleted')),
                ('tasks_created_100', models.DateField(blank=True, null=True, verbose_name='100th Board Deleted')),
                ('tasks_doing_1', models.DateField(blank=True, null=True, verbose_name='1st Board Deleted')),
                ('tasks_doing_10', models.DateField(blank=True, null=True, verbose_name='10th Board Deleted')),
                ('tasks_doing_50', models.DateField(blank=True, null=True, verbose_name='50th Board Deleted')),
                ('tasks_doing_100', models.DateField(blank=True, null=True, verbose_name='100th Board Deleted')),
                ('tasks_completed_1', models.DateField(blank=True, null=True, verbose_name='1st Board Deleted')),
                ('tasks_completed_10', models.DateField(blank=True, null=True, verbose_name='10th Board Deleted')),
                ('tasks_completed_50', models.DateField(blank=True, null=True, verbose_name='50th Board Deleted')),
                ('tasks_completed_100', models.DateField(blank=True, null=True, verbose_name='100th Board Deleted')),
                ('logins_completed_1', models.DateField(blank=True, null=True, verbose_name='1st Board Deleted')),
                ('logins_completed_10', models.DateField(blank=True, null=True, verbose_name='10th Board Deleted')),
                ('logins_completed_50', models.DateField(blank=True, null=True, verbose_name='50th Board Deleted')),
                ('logins_completed_100', models.DateField(blank=True, null=True, verbose_name='100th Board Deleted')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
