''' apache basic authentication handler

provide script in django project like this::

    #: - activate virtualenv
    activate_this = '/home/hdknr/ve/paloma/bin/activate_this.py'
    execfile(activate_this,dict(__file__ =activate_this))

    #: - export symbol
    from accounts.authbasic import groups_for_user,check_password,authenhandler,enable_django

    #: - enable django 
    import os
    enable_django( os.path.dirname( os.path.abspath(__file__)))

'''
import os
import sys
import syslog

import re

try:
    from mod_python import apache
except:
    pass

def enable_django(project_path,setting_module="settings" ):
    sys.path.insert(0, os.path.dirname( project_path) )
    sys.path.insert(0, project_path ) 
    os.environ['DJANGO_SETTINGS_MODULE'] = "%s.%s" % (project_path.split('/')[-1:][0],setting_module )
    from app import settings
    from django.core.management import setup_environ
    setup_environ(settings)
 
def authuser(usr,pwd,groups=[]):

    from django.contrib.auth import authenticate
    u=authenticate(username=usr,password=pwd )
    if u == None:
        return False
    if len(groups) > 0 : 
        return u.groups.filter(name__in = groups).exists()
    return True

def handler(req):
    return apache.OK

def authenhandler(req ):
    ''' mod_pyton authentication handler

    apache conf ::

        PythonAuthenHandler   authbasic
        AuthType        Basic
        AuthName        "Ristricted Area"
        Require         valid-user
        Require     group hogegroup  
        PythonPath      "['/home/www/.ve/admin/src/authadmin']+sys.path"
        AuthBasicAuthoritative Off

    '''
    pwd = req.get_basic_auth_pw()
    user = req.user
    groups= [ re.split('[\t\s]+',g)[1]  for g in req.requires() if g !="valid-user" ]
    if user != None:
        u = user.decode('utf-8')
        if authuser(u,pwd,groups ):
            return apache.OK
    return apache.HTTP_UNAUTHORIZED

def check_password(environ, user, password):
    ''' mod-wsgi basic authentication handler

    apache conf::

        <Location /wsgi >
        
        AuthType Basic
        AuthName "Mod-Wsgi Basic Authentication"
        AuthBasicProvider wsgi
        WSGIAuthUserScript /home/hdknr/ve/paloma/src/peacock/example/app/basicauth.py
        WSGIAuthGroupScript /home/hdknr/ve/paloma/src/peacock/example/app/basicauth.py
        Require valid-user
        Require group hoge
        
        </Location>
        
    '''
    return authuser(user,password)

def groups_for_user(environ, user):
    ''' mod-wsgi groups
    '''
    from django.contrib.auth.models import User
    try:
        return map(lambda g:g.name.encode('ascii') , User.objects.get(username=user).groups.all() )
    except:
        return [""]

def get_realm_hash(environ, user, realm):
    ''' mod-wsgi digest authentication handler

    .. tod::
        implement later. ( http://code.google.com/p/modwsgi/wiki/AccessControlMechanisms )
    '''
    return None

