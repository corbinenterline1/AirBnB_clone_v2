#!/usr/bin/env bash
# Set up web server for deployment of web_static

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "BABABABA" > /data/web_static/releases/test/index.html
GETOUT="/data/web_static/current"
if test -f "$GETOUT"; then
	rm -rf $GETOUT
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     add_header X-Served-By $HOSTNAME;
     root        /etc/nginx/html;
     index       index.html index.htm;

     location /hbnb_static {
         alias /data/web_static/current/;
         index index.html index.htm;
     }
}
" > /etc/nginx/sites-available/default
service nginx restart
