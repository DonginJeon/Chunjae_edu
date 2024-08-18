from flask import Flask, abort, flash, g, redirect, render_template, request, session, url_for, jsonify
from db.connection import db_connect

USERNAME="root"
PASSWORD="1234"

# 플라스크 사용
app = Flask(__name__)
# 모듈 이름을 통해 파이썬 파일을 서치하는데,
# __name__을 직접 넣으면 내 파일을 바라봅니다.
app.config.from_object(__name__)
# 세션 사용을 위한 암호화 키
app.secret_key = "nmrkgpajc72m9rf62ff081xf48rrkyfr"
app.debug = True

#. 예를들어 /user 라는 요청이 왔을 때
#. /user에 해당하는 라우터를 실행하기 전에
#. 데이터베이스에 미리 커넥션을 해놓습니다.
@app.before_request
def before_request():
    g.conn = db_connect()

#. /user에서 라우터의 함수 실행이 끝난 후(요청에 대한 응답을 보내준 후)
#. 데이터베이스의 커넥션을 종료합니다.
@app.teardown_request
def teardown_request(exception):
    g.conn.close() 

@app.route("/")
def show_entries():
    SQL = """
        SELECT title, text
        FROM entries
        ORDER BY id DESC
    """
    entries = []
    with g.conn.cursor() as cur:
        cur.execute(SQL)
        entries = cur.fetchall()
    # from Flask import render_template
    return render_template('show_entries.html', entries=entries)

# 하고 싶은 것:
# 우리의 Flask는 지금 HTML만 받아요.
# HTML 뿐만 아니라, JSON이라고 하는,
# 데이터 형태로 response를 전달하고 싶어요
@app.route("/api/entries")
def json_entries():
    SQL = """
        SELECT id, title, text
        FROM entries
        ORDER BY id DESC
    """
    entries = []
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL)
            entries = cur.fetchall()

    # 파이썬이 가지고 있는 튜플, 리스트, D.D를
    # JSON 문법에 맞게(배열, 자바스크립트 객체)로 변경해주는 것.
    return jsonify(entries)

# 실습
@app.route("/entries")
def view_entries():
    # 0. 데이터베이스나, 지금 이 사이트를 이용하여 데이터를 추가합니다.
    # 1. 이 라우터가 빈 HTML을 반환하도록 합니다.
    # 2. JS에서 fetch()를 이용해서 entries 데이터를 호출합니다.
    # 3. JS를 이용하여 화면에 entries의 제목들이 나오도록 해 봅시다.
    return render_template("entries.html")
    



#. methods=POST는 POST 요청만 받는다는 뜻이다
@app.route('/add', methods=['POST'])
def add_entry():
    # session은 서버의 임시 공간인데, 주로 유저 정보를 저장한다.
    if not session.get("logged_in"):
        # 요청에 대한 거절이다.
        abort(401)

    SQL = """
        INSERT INTO entries(
            title, text
        ) VALUES(
            %s, %s
        )
    """
    
    with g.conn.cursor() as cur:
        # request는 유저의 요청에 대한 정보를 담고 있습니다.
        # request 내부에는 데이터를 저장하고 있는 form이란 객체가 있습니다.(POST일때)
        cur.execute(SQL, (request.form["title"], request.form["text"]))
    g.conn.commit()
    # 메시지 띄우는 용도입니다.
    flash("New entry was successfully posted")
    # redirect는 다른 화면으로 보내는 함수입니다.
    # url_for는 함수 이름으로 연결된 route를 찾습니다.
    return redirect(url_for("show_entries"))

# GET, POST : GET과 POST 요청을 다 받는다
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    # POST 요청일 경우에만 실행
    if request.method == "POST":
        # 유저의 요청 안에 유저명/비밀번호를 체크
        if request.form["username"] != app.config["USERNAME"]:
            error = "Invalid username"
        elif request.form["password"] != app.config["PASSWORD"]:
            error = "Invalid password"
        else:
            # 로그인에 성공했으면
            # session : 임시 저장소에 logged_in을 넣어준다.
            session["logged_in"] = True
            flash("You were logged in")
            # 함수명에 맞는 router로 요청을 다시 보낸다.
            return redirect(url_for("show_entries"))
    # 로그인 html을 보여준다.
    return render_template("login.html", error=error)
    
@app.route("/logout")
def logout():
    # pop() 함수는 해당 키에 있는 데이터를 제거합니다.
    session.pop("logged_in", None)
    flash("you were logged out")
    # 함수 이름에 맞는 라우터를 찾아서 요청을 다시 보냅니다.
    return redirect(url_for("show_entries"))


if __name__ == "__main__":
    app.run()
    