import os

# Set environment variables
test = "server"
if test == "server":
    os.environ['APP_SECRET_KEY'] = 'django-insecure-_3%up&jx^vfhsdfasdfaw3rawdfsdefaw3'
    os.environ['DJANGO_DEBUG'] = 'False'
    os.environ['DJANGO_ALLOWED_HOSTS'] = '* localhost inventorytest-mansouri.fandogh.cloud'
    os.environ['APP_DB_ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    os.environ['DB_NAME'] = 'belitmes_main'
    os.environ['DB_USER'] = 'postgres'
    os.environ['DB_PASSWORD'] = 'asdfl2k323f90s@42'
    os.environ['DB_HOST'] =  'callcenter-dbms'
    os.environ['DB_PORT'] = '5432'
    os.environ['EMAIL_HOST_PASSWORD'] = 'kashefan@siah22'
    os.environ['EMAIL_HOST_USER'] = 'kashefancompany@gmail.com'
else:
    os.environ['APP_SECRET_KEY'] = 'django-insecure-_@#@#%@#RWDSFsdf23r23fwdfsdf2w3r2efsdf8='
    os.environ['DJANGO_DEBUG'] = 'True'
    os.environ['DJANGO_ALLOWED_HOSTS'] = '* localhost'
    os.environ['APP_DB_ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    os.environ['DB_NAME'] = 'belitmes'
    os.environ['DB_USER'] = 'pourya'
    os.environ['DB_PASSWORD'] = '123456'
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_PORT'] = '5432'
    os.environ['EMAIL_HOST_PASSWORD'] = 'kashefan@siah22'
    os.environ['EMAIL_HOST_USER'] = 'kashefancompany@gmail.com'
