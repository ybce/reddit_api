import praw
import datetime
import time
import arrow



reddit = praw.Reddit(client_id='3WQCPknt9uN63g',
                     client_secret='F6CVoE_M51YzugLqlT6VGqAh34g',
                     password='',
                     user_agent='testscript by /u/ybce',
                     username='ybce')


#Get submission and link from certain subbreddits

'''
subreddit = reddit.subreddit('soccer')
for submission in subreddit.top('all'):
        if submission.title.find('Ronaldo') != -1:
            print type(submission)

'''

#Fetch a stream of submissions from a subreddit
'''
for submission in reddit.subreddit('soccer').stream.submissions():
    print submission.date
'''




def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

def unix_time(datetime):
    return arrow.get(datetime).timestamp





#Fetch submissions between certain time periods in UNIX time and certain keywords
subreddit = reddit.subreddit('soccer')

count = 0
for submission in subreddit.submissions(1451606400,1451692800, extra_query="title:'Messi'"):
    count += 1
    print str(count) + ": " + submission.title + ' ' + submission.shortlink + ' ('+ str(get_date(submission)) + ')'




