SELECT 1;


SELECT 1,
       2,
       3;


SELECT 1+2;


SELECT 1-2;


SELECT 1*2;


SELECT 1/2;


SELECT 1%2;


SELECT '가나다';


SELECT CONCAT('가', '나');


SELECT CURRENT_DATE;


SELECT 1>2;


SELECT 1=2;


SELECT 1!=2;


SELECT 1<>2;


SELECT 1 IN (1,
             2,
             3);


SELECT 'A' = 'a';


SELECT not TRUE;


SELECT "proc_ym" AS "처리일자",
       1 AS "number"
FROM "learning_analytics"."asdasdasd"
LIMIT 5;


SELECT "proc_ym",
       "proc_ymd"
FROM "learning_analytics"."asdasdasd"
LIMIT 5;


SELECT *
FROM "learning_analytics"."asdasdasd"
WHERE 1=1
  AND "userid" = '00176656-46ae-4afb-97ff-625fc287b50f'
  AND "proc_ymd" = '20240808'
LIMIT 5;


SELECT COUNT(*)
FROM "learning_analytics"."asdasdasd"
WHERE 1=1
  AND "content_grade" = 3
  OR "content_grade" = 4;


LIMIT 5;


SELECT *
FROM "learning_analytics"."asdasdasd"
WHERE 1=1
  AND "lrn_s_date" BETWEEN CAST('2024-03-01' AS TIMESTAMP) AND CAST ('2024-03-02' AS TIMESTAMP);

-- LIKE

SELECT *
FROM "asdasdasd"."asdasdasd"
WHERE 1=1
  AND "l_template_nm" LIKE '%탭%'
LIMIT 5;

-- 정규표현식

SELECT *
FROM "asdasdasd"."asdasdasd"
WHERE 1=1
  AND REGEXP_LIKE ("l_template_nm", '^.+_.*$')
LIMIT 5;

-- null값 조회

SELECT COUNT(*)
FROM "asdasdasd"."asdasdasd"
WHERE 1=1
  AND "service_1depth" IS NULL;


SELECT COUNT(*)
FROM "asdasdasd"."asdasdasd"
WHERE 1=1
  AND "l_type" IS NULL
  OR LENGTH(TRIM("l_type"))<1;


SELECT COUNT(*)
FROM "asdasdasd"."asdasdasd"
WHERE 1=1
  AND "proc_ymd" = '20240319'
  AND ("user_grade_nm" = '초5학년'
       OR "user_grade_nm" = '초4학년');


SELECT *,
       IF("mm" = '01', '1월', 'X') AS "1월인가"
FROM "asdasdasd"."asdasdasd"
LIMIT 5;


SELECT *,
       CASE
           WHEN "rn" IN ('01',
                         '02',
                         '03' THEN '1분기')
           WHEN "rn" IN ('01',
                         '02',
                         '03' THEN '2분기')
           ELSE '기타'
       END AS "quarter"
