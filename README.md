uv add django djangorestframework djangorestframework-simplejwt
       django-filter django-cors-headers 
       psycopg2-binary python-decouple

sudo chown -R shopapi:www-data /opt/Orozco-shopapi/staticfiles
sudo chmod -R 755 /opt/Orozco-shopapi/staticfiles
sudo chmod -R 755 /opt/Orozco-shopapi
sudo usermod -aG www-data root
# [Unit]
# Description=Gunicorn daemon for ShopAPI
# After=network.target postgresql.service

# [Service]
# User=root
# Group=www-data
# WorkingDirectory=/opt/Orozco-shopapi
# Environment="PATH=/opt/Orozco*shopapi/.venv/bin"
# EnvironmentFile=/opt/Orozco-shopapi/.env
# ExecStart=/opt/Orozco-shopapi/.venv/bin/gunicorn \
#           --workers 3 \
#           --bind unix:/run/gunicorn-shopapi.sock \
#           --access-logfile /var/log/gunicorn-shopapi-access.log \
#           --error-logfile /var/log/gunicorn-shopapi-error.log \
#           config.wsgi:application
# ExecReload=/bin/kill -s HUP $MAINPID
# Restart=on-failure
# RestartSec=5

# [Install]
# WantedBy=multi-user.target

curl -v --unix-socket /run/gunicorn-shopapi.sock http://localhost/api/health/