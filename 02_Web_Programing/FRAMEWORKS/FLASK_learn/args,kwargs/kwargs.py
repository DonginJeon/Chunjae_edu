# **kwargs는 특정 키 값을 같이 전달한다.

def my_function(**kwargs):
    print(
        kwargs.get("first"),
        kwargs.get("mid"),
        kwargs.get("last")
    )

my_function(
    first = "Jeon",
    mid = "Dong",
    last = "in"
)