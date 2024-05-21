--lists the number of records with the same score in the table
SELECT scores, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
