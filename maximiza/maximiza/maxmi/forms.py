from django import forms



#estudar ChoiceField
class Contato(forms.Form):
	
	nome = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea) 
	Telefone = forms.CharField(label='Telefone', max_length=11)

	