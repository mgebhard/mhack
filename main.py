import webapp2
import jinja2
import urllib2
import logging
import os
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class ImageEvent(ndb.Model):
    photo = ndb.StringProperty(required=True)
    sender = ndb.UserProperty(required=True)
    reciever = ndb.UserProperty(required=True)
    answer = ndb.StringProperty(required=True)

def RenderTemplate(template_name, values):
    template = jinja_environment.get_template(template_name)
    return template.render(values)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('home2.html', {}))


class SendHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        self.response.out.write(RenderTemplate('home2.html', {}))


    def post(self):
        src = self.request.get('pic_src')
        sender = users.get_current_user()
        friend = users.User('mgebhard1995@gmail.com')
        pic_event = ImageEvent(user=sender, 
                               friend=friend, 
                               photo=src)
        pic_event.put()
        self.redirect('/')

class GuessHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('home2.html', {}))


    def post(self):
        self.redirect('/')

routes = [
    ('/', HomeHandler),
    ('/send', SendHandler),
    ('/guess', GuessHandler),


]

app = webapp2.WSGIApplication(routes, debug=True)
