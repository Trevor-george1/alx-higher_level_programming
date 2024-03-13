-- lists cities contained in the database
-- displayed as cities.id - cities.name - states.name
-- sorted in ascending order
-- use only one SELECT
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id ASC;

