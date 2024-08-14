from rest_framework import serializers
from catalog.models import Book

# Class를 json이나 XML형태로 쉽게 변환할 수 있게 해주는 기능
# Serializer가 자동으로 D.D 형태로 만들어주는 것
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # Book이 가진 모든 필드를 대상으로 함
        filelds = "__all__"

class BookinstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinstance
        fields = "__all__"