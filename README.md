# Anki GIF et motivation

Greffon Anki basique motivant permettant de voir un GIF toutes les X révisions.

Un greffon léger pour **Anki** qui affiche automatiquement un GIF d'encouragement au centre de votre écran toutes les 10 cartes révisées pour rendre vos sessions d'apprentissage plus ludiques.

---

## Fonctionnalités

* Compteur dynamique de cartes : Analyse vos réponses en temps réel et décompte le nombre de révisions effectuées pendant votre session.
* Overlay éphémère et fluide : Affiche un GIF stylisé au centre de l'écran qui disparaît automatiquement au bout de 2 secondes sans bloquer vos clics.
* Sélection aléatoire : Pioche au hasard parmi une liste d'URLs de GIFs d'encouragement personnalisables.

---

## Installation pas à pas

Puisque ce greffon est fourni sous la forme d'un script Python direct (`__init__.py`), voici comment l'installer manuellement dans votre logiciel Anki :

### Étape 1 : Localiser le dossier des add-ons d'Anki

1. Ouvrez l'application **Anki** sur votre ordinateur.
2. Dans le menu supérieur, cliquez sur **Outils** (ou *Tools*) puis sur **Greffons** (ou *Add-ons*). *(Raccourci : `Ctrl + Shift + A` sur Windows/Linux ou `Cmd + Shift + A` sur Mac)*.
3. Dans la fenêtre qui s'ouvre, cliquez sur le bouton **Afficher les fichiers** (ou *View Files*) en bas à droite.
4. Cela ouvre le dossier des greffons Anki (`addons21`) dans votre explorateur de fichiers.

### Étape 2 : Créer le dossier pour le greffon

1. À l'intérieur du dossier `addons21`, créez un nouveau dossier.
2. Nommez ce dossier de manière explicite, par exemple : `gif_reward`.

### Étape 3 : Ajouter le fichier `__init__.py`

1. Récupérez le fichier `__init__.py` présent à la racine de ce dépôt GitHub.
2. Copiez ce fichier `__init__.py` directement dans le dossier `gif_reward` que vous venez de créer.

> **Remarque :** L'arborescence finale doit ressembler à ceci :
> ```text
> Anki2/
> └── addons21/
>     └── gif_reward/
>         └── __init__.py
> 
> ```
> 
> 

### Étape 4 : Redémarrer Anki

1. Fermez complètement l'application **Anki**.
2. Relancez **Anki**.
3. Lancez vos révisions : un GIF félicitant votre effort apparaîtra au centre de l'écran à chaque palier de 10 cartes ! 🎉
