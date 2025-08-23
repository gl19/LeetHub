# Write your MySQL query statement below
SELECT
    a.player_id,
    a.event_date,
    SUM(b.games_played) as games_played_so_far
FROM
    Activity a LEFT JOIN
    Activity b ON 
    a.player_id = b.player_id AND
    a.event_date >= b.event_date
GROUP BY
    1, 2
ORDER BY
    1, 2 DESC
