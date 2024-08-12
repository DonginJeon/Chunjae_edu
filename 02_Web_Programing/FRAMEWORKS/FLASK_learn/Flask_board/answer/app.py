from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from db.connection import db_connect

app = Flask(__name__)
# 서버에 바로 수정사항이 반영되도록 옵션을 지정
app.secret_key = "rvq629mvr79t3v5v2v91l3p1itxcgifj"

@app.route("/")
def index():
    return render_template("index.html")

# 로그인 페이지
@app.route("/login", methods=["GET", "POST"])
def login():
    SQL = """
        SELECT * FROM tb_user 
        WHERE 1 = 1
            AND login_id = %s
            AND login_password = %s
    """
    error_message = None
    if request.method == "POST":
        login_id = request.form["login_id"]
        login_password = request.form["login_password"]
        with db_connect() as conn:
            with conn.cursor() as cur:
                cur.execute(SQL, [login_id, login_password])
                user = cur.fetchone()
                if (user != None and len(user) > 0):
                    session["user"] = user
                    return redirect(url_for("index"))
                else:
                    error_message = "유저가 존재하지 않습니다."
                
    return render_template("login.html", error_message=error_message)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

# 게시판 페이지
@app.route("/board")
def view_board():
    SQL = """
        SELECT id, title, update_date
        FROM tb_board
        WHERE 1=1
        ORDER BY update_date
    """
    boards = []
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL)
            boards = cur.fetchall()
    return render_template("board.html", boards=boards)

@app.route("/board/new", methods=["GET"])
def view_insert_board():
    return render_template("insert_board.html")

@app.route("/board/new", methods=["POST"])
def insert_board():
    SQL = """
        INSERT INTO tb_board(
            title, content, user_id
        )
        VALUES(
            %s, %s, %s
        )
    """
    if not session["user"]:
        return redirect(url_for("login"))
     
    user_id = session["user"]["id"]
    title = request.form["title"]
    content = request.form["content"]
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, [title, content, user_id])
            conn.commit()
            return redirect(url_for("view_board"))

# 게시판 상세 페이지
@app.route("/board/<int:board_id>")
def view_board_detail(board_id):
    SQL = """
        SELECT 
            board.id, 
            board.title, 
            board.content,
            board.user_id,
            user.name, 
            board.create_date, 
            board.update_date
        FROM tb_board AS board
            INNER JOIN tb_user AS user ON board.user_id = user.id
        WHERE board.id = %s
    """
    board = {}
    # 실습: 댓글도 가져오세요. 방법은 아무렇게나
    # 1. 여기서 쿼리를 한번 더 해서 댓글을 가져온다.
    # 2. API 라우터를 하나 만들어서 fetch()로 가져온다.
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, board_id)
            # fetchone : 데이터가 반드시 한 건임을 보장한다.
            board = cur.fetchone() 
    return render_template("board_detail.html", board=board)


@app.route("/board/update/<int:board_id>", methods=["GET"])
def view_update_board(board_id):
    SQL = """
        SELECT 
            id, 
            title, 
            content
        FROM
            tb_board
        WHERE id = %s
    """
    board = {}
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, board_id)
            board = cur.fetchone()

    return render_template("update_board.html", board=board)

@app.route("/board/update", methods=["POST"])
def update_board():
    SQL = """
        UPDATE tb_board SET
            title = %s,
            content = %s,
            update_date = NOW()
        WHERE 1 = 1
            AND id = %s
    """
    title = request.form["title"]
    content = request.form["content"]
    board_id = request.form["board_id"]
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, [title, content, board_id])
            conn.commit()
            return redirect(url_for("view_board_detail", board_id=board_id))
            

@app.route("/api/comment/<int:board_id>")
def get_board_comments(board_id):
    SQL = """
        SELECT 
            user.name, comment.id, 
            comment.comment, comment.update_date
        FROM 
            tb_board_comment comment
            INNER JOIN tb_user user 
                ON comment.user_id = user.id
        WHERE 1=1
            AND comment.board_id = %s

    """
    comments = []
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, board_id)
            comments = cur.fetchall()
    return jsonify(comments)        


if __name__ == "__main__":
    app.run()