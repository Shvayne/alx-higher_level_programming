-- lists all the cities of california found in a db
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California')
ORDER BY id;

