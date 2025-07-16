-- Create user_0d_1 with full root-level privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 with SELECT and INSERT privileges only on user_2_db
CREATE DATABASE IF NOT EXISTS user_2_db;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
