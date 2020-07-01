import tweepy
from time import sleep

auth = tweepy.OAuthHandler('f90KN0JjDogEiwi0iVNFKviyA', '1OmBBNcwt66HMdaIw0Gy1kkfwMQ9N7rj9RjwB485KxBBelXLec')
auth.set_access_token('4761843672-oAO0MhCH3yaEbcQWLFJNtZ6BdrFOzUnTvuNMI8H','uZnUoXy50MnasrsPog9VAm0vE9L6JwJ8qWcOIotm8h0br')

api = tweepy.API(auth)

user = api.get_user('sonakshisinha')
user.unfollow()
def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)
	except StopIteration:
		print('Done!')


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	if(follower.screen_name == 'pravar_pagare'):
		follower.follow()

# user = api.me()
# print(user.screen_name)
# print(user.followers_count)
# print(user.user_name)