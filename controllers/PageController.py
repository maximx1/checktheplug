from bottle import get, post, template, request, redirect
from data.UserDao import UserDao
from data.AppDao import AppDao
from models.AppCommonContainer import AppCommonContainer
from models.User import User

def checkSession(func):
    def wrapped(*args, **kwargs):
        if not extractUserFromSession():
            redirect('/login')
        return func(*args, **kwargs)
    return wrapped

@get('/')
@checkSession
def loadHomepage():
    return template('home_page', user = extractUserFromSession())

@get('/login')
def loadLogin():
    return template('login_page', title='Check The Plug, Time to sign in')

@post('/login')
def attemptLogin():
    username = request.forms.get('username')
    password = request.forms.get('password')
    user = UserDao(AppCommonContainer().settings).login(username, password)
    if user:
        session = request.environ.get('beaker.session')
        session['user'] = user
        session.save()
        redirect('/')
    return template('login_page', title='Check The Plug, Time to sign in')

@get('/logout')
def logout():
    session = request.environ.get('beaker.session')
    session.invalidate()
    redirect('/login')

@get('/search')
@checkSession
def loadSearchPage():
    return template('search_page', title='Check The Plug Search')

@get('/search/:term')
def loadSearchPageWithTerm(term):
    return template('search_page', title='Check The Plug Search', searchTerm=term)

@get('/create')
@checkSession
def loadCreatePage():
    return template('create_page', title='Check The Plug Create', message=None)

@post('/create')
@checkSession
def attemptCreatePage():
    appname = request.forms.get('appname')
    description = request.forms.get('description')
    host = request.forms.get('host')
    user = extractUserFromSession()
    if user:
        newId, newAppShortKey, message = AppDao(AppCommonContainer().settings).createNewApp(user, appname, description, host)
        if newId == -1:
            return template('create_page', title='Check The Plug Create', message=message)
        else:
            return template('display_app_page', title='New App: ' + newAppShortKey, message='New App: ' + str(newId))

    

def extractUserFromSession():
    session = request.environ.get('beaker.session')
    return session.get('user', None)