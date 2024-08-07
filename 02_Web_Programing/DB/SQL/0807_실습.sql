-- 실습1
insert into tb_user(
	login_id,
	login_password,
	name,
	address,
	phone
) values 
	('skywalker','1234','Anakin Skywalker','Temple1','111'),
	('kenobi','1234','Obiwan Kenobi','Temple2','222'),
	('tano','1234','Ashoka Tano','Temple3','333');

set foreign_key_checks = 1;

insert into tb_board(
	title,
	content,
	user_id 
) values (
	'Mustafar',
	'invasion.',
	1
),(
	'coursant',
	'defend',
	2
),(
	'naboo',
	'protect',
	3
),(
	'hoth',
	'travel',
	4
),(
	'dathomir',
	'investigation.',
	5
),(
	'Mustafar',
	'invasion.',
	6
),(
	'coursant',
	'defend',
	7
),(
	'naboo',
	'protect',
	8
),(
	'hoth',
	'travel',
	9
),(
	'dathomir',
	'investigation.',
	10
);


select id
from tb_board
where id =3;




-- 실습2
-- 코멘트 테이블 생성
create table tb_board_comment(
	id bigint not null auto_increment primary key,
	board_id bigint not null,
	user_id bigint not null,
	comment varchar(200),
	create_date datetime not null default current_timestamp,
	update_date datetime not null default current_timestamp,
	foreign key(board_id) references tb_board(id),
	foreign key(user_id) references tb_user(id)
);


insert into tb_board_comment(
	board_id,
	user_id
	
) value (
	2,
	4
), (
	2,
	4	
), (
	2,
	5	
), (
	3,
	4	
), (
	3,
	6	
), (
	3,
	6	
), (
	4,
	4
),(
	4,
	5	
),(
	4,
	5
),(
	4,
	6	
);

update tb_board_comment set 
	comment = CONCAT(comment, '-', id)
where user_id = 5;

delete from 
	tb_board_comment
where board_id=4;


--외래키 지정하기
alter table tb_board add constraint
foreign key (user_id) references tb_user(id);



-- 데이터를 조인하여 가져오기
select * from tb_board as board
inner join tb_board_comment as comment
	on board.id = comment.board_id
where board.id=3;


-- left outer join은 상위 테이블에서 하위 테이블로 내려갑니다
select  *
from 
	tb_board as board
	left outer join tb_board_comment as comment
		on board.id = comment.board_id;

		
-- right outer join은 하위 테이블에서 상위 테이블로 올라갑니다
select * 
from 
	tb_board_comment as comment
	right outer join tb_board as board on board.id = comment.board_id ;


-- 실습3
-- 1
insert into tb_user(
	login_id,
	login_password,
	name,
	address,
	phone
) values 
	('windu','1234','Mace Windu','Temple4','444'),
	('jinn','1234','Quigon Jinn','Temple5','555'),
	('ti','1234','shakk ti','Temple6','666');

delete from tb_user;

-- 2
select
	'user'.name,
	board.title,
	board.content
from 
	tb_user as 'user'
	inner join tb_board as board on 'user'.id = board.user_id
where 'user'.id = 3;





delete from tb_user;

delete from tb_board_comment;

delete from tb_board;





