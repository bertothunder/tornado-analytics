# -*- coding: utf-8 -*-

import os.path

from tornado.options import define

SERVICE_ACCOUNT = '***REMOVED***'
# seconds
CACHE_EXPIRES = 180

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

settings = {}

settings["debug"] = True
settings["cookie_secret"] = "askdfjpo83q47r9haskldfjh8"
settings["login_url"] = "/login"
settings["static_path"] = os.path.join(os.path.dirname(__file__), "static")
settings["template_path"] = os.path.join(os.path.dirname(__file__), "templates")
settings["xsrf_cookies"] = False
settings["service_account_email"] = SERVICE_ACCOUNT
