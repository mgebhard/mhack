import webapp2
import jinja2
import urllib2
import logging
import os
from google.appengine.ext import ndb

# CONSUMER_KEY = "u0Cv2bijnTUiKYgcI0ruhg"
# CONSUMER_SECRET = "MJQypkYkc1i2ighitRv2AHgA4g72Uoi6kWJPZ2sC0"
# OAUTH_TOKEN = "260744596-cfKGAYckxq1K5AxnJuSNZJbTlDPI7dzavMGSozLh"
# OAUTH_SECRET = "3KoHWwmUuc4RHiv6Wo1HflMqPblFncv2wzqb3WwGjU4jz"

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

def RenderTemplate(template_name, values):
    template = jinja_environment.get_template(template_name)
    return template.render(values)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate('motion.html', {}))


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
