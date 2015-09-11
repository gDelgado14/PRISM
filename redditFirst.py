'''
    ######################################################################
                            First Look At Reddit's API
                            
                                Karma Breakdown
                breaks down a redditors karma by subreddit
                
    from: https://praw.readthedocs.org/en/latest/pages/getting_started.html
    ######################################################################
    
    
    NOTES:
    Python Reddit API Wrapper (PRAW) library required to for bot to run
    use 'sudo pip install praw' in terminal to install PRAW in your local machine
    
    Installation details: https://praw.readthedocs.org/en/latest/index.html#installation
    
    PRAW documentation home page: https://praw.readthedocs.org/en/latest/index.html
'''

# import PRAW library
import praw

# pprint library allows for data to look nice and legible
import pprint

# give the bot a unique identity so that if we violate any Reddit API rules
# we may be notified or banned altogether.
# your user_agent string should not contain the keyword "bot"
# Reddit API rules: https://github.com/reddit/reddit/wiki/API#rules
user_agent = "karma breakdown, hosted on Cloud9, v: 1.0, by /u/gigi14"


#                           IT's ALIIIIIVEEEEEE.
# this is the same as a human going to www.reddit.com
# and landing on the home page
karma_bot = praw.Reddit(user_agent=user_agent)

# variable representing /u/gigi14
user_name = "gigi14"

# retrieve data about /u/gigi14
# similar to going to https://reddit.com/u/gigi14
user = karma_bot.get_redditor(user_name)

# let's not make our bot work too hard
submit_limit = 10

# this variable contains /u/gigi14's 10 latest submissions
submissions = user.get_submitted(limit=submit_limit)

# variable containing an empty data structure
# this data structure is known as a dictionary
karma_by_subreddit = {}

# iterate through the 10 submissions, each one reffered to as "item"s 
# and store them in our dictionary

# using a method (set of instructions) on the dictionary called "get"
# http://www.tutorialspoint.com/python/dictionary_get.htm
for item in submissions:
    sub = item.subreddit.display_name
#                               if within our 10 submissions we have repeting
#                               subreddits, add karma together    
    karma_by_subreddit[sub] = ( karma_by_subreddit.get(sub, 0) + item.score )


# let's print out the data we've retrieved to the console! 
pprint.pprint(karma_by_subreddit)


