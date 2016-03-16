# -*- coding: utf-8 -*-
### required - do no delete
def user():
    return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
import datetime
import time
### end requires

def index():
    uid     = request.args(0)
    user2   = db.auth_user[request.args(0)]
    its2    = db().select(db.all_itinerary.ALL, orderby=db.all_itinerary.date_created)
    listOfAllUsers = db().select(db.auth_user.ALL, orderby=db.auth_user.first_name)
    #funcForBar()
    return dict(message="Mapping the world, for travelers", its2=its2, user2=user2, listOfAllUsers=listOfAllUsers,
        searching=funcForBar())

def funcForBar():
    partialstr = request.vars.partialstr if request.vars else None
    query      = db.auth_user.first_name
    auth_user   = db(query).select(db.auth_user.first_name)
    items = []

    for (i,auth_user) in enumerate(auth_user):
        items.append(DIV(A(auth_user.first_name, _id="res%s"%i, _href="#", _onclick="copyToBox($('#res%s').html())"%i), _id="resultLiveSearch"))

    return TAG[''](*items)

def error():
    return dict()

#@auth.requires_login()
def destinations_manage():
    form = SQLFORM.smartgrid(db.t_destinations,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def profile():
    return redirect(URL('default','users/'+str(auth.user.id)))

@auth.requires_login()
def doStuff():
    it_name = request.vars.d_name
    it_loc  = request.vars.d_location
    place_id = request.vars.d_place_id
    if db(db.place_names.place_id==place_id).select().first() is None:
        # No one has traveled here.. we need to save this location
        print it_loc
        place_name_row = db.place_names.insert(place_id=place_id, p_name=it_loc)
    else:
        place_name_row = db(db.place_names.place_id==place_id).select().first()
    index = db.all_itinerary.insert(it_name=it_name, 
                                    place=place_name_row,
                                    days_staying_start=request.vars.d_start_date,
                                    days_staying_end=request.vars.d_end_date,
                                    description_of_stays=request.vars.d_description,
                                    ownerA=auth.user, 
                                    date_created=datetime.datetime.today())
    return "jQuery('#target').append('<li><a href=\"../showIts/%d\">%s</a></li>');" % (index.id, index.it_name)

"""    
def updateItOnView():
    its = db().select(db.all_itinerary.ALL, orderby=db.all_itinerary.date_created)
    return "jQuery('#target').append('<li><a href=\"showIts?arg1=%s&arg2=%s&arg3=%s&arg4=%s&arg5=%s\">%s</a></li>');" % (its.it_name,its.des_location,str(its.days_staying_start),str(its.days_staying_end),its.description_of_stays,its.it_name)
    #return dict(its=its)
"""

def showIts():
    it = db.all_itinerary[request.args(0)]
    if it is None:
        return HTTP(400)
    else:
        return dict(it=it)

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
        if user is None:
            return HTTP(400)
        else:
            pass
        name = user.first_name + ' ' + user.last_name
        its  = db(db.all_itinerary.ownerA==user).select(db.all_itinerary.ALL, orderby=db.all_itinerary.date_created)
        #all_names    = db().select(db.all_itinerary.it_name)
        followers    = db(db.follows.followee==uid).select(db.follows.ALL)
        following    = db(db.follows.follower==uid).select(db.follows.ALL)
        picture      = user.picture
        gender       = user.gender
        experance    = user.experance
        description  = user.description
        it_all       = db.all_itinerary[request.args(0)]
#        des_location = db(db.all_itinerary.des_location!=None).select(db.all_itinerary.des_location)
        #it_name      = db(db.all_itinerary.it_name.des_name!=None).select()
        days_staying_start   = db(db.all_itinerary.days_staying_start!=None).select(db.all_itinerary.days_staying_start)
        days_staying_end     = db(db.all_itinerary.days_staying_end!=None).select(db.all_itinerary.days_staying_end)
        description_of_stays = db(db.all_itinerary.description_of_stays!=None).select(db.all_itinerary.description_of_stays)
        context = dict(name=name,followers=followers,following=following,picture=picture,description=description,
            experance=experance,gender=gender, #it_name=it_name, 
            des_location='',days_staying_start=days_staying_start,
            days_staying_end=days_staying_end,description_of_stays=description_of_stays, its=its, user=user)
        return response.render('default/users.html', context)
    else:
        # TODO do something sensible?
        return redirect(URL('default','index'))
