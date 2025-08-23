# Write your MySQL query statement below
WITH player_first_logins AS (
    SELECT
        player_id,
        min(event_date) as first_login
    FROM
        Activity
    GROUP BY
        player_id
)

SELECT
    b.player_id,
    b.device_id
FROM
    player_first_logins a INNER JOIN
    Activity b ON
    a.player_id = b.player_id AND
    a.first_login = b.event_date