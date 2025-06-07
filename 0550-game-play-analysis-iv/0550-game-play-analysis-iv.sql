# Write your MySQL query statement below
With ranked_date AS (
    SELECT
        player_id,
        event_date,
        rank() OVER (PARTITION BY player_id ORDER BY event_date) as r
    FROM
        Activity
),

first_date AS (
    SELECT
        player_id,
        event_date
    FROM
        ranked_date
    WHERE
        r = 1
),

second_date AS (
    SELECT
        player_id,
        event_date
    FROM
        ranked_date
    WHERE
        r = 2
)

SELECT
    ROUND(count(DISTINCT s.player_id) / count(*), 2) as fraction
FROM
    first_date f LEFT JOIN second_date s ON
    f.player_id = s.player_id AND
    DATEDIFF(s.event_date, f.event_date) = 1
