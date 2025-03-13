-- This script lists all records from the second_table in the hbtn_0c_0 database
-- with a score greater than or equal to 10. The results display both the scor
-- e and the name, ordered by score (top score first).

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
