# -*- coding: utf-8 -*-
### required - do no delete
def user():
    return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
<<<<<<< HEAD
def index():    
    #    redirect(URL(c = 'create_profile', f = 'testing'))
    return dict(message="Mapping the world, for travlers")
=======
def index():
    return dict(message="Mapping the world, for travelers")
>>>>>>> 52242180f257d101fbada5911903348870013b0a

def error():
    return dict()

#@auth.requires_login()
def destinations_manage():
    form = SQLFORM.smartgrid(db.t_destinations,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def profile_manage():
    return dict(bla="testing")

@auth.requires_login()
def profile():
    return redirect(URL('default','users/'+str(auth.user.id)))

def users():
    """
    Display user profile
    """
    if request.args(0) is not None:
        uid = request.args(0)
        # TODO handle failure
        user = db.auth_user[request.args(0)]
        name = user.first_name + ' ' + user.last_name
        followers = db(db.follows.followee==uid).select(db.follows.ALL)
        following = db(db.follows.follower==uid).select(db.follows.ALL)
        context = dict(name=name,followers=followers,following=following)
        return response.render('default/users.html', context)
    else:
        # TODO do something sensible?
        return redirect(URL('default','index'))
