-- lists all recors with a score >= 10 in second_table
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;