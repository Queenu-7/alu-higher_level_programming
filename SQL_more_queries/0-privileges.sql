-- List privileges for user_0d_1 only if the user exists
SELECT 'Grants for user_0d_1@localhost' AS info;
SELECT 
    IF(COUNT(*) = 0, 'User user_0d_1@localhost does not exist', '') AS message 
FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2 only if the user exists
SELECT 'Grants for user_0d_2@localhost' AS info;
SELECT 
    IF(COUNT(*) = 0, 'User user_0d_2@localhost does not exist', '') AS message 
FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
