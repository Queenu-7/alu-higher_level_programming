USE mysql;

DELIMITER $$

CREATE PROCEDURE show_user_grants(IN username VARCHAR(64), IN host VARCHAR(255))
BEGIN
  DECLARE cnt INT DEFAULT 0;
  SELECT COUNT(*) INTO cnt
  FROM mysql.user WHERE user = username AND host = host;
  
  IF cnt > 0 THEN
    SET @s = CONCAT('SHOW GRANTS FOR \'', username, '\'@\'', host, '\'');
    PREPARE stmt FROM @s;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
  ELSE
    SELECT CONCAT('User ', username, '@', host, ' does not exist') AS message;
  END IF;
END$$

DELIMITER ;

-- Show grants for user_0d_1
SELECT 'Grants for user_0d_1@localhost' AS info;
CALL show_user_grants('user_0d_1', 'localhost');

-- Show grants for user_0d_2
SELECT 'Grants for user_0d_2@localhost' AS info;
CALL show_user_grants('user_0d_2', 'localhost');

DROP PROCEDURE show_user_grants;
