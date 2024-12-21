#Basic urls for our http requests
BASE_URL = "http://127.0.0.1:8080/"
AUTHORIZATION_URL = f"{BASE_URL}authorization/"
GET_USERNAMES_URL = f"{BASE_URL}peer/list/"
GET_USER_IP =  f"{BASE_URL}peer/get/ip?username="

#ports
TCP_HANDSHAKE_PORT = 10000
REQUEST_HANDLER_POST = 8080

#HTTP STATUS CODES
NOT_FOUND_CODE = 404
ACCESS_DENIDE_CODE = 403
BAD_REQUEST= 400
NOT_AUTHORIZED= 401
METHOD_NOT_ALLOWED= 405
NOT_ACCEPTABLE= 406 #FOR FILDES
REQUEST_TIMEOUT= 408
TO_MANY_REQUESTS= 429
ACCEPTED_CODE = 200
SERVER_ERROR_CODE = 500

#FILES SECTION
ENCODE_STANDARD = 'utf-8'
BUFFER_SIZE = 1024
FILES_BASE_URL = './files/'

#Redis info
REDIS_PORT = 6379
REDIS_HOST = 'localhost'