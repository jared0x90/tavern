from flask import *
import language
import settings

if(settings.DEBUG == True):
    print (language.DEBUG_ENABLED)
    print (dir(settings))

# initiate flask
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/static'
)

# before requests are processed
@app.before_request
def before_request():
    # split the request URL into peices and grab the domain and path
    url_base = str(request.url)
    url_parts = url_base.split('/', 3)
    g.request_domain = url_parts[2]
    g.request_path = url_parts[3]


# create routes
@app.route("/")
def index():
    return g.request_domain

# start flask
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 80)
