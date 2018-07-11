from django.contrib import admin

from .models import (
    User,
    FriendInvitation,
    ManagedFriendship,
    ThumbsUp,
    Report
)

users_models = [User, FriendInvitation, ManagedFriendship, ThumbsUp, Report]
admin.site.register(users_models)
