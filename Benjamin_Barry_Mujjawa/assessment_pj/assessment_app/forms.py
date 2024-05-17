from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    course = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    entry_scheme = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    intake = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    sponsorship = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    gender = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)
    residence = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        course = cleaned_data.get('course')
        entry_scheme = cleaned_data.get('entry_scheme')
        intake = cleaned_data.get('intake')
        sponsorship = cleaned_data.get('sponsorship')
        gender = cleaned_data.get('gender')
        dob = cleaned_data.get('dob')
        residence = cleaned_data.get('residence')

        if not first_name or not last_name or not course or not entry_scheme or not intake or not sponsorship or not gender or not dob or not residence:
            self.add_error('first_name', 'invalid field')
            self.add_error('last_name', 'invalid field')
            self.add_error('course', 'this field is required')
            self.add_error('entry_scheme', 'this field is required')
            self.add_error('intake', 'this field is required')
            self.add_error('sponsorship', 'this field is required')
            self.add_error('gender', 'this field is required')
            self.add_error('dob', 'this field is required')
            self.add_error('residence', 'invalid field')
        elif dob < 18:
            self.add_error('dob', 'has to be above 18')

                