from django import forms
from AllInOne.models import Branch, Semester, Material


class BranchForm(forms.ModelForm):
	 class Meta:
	 	model = Branch
	 	fields = ('branch',)


class SemesterForm(forms.ModelForm):
	 class Meta:
	 	model = Semester
	 	fields = ('semester',)



class MaterialForm(forms.ModelForm):
	 class Meta:
	 	model = Material
	 	fields = ('material',)