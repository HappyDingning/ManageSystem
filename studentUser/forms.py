from django.forms import ModelForm, ValidationError
from django import forms
from .models import UndergraduateInfo, UndergraduateOtherInfo

class studentInfo(ModelForm):
    class Meta:
        model = UndergraduateInfo
        fields = ("studentID", "studentName", "gender", "enrollmentYear", 
                  "specialty", "studentClass", "mobileNumber", "qqNumber", 
                  "politicalStatus", "instructor", "position")
    
    def __init__(self, *args, **kwargs):
        super(studentInfo, self).__init__(*args, **kwargs)

class studentOtherInfo(ModelForm):
    class Meta:
        model = UndergraduateOtherInfo
        exclude = ("baseInfo", )
    
    def __init__(self, *args, **kwargs):
        super(studentOtherInfo, self).__init__(*args, **kwargs)
