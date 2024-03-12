-- converts hbtn_0c_0 databse to UTF8
-- convert Database, first_table, name in first_table
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(255)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
