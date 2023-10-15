from django import forms

class RatingForm(forms.Form):
    rating = forms.IntegerField(
        label='Рейтинг',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'rating-input'})
    )