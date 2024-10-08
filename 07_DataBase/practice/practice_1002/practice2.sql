-- #1
-- easdasd 테이블확인후함수사용해보기
-- asdasdasdasd 의날짜가
-- 해당월의마지막날이라면"Y",
-- 해당월의마지막날이아니라면"N"으로
-- 표시되는"last_day_yn" 컬럼을만들고,
-- 2024년3월에해당하는asdasdasdasd와
-- last_day_yn 컬럼을
-- asdasdasdasd 오름차순으로출력하세요.

SELECT DISTINCT "asdasdasdasd",
                IF((DAY(DATE_ADD('day', -1, date_trunc('month', DATE_ADD('month', 1, DATE_PARSE("asdasdasdasd", '%Y%m%d'))))))=(DAY(DATE_PARSE("asdasdasdasd", '%Y%m%d'))), 'Y', 'N') as "last_dat_yn"
FROM "asdasdasd"."easdasd"
WHERE "asdasd"='202401'
ORDER BY "asdasdasdasd" DESC
LIMIT 5;