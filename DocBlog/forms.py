from django import forms
import codecs 
  
f = open('GFG.html', 'w') 


SCRAP_CHOICES= [
    ('20', '20'),
    ('100', '100'),
    ('500', '500'),
    ('1000', '1000'),
    ('10 000', '10 000'),
    ]

COUNTRY_CHOICES= [
    ('France', 'France'),
    ('Espagne', 'Espagne'),
    ('Etats-Unis', 'Etats-Unis'),
    ('Angleterre', 'Angleterre'),
    ('Belgique', 'Belgique'),
    ]

class NameForm(forms.Form):
    enseigne = forms.CharField(label='Enseigne à scraper *  \n ', max_length=100)
    ville = forms.CharField(label='Nom de la Ville  ', max_length=100) 
    
    departement = forms.CharField(label='Nom de la région  ', max_length=100)

    pays = forms.CharField(label='Pays à scraper ? * ', widget=forms.Select(choices=COUNTRY_CHOICES))
    scrap_choices= forms.CharField(label='Combien de lignes voulez vous Scraper?', widget=forms.Select(choices=SCRAP_CHOICES))
    
    
    