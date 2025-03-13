-- This script lists the number of records with the same score in the 2ndtable
-- of the hbtn_0c_0 database. The results are ordered by the number of records
-- (descending).The result will display the score and the count of records for
-- each score with the label 'number'.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
