# Database
FROM mysql:8.0

ENV MYSQL_DATABASE=safebox_api \
  MYSQL_USER=dev \
  MYSQL_PASSWORD=devatsafebox \
  MYSQL_ROOT_PASSWORD=devatsafebox \
  TZ=Asia/Tokyo

COPY ./database.cnf /etc/mysql/conf.d/database.cnf
RUN chmod 644 /etc/mysql/conf.d/database.cnf

# EXPOSE 8009

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8009" , "--noreload"]