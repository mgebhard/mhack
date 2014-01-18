import webapp2
import jinja2
import logging
import os
from google.appengine.ext import ndb
# Access level	 Read-only 
# About the application permission model
# Consumer key	YzDNu4d0GjT1cUxRE5Og
# Consumer secret	K0TXb6icTvv9Ka1ir7IyX7j1m3jTE1uriXPcqpqtH0A
# Request token URL	https://api.twitter.com/oauth/request_token
# Authorize URL	https://api.twitter.com/oauth/authorize
# Access token URL	https://api.twitter.com/oauth/access_token
# Callback URL	None
# Sign in with Twitter	No
# Your access token

# Use the access token string as your "oauth_token" and the access token secret as your "oauth_token_secret" to sign requests with your own Twitter account. Do not share your oauth_token_secret with anyone.

# Access token	260744596-JRgvDuj3qR6RQWxrTWZ5cuGPN4GXpiboxf3fjwXm
# Access token secret	F5x7P1VmubIcjjADmOhdVKT0cWETZIKdXW2ootZzutd4J
# Access level	Read-only

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

def RenderTemplate(template_name, values):
    template = jinja_environment.get_template(template_name)
    return template.render(values)

# class Blog(ndb.Model):


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('home.html', {}))
    
    def post(self):
        word = self.request.get('word')
        # query request the stream api
        self.response.out.write(RenderTemplate('home.html', {}))


# class PostHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.out.write(RenderTemplate('post_blog.html', {'date': date.today().isoformat()}))

#     def post(self):
#         if self.request.get('pwd') == 'cseMIT17':
            
#             dt = datetime.strptime(date, '%Y-%m-%d')
#             secret = False

#             if self.request.get('private') == 'True':
#                 secret = True

#             new_blog = Blog(date=dt,
#                             blog_writing=self.request.get('writing'),
#                             photo=self.request.get('photo'),
#                             private=secret)
#             new_blog.put()
#             self.redirect('/blog/%s' % dt.strftime('%m.%d.%Y'))

 
routes = [
    ('/', HomeHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
