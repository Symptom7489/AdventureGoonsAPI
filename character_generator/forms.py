from django import forms
from player.models import PlayerCharacter

class PlayerCharacterForm(forms.ModelForm):
    class Meta:
        model = PlayerCharacter
        fields = '__all__'
        exclude = ('user','combat_class',)

    def __init__(self, *args, **kwargs):
        super(PlayerCharacterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Apply W3.CSS classes to the labels
            field.widget.attrs.update({'class': 'w3-label'})