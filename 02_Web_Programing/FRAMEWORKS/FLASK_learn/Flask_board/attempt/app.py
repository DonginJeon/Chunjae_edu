from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from connection import db_connect
app = Flask(__name__)


##대문
@app.route("/")
def index():
    return render_template("index.html")
app.secret_key = "hbesfknhdj0o835p1703h98q3nl9dwsp"

## 스테틱과 템플릿, 두개의 폴더 생성
# templates(끝에 s를 붙이는 것이 중요)
# static

## 로그인 페이지 생성
@app.route("/login")
def login():
    SQL = """
        select * 
        from tb_user
        where 1=1
        and login_id = %s and login_password = %s
    """
    error_message = None
    if request.method == "POST":
        login_id = request.form["login_id"]
        login_password = request.form["login_password"]
        
        with db_connect() as conn:
            with conn.cursor() as cur:
                cur.execute(SQL,[login_id, login_password])
                user = cur.fetchone()
                if (user != None and len(user) > 0):
                    session["user"] = user
                    return redirect(url_for("index"))
                else:
                    error_message = "유저가 존재하지 않습니다."
    return render_template("login.html", error_message=error_message)

## 로그아웃
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

## 게시판 페이지 생성
@app.route("/board")
def view_board():
    SQL = """
        select id, title, update_date
        from tb_board
        where 1=1
        order by update_date
    """
    boards = []
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL)
            boards = cur.fetchall()
    return render_template("board.html", boards = boards)

@app.route("/board/new", methods = ["GET"])
def view_insert_board():
    return render_template("insert_board.html")

@app.route("/board/new" ,methods=["POST"])
def insert_board():
    SQL = """
        insert into tb_board(
            title,content,user_id
        ) values(
            %s,%s,%s 
        )
    """
    if not session.user:
        return redirect(url_for("login"))
    user_id = session.user.id
    title = request.form["title"]
    content = request.form["content"]
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, [user_id,title,content])
            conn.commit()
            return redirect(url_for("view_board"))


## 게시판 상세 페이지
@app.route("/board/<int:board_id>")
def view_board_detail(board_id):
    SQL = """
        select 
            board.id,board.title,board.content,board.user_id,user.name, board.create_date, board.update_date
        from tb_board as board
            inner join tb_user as user on board.user_id = user.id
        where id = %s
    """

    
    board = {}
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, board_id)
            # fetchone : 데이터가 반드시 한 건임을 보장함


            board = cur.fetchone()

    # TODO 보드 아이디를 그냥 넘겨주지만 나중에는 데이터베이스를 검색
    return render_template("board_detail.html",board=board)

@app.route("/board/update/<int:board_id", methods=["GET"])
def view_update_board(board_id):
    SQL = """
        select id, title, content
        from tb_board
        where id = %s
    """
    board = {}
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL,board_id)
            board = cur.fetchone()
    return render_template("update_board.html",board = board_id)

@app.route("/board/update", methods=["POST"])
def update_board():
    SQL = """
        update tb_board set
            title = %s,
            content = %s,
            update_date = NOW()

        where 1=1
            and id = %s
    """

    title = request.form["title"]
    content = request.form["content"]
    board_id = request.form["board_id"]
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL,[title,content,board_id])
            conn.commit()
            return redirect(url_for("view_board_detail", board_id))
    
## 실습 : 댓글도 가져오세요
    # 1. 여기서 쿼리를 한번 더 작성해서 가져온다
    # 2. API라우터를 하나 만들어서 fetch()로 가져온다

## 게시판 상세 페이지 (+댓글)
@app.route("/api/comment/<int:board_id>")
def get_board_comments(board_id):
    SQL = """
        select 
            user.name as name, comment.id, comment.comment,comment.update_date
        from 
            tb_board_comment comment
            inner join tb_user user
                on comment.user_id = user.id
        
        where 
            and comment.board_id = %s
    """
    comments = []
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, board_id)
            # fetchone : 데이터가 반드시 한 건임을 보장함

            comments = cur.fetchall()
    return jsonify(comments)



## 플라스크를 구동할 준비
if __name__ == "__main__":
    app.run()
