from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms

# from models import Contact
from models import Submission

class SubmissionForm(forms.Form):

    # model = Contact

    software_download = forms.ChoiceField(
            label = "Which software do you wish to download?",
            choices = (
                ('KOLAM', "Kolam"), 
                ('ROOTFLOW', "Rootflow")
            ),
            widget = forms.RadioSelect,
            initial = 'KOLAM',
        )
    
    
    email_address = forms.CharField( label = "Your email address" )
    submitter_name = forms.CharField( label = "Your name" )
    institution = forms.CharField( label = "Your institution" )



    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(SubmissionForm, self).__init__(*args, **kwargs)