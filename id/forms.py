from django import forms
from .models import CommunityPost, Identified

class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['fungi_id', 'image_url', 'location', 'latitude', 'longitude', 'notes', 'status']

class IdentifiedForm(forms.ModelForm):
    post_id = forms.ModelMultipleChoiceField(
        queryset=CommunityPost.objects.none(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for multiple selection
        label="Community Posts"
    )

    class Meta:
        model = Identified
        fields = ['list_name', 'post_id']  # Include other fields if needed

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Filter post_id choices to show only posts created by the logged-in user
            self.fields['post_id'].queryset = CommunityPost.objects.filter(user_id=user)
            # Customize the display of each post in the form
            self.fields['post_id'].label_from_instance = lambda obj: f"{obj.fungi_id} - {obj.time} - {obj.location}"