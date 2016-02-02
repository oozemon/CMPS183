# -*- coding: utf-8 -*-
# try something like
def index():
    form = SQLFORM.factory(Field('first_name', requires=IS_NOT_EMPTY()),
                          Field('second_name', requires=IS_NOT_EMPTY()),
                          Field('gender', requires=IS_NOT_EMPTY()),
                          Field('location', requires=IS_NOT_EMPTY()),
                          Field('age', requires=IS_NOT_EMPTY()),
                          Field('birth_date', 'date'),
                          Field('profile_pic', 'upload')).process()
    if form.accepted:
        redirect(URL('created', vars={'first_name':form.vars.first_name}))
    elif form.errors:
        response.flash = 'try again the page has missing fields.'
    return locals()

def created():
    x = 'Profile created for %s ' % request.vars.first_name
    return locals()
