#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories
directories=(
    "/data/"
    "/data/web_static/"
    "/data/web_static/releases/"
    "/data/web_static/shared/"
    "/data/web_static/releases/test/"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi
done

# Create a fake HTML file
html_file="/data/web_static/releases/test/index.html"
echo "<html>
<head>
    <title>Test HTML</title>
</head>
<body>
    <h1>This is a test HTML file.</h1>
</body>
</html>" > "$html_file"

# Create or recreate the symbolic link
symbolic_link="/data/web_static/current"
if [ -L "$symbolic_link" ]; then
    rm "$symbolic_link"
fi
ln -s /data/web_static/releases/test/ "$symbolic_link"

# Give ownership of /data/ folder to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
#sed -i "/^server {/a location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" "$nginx_config"
sed -i '/^\s*location \/hbnb_static/ {s/^\s*location \/hbnb_static.*$/\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/}' "$nginx_config"

# Restart Nginx
systemctl restart nginx

exit 0
