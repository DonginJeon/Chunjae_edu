WITH f_study AS (
    SELECT DISTINCT
        s.mcode,
        s.userid,
        s.system_learning_time,
        array_join(s.subcontent_name_sequence, ',') AS subcontent_string
    FROM text_biz_dw.e_study AS s
    WHERE 1=1
        AND s.yyyy = '2022'
        AND s.mm IN ('01', '02', '03') --> 여기서 분기를 조정해주세요(ex. 1분기 : '01','02','03')
        AND REGEXP_LIKE(array_join(s.subcontent_name_sequence, ','), '.*인트로.*')
        AND REGEXP_LIKE(array_join(s.subcontent_name_sequence, ','), '.*문제.*')
),
filtered_members AS (
    SELECT DISTINCT 
        mem.userid, 
        mem.grade
    FROM text_biz_dw.e_member AS mem
    WHERE mem.grade BETWEEN 3 AND 6
),
user_data AS (
    SELECT
        fs.mcode,
        fs.userid,
        fm.grade AS student_grade,
        fs.system_learning_time
    FROM f_study AS fs
    INNER JOIN filtered_members AS fm ON fs.userid = fm.userid
),
content_meta AS (
    SELECT DISTINCT 
        c.mcode
    FROM text_biz_dw.e_content_meta AS c
    INNER JOIN text_biz_dw.e_media AS m ON c.mcode = m.mcode
),
study_content AS (
    SELECT 
        ud.mcode,
        ud.userid,
        ud.student_grade,
        ud.system_learning_time
    FROM user_data AS ud
    INNER JOIN content_meta AS cm ON ud.mcode = cm.mcode
),
test_data AS (
    SELECT 
        t.mcode, 
        ROUND(AVG(t.item_count), 2) AS avg_item_count,
        ROUND(AVG(t.correct_count), 2) AS avg_correct_count,
        ROUND(AVG(t.score), 2) AS avg_score
    FROM text_biz_dw.e_test AS t
    GROUP BY t.mcode
)

SELECT 
    sc.mcode AS "콘텐츠 코드",
    COUNT(sc.userid) AS "학습한 학생 수",
    ROUND(AVG(sc.student_grade), 2) AS "학생의 학년 평균",
    SUM(sc.system_learning_time) AS "학습 시간", 
    td.avg_item_count AS "평가 문항 평균 개수",
    td.avg_correct_count AS "정답 문항 평균 개수",
    td.avg_score AS "평가 점수 평균"
FROM study_content AS sc
LEFT JOIN test_data AS td ON sc.mcode = td.mcode
WHERE td.avg_item_count IS NOT NULL
GROUP BY sc.mcode, td.avg_item_count, td.avg_correct_count, td.avg_score
ORDER BY "콘텐츠 코드";
