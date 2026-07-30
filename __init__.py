import random
from aqt import gui_hooks

# Compteur de répétitions
REVIEW_COUNTER = 0
INTERVALLE_GIF = 10  # Déclenchement toutes les X cartes

# Liste de GIFs d'encouragement
GIF_URLS = [
    "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",  # Great Job
    "https://media.giphy.com/media/g9582DNuQppxC/giphy.gif",   # Cheers / Leo
    "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif", # Success / Anime
]

def afficher_gif_overlay(reviewer, card, ease):
    global REVIEW_COUNTER
    REVIEW_COUNTER += 1
    
    if REVIEW_COUNTER % INTERVALLE_GIF == 0:
        gif_url = random.choice(GIF_URLS)
        
        # Script JS qui crée une image en arrière-plan, puis la supprime après 1500 ms
        js_code = f"""
        (function() {{
            var oldOverlay = document.getElementById('anki-gif-overlay');
            if (oldOverlay) oldOverlay.remove();

            var overlay = document.createElement('div');
            overlay.id = 'anki-gif-overlay';
            overlay.style.position = 'fixed';
            overlay.style.top = '50%';
            overlay.style.left = '50%';
            overlay.style.transform = 'translate(-50%, -50%)';
            overlay.style.zIndex = '9999';
            overlay.style.pointerEvents = 'none'; // Laisse passer les clics
            overlay.style.textAlignment = 'center';
            
            var img = document.createElement('img');
            img.src = "{gif_url}";
            img.style.maxWidth = '500';
            img.style.maxHeight = '500';
            img.style.borderRadius = '15px';
            img.style.boxShadow = '0px 10px 30px rgba(0,0,0,0.5)';
            
            overlay.appendChild(img);
            document.body.appendChild(overlay);

            // Fait disparaître le GIF automatiquement après 2 seconde (2000 ms)
            setTimeout(function() {{
                if (overlay) {{
                    overlay.style.transition = 'opacity 0.3s transparent';
                    overlay.style.opacity = '0';
                    setTimeout(function() {{ overlay.remove(); }}, 300);
                }}
            }}, 2000);
        }})();
        """
        reviewer.web.eval(js_code)

# Accrochage au hook d'Anki
gui_hooks.reviewer_did_answer_card.append(afficher_gif_overlay)