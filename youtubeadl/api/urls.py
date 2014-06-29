from django.conf.urls import patterns, url

from api.views import extract_audio, download_file


urlpatterns = patterns(
    '',
    url(
        regex=r'^extract-audio/',
        view=extract_audio,
        name='extract_audio',
    ),
    url(
        regex=r'^download-file/(?P<video_id>.*)/(?P<filename>.*)$',
        view=download_file,
        name='download_file'
    )
)
