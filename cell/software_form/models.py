from django.db import models


class Submission(models.Model):
	software_download = models.CharField(max_length=250)
	email_address = models.CharField(max_length=250)
	submitter_name = models.CharField(max_length=250)
	institution = models.CharField(max_length=250)

	class Admin:
		pass
	
	def __repr__(self):
		return self.email_address
	
	def __str__(self):
		return self.email_address
