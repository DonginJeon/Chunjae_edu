SELECT "asdasdasd",
       COUNT("asdasdasd") AS "count_member",
       COUNT(DISTINCT "asdasdasd") AS "asdasdasd"
FROM "asdasdasd"."asdasdasd"
WHERE 1=1
  AND "asdasdasd" = '20240601'
GROUP BY "asdasd"
LIMIT 5;

---

SELECT "asdasdasd",
       "dasdasdasd",
       COUNT("point") AS "count",
       MAX("point") AS "max",
       MIN("point") AS "min",
       AVG("point") AS "average",
       SUM("point") AS "sum"
FROM "asdasdasd"."e_point"
WHERE 1=1
  AND "asdasdasd" = '20240304'
GROUP BY "asdasdasd",
         "dasdasdasd"
HAVING MAX("point") >= 30
ORDER BY 'sum' ASC ;
