from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'TRVLR'
settings.subtitle = 'powered by web2py'
settings.author = 'Marvin Corro'
settings.author_email = 'mcorro1@ucsc.edu'
settings.keywords = 'travel'
settings.description = 'Mapping the world, for travelers'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'c0db4cd0-f960-4e07-8682-da1bec5e609d'
settings.email_server = 'localhost'
settings.email_sender = 'explorer@trvlr.com'
settings.email_login = 'admin'
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
