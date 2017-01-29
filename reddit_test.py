import praw



reddit = praw.Reddit(client_id='3WQCPknt9uN63g',
                     client_secret='F6CVoE_M51YzugLqlT6VGqAh34g',
                     password='bassem123',
                     user_agent='testscript by /u/ybce',
                     username='ybce')

subreddit = reddit.subreddit('soccer')
for submission in subreddit.top('all'):
    if submission.title.find('Ronaldo') != -1:
        print submission.title+': '+ submission.shortlink
