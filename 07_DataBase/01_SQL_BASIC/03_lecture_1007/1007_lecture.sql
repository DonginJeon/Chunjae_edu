SELECT *
FROM "asdasdasd"."asdasdasdasd"
WHERE 1=1
  AND "proc_ym" = '202409'
  AND "asdasdasd" IS NOT NULL
  AND "asdasdasdasd" IS NOT NULL
LIMIT 5;

-- groupcy

SELECT "asdasdasd",
       "asdasdasdasd",
       COUNT(*) AS "cnt"
FROM "asdasdasd"."asdasdasdasd"
WHERE 1=1
  AND "proc_ym" = '202409'
  AND "asdasdasd" IS NOT NULL
  AND "asdasdasdasd" IS NOT NULL
GROUP BY "asdasdasd",
         "asdasdasdasd"
ORDER BY "asdasdasd",
         "asdasdasdasd"
LIMIT 5;

--

SELECT "asdasdasd",
       "asdasdasdasd",
       COUNT(*) AS "cnt"
FROM "asdasdasd"."asdasdasdasd"
WHERE 1=1
  AND "proc_ym" = '202409'
  AND "asdasdasd" IS NOT NULL
  AND "asdasdasdasd" IS NOT NULL
GROUP BY GROUPING
SETS ("asdasdasd",
      "asdasdasdasd")
ORDER BY "asdasdasd",
         "asdasdasdasd";

--

SELECT "asdasdasd",
       "asdasdasdasd",
       COUNT(*) AS "cnt"
FROM "asdasdasd"."asdasdasdasd"
WHERE 1=1
  AND "proc_ym" = '202409'
  AND "asdasdasd" IS NOT NULL
  AND "asdasdasdasd" IS NOT NULL
GROUP BY ROLLUP ("asdasdasd",
                 "asdasdasdasd")
ORDER BY "asdasdasd",
         "asdasdasdasd";

--

SELECT "asdasdasd",
       "asdasdasdasd",
       COUNT(*) AS "cnt"
FROM "asdasdasd"."asdasdasdasd"
WHERE 1=1
  AND "proc_ym" = '202409'
  AND "asdasdasd" IS NOT NULL
  AND "asdasdasdasd" IS NOT NULL
GROUP BY CUBE ("asdasdasd",
               "asdasdasdasd")
ORDER BY "asdasdasd",
         "asdasdasdasd";

--

SELECT "asdasdasd",
       "userid",
       "cjt050_timestamp",
       RANK() OVER(PARTITION BY "asdasdasd", "userid", "cjt050_timestamp"
                   ORDER BY "cjt050_timestamp" ASC NULLS FIRST) AS "RANK"
FROM "asdasdasd"."e_media"
WHERE 1=1
  AND "asdasdasd" = '20240621'
  AND "userid" = '00014ecf-3384-4385-8365-326b832297d1'
ORDER BY "cjt050_timestamp" ASC NULLS FIRST;