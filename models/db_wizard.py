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
