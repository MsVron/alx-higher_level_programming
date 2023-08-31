-- This script sets up the hbtn_0d_2 database and user user_0d_2.

-- Create the hbtn_0d_2 database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;

-- Grant user_0d_2 permission to access the hbtn_0d_2 database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
