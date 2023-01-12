FROM adminer:4.7.1
# WATCH OUT WHEN UPGRADING, THE SED BELOW MIGHT STOP WORKING

USER root

RUN apk add autoconf gcc g++ make libffi-dev openssl-dev
RUN pecl install -f mongodb
RUN echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini

RUN sed -i "s|{\$h->connect(\"mongodb://\$N\",\$yf);return|{|" adminer.php
RUN sed -i "s|lang(22);}|}|" adminer.php

USER adminer

# ENV ADMINER_DESIGN galkaev
ENV ADMINER_DESIGN pepa-linha
# ENV ADMINER_DESIGN mvt 
# ENV ADMINER_DESIGN lucas-sandery 