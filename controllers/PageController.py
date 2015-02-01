from bottle import get, post, template, request, redirect
from data.UserDao import UserDao
from models.AppCommonContainer import AppCommonContainer

def checkSession(func):
    def wrapped(*args, **kwargs):
        session = request.environ.get('beaker.session')
        if not session.get('user', None):
            redirect('/login')
        return func(*args, **kwargs)
    return wrapped

@get('/')
@checkSession
def loadHomepage():
    return template('home_page', title='Check The Plug App Controller')

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