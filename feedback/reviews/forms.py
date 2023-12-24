from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your Name", max_length=100, required=True, error_messages={
        'required': 'Your name must not be empty',
        'max_length': 'Please enter a shorter name less than 100 characters.'},
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Username...', 'id': 'username', 'style': 'border: 3px solid #888; border-radius: 20px;'}),
    )

    review_text = forms.CharField(label="Your Feedback", max_length=200, min_length=10, required=True, error_messages={
        'required': 'Your feedback must not be empty',
        'max_length': 'Please enter a shorter feedback less than 200 characters.',
        'min_length': 'Please enter a longer feedback more than 10 characters.'},
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your Feedback...', 'id': 'review_text', 'style': 'width: 100%; padding: 20px; margin: 10px; border: 3px solid #888; border-radius: 20px;'}),
    )

    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

    def clean_username(self):
        username = self.cleaned_data['username']
        # Add your validation logic here
        if len(username) < 3:
            raise forms.ValidationError(
                "Username must be at least 5 characters long.")
        return username
