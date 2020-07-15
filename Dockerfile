FROM python:3.7.5-slim-buster
LABEL maintainer="kb ko <kb.ko@battong.com>"
LABEL description="Development server wsgi"

# Enable all IPs to connect gunicorn
ENV FORWARDED_ALLOW_IPS '*'

# Adds all the file to /app/ and work there
ADD . /app/
WORKDIR /app/
RUN chmod +x ./gunicorn.sh

# install requirements
RUN pip install -r requirements.txt

# now run gunicorn using configuration
# CMD ["/bin/sh", "-c", "./gunicorn.sh"]
ENTRYPOINT ["bash", "echo AAA"]