import webapp2
import jinja2
import logging
import os
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

def RenderTemplate(template_name, values):
    template = jinja_environment.get_template(template_name)
    return template.render(values)

# class Blog(ndb.Model):


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(RenderTemplate(template, template_values))
    
    def post(self):
        self.response.out.write(RenderTemplate('blog.html', template_values))


# class PostHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.out.write(RenderTemplate('post_blog.html', {'date': date.today().isoformat()}))

#     def post(self):
#         if self.request.get('pwd') == 'cseMIT17':
            
#             date = self.request.get('date')
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
    # ('/blog/(.*)', BlogHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
