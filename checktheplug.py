from bottle import route, run, template
from controllers.ApiKeyController import ApiKeyController

@route('/isLiveKey/<inKey>')
def isLiveKey(inKey):
    apiKeyController = ApiKeyController()
    return apiKeyController.getIsLiveKey(inKey)

if __name__ == "__main__":
    run(host='localhost', port=8080)