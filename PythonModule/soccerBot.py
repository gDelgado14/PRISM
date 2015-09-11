
'''
    ######################################################################
                                Final Project
                            
    Send me a daily email containing the best gif of the day based by upvotes
                
    author: Giorgio Delgado
    ######################################################################
    
    
    NOTES:
    Python Reddit API Wrapper (PRAW) library required to for bot to run
    use 'sudo pip install praw' in terminal to install PRAW in your local machine
    
    Installation details: https://praw.readthedocs.org/en/latest/index.html#installation
    
    PRAW documentation home page: https://praw.readthedocs.org/en/latest/index.html
'''

import praw
import time
import smtplib

user_agent = "getting top posts from /r/soccer, v0.1, by /u/gigi14"

soccer_bot = praw.Reddit(user_agent=user_agent)

r_soccer = soccer_bot.get_subreddit('soccer')

top_posts = r_soccer.get_top_from_day()

video_link = 'streamable.com'


GMAIL_USERNAME = "wilf.the.programmer@gmail.com"
GMAIL_PASSWORD = "Nivh?2KZ3g.b9dEZJ4i"
email_subject = "Your daily top soccer video"
recipient = "delg4200@mylaurier.ca"


while True:
    
    # this loop iterates from most popular to least popular
    for top in top_posts:
        print(top)
        # check to see if current submission url is from streamable.com
        if video_link in top.url:
            
            # adapted from http://jmduke.com/posts/how-to-send-emails-through-python-and-gmail/
            # The body of the email is using HTML tags to add links and line breaks
            body_of_email = """Hey Gio,
            <br><br>
            this was yesterday's top highlight:
            <br>
            <a href="{0}">{1}</a>
            <br>
            <a href="{2}">Permalink</a>
            <br><br>
            Till next time!""".format(top.url, top.title, top.permalink)
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.ehlo()
            session.starttls()
            session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
            headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                           "subject: " + email_subject,
                           "to: " + recipient,
                           "mime-version: 1.0",
                           "content-type: text/html"])
    
            # body_of_email can be plaintext or html!                    
            content = headers + "\r\n\r\n" + body_of_email
            session.sendmail(GMAIL_USERNAME, recipient, content)
            #print (top.url)
            print ("successfully sent mail")
            break
        
    # do this again tomorrow
    time.sleep(86400)