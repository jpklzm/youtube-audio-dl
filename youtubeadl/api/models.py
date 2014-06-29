from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base class that provides self-updating 'created' and 'modified'
    fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class YouTube(TimeStampedModel):
    video_id = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    duration = models.IntegerField(null=True)
    audio_filename = models.CharField(max_length=255, null=True, blank=True)
    audio_filesize = models.IntegerField(null=True)
    download_count = models.IntegerField(null=True, default=0)
    last_download_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'YouTube Video'
        verbose_name_plural = 'YouTube Videos'


class ActivityLog(TimeStampedModel):
    """
    Record user activity.

    Retrieve client IP address and record whether the user requested an
    EXTRACT or DOWNLOAD. Also record the video_id so we can map it to the
    YouTube model.

    Only record successful attempts.
    """
    client_ip = models.IPAddressField(null=True)
    action = models.CharField(max_length=50)
    video_id = models.CharField(max_length=100)

