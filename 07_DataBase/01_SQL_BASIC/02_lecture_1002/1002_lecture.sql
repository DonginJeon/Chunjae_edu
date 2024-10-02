SELECT position('T' IN 'XTX');


SELECT position('T' IN 'XTTX');


SELECT substring('absd', 2);


SELECT substring('CHUMJAE EDUCATAION', 9, 3);


SELECT "proc_ymd",
       substring("proc_ymd", -2)
FROM "learning_analytics"."e_assessment"
LIMIT 5;


SELECT UPPER('absd');


SELECT "userid",
       upper(substring("userid", -12))
FROM "learning_analytics"."e_assessment"
LIMIT 5;

---

SELECT "userid",
       regexp_position("userid", '(?<=\-)$', 13)
FROM "learning_analytics"."e_assessment"
LIMIT 5;

---
 -- 10:00

SELECT REPLACE('TEXTBOOK', 'X', 'S');


SELECT LPAD('asdf', 10, 'x');


SELECT FLOOR(-23.1);

-- 11:00

SELECT NOW() AS "현재",
       YEAR(NOW()) AS "연",
       QUARTER(NOW()) AS "분기",
       MONTH(NOW()) AS "월",
       DAY(NOW()) AS "주",
       HOUR(NOW()) AS "시",
       MINUTE(NOW()) AS "분",
       SECOND(NOW()) AS "초",
       millisecond(NOW()) as "밀리초";


SELECT NOW() as "현재",
       DAY_OF_YEAR(NOW()) AS "연 중 몇번째 일",
       DAY_OF_WEEK(NOW()) AS "주주 중 몇번째 일";


SELECT NOW() AS "현재",
       DATE_TRUNC('year', NOW()),
       DATE_TRUNC('second', NOW());


SELECT NOW() AS "현재",
       DATE_ADD('month', 14, NOW()),
       DATE_DIFF('year', DATE_ADD('month', 14, NOW()), NOW());


SELECT NOW(),
       DATE_FORMAT(NOW(), '%Y-%m-%d--'),
       DATE_FORMAT(NOW(), '%Y%m%d');


SELECT NOW(),
       CONCAT(DATE_FORMAT(NOW(), '%Y-%m-%d'), DATE_FORMAT(NOW(), '%H:%i:%s'));


SELECT date_parse('2024-03-27', '%Y-%m-%d');


SELECT NOW(),
       CAST(DATE_FORMAT(NOW(), '%Y-%m-%d%H:%i:%s') AS VARCHAR);


SELECT NOW(),
       CAST(NOW() AS VARCHAR);


SELECT NOW(),
       CAST(CAST(NOW() AS VARCHAR) AS TIMESTAMP);

--

SELECT *
FROM "information_schema"."columns"
WHERE 1=1
  AND "table_schema" = 'learning_analytics'
  AND "table_name" = 'e_learning_action'
  SELECT "proc_ym",
         "userid",
         "mcode",
         "lecture_type",
         "eventtime_kst",
         ROW_NUMBER() OVER(PARTITION BY "proc_ym", "userid", "mcode", "lecture_type"
                           ORDER BY "eventtime_kst" ASC),
                      RANK() OVER(PARTITION BY "proc_ym", "userid", "mcode", "lecture_type"
                                  ORDER BY "eventtime_kst" ASC),
                             DENSE_RANK() OVER(PARTITION BY "proc_ym", "userid", "mcode", "lecture_type"
                                               ORDER BY "eventtime_kst" ASC)
  FROM "learning_analytics"."e_learning_action" WHERE 1=1
  AND "userid" = '15222165-bb07-4327-85d9-720dab5256a7'
LIMIT 5;

-- 실습

SELECT "proc_ymd",
       "userid",
       RANK() OVER(PARTITION BY "proc_ymd", "userid"
                   ORDER BY "point"),
              DENSE_RANK() OVER(PARTITION BY "proc_ymd", "userid"
                                ORDER BY "point")
FROM "learning_analytics"."e_point"
WHERE 1=1
  AND "proc_ym" = '202403'
  AND "point" > 0
LIMIT 50;

--

SELECT *,
       SUM("sum_point") OVER (PARTITION BY "userid"
                              ORDER BY "proc_ymd" ASC ROWS between 1 preceding and 1 following) as "test"
FROM
  (SELECT "proc_ymd",
          "userid",
          SUM("point") AS "sum_point"
   FROM "learning_analytics"."e_point"
   WHERE 1=1
     AND "point">0
     AND "proc_ym" = '202403'
   GROUP BY "proc_ymd",
            "userid");

-- join
WITH "temp1" AS
  (SELECT distinct "userid"
   FROM "learning_analytics"."e_assessment"
   WHERE 1=1
     AND "proc_ymd" = '20230101' ),
     "temp2" AS
  (SELECT distinct "userid"
   FROM "learning_analytics"."e_assessment_detail"
   WHERE 1=1
     AND "proc_ymd" = '20230101' )
SELECT COUNT(*)
FROM "temp1"
FULL OUTER JOIN "temp2" ON "temp1"."userid" = "temp2"."userid";


SELECT distinct "userid"
FROM "learning_analytics"."e_assessment_detail"
WHERE 1=1
  AND "proc_ymd" = '20230101'
LIMIT 5;


SELECT "ea"."proc_ymd",
       "ea"."userid",
       "ea"."mcode",
       "ea"."score",
       "ead"."no",
       "ead"."answer",
       "ead"."correct"
FROM "learning_analytics"."e_assessment" AS "ea"
INNER JOIN "learning_analytics"."e_assessment_detail" AS "ead" ON "ea"."userid" = "ead"."userid"
AND "ea"."proc_ymd" = '20230101'
AND "ead"."proc_ymd" = '20230101'
AND "ea"."proc_ymd" = "ead"."proc_ymd"
AND "ea"."mcode" = "ead"."mcode";


SELECT *
FROM "learning_analytics"."e_assessment" AS "ea"
INNER JOIN "learning_analytics"."e_learning_time" AS "eat" ON "ea"."userid" = "eat"."userid"
AND "ea"."proc_ymd" = '20230101'
AND "eat"."proc_ymd" = '20230101';

-- union

SELECT 1,
       2,
       3
union
SELECT 1,
       2,
       4;


SELECT *
FROM
  (SELECT "proc_ym",
          COUNT(*) as "cnt",
          'e_learning_action' AS "table_name"
   FROM "learning_analytics"."e_learning_action"
   GROUP BY "proc_ym"
   UNION ALL SELECT "proc_ym",
                    COUNT(*) as "cnt",
                    'e_learning_action' AS "table_name"
   FROM "learning_analytics"."e_assessment_detail"
   GROUP BY "proc_ym");

with _temp1 AS(
               VALUES (CHAR '202208')),
     _temp2 (yyyy, mm) AS (
                           VALUES (CHAR '2022', CHAR '08'))
SELECT *
FROM _temp2 WITH _temp1 AS (
                            VALUES (CHAR '202208')),
                 _temp2 ("yyyy", "mm") AS (
                                           VALUES (VARCHAR '2022', VARCHAR '08')),
                 _temp3 AS
  (SELECT *
   FROM "learning_analytics"."e_assessment"
   WHERE CONCAT("yyyy", "mm") = '202208'),
                 _temp5 AS
  (SELECT *
   FROM "learning_analytics"."e_assessment"
   WHERE 1=1
     AND "yyyy" =
       (SELECT "yyyy"
        FROM _temp2)
     AND "mm" =
       (SELECT "mm"
        FROM _temp2) )
SELECT *
FROM _temp5
LIMIT 10;
