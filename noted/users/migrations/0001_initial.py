# Generated by Django 4.1.3 on 2023-02-12 19:20

import taggit.managers

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import users.models
import users.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tags", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=254,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        help_text="Username should include only latin letters, digits and dots.             Username can't start and end with a dot or don't contain letters.             Digits can be added only at the end.",
                        max_length=150,
                        unique=True,
                        verbose_name="Username",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        blank=True,
                        help_text="Your name appear around NoteD where you post or do actions.",
                        max_length=50,
                        verbose_name="Full Name",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Staff"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False, verbose_name="Superuser"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="User activated"
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Last Login"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date Joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AuthToken",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Token"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("sn", "Sign Up Token"),
                            ("cm", "Change Email Token"),
                        ],
                        max_length=2,
                        verbose_name="Type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        default="user/default_avatar.jpg",
                        upload_to=users.models.user_avatars_path,
                        validators=[users.validators.validate_image],
                        verbose_name="Profile picture",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=700, verbose_name="Bio"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=40, verbose_name="Location"
                    ),
                ),
                (
                    "socials",
                    models.JSONField(
                        blank=True,
                        default=users.models.default_social_media_json,
                        verbose_name="Social Media Links",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="tags.UnicodeTaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tag subscriptions",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Following",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "followed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "follower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriptions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
