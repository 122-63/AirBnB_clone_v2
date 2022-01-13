#!/usr/bin/env bash
# deployment of web_static

apt-get -y update
apt-get -y upgrade
apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

new_rut="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "24i $new_rut" /etc/nginx/sites-available/default

service nginx reload
service nginx start