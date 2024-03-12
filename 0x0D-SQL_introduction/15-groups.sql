-- lists the number of records with the same score
-- the result should display score
-- number of records for this score with the label number
-- sorted in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
