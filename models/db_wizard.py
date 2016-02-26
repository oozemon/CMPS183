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

db.define_table('up_coming_itinerary',
               Field('it_name', 'reference des'),
               Field('des_location'),
               Field('days_staying', 'double'),
               Field('description_of_stays', 'text')
               )

db.define_table('past_itinerary',
                Field('view_original', 'reference up_coming_itinerary'),
                Field('past_it_tips', 'text', length=256),
                Field('past_it_regrets', 'text', length=256))

"""
Sketch of a destinations table using the google api
Google API's place_id is a unique identifier of a place
We should also consider saving other metadata eg place name, country, etc..
"""
"""
db.define_table('destinations',
                Field('place_id', unique=True),
                )
"""

# TODO distinguish between capital/uncapitalized names
db.define_table('countries',
                Field('country_name', unique=True)
                )

db.define_table('regions',
                Field('region_name', unique=True)
                )

db.define_table('cities',
                Field('city_name', unique=True)
                )

"""
Every destination is in a country
Optionally has a region or city

When determining what the name of the destination is, 
we should look to see if city is not None. If it is None, then check region.
If region is none, the destination is a country.
"""
# TODO need to ensure that the (des_country, des_region, des_city) tuple is unique
# TODO support having destinations with cities
db.define_table('destinations',
                Field('des_country', 'reference countries', required=True),
                Field('des_region', 'reference regions'),
                Field('des_city', 'reference cities')
                )

db.define_table('images',
                Field('img_file', 'upload')
                )

db.define_table('images_destinations',
                Field('img', 'reference images'),
                Field('dest', 'reference destinations')
                )
