import webapp2
import jinja2
import urllib2
import logging
import os
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class User(ndb.Model):
    user = ndb.UserProperty(required=True)
    points = ndb.IntegerProperty(required=False)

class ImageEvent(ndb.Model):
    src = ndb.StringProperty(required=True)
    sender = ndb.ReferenceProperty(User)
    receiver = ndb.ReferenceProperty(User)
    answer = ndb.StringProperty(required=True)

def RenderTemplate(template_name, values):
    template = jinja_environment.get_template(template_name)
    return template.render(values)

def getUser():
    current_user = users.get_current_user()
    return User.query().filter(User.user==current_user).get()

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        # check to see if the user is a new user
        userData = getUser()

        # Create new user if not found in the db
        if not userData:
            new_user = User(user=current_user, 
                            points=0)
            new_user.put()
            userData = new_user

        # Fetch photos
        photo_objects = []
        new_photos = ImageEvent.query().filter(ImageEvent.receiver==userData.key()).get()
        for photo_instance in new_photos:
            photo_objects.append(photo_instance)

        self.response.out.write(RenderTemplate('home.html', {'photoList': photo_objects}))




class SendHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        self.response.out.write(RenderTemplate('home.html', {}))


    def post(self):
        src = self.request.get('pic_src')
        userData = getUser()
        friend = users.User('mgebhard1995@gmail.com')
        pic_event = ImageEvent(sender=userData.key(), 
                               receiver=friend, 
                               src=src,
                               answer='cat')
        pic_event.put()
        self.redirect('/')

class GuessHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('home.html', {}))


    def post(self):
        answer = self.request.get('answer')
        self.redirect('/')

routes = [
    ('/', HomeHandler),
    ('/send', SendHandler),
    ('/guess', GuessHandler),


]

app = webapp2.WSGIApplication(routes, debug=True)
