CREATE TABLE "imsi0" ("col0" VARCHAR, "col1" INT, "col2" TIMESTAMP);


ALTER TABLE "imsi0" ADD COLUMN "col3" VARCHAR;


ALTER TABLE "imsi0"
DROP COLUMN "col3";


ALTER TABLE "imsi0" RENAME COLUMN "col0" TO "text";


ALTER TABLE "imsi0" RENAME TO "imsi1";


ALTER TABLE "imsi1"
ALTER COLUMN col1 TYPE float;


DROP TABLE "imsi1";

--

CREATE TABLE "today_study" ("today" CHAR(8),
                                    "summary" VARCHAR, "note" VARCHAR);


ALTER TABLE "today_study" ADD COLUMN "idx" INT;

--

INSERT INTO "today_study" ("today",
                           "summary",
                           "note",
                           "idx")
VALUES ('20240930', '오리엔테이션', '     ', 1);


INSERT INTO "today_study" ("today",
                           "summary",
                           "note",
                           "idx")
VALUES ('20240930', '관련직무', '     ', 2),
       ('20240930', '환경구성', '     ', 3),
       ('20240930', '데이터의 위치', '     ', 2),
       ('20240930', '데이터의 종류', '     ', 3);

--

CREATE TABLE "today_study_backup" AS
SELECT *
FROM "today_study"
WHERE 0=1 ;

--
--> 조건 안 넣고 백업 만들기

CREATE TABLE "today_study_backup2" AS
SELECT *
FROM "today_study" ;

--

INSERT INTO "today_study_backup"
SELECT *
FROM "today_study" ;

--

UPDATE "today_study"
SET "idx" = 4
WHERE "summary" = '데이터의 위치' ;

--

UPDATE "today_study"
SET "idx" = 5
WHERE "summary" = '데이터의 종류' ;


UPDATE "today_study"
SET "note" = null
WHERE "note" = '     ' ;

--

DELETE
FROM "today_study"
WHERE "summary" = '데이터의 위치' ;

--

DELETE
FROM "today_study" -- > 이렇게 하면 다 지워짐
;

--
TRUNCATE TABLE "today_study_backup2" -- > 이렇게 하면 다 지워짐
;

--

DROP TABLE "today_study_backup2";

-- 실습

INSERT INTO "today_study" ("today",
                           "summary",
                           "note",
                           "idx")
VALUES ('20241001', '관련직무', 'ㅇㅇ', 2),
       ('20241001', '환경구성', '12', 3),
       ('20241001', '데이터의 위치', '23', 2),
       ('20241001', '데이터의 종류', '  ', 3);


SELECT "summary",
       "note",
       "idx",
       RANK() OVER(PARTITION BY "summary", "note", "idx"
                   ORDER BY "note" ASC NULLS FIRST) AS "RANK"
FROM "today_study";

--
--

CREATE TABLE "account" ("user_id" SERIAL PRIMARY KEY,
                                                 "user_name" varchar(50) UNIQUE NOT NULL,
                                                                                "password" varchar(50) NOT NULL,
                                                                                                       "email" varchar (500) UNIQUE NOT NULL,
                                                                                                                                    "created_on" TIMESTAMP NOT NULL,
                                                                                                                                                           "last_login" timestamp);


INSERT INTO "account"
VALUES (1, '전동인', '123456','dasdsf@naver.com',CURRENT_TIMESTAMP, null);


INSERT INTO "account"
VALUES (2, '전동인', '456','dasdfasf@naver.com',current_timestamp,null);


INSERT INTO "account"
VALUES (1, null, '123456','dasdfasf@naver.com',current_timestamp,null);


INSERT INTO "account"
VALUES (2, '이종석', '231231','ㄴㅇㄴㅇㅁsf@naver.com',CURRENT_TIMESTAMP, null);


INSERT INTO "account"
VALUES (3, 'ㄴㄴㄴ', 'ㅁㄴㅇㅁㄴㅇ','ㅁㄴㅇㅁㅗ호ㄴㅇ@naver.com',CURRENT_TIMESTAMP, null);


INSERT INTO "account"
VALUES (4, 'ㅇㅇㅇ', 'ㅁㄴㅇㅁㄴㅇ','ㅁㄴㅇㅁㄴㅇ@naver.com',CURRENT_TIMESTAMP, null);


DELETE
FROM "account";

--

ALTER TABLE "account" ADD CONSTRAINT "unique_password" UNIQUE ("password");


ALTER TABLE "account"
DROP CONSTRAINT "unique_password";

-- 이미 중복되는 키가 있을때

ALTER TABLE "account"
ALTER COLUMN "password"
SET NOT NULL;


ALTER TABLE "account"
ALTER COLUMN "password"
DROP NOT NULL;

--

ALTER TABLE "account" ADD CONSTRAINT "account_pkey" PRIMARY key("user_id");


ALTER TABLE "account"
DROP CONSTRAINT "account_pkey";

--> 드랍을 하면 더이상 pk역할을 못하기 때문에 중복이 허용되게 됨
 --

ALTER TABLE "account" ADD CONSTRAINT "check_password" CHECK ("password" ~ '^[0-9]+$');


ALTER TABLE "account"
DROP CONSTRAINT "check_password";

--

DROP TABLE "account";

--

CREATE TABLE ACCOUNT ("user_id" SERIAL PRIMARY KEY,
                                               "user_name" varchar(50) UNIQUE NOT NULL,
                                                                              "password" varchar(50) NOT NULL,
                                                                                                     "email" varchar (500) UNIQUE NOT NULL,
                                                                                                                                  "created_on" TIMESTAMP NOT NULL,
                                                                                                                                                         "last_login" timestamp);


CREATE TABLE ROLE("role_id" SERIAL PRIMARY KEY,
                                           "role_name" VARCHAR (255) UNIQUE NOT NULL);


CREATE TABLE ACCOUNT_ROLE
  ("user_id" INTEGER NOT NULL,
                     "role_id" INTEGER NOT NULL,
                                       "grant_date" TIMESTAMP WITHOUT TIME ZONE,
                                                                           PRIMARY KEY ("user_id",
                                                                                        "role_id"), CONSTRAINT ACCOUNT_ROLE_ROLE_ID_FKEY
   FOREIGN KEY ("role_id") REFERENCES ROLE ("role_id") MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
                                                                                                     CONSTRAINT ACCOUNT_ROLE_USER_ID_FKEY
   FOREIGN KEY ("user_id") REFERENCES ACCOUNT ("user_id") MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);


INSERT INTO ACCOUNT
VALUES (1,'전동인','1234','sdfasdf@naver.com',CURRENT_TIMESTAMP,NULL);


INSERT INTO ROLE
VALUES (1,'학생');


INSERT INTO ACCOUNT_ROLE
VALUES (1, 1, CURRENT_TIMESTAMP);

---
--DCL
BEGIN;

--

INSERT INTO ROLE
VALUES (2,'교사');


COMMIT;


INSERT INTO ROLE
VALUES (3,'친구');


ROLLBACK;


INSERT INTO ROLE
VALUES (4,'fd');

SAVEPOINT "mysave";


INSERT INTO ROLE
VALUES (5,'asdasd');


ROLLBACK TO SAVEPOINT "mysave";