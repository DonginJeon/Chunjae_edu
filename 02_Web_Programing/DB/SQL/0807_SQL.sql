insert into tb_board(
	title,
	content,
	user_id 
) values (
	'제목 1',
	'내용입니다.',
	1
)

update tb_board set 
	title  = '수정되었습니다.',
	content = '수정내용'
where id = 1;


select 
	id,
	title,
	content
from
	tb_board
where id = 1;
