### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_destinations',
    Field('f_destination_name', type='string',
          label=T('Destination Name')),
    Field('f_description', type='string',
          label=T('Description')),
    Field('f_comments', type='string',
          label=T('Comments')),
    Field('f_itineraries', type='string',
          label=T('Itineraries')),
    auth.signature,
    format='%(f_destination_name)s', 
    migrate=settings.migrate)

db.define_table('t_destinations_archive',db.t_destinations,Field('current_record','reference t_destinations',readable=False,writable=False))

db.define_table('follows',
                Field('follower', 'reference auth_user'),
                Field('followee', 'reference auth_user')
                )


db.define_table('des',
               Field('des_name'),
               Field('picture_des', 'upload'),
               Field('description_des', 'text'),
               Field('tips', 'text', length=256))

# Map Google API place_id to the human-readable place name
db.define_table('place_names',
                Field('place_id', required=True, notnull=True, unique=True),
                Field('p_name', required=True)
                )

db.define_table('all_itinerary',
                Field('it_name'),
                Field('ownerA', 'reference auth_user'),
                Field('place', 'reference place_names'),
                Field('days_staying_start', 'date'),# requires=IS_DATE('%m/%d/%Y')),
                Field('days_staying_end', 'date'),# requires=IS_DATE('%m/%d/%Y')),
                Field('description_of_stays', 'text'),
                Field('date_created', 'date')
               )



#db.define_table('past_itinerary',
#                Field('view_original', 'reference up_coming_itinerary'),
#                Field('past_it_tips', 'text', length=256),
 #               Field('past_it_regrets', 'text', length=256))
