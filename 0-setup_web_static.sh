#!/usr/bin/env bash
# Script sets up web server for deployment of web_static.

apt-get update
apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

# make directories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# make a fake HTML file
touch /data/web_static/releases/test/index.html
echo "Hello World!" > /data/web_static/releases/test/index.html

# make a symbolic link, if exist delete and recreate everytime script is run
link_path="/data/web_static/current"
target="/data/web_static/releases/test/"

# check if the symbolic link already exists
if [ -L "$link_path" ]; then
	rm "$link_path"
fi

# recreate new symbolic link
sudo ln -s "$target" "$link_path"

# change owner and group to ubuntu user recursively
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# update the Nginx configuration
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root   /var/www/html;
	index  index.html index.htm;

	location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
	}
	location /redirect_me {
	return 301 http://putech.tech/;
	}
	error_page 404 /404.html;
	location /404 {
	root /var/www/html;
	internal;
	}
}" > /etc/nginx/sites-available/default

# restart Nginx
sudo service nginx restart
