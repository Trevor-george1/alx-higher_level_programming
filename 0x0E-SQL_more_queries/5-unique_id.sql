-- script that creates a table
-- attributes id(daefault 1) unique
--            name
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);