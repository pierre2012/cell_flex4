from django.db import models

from django import forms

class Contact(models.Model):
	sender = models.CharField(max_length=250)
	subject = models.CharField(max_length=250)
	message = models.CharField(max_length=10000)

	class Admin:
		pass
	
	def __repr__(self):
		return self.sender
	
	def __str__(self):
		return self.sender



class ContactForm(forms.Form):
	sender = forms.EmailField()
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea())

	def save (self): 
		data = self.cleaned_data 
		contact = Contact() 
#		contact.subject = data.get('subject', '') 
#		contact.message = data.get('message', '') 
#		contact.sender = data.get('sender', '')
		contact.subject = self.cleaned_data['subject']
		contact.message = self.cleaned_data['message']
		contact.sender = self.cleaned_data['sender']
		 
		contact.save() 
		return contact

