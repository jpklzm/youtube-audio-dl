import re
from unicodedata import normalize

import youtube_dl


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')


def slugify(text, delim=u'-'):
    """
    Slugifies a string.

    Source: http://stackoverflow.com/questions/9042515/normalizing-unicode-\
        text-to-filenames-etc-in-python
    """
    result = []
    for word in _punct_re.split(text):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


def create_filename(value):
    """
    Delete non-ASCII characters from the value and replace spaces with
    underscores. Also strip slashes and percent signs.
    """
    return '%s.mp3' % slugify(value, u'_')


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