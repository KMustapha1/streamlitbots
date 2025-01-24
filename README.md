# streamlitbots

## Groupe:
    * KHELFA Mustapha
    * TOHNGODO Ines
    * TOHNGODO Maelisse

# Comment récupérer le projet et l'exécuter ?


1. Installer les outils nécessaires
Avant de commencer, assurez-vous d'avoir ces deux outils installés sur votre ordinateur :

Git : pour télécharger le projet. Téléchargez-le ici : https://git-scm.com/
Python : pour exécuter le code. Téléchargez-le ici : https://www.python.org/downloads/

2. Télécharger le projet

#### Ouvrez une fenêtre de Terminal (ou Invite de commandes sur Windows).

#### Tapez la commande suivante pour télécharger le projet :
git clone https://github.com/KMustapha1/streamlitbot.git

#### Cela téléchargera les fichiers du projet dans un nouveau dossier nommé streamlitbot.

#### Entrez dans le dossier du projet :

cd streamlitbot

#### Vérifiez les fichiers téléchargés :

Si certains fichiers (comme .streamlit/secrets.toml ou requirements.txt) semblent manquants ou incomplets, ouvrez-les et corrigez-les en les copiant directement depuis le dépôt GitHub.

3. Créer un environnement Python

#### Un environnement Python est comme un espace isolé où seules les dépendances nécessaires à ce projet sont disponibles.

#### Créez un environnement virtuel en tapant :

python -m venv stenv

#### Activez l’environnement virtuel :

#### Sur Windows :
stenv\Scripts\activate

#### Sur macOS/Linux :
source stenv/bin/activate

Une fois l’environnement activé, vous verrez quelque chose comme (stenv) avant votre invite de commande.

4. Installer les dépendances nécessaires au projet
#### Installez les bibliothèques nécessaires avec la commande :
pip install -r requirements.txt

#### Vérifiez l’installation des dépendances : Si une bibliothèque manque ou si des erreurs apparaissent, ouvrez le fichier requirements.txt et corrigez-le si nécessaire en ajoutant manuellement les bibliothèques requises, comme :

streamlit
openai

#### Puis réessayez la commande :

pip install -r requirements.txt

5. Recréer les fichiers manquants

#### Si les fichiers cachés (comme .streamlit/secrets.toml) n'ont pas été téléchargés correctement :

#### Créez le dossier .streamlit :

mkdir .streamlit

#### Créez le fichier secrets.toml à l'intérieur :

touch .streamlit/secrets.toml

#### Ajoutez votre clé API dans le fichier secrets.toml :

#### Ouvrez le fichier avec un éditeur de texte :

nano .streamlit/secrets.toml

#### Ajoutez le contenu suivant (remplacez votre_cle_api_openai par votre clé OpenAI) :

[OPENAI_API_KEY]
key = "votre_cle_api_openai"

#### Sauvegardez et fermez le fichier.

6. Lancer l'application

#### Lancez l'application Streamlit en tapant :

streamlit run chatbot.py

#### ou :

streamlit run chatbotgpt.py

#### Une page web s'ouvrira automatiquement dans votre navigateur à l'adresse http://localhost:8501. Si ce n'est pas le cas, copiez-collez l'URL affichée dans le terminal.

7. Résolution des problèmes courants

#### Fichiers manquants : Si des fichiers essentiels comme .streamlit/secrets.toml ou requirements.txt ne sont pas présents ou sont incomplets, vérifiez sur le dépôt GitHub et copiez-les manuellement.

#### Erreur de dépendances : Si une bibliothèque manque, installez-la directement avec pip install nom_de_la_bibliotheque.

#### Clé API manquante ou invalide : Vérifiez que vous avez une clé API OpenAI valide et qu'elle est correctement configurée dans .streamlit/secrets.toml.   