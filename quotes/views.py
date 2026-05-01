from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from .models import Quote, Category, Like
import json


def get_session_id(request):
    """Obtient ou crée un identifiant de session unique pour le navigateur"""
    if 'session_id' not in request.session:
        import uuid
        request.session['session_id'] = str(uuid.uuid4())
    return request.session['session_id']


def index(request):
    get_token(request)  # Générer le token CSRF
    quotes = Quote.objects.all()
    categories = Category.objects.all()
    session_id = get_session_id(request)

    # Ajouter les likes pour chaque citation
    quotes_data = []
    for quote in quotes:
        liked = Like.objects.filter(quote=quote, session_id=session_id).exists()
        quotes_data.append({
            'id': quote.id,
            'text': quote.text,
            'author': quote.author,
            'category': quote.category.name,
            'likes': quote.likes.count(),
            'liked': liked
        })

    context = {
        'quotes': quotes_data,
        'categories': [cat.name for cat in categories],
        'session_id': session_id
    }

    return render(request, 'quotes/index.html', context)


@require_http_methods(["POST"])
def toggle_like(request):
    """API pour ajouter/retirer un like"""
    try:
        data = json.loads(request.body)
        quote_id = data.get('quote_id')

        quote = Quote.objects.get(id=quote_id)
        session_id = get_session_id(request)

        like_obj, created = Like.objects.get_or_create(
            quote=quote,
            session_id=session_id
        )

        if not created:
            # Le like existe déjà, on le supprime
            like_obj.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({
            'success': True,
            'liked': liked,
            'likes_count': quote.likes.count()
        })
    except Quote.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Citation not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
