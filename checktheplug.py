import web
from controllers.TestController import TestController

urls = (
	'/isLiveKey', 'TestController'
)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
