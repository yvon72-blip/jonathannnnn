#!/bin/bash

echo "=== Citations Inspirantes - Django Application ==="
echo ""

# Vérifier si Django est installé
if ! python3 -c "import django" 2>/dev/null; then
    echo "Django n'est pas installé. Installation en cours..."
    python3 -m pip install Django --user
    echo ""
fi

# Appliquer les migrations
echo "Application des migrations..."
python3 manage.py migrate

echo ""
echo "=== Démarrage du serveur Django ==="
echo "Accédez à l'application sur: http://127.0.0.1:8000/"
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

# Lancer le serveur
python3 manage.py runserver
