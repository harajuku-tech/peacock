# - Virutalenv Settings
#   - configure your virtual env activate_this.py 
#
activate_this = '/home/hdknr/ve/paloma/bin/activate_this.py'
execfile(activate_this,dict(__file__ =activate_this))
#
import os
#from accounts import authbasic
from accounts.authbasic import groups_for_user,check_password,authenhandler,enable_django
#
enable_django( os.path.dirname( os.path.abspath(__file__)))

##mod_python authentication handler
#def authenhandler(req):
#    return authbasic.authenhandler(req )
