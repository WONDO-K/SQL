from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__' # 외래키 필드가 노출됨
        fields = ('content',)
