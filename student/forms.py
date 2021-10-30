from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateAccountForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


class AddClassForm(forms.Form):
    course_name = forms.CharField()
    teacher_first_name = forms.CharField()
    teacher_last_name = forms.CharField()
    day = forms.TimeField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()

class SendFriendRequestForm(forms.Form):
    friend_username = forms.CharField()
