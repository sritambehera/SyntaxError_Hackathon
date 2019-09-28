from django import forms
from AllInOne.models import Paper


class UploadFileForm(forms.ModelForm):
	
	class Meta:
		model = Paper
		fields = ('branch','semester', 'file',)
			