WITH quarter_1 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score",
          array_join("s"."subcontent_name_sequence", ',') AS "subcontent_string"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('01',
                      '02',
                      '03')
     AND REGEXP_LIKE(array_join("s"."subcontent_name_sequence", ','), '.*인트로.*문제.*') ),
     quarter_2 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score",
          array_join("s"."subcontent_name_sequence", ',') AS "subcontent_string"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('04',
                      '05',
                      '06')
     AND REGEXP_LIKE(array_join("s"."subcontent_name_sequence", ','), '.*인트로.*문제.*') ),
     quarter_3 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score",
          array_join("s"."subcontent_name_sequence", ',') AS "subcontent_string"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('07',
                      '08',
                      '09')
     AND REGEXP_LIKE(array_join("s"."subcontent_name_sequence", ','), '.*인트로.*문제.*') ),
     quarter_4 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score",
          array_join("s"."subcontent_name_sequence", ',') AS "subcontent_string"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('10',
                      '11',
                      '12')
     AND REGEXP_LIKE(array_join("s"."subcontent_name_sequence", ','), '.*인트로.*문제.*') )
SELECT "mcode" AS "콘텐츠 코드",
       COUNT(DISTINCT "userid") AS "학습한 학생 수" -- ROUND(AVG("student_grade"), 2) AS "학년 평균",
 -- SUM("system_learning_time") AS "학습 시간",
 -- ROUND(AVG("item_count"), 2) AS "평가 문항 평균 개수",
 -- ROUND(AVG("correct_count"), 2) AS "정답 문항 평균 개수",
 -- ROUND(AVG("score"), 2) AS "평가 점수 평균"
FROM quarter_1
GROUP BY "mcode"
ORDER BY "학습한 학생 수" DESC
LIMIT 5;

------------------------------------------------------
WITH quarter_1 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('01',
                      '02',
                      '03')
     AND "m"."latest_completed_yn" = 'Y'
     AND "t"."latest_completed_yn" = 'Y' ),
     quarter_2 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('04',
                      '05',
                      '06')
     AND "m"."latest_completed_yn" = 'Y'
     AND "t"."latest_completed_yn" = 'Y' ),
     quarter_3 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('07',
                      '08',
                      '09')
     AND "m"."latest_completed_yn" = 'Y'
     AND "t"."latest_completed_yn" = 'Y' ),
     quarter_4 AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score"
   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "s"."mm" IN ('10',
                      '11',
                      '12')
     AND "m"."latest_completed_yn" = 'Y'
     AND "t"."latest_completed_yn" = 'Y' )
SELECT --"mcode" AS "콘텐츠 코드",
 COUNT(DISTINCT "userid") AS "학습한 학생 수",
 ROUND(AVG("student_grade"), 2) AS "학년 평균" -- SUM("system_learning_time") AS "학습 시간",
 -- ROUND(AVG("item_count"), 2) AS "평가 문항 평균 개수",
 -- ROUND(AVG("correct_count"), 2) AS "정답 문항 평균 개수",
 -- ROUND(AVG("score"), 2) AS "평가 점수 평균"
FROM quarter_1
GROUP BY "mcode"
LIMIT 2;

---------------------------------------------------------------------------------
WITH combined_quarters AS
  (SELECT "c"."mcode",
          "s"."userid",
          "mem"."grade" AS "student_grade",
          "s"."system_learning_time",
          "t"."item_count",
          "t"."correct_count",
          "t"."score",
          "s"."mm" -- 분기별로 필터링하기 위해 mm 필드를 가져옴

   FROM "text_biz_dw"."e_content_meta" AS "c"
   INNER JOIN "text_biz_dw"."e_media" AS "m" ON "c"."mcode" = "m"."mcode"
   INNER JOIN "text_biz_dw"."e_test" AS "t" ON "c"."mcode" = "t"."mcode"
   INNER JOIN "text_biz_dw"."e_study" AS "s" ON "c"."mcode" = "s"."mcode"
   INNER JOIN "text_biz_dw"."e_member" AS "mem" ON "s"."userid" = "mem"."userid"
   WHERE "mem"."grade" BETWEEN 3 AND 6
     AND "m"."latest_completed_yn" = 'Y'
     AND "t"."latest_completed_yn" = 'Y' )
SELECT "mcode" AS "콘텐츠 코드",
       CASE
           WHEN "mm" IN ('01',
                         '02',
                         '03') THEN '1분기'
           WHEN "mm" IN ('04',
                         '05',
                         '06') THEN '2분기'
           WHEN "mm" IN ('07',
                         '08',
                         '09') THEN '3분기'
           WHEN "mm" IN ('10',
                         '11',
                         '12') THEN '4분기'
           ELSE '알 수 없음'
       END AS "분기",
       COUNT(DISTINCT "userid") AS "학습한 학생 수",
       ROUND(AVG("student_grade"), 2) AS "학년 평균" -- SUM("system_learning_time") AS "학습 시간",
 -- ROUND(AVG("item_count"), 2) AS "평가 문항 평균 개수",
 -- ROUND(AVG("correct_count"), 2) AS "정답 문항 평균 개수",
 -- ROUND(AVG("score"), 2) AS "평가 점수 평균"
FROM combined_quarters
GROUP BY "mcode",
         CASE
             WHEN "mm" IN ('01',
                           '02',
                           '03') THEN '1분기'
             WHEN "mm" IN ('04',
                           '05',
                           '06') THEN '2분기'
             WHEN "mm" IN ('07',
                           '08',
                           '09') THEN '3분기'
             WHEN "mm" IN ('10',
                           '11',
                           '12') THEN '4분기'
             ELSE '알 수 없음'
         END
ORDER BY "학습한 학생 수" DESC
LIMIT 2;