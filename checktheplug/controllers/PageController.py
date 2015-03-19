from bottle import get, post, template, request, redirect, static_file
from checktheplug.data.UserDao import UserDao
from checktheplug.data.ServerDao import ServerDao
from checktheplug.data.AppDao import AppDao
from checktheplug.models.AppCommonContainer import AppCommonContainer
import base64

def check_session(func):
    def wrapped(*args, **kwargs):
        if not extract_user_from_session():
            redirect('/login')
        return func(*args, **kwargs)
    return wrapped

@get('/')
@check_session
def loadHomepage():
    return template('home_page', user = extract_user_from_session())

@get('/login')
def load_login():
    return template('login_page', title='Check The Plug, Time to sign in')

@post('/login')
def attempt_login():
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
@check_session
def load_search_page():
    return template('search_page', title='Check The Plug Search', searchTerm=None)

@get('/search/<term>')
def load_search_page_with_term(term):
    return template('search_page', title='Check The Plug Search', searchTerm=term)

@get('/create')
@check_session
def load_create_page():
    return template('create_page', title='Check The Plug Create', message=None)

@post('/create')
@check_session
def attempt_create_page():
    appname = request.forms.get('appname')
    description = request.forms.get('description')
    host = request.forms.get('host')
    user = extract_user_from_session()
    dockerfile = request.files.get('dockerfile')
    dockerfileEncoded = base64.b64encode(dockerfile.file.read()).decode("utf-8") if dockerfile else ""
    if user:
        newId, newAppShortKey, message = AppDao(AppCommonContainer().settings).createNewApp(user, appname, description, host, dockerfileEncoded)
        if newId == -1:
            return template('create_page', title='Check The Plug Create', message=message)
        else:
            redirect('/app/' + str(newId))

@get('/app/<id>')
@check_session
def load_app_page(id):
    user = extract_user_from_session()
    appDao = AppDao(AppCommonContainer().settings)
    results = appDao.get_app_details_by_id(id)
    message = "Access Denied"
    can_display_contents = False
    if "status" in results:
        message = results["status"]
    else:
        if user.id != int(results["owner"]):
            if appDao.verify_user_access_to_app(user.id, id, True):
                can_display_contents = True
        else:
            can_display_contents = True
    return template('display_app_page', title='App Information', message=None if can_display_contents else message, appData=results if can_display_contents else None)

def extract_user_from_session():
    session = request.environ.get('beaker.session')
    return session.get('user', None)

@get('/servers')
@check_session
def retrieve_all_servers():
    user = extract_user_from_session()
    server_dao = ServerDao(AppCommonContainer().settings)
    results = server_dao.retrieve_all_servers()
    data = {"servers": results[0], "message": None}
    return template('display_servers_page', title='Server List', **data)

# Static Routes a la - http://stackoverflow.com/questions/10486224/bottle-static-files
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')