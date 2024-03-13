-- creates a user and grants all privileges
-- password should be user_0d_1_pwd
-- should not fail if user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user-0d_1-pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
