import tweepy as tw
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

user = api.me()

print('User details are: ')
print(user.name)
print(user.screen_name)
print(user.followers_count)


def limit_handled(cursor):
    try:
        while True:
            yield cursor.next()

    except tw.RateLimitError:
        time.sleep(10)

    except StopIteration:
        time.sleep(10)


for friend in user.friends():
    print(friend.name)


for follower in limit_handled(tw.Cursor(api.followers).items()):
    print(follower.screen_name)
    follower.follow()


api.create_favorite('tweet_id')
api.destroy_favorite('tweet_id')
