from django import forms
from .models import Board
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    tag2_choices = [
        ('자료', '자료'),
        ('인물정보', '인물정보'),
        ('보고서', '보고서'),
        # 여러 선택 옵션을 추가할 수 있습니다.
    ]
    
    tag2 = forms.ChoiceField(
        required=False,
        label="tag2",
        choices=tag2_choices,
        widget=forms.Select(attrs={
            "style": "border: 1px solid #dbdbdb; width: 735px; height:30px; margin-bottom:10px",
        }),
    )
    
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "style": "border: 1px solid #dbdbdb; width: 735px; height:30px; margin-bottom:10px",
                "placeholder": " 자료 이름",
            }
        ),
    )
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "style": "border: 1px solid #dbdbdb; width: 735px; height:200px; margin-bottom:10px",
                "placeholder": "자료 내용 요약",
            }
        ),
    )
    
    tag = forms.CharField(
        required=False,  # 이 필드는 선택 사항으로 지정할 수 있습니다.
        label="tag",
        widget=forms.TextInput(attrs={
            "style": "border: 1px solid #dbdbdb; width: 735px; height:30px; margin-bottom:10px",
            "placeholder": "태그를 콤마로 구분해서 입력하세요.",
        }),
    )
    
    # image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'image'}))
    
    image = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'image'}))
    
    def clean_tag(self):
        tag = self.cleaned_data.get('tag', '')
        if isinstance(tag, list):
            # 이미 리스트 형태인 경우
            return tag
        elif tag:
            # 입력된 문자열을 콤마로 분리하여 리스트로 변환
            return [item.strip() for item in tag.split(',')]
        else:
            return []

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['tag'] = self.clean_tag()
        return cleaned_data

    class Meta:
        model = Board
        exclude = []

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.tag = self.clean_tag()
        if commit:
            instance.save()
        return instance
        
    
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    
class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'login-input'}),
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'login-input'}),
        label='',
    )
    
class SearchCrimeForm(forms.Form):
    query = forms.CharField(label='검색어', max_length=100)