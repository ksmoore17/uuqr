from .classes import *

# should warn, prompt for u and p, give option to output database contents
def reset(root_user, root_pass):
    try:
        Series.drop()
        Unit.drop()

    except:
        print("Couldn't initialize database")
