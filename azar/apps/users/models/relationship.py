from django.conf import settings
from django.db import models

from core.models import TimeStampedModel, CreatedTimeStampedModel

__all__ = (
    'FriendInvitation',
    'ManagedFriendship',
    'ThumbsUp',
    'Report',
)


# Relationships

class FriendInvitation(TimeStampedModel):
    """
    친구 신청 관계에 대한 Table

    친구신청을 수락한 경우,

    1. FriendInvitation Table의 `is_accepted` Field가 True가 되며
    확정된 친구 관계에 대해,
    2. users_user_friends에 symmetrical한 2개의 친구관계 Record가 생성된다
    """
    # 친구신청을 보낸 유저
    source = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friend_invitation_to')
    # 친구신청을 받은 유저
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='friend_invitation_from')
    is_accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('source', 'target')


class ManagedFriendship(TimeStampedModel):
    """
    관리가 되는 친구 관계에 대한 Table

    3가지 Type
    1) Bookmarked(즐겨찾기)
    2) Hidden(숨김)
    3) Blocked(차단)

    """
    BOOKMARKED = 'BM'
    HIDDEN = 'HD'
    BLOCKED = 'BL'
    MANAGE_CHOICES = (
        (BOOKMARKED, 'Bookmarked'),
        (HIDDEN, 'Hidden'),
        (BLOCKED, 'Blocked')
    )
    # 친구를 관리목록에 등록한 유저
    source = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_friendship')
    # 관리목록에 등록당한 유저
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=MANAGE_CHOICES)

    class Meta:
        unique_together = ('source', 'target')


class ThumbsUp(CreatedTimeStampedModel):
    # 엄지척을 보낸 유저
    source = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='thumbsup_to')
    # 엄지척을 받은 유저
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='thumbsup_from')

    class Meta:
        unique_together = ('source', 'target')


class Report(CreatedTimeStampedModel):
    VERBAL_ABUSE = 'VA'
    SEXUAL_ABUSE = 'SA'
    ABUSE_CHOICES = (
        (VERBAL_ABUSE, 'Verbal Abuse'),
        (SEXUAL_ABUSE, 'Sexual Abuse')
    )
    # 신고를 한 유저
    source = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='report_to')
    # 신고를 당한 유저
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='report_from')
    type = models.CharField(max_length=2, choices=ABUSE_CHOICES)
    screenshot = models.ImageField(upload_to='report-screenshot/', blank=True)

    class Meta:
        unique_together = ('source', 'target')
