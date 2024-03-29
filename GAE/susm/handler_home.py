#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import users


class MainHandler(webapp.RequestHandler):
    def get(self):
        logged = False
        username = ""
        user = users.get_current_user()
        if user:
            logged = True
            username = user.nickname()
            self.redirect("/user/"+username)
        else:            
            path = os.path.join(os.path.dirname(__file__), os.path.join('templates', 'home.html'))
            # create template values
            template_values = {
                'url_login': users.create_login_url("/"),
                'url_logout': users.create_logout_url("/"),
                'logged': logged,
                'username': username
                }
        
            # render the template and display it
            self.response.out.write(template.render(path, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
