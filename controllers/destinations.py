# -*- coding: utf-8 -*-
import json

# try something like
def index():
    return dict(destinations="TODO insert list of itineraries")

def get_itineraries():
    """
    Return all itineraries matching a place_id
    """
    place_id = request.vars['place_id']
    if place_id is None:
        return HTTP(400)
    else:
        itineraries = db(db.destinations.place_id==place_id,
                         db.destinations.id == db.itineraries.destination).select(db.itineraries.ALL).as_list()
        # if request.args[0] and request.args[0] == 'json':
        return json.dumps(dict(itineraries=itineraries))
