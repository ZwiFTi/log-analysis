

```
CREATE VIEW view_errorPercent AS 
SELECT date(log.time),
       ROUND(100.0 * COUNT(*) FILTER (WHERE log.status NOT LIKE '%200%') / COUNT(*),2) AS "errorPercent"
  FROM log
 GROUP BY date(log.time);
```
