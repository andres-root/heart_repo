#!/usr/bin/env python
# vim: ts=4 shiftwidth=4 expandtab

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name", "none")
        e = self.response.write
        e("This is  Test:<b>" + name + "</b>")
        e('<br/>Options')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
