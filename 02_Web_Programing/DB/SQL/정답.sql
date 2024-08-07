-- 1. 유저 데이터를 3건 추가합니다.
INSERT INTO tb_user (
	login_id, login_password, name, address, phone	
) VALUES 
('user1', 'user1', 'aaa', '서울시', NULL),
('user2', 'user2', 'bbb', NULL, '010-1111-111'),
('user3', 'user3', 'ccc', '경기도 안양시', '010-222-2222')

-- 2. 게시판 테이블에 데이터를 10건 추가합니다.
INSERT INTO tb_board(
	title, content, user_id
) VALUES
('제목 1', '내용입니다.', 1),
('제목 2', '안녕하세요', 2),
('제목 3', '데이터베이스는 재미있어요', 3),
('제목 4', '내용입니다.', 1),
('제목 5', '반갑습니다.', 2),
('제목 6', '오늘은 점심으로 무엇이 좋을까요', 3),
('제목 7', '안녕하세요', 3),
('제목 8', '데이터가 골고루 들어갈 수 있도록 해주세요', 3),
('제목 9', '내용입니다.', 2),
('제목 10', '내용입니다.', 1)

-- 3. id=3인 tb_board 데이터를 검색합니다.
SELECT 
	id, 
	title, 
	content, 
	user_id, 
	create_date, 
	update_date 
FROM 
	tb_board
WHERE id = 3;

-- 4. 전화번호가 없는 회원 데이터에 전화번호 추가하기
-- 특정 컬럼이 NULL 일경우 찾아오는 방법 : IS NULL
-- 아닐 경우 : IS NOT NULL
SELECT id, login_id FROM tb_user WHERE tb_user.phone IS NULL
UPDATE tb_user SET
	phone = '010-333-3333'
WHERE phone IS NULL

-- 5. 최근에 만들어진 tb_board의 데이터 삭제하기
DELETE FROM tb_board WHERE id = 10;

-- 1. 댓글 테이블 만들기
CREATE TABLE tb_board_comment (
	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	board_id BIGINT NOT NULL,
	user_id BIGINT NOT NULL,
	comment varchar(200) NULL,
	create_date datetime DEFAULT current_timestamp,
	update_date datetime DEFAULT current_timestamp
);

-- 2. 댓글 테이블에 데이터 10건 입력하기
INSERT INTO tb_board_comment (
	board_id, user_id, comment 
) VALUES
(2, 1, '댓글입니다 1'),
(3, 2, '댓글입니다 2'),
(4, 3, '댓글입니다 3'),
(2, 2, '댓글입니다 4'),
(3, 2, '댓글입니다 5'),
(4, 3, '댓글입니다 6'),
(4, 1, '댓글입니다 7'),
(2, 3, '댓글입니다 8'),
(3, 2, '댓글입니다 9'),
(2, 1, '댓글입니다 10')


-- 2. user_id가 2번인 tb_board_comment의 댓글 값을 ‘원본 댓글’ + ‘-’ + ‘id’로 변경해 봅시다.
-- MariaDB에는 데이터를 합칠 수 있도록 CONCAT()이라는 함수를 지원해준다.
UPDATE tb_board_comment SET 
	comment = CONCAT(comment, '-', id)
WHERE user_id = 2;

-- 3. board_id가 4번인 댓글을 모두 삭제해 봅시다.
DELETE FROM tb_board_comment
WHERE board_id = 4;


CREATE TABLE tb_board_comment (
	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	board_id BIGINT NOT NULL,
	user_id BIGINT NOT NULL,
	comment varchar(200) NULL,
	create_date datetime DEFAULT current_timestamp,
	update_date datetime DEFAULT current_timestamp,
	-- FK를 테이블을 새로 만들 때 지정해주는 방법
	FOREIGN KEY(board_id) REFERENCES tb_board(id),
	FOREIGN KEY(user_id) REFERENCES tb_user(id)
);


-- 기존에 있는 테이블에 FK 추가하기.
ALTER TABLE tb_board ADD CONSTRAINT
FOREIGN KEY(user_id) REFERENCES tb_user(id);


-- 유저 데이터 3건 추가하기
INSERT INTO tb_user(
	login_id, login_password, name, address, phone 
) VALUES 
('user4', 'user4', 'ddd', NULL, NULL),
('user5', 'user5', 'eee', NULL, NULL),
('user6', 'user6', 'Fff', NULL, NULL)

-- user.id가 3인 회원의 이름과 작성글의 제목, 내용을 가져옵니다.
SELECT
	`user`.name,
	board.title,
	board.content
FROM
	tb_user AS `user`
	INNER JOIN tb_board AS board ON `user`.id = board.user_id
WHERE `user`.id = 3	

-- 모든 회원 목록과 회원들이 작성한 게시글의 이름, 내용을 가져옵니다. 이 때, 회원이 작성한 글이 없다면 게시글 목록은 NULL로 표시합니다.
SELECT
	`user`.id,
	`user`.login_id,
	`user`.login_password,
	`user`.name,
	`user`.address,
	`user`.phone,
	`user`.error_count,
	board.title,
	board.content
FROM
	tb_user `user`
	LEFT OUTER JOIN tb_board board ON `user`.id = board.user_id

	
	

