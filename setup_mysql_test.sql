-- Creation of hbnb_dev_db database
-- Creation of new user (hbnb_dev)
CREATE DATABASE IF NOT EXISTS test_HBNB_MYSQL_DB;
CREATE USER IF NOT EXISTS 'HBNB_MYSQL_USER'@'HBNB_MYSQL_HOST';
SET PASSWORD FOR 'HBNB_MYSQL_USER'@'HBNB_MYSQL_HOST' = 'HBNB_MYSQL_PWD';
USE test_HBNB_MYSQL_DB;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'HBNB_MYSQL_USER'@'HBNB_MYSQL_HOST';
GRANT SELECT ON performance_schema.* TO 'HBNB_MYSQL_USER'@'HBNB_MYSQL_HOST';
FLUSH PRIVILEGES;

