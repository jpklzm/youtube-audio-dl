from django.contrib import admin

from djcelery.models import TaskMeta

from api.models import ActivityLog, YouTube


class TaskMetaAdmin(admin.ModelAdmin):
    readonly_fields = ('result',)

    list_filter = ['status']
    list_display = [
        'task_id',
        'status',
        'result',
        'date_done',
    ]


class ActivityLogAdmin(admin.ModelAdmin):
    search_fields = [
        'client_ip',
        'video_id',
    ]

    list_display = (
        'video_id',
        'client_ip',
        'action',
    )

    list_filter = (
        'action',
    )


class YouTubeAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'url',
        'video_id',
        'audio_filename'
    ]

    list_display = (
        'title',
        'video_id',
        'url',
        'duration',
        'audio_filename',
        'audio_filesize',
        'download_count',
        'last_download_date',
        'created',
        'modified',
    )


admin.site.register(TaskMeta, TaskMetaAdmin)

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(YouTube, YouTubeAdmin)