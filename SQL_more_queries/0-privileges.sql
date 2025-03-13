-- This script lists all privileges for the MySQL users 'user_0d_1' and 'user_0d_2' on the MySQL server.

-- List privileges for user_0d_1 (the root user)
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2 on the user_2_db database
SHOW GRANTS FOR 'user_0d_2'@'localhost' LIKE 'GRANT SELECT, INSERT% ON `user_2_db`.* TO `%`';
