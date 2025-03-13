-- This script creates a MySQL user 'user_0d_1' if it doesn't already exist
-- It grants the user all privileges and sets the password to 'user_0d_1_pwd'

-- Check if the user 'user_0d_1' already exists and create the user if not
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 
'user_0d_1_pwd';

-- Grant all privileges to the user 'user_0d_1' on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Make sure to apply the changes
FLUSH PRIVILEGES;
