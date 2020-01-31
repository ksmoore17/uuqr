from ..db_services import roles_required, get_current_user
from models import *

# should warn, prompt for u and p, give option to output database contents
def init(root_user, root_pass):
    try:
        User.drop_collection()
        Role.drop_collection()
        Unit.drop_collection()
        Company.drop_collection()
        Product.drop_collection()
        r = Role(name='root', can_create=True, can_print=True, can_certify=True).save()

        User(username=root_user, password=root_pass, roles=[r]).save()

    except:
        print("Couldn't initialize database")
