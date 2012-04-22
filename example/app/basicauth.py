# - Virutalenv Settings
#   - configure your virtual env activate_this.py 
#
activate_this = '/home/hdknr/ve/paloma/bin/activate_this.py'
execfile(activate_this,dict(__file__ =activate_this))
#
import os
from accounts import authbasic
#
authbasic.enable_django( os.path.dirname( os.path.abspath(__file__)))

def authenhandler(req):
    return authbasic.authenhandler(req )
