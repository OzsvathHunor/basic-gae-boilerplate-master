#!/usr/bin/env python

import webapp2
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com'

response = urlopen(url).read()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write(response)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
