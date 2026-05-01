# Citations Inspirantes - Application Django

Cette application est une conversion complète du site React original en Django, conservant toutes les fonctionnalités :

## Fonctionnalités

- ✅ Affichage de citations inspirantes avec filtrage par catégories
- ✅ Barre de recherche pour filtrer par texte, auteur ou catégorie
- ✅ Mode sombre/clair avec persistance dans localStorage
- ✅ Citation vedette avec défilement automatique toutes les 5 secondes
- ✅ Système de "J'aime" avec persistance
- ✅ Fonctionnalités de copie et partage
- ✅ Design responsive avec Tailwind CSS
- ✅ Animations et effets visuels

## Installation

1. Créer un environnement virtuel Python :
```bash
cd django_quotes
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Appliquer les migrations :
```bash
python manage.py migrate
```

4. Lancer le serveur de développement :
```bash
python manage.py runserver
```

5. Ouvrir votre navigateur à : `http://127.0.0.1:8000/`

## Structure du projet

```
django_quotes/
├── django_quotes/          # Configuration du projet Django
│   ├── settings.py         # Paramètres Django
│   ├── urls.py             # URLs principales
│   └── ...
├── quotes/                 # Application Django
│   ├── templates/          # Templates HTML
│   │   └── quotes/
│   │       └── index.html  # Template principal
│   ├── views.py            # Vues Django (données des citations)
│   └── urls.py             # URLs de l'application
├── manage.py               # Script de gestion Django
└── requirements.txt        # Dépendances Python
```

## Différences avec la version React

- **Frontend** : Utilise du JavaScript vanilla au lieu de React/hooks
- **Backend** : Django sert les données via le contexte de template
- **État** : localStorage pour la persistance côté client
- **Styling** : Tailwind CSS via CDN (identique)
- **Fonctionnalités** : 100% identiques à la version React

## Données

Les citations sont actuellement définies dans `quotes/views.py`. Pour une version production, vous pouvez :
- Créer un modèle Django pour stocker les citations dans la base de données
- Ajouter une interface d'administration Django
- Créer une API REST avec Django REST Framework

## Prochaines étapes possibles

1. Créer des modèles Django pour les citations
2. Ajouter l'authentification utilisateur
3. Permettre aux utilisateurs d'ajouter leurs propres citations
4. Créer une API REST
5. Ajouter des tests unitaires
