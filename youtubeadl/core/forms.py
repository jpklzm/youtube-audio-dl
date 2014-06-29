from django import forms

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit, Fieldset, HTML, Field, Div
from crispy_forms.bootstrap import FormActions


class DownloadForm(forms.Form):
    url = forms.URLField(max_length=255, label='YouTube URL')

    def __init__(self, *args, **kwargs):
        super(DownloadForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'download_form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal col-xs-12 col-sm-12 ' \
                                 'col-md-8 col-lg-8 col-md-offset-2 ' \
                                 'col-lg-offset-2'
        self.helper.field_class = 'col-lg-12'
        self.helper.form_show_labels = False

        self.helper.layout = Layout(
            Fieldset(
                "Enter the video URL to convert to MP3",
                Div(
                    css_id='result',
                ),
                Field('url',
                      placeholder='e.g. https://www.youtube.com/watch?v=JAFQFvSPhQ8',
                      onclick='select("id_url");',
                      autofocus=True,
                ),
                FormActions(
                    HTML("""<p class="text-center">"""),
                    Submit('submit',
                           'Start Conversion',
                           css_class='btn-lg'),
                ),
            ),
        )