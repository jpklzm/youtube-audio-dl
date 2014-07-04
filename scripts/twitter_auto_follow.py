import os
import time

import tweepy


API_KEY = os.environ['TWITTER_API_KEY']
API_SECRET = os.environ['TWITTER_API_SECRET']

ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_TOKEN_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

search_terms = [
    'youtube mp3',
    # '#t1d',
    # '#insulin',
    # '#glucose',
]

for search_term in search_terms:
    print 'Searching for %s...' % search_term
    search_results = api.search(q=search_term)
    for result in search_results:
        if not result.user.following:
            print 'Following %s...' % result.user.screen_name
            result.user.follow()
            time.sleep(10)


# Unfollow users not following me (yes, not nice, but gotta cleanup sometimes).
# for f in tweepy.Cursor(api.friends).items(1200):
#     source, target = api.show_friendship(source_screen_name=f.screen_name,
#                                          target_screen_name='glucosetracker')
#     print source.screen_name, target.screen_name, target.followed_by
#
#     if not target.followed_by:
#         api.destroy_friendship(screen_name=source.screen_name)
#
#     time.sleep(20)