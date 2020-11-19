import logging.handlers
from flask import Flask, Response
import os
import flask
import time

application = Flask(__name__)

@application.route("/health", methods=["get"])
def health():

    rsp = "I am super happy at ... " + str(time.time())
    frsp = Response(rsp, content_type="text/plain", status=200)
    return rsp


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.

    application.debug = True
    #application.before_request(do_something_before)
    #application.after_request(do_something_after)
    application.run(host='0.0.0.0', port=5001)
