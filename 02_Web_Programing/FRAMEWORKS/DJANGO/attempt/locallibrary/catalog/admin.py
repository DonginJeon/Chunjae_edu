from django.contrib import admin
from catalog.models import Author, Bookinstance, Genre, Book


# Register your models here.
# 설정을 통해서 관리자 사이트에서 우리 모델을 관리하게 해줌
# Book, BookInstance, Author, Genre 에 대한 CRUD를 쉽게 할 수 있도록 지원해줌

# admin 사이트에 등록
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(Bookinstance)

class BookInline(admin.TabularInline):
    model = Book

# admin 페이지에 대한 커스텀 화면을 제공하는 방법
class AuthorAdmin(admin.ModelAdmin):
    # 리스트 화면에서 데이터를 보여주는 방식을 결정한다
    list_display = ("last_name", "first_name", "date_of_birth","date_of_death")
    
    # 상세화면에서 데이터를 보여주는 방식을 결정한다.
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inline = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInlince(admin.TabularInline):
    model = Bookinstance

# 다음과 같이 줄여서 쓸 수도 있습니다.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","display_genre")
    inlines = [BooksInstanceInlince]


@admin.register(Bookinstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ("status","due_back")
    list_display = ("book", "status","due_back","id")
    # 상세화면에서 데이터를 표시하는 방법
    # 섹션을 원하는 형태로 배치
    fieldsets = (
        (None, {"fields" : ("book","imprint","id")}), ("Availablity",{"fields": ("status","due_back","borrower")})
    )
