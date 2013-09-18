import flask
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
