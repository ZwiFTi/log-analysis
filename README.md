

```
CREATE VIEW view_error_percent AS 
SELECT date(log.time),
       ROUND(100.0 * COUNT(*) FILTER (WHERE log.status NOT LIKE '%200%') / COUNT(*),2) AS error_percent
  FROM log
 GROUP BY date(log.time);
```
