-- #1

SELECT *
FROM "asdfasdfasdf"."dfadfasdfasdf"
limit 10;

-- #2

SELECT *
FROM "information_schema"."columns"
WHERE 1=1
  AND "table_schema" = 'asdasdasd'
  AND "table_name" = 'asdasdasdasd';

-- #3

SELECT COUNT(DISTINCT "subject")
FROM "asdfasdfasdf"."dfadfasdfasdf";

-- #4

SELECT COUNT(*)
FROM "asdfasdfasdf"."dfadfasdfasdf"
WHERE 1=1
  AND "service_1depth" IS not NULL;

-- #5

SELECT *
FROM "asdfasdfasdf"."dfadfasdfasdf"
WHERE 1=1
  AND "yyyy" = '2023'
  AND "mm" = '08';

-- #6

SELECT *,
       IF("content_grade"<=3, 'Y', 'N') as "under_3"
FROM "asdfasdfasdf"."dfadfasdfasdf"
limit 5;