-- This script lists all records from the second_table of the database
-- where the name is not null. The results display the score and name, ordered
-- by score in descending order.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
