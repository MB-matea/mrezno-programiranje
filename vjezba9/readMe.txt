*** CERTIFIKATI ***

SERVER - "openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt"
        (! Make sure to enter ‘example.com’ for the Common Name for server)
CLIENT - "openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt"