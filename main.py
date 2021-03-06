import webapp2
import jinja2
import urllib2
import logging
import os
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Account(ndb.Model):
    user = ndb.UserProperty(required=True)
    points = ndb.IntegerProperty(required=False)

class ImageEvent(ndb.Model):
    src = ndb.StringProperty(required=True)
    sender = ndb.KeyProperty(Account)
    receiver = ndb.KeyProperty(Account)
    answer = ndb.StringProperty(required=True)

def RenderTemplate(template_name, values):
    template = jinja_environment.get_template(template_name)
    return template.render(values)

def getUser(usr):
    return Account.query().filter(Account.user==usr).get()

def determineIdentifier(account_instance):
    """returns a string that will identify the account reasonably
       string chosen by this order: first name last initial,
       first name, last name, email"""
    if account_instance.user.user_id() != "":
        return account_instance.user.user_id()
    if account_instance.user.nickname() != "":
        return account_instance.user.nickname()


def topNPointLeaders(n):
    """returns a list of n {identifier, points} dictionaries"""
    topN = []

    sorted_accounts = Account.query().order(-Account.points).fetch(n)

    for account_instance in sorted_accounts:
        identifier = determineIdentifier(account_instance)
        topN.append( {'identifier': identifier, 'points': account_instance.points} )

    return topN


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        # check to see if the user is a new user
        current_user = users.get_current_user()
        userData = getUser(current_user)

        # Create new user if not found in the db
        if not userData:
            userData = Account(user=current_user, 
                                points=0)
            userData.put()
            self.response.out.write(RenderTemplate('home.html', {'photoList': []}))

        # Fetch photos
        photo_objects = []
        new_photos = ImageEvent.query().filter(ImageEvent.receiver==userData.key)
        if new_photos:
            for photo_instance in new_photos:
                photo_objects.append(photo_instance)

        self.response.out.write(RenderTemplate('home.html', {'photoList': photo_objects}))


class SendHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('send.html', {}))


    def post(self):
        current_user = users.get_current_user()
        answer = self.request.get('answer').lower()
        src = self.request.get('pic_src')
        userData = getUser(current_user)
        friend = users.User(self.request.get('friend'))
        friendData = getUser(friend)
        if not friendData:
            friendData = Account(user=friend, 
                                points=0)
            friendData.put()

        pic_event = ImageEvent(sender=userData.key, 
                               receiver=friendData.key, 
                               answer=answer,
                               src=src)
        pic_event.put()
        self.redirect('/')

class GuessHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('home.html', {}))


    def post(self):
        guess = self.request.get('guess').lower()
        image_id = int(self.request.get('img_id'))
        used_image = ImageEvent.get_by_id(image_id)
        answer = used_image.answer
        possible_answers = [answer, 
                            answer[:-3], 
                            answer[:-1], 
                            answer + 's', 
                            answer + 'ing']

        userData = getUser(users.get_current_user())
        if guess in possible_answers:
            used_image.key.delete()
            userData.points += 1
            userData.put()
            isCorrect = True

        else:
            isCorrect = False

        # Grab the top point leaders to display on the leaderboard
        num = 5
        sorted_accounts = Account.query().order(-Account.points).fetch(num)
        #point_leaders = topNPointLeaders(num)

        self.response.out.write(RenderTemplate('results.html', 
                                              {'isCorrect': isCorrect, 
                                               'points': userData.points,
                                               'sorted_accounts': sorted_accounts,
                                               'number_of_leaders': num }))

routes = [
    ('/', HomeHandler),
    ('/send', SendHandler),
    ('/guess', GuessHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
