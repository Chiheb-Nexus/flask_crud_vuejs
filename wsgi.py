#
# WSGI file
#

from app import application

HOST = '0.0.0.0'
PORT = '8000'

if __name__ == '__main__':
    application.run(host=HOST, port=PORT)
