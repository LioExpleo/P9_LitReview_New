from django.forms import ModelForm
from .models import Review, Ticket, Abonnement, Review2

# créer une classe qui va hériter de la class ModelForm et qui va servir à créer le formulaire pour insertion données
# class ReviewForm(ModelForm): ReviewForm hérite de ModelForm
class ReviewForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire

    # Le modèle Review doit être utilisé pour créer le formulaire
    # Précision des champs du modèle à utiliser dans le formulaire
    class Meta:
        model = Review
        fields = ['ticket','rating', 'user', 'headline', 'body']
        enctype = "multipart/form-data"
class Review2Form(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire

    # Le modèle Review doit être utilisé pour créer le formulaire
    # Précision des champs du modèle à utiliser dans le formulaire
    class Meta:
        model = Review2
        fields = ['ticket','rating', 'user', 'headline', 'body']
        enctype = "multipart/form-data"
class TicketForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire

    # Le modèle Review doit être utilisé pour créer le formulaire
    # Précision des champs du modèle à utiliser dans le formulaire
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', 'user']
        enctype = "multipart/form-data"
        """
         'image': forms.TextInput(
                attrs={
                    'class': 'ticket_body__form__form',
                    'placeholder': "facultatif, lien URL uniquement."
                }
            )
        """
class AbonnementForm(ModelForm):
     class Meta:
        model = Abonnement
        fields = ['title', 'content', 'author']
        enctype = "multipart/form-data"


