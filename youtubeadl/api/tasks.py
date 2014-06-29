from __future__ import absolute_import

import os
import shutil
import subprocess
import uuid

from django.conf import settings

from celery import shared_task

from api import utils
from api.models import YouTube, ActivityLog


@shared_task
def extract_audio(url, client_ip=None):
    """
    Extract the YouTube audio to mp3 format.

    Steps:
        1. Get the video's information to make sure the provided url is valid.
        2. If info is returned and the duration is no more than 120 minutes,
           log the request and start the extraction.
        3. Return the download link if extraction completes successfully.
    """
    info = utils.get_video_info(url)

    result = None
    if info and info['duration'] <= settings.MAX_DURATION_MINUTES:
        video_id = info['id']
        title = info['title']

        ActivityLog.objects.create(
            client_ip=client_ip,
            video_id=video_id,
            action='EXTRACT',
        )

        audio_filename = utils.create_filename(info['title'])

        youtube, created = YouTube.objects.get_or_create(video_id=video_id)
        youtube.url = url
        youtube.title = title
        youtube.duration = int(info['duration'])
        youtube.save()

        result = {'video_id': video_id, 'title': title}

        # Simply return the filename if it already exists, otherwise, start
        # the extraction.
        output_filepath = '%s%s' % (settings.MEDIA_ROOT, audio_filename)
        if os.path.exists(output_filepath):
            result['filename'] = audio_filename
        else:
            extraction_result = start_extraction(url, audio_filename, youtube)

            # If extraction result is 0, extraction is successful.
            if extraction_result == 0:
                result['filename'] = audio_filename

    return result


def start_extraction(url, output_file, youtube_obj):
    # We're creating a temporary file in case multiple workers are in the
    # process of extracting the same video.
    temp_filepath = '%s%s_%s' % (settings.MEDIA_ROOT, uuid.uuid4(), output_file)

    output_filepath = '%s%s' % (settings.MEDIA_ROOT, output_file)

    result = subprocess.check_call([
        'youtube-dl',
        '--no-playlist',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--output', temp_filepath,
        url,
    ])

    # Status code 0 is successful.
    if result == 0:
        # Move the temporary file to the proper location.
        shutil.move(temp_filepath, output_filepath)

        # Update the YouTube object.
        youtube_obj.audio_filename = output_file
        youtube_obj.audio_filesize = os.path.getsize(output_filepath)
        youtube_obj.save()

    return result