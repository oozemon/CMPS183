# -*- coding: utf-8 -*-
### required - do no delete
def user():
    return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
#<<<<<<< HEAD
#def index():    
    #    redirect(URL(c = 'create_profile', f = 'testing'))
#    return dict(message="Mapping the world, for travlers")
#=======
def index():
    return dict(message="Mapping the world, for travelers")
#>>>>>>> 52242180f257d101fbada5911903348870013b0a

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

@auth.requires_login()
def follow():
    if request.env.request_method != 'POST':
        raise HTTP(400)
    tablename = 'follows'
    to_follow = db.auth_user(request.vars['user'])
    action = request.vars['action']
    # FIXME ensure that to-follow user exists!
    if to_follow is not None:
        if action == 'follow':
            db[tablename].insert(follower=auth.user.id, followee=to_follow)
            return HTTP(200)
        elif action == 'unfollow':
            db(db.follows.follower==auth.user.id,
               db.follows.followee==to_follow).delete()
            return HTTP(200)
        else:
            return HTTP(400)
        return HTTP(200)
    else:
        raise HTTP(400)

def users():
    """
    Display user profile
    """
    if request.args(0) is not None:
        uid = request.args(0)
        # TODO handle failure
        user = db.auth_user[request.args(0)]
        name = user.first_name + ' ' + user.last_name
        followers   = db(db.follows.followee==uid).select(db.follows.ALL)
        following   = db(db.follows.follower==uid).select(db.follows.ALL)
        picture     = user.picture
        gender      = user.gender
        experance   = user.experance
        description = user.description
        itineraries = db(db.itineraries.traveler==user).select(db.itineraries.ALL)
        context = dict(name=name,followers=followers,following=following,picture=picture,description=description,experance=experance,gender=gender,itineraries=itineraries)
        return response.render('default/users.html', context)
    else:
        # TODO do something sensible?
        return redirect(URL('default','index'))
