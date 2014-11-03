from twitter import *
import random, threading, re, os

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

t = Twitter(
    auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

def tweet():
	status = create_tweet()
	try:
		t.statuses.update(status=status)
	except:
		print "error"
	threading.Timer(60, tweet).start()

def create_tweet():
	statuses = t.search.tweets(q='#fortunecookie "you are" OR "you will" OR "you must"', count=1000)['statuses']
	status = random.choice(statuses)
	text = status['text']
	screen_name = '@' + status['user']['screen_name']
	
	parsed_text = ' '.join([word for word in text.split() if word[0] != '#' and word[0] != '@' and not re.match('http:\/\/*', word) and not re.match('^RT$', word)])	
	return ' '.join([screen_name, parsed_text.strip(',.-;"!'), 'in bed.'])

tweet()



