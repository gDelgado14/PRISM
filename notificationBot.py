'''
    ######################################################################
                            2nd look at PRAW
                            
                    Question Notification Bot
                Notify me of user submissions for PRAW keywords
                
    from: https://praw.readthedocs.org/en/stable/pages/writing_a_bot.html
    ######################################################################
    
    
    NOTES:
    Python Reddit API Wrapper (PRAW) library required to for bot to run
    use 'sudo pip install praw' in terminal to install PRAW in your local machine
    
    Installation details: https://praw.readthedocs.org/en/latest/index.html#installation
    
    PRAW documentation home page: https://praw.readthedocs.org/en/latest/index.html
'''

import time
import praw

user_agent = """ 'PRAW related-question monitor by /u/gigi14 v 1.0.'
'Url: https://praw.readthedocs.org/en/latest/'
'pages/writing_a_bot.html' """

question_monitor = praw.Reddit(user_agent=user_agent)

question_monitor.login()

already_done = []

prawWords = ['praw', 'reddit_api', 'mellort']

# run bot indefinately
while True:
    
    # search only in /r/learnpython
    subreddit = question_monitor.get_subreddit('learnpython')
    
    for submission in subreddit.get_hot(limit=10):
        op_text = submission.selftext.lower()
        has_praw = any(string in op_text for string in prawWords)
        
        #test if it contians a PRAW-related question 
        if submission.id not in already_done and has_praw:
            msg = '[PRAW related thread (%s)]' % submission.short_link
            question_monitor.send_message('gigi14', 'PRAW Thread', msg)
            already_done.append(submission.id)
            
    # sleep for 30 mins and then restart the main loop
    time.sleep(1800)