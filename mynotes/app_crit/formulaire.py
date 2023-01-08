from django.forms import ModelForm
from .models import Review

# créer une classe qui va hériter de la class ModelForm et qui va servir à créer le formulaire pour insertion données
# class ReviewForm(ModelForm): ReviewForm hérite de ModelForm
class ReviewForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser pour le formaulaire
    # Le modèle Review doit être utilisé pour créer le formulaire
    # Précision des champs du modèle à utiliser dans le formulaire
    class Meta:
        model = Review
        fields = ['ticket','rating', 'user', 'headline', 'body']

