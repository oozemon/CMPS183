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

def doStuff():
    #d_name        = request.vars.d_name
    #d_location    = request.vars.d_location
    #print d_name
    #print d_location
    #d_start_date  = request.vars.d_start_date
    #d_end_date    = request.vars.d_end_date
    #d_description = request.vars.d_description
    db.all_itinerary.insert(it_name=request.vars.d_name)
    db.all_itinerary.insert(des_location=request.vars.d_location)
    #db.all_itinerary.insert(days_staying_start=d_start_date)
    #db.all_itinerary.insert(days_staying_end=d_end_date)
    #db.all_itinerary.insert(description_of_stays=d_description)
    return "jQuery('#target').html('%s');" % str(request.vars.d_name)

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
        followers    = db(db.follows.followee==uid).select(db.follows.ALL)
        following    = db(db.follows.follower==uid).select(db.follows.ALL)
        picture      = user.picture
        gender       = user.gender
        experance    = user.experance
        description  = user.description
        itineraries = db(db.user_itinerary.ownerA==uid).select(db.all_itinerary.ALL)
        des_location = db(db.all_itinerary.des_location!=None).select(db.all_itinerary.des_location)
        #it_name      = db(db.all_itinerary.it_name.des_name!=None).select()
        days_staying_start   = db(db.all_itinerary.days_staying_start!=None).select(db.all_itinerary.days_staying_start)
        days_staying_end     = db(db.all_itinerary.days_staying_end!=None).select(db.all_itinerary.days_staying_end)
        description_of_stays = db(db.all_itinerary.description_of_stays!=None).select(db.all_itinerary.description_of_stays)
        context = dict(name=name,followers=followers,following=following,picture=picture,description=description,
            experance=experance,gender=gender, #it_name=it_name, 
            des_location=des_location,days_staying_start=days_staying_start,
            days_staying_end=days_staying_end,description_of_stays=description_of_stays,itineraries=itineraries)
        return response.render('default/users.html', context)
    else:
        # TODO do something sensible?
        return redirect(URL('default','index'))
