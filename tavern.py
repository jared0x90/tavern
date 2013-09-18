import flask
import language
import settings

if(settings.DEBUG == True):
	print (language.DEBUG_ENABLED)
	print (dir(settings))
