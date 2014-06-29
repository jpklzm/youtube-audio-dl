import re

import youtube_dl


def create_filename(value):
    """
    Delete non-ASCII characters from the value and replace spaces with
    underscores. Also strip slashes.
    """
    return '%s.mp3' % re.sub(r'[^\x00-\x7F]+', '', value)\
        .replace(' ', '_').replace('/', '')


def get_video_info(url):
    """
    Retrieve the YouTube videos' information without downloading it.

    Source: http://stackoverflow.com/questions/18054500/how-to-use-youtube-dl-\
            from-a-python-programm/18947879#18947879
    """
    ydl = youtube_dl.YoutubeDL()
    ydl.add_default_info_extractors()

    try:
        return ydl.extract_info(url, download=False)
    except youtube_dl.DownloadError:
        return None


def get_client_ip(request):
    """
    Retrieve the client's IPv4 address from the request object.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip