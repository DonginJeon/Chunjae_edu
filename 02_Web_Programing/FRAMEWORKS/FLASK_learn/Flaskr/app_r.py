from flask import (
    Flask,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from db.connection import db_connect

USERNAME = "user"
PASSWORD = "1234"
# 플라스크 사용
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "q86lralpq9bo22xmguvwqdt9hmhvujpm"


# 예를들어 /user 하는 요청이 왔을 때, ./user에 해당하는 라우터를 실행하기 전에
# 미리 커넥션을 해놓습니다.
@app.before_request
def before_request():
    g.conn = db_connect()


# ./user에서 라우터에서 함수 실행이 끝난후(요청에 대한 응답을 보내준 후)
# 데이터 베이스의 커녁션을 종료한다


@app.teardown_request
def teardown_request(exception):
    g.conn.close()


@app.route("/")
def show_entries():
    SQL = """
        select title,text 
        from entries
        order by id desc
    """
    entries = []
    with g.conn.cursor() as cur:
        cur.execute(SQL)
        entries = cur.fetchall()

    return render_template("show_entries.html", entries=entries)

## 주소 뒤에다 입력해서 가져오는 건 GET 요청, POST만 썻기 때문에 아래에선 오류가 발생
# request(get,post,update,delete) 중에 post 요청만 받겠다
@app.route("/add", methods=["POST"])
def add_entry():
    # session은 임시 공간인데 주로 유저 정보를 저장한다
    if not session.get("logged_in"):
        # 요청에 대한 거절
        abort(401)

    SQL = """
        insert into entries(
            title, text
        ) values(
            %s,%s
        )
    """

    with g.conn.cursor() as cur:
        # request는 유저의 요청에 대한 정보를 담고 있음
        # request 내부에는 데이터를 저장하고 있는 form이라는 객체가 있음(GET이 아닐때, POST일때)
        cur.execute(SQL, (request.form["title"], request.form["text"]))
    g.conn.commit()
    # 메시지 띄우는 용도
    flash("성공")
    # 요청을 다시 해서 다른 화면으로 보내는 함수
    # url_for는 함수 이름으로 연결된 라우터를 찾음
    return redirect(url_for("show_entries"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        # 유저의 요청 안에 유저명/비밀번호를 체크
        if request.form["username"] != app.config["USERNAME"]:
            error = "Invalid username"
        elif request.form["password"] != app.config["PASSWORD"]:
            error = "Invalid password"
        else:
            # 로그인에 성공했으면
            # session : 임시 저장소에 logged_in을 넣어준다
            session["logged_in"] = True
            flash("you were logged in")
            return redirect(url_for("show_entries"))
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    # pop() 함수는 해당 키에 있는 데이터를 제거
    session.pop("logged_in", None)
    flash("you were logged out")
    # 함수 이름에 맞는 라우터를 찾아서 요청을 다시 보냄
    return redirect(url_for("show_entries"))


if __name__ == "__main__":
    app.run()
