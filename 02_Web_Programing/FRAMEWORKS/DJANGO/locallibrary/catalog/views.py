from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Author, Bookinstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.urls import reverse
from catalog.forms import RenewBookform

# Create your views here.
# URL을 받아서 실제 뷰를 생성합니다.

# index라고하는 함수나 클래스가 필요함.


# Flask의 다음 함수와 같다.
# @app.route("~~~")
# def aaa():
#    return render_template()

# 함수형 뷰에서 로그인 정보를 체크하는 방법
# @login_
def index(request):

    # ?keyword=asdf 받을 수 있게 해야 한다.
    keyword = request.GET.get("keyword")

    # 세션을 가져오는 방법
    num_visits = request.session.get("num_visits",0)
    request.session["num_visits"] = num_visits + 1


    # Django ORM
    num_books = Book.objects.count()
    num_instances = Bookinstance.objects.all().count()
    # SELECT COUNT(1) FROM Bookinstance WHERE status = "a"
    num_instances_available = Bookinstance.objects.filter(status__exact="a").count()

    num_authors = Author.objects.count()

    # keyword로 장르와 책들의 개수를 가져온다.
    num_books_by_keyword = Book.objects.filter(title__exact=keyword).count()
    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_books_by_keyword": num_books_by_keyword,
    }

    return render(request, "index.html", context=context)

# LoginRequiredMixin > 이 클래스를 상속하면 로그인이 필요해진다
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 5
    # template안에서 [model]_list 형태로 보여지게 된다.
    # context_object_name > 함수 view context
    # context_object_name = "my_book_list"
    # 모델이 보여지는 방식을 지정
    # queryset = Book.objects.all()[:5]

    # queryset은 다음과 같이 지정할수도 있습니다.
    # def get_queryset(self):
    #    return Book.objects.all()[:5]
    # template_name = "book_list.html"

    # context=context, context에 리턴할 데이터가 많을 경우
    # 다음 함수를 오버라이드 해서 필요한 데이터를
    # 추가로 넣어줄 수도 있습니다.
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context["some_data"] = "just data"
        return context


# 클래스 기반의 디테일 뷰
class BookDetailView(generic.DetailView):
    model = Book


# 디테일 뷰를 함수로 변경했을 경우 다음과 같이 표현됩니다.
# def book_detail_view(request, pk):
#    try:
#        book = Book.objects.get(pk=pk)
#    except Book.DoesNotExist:
#        raise Http404("Book dose not exist")

# 리버스 검색
# Forienkey가 달려있지 않은 곳에서 연결된 리스트를 찾아주는 함수
#   book_instances = book.bookinstance_set.all()
#   return render(request, "catalog/book_detail.html", contenxt={"book", book})


# Author_list
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


# author_detail
class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = Bookinstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 5
    def get_queryset(self):
        return (
            Bookinstance.objects.filter(borrower = self.request.user)
            .filter(status__exact = "o")
            .order_by("due_back")
        )

def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(Bookinstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookform(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookform(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)