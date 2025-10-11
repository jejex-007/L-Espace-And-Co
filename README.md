# L'Espace & Co. - Plateforme de Réservation

## 📋 À propos du projet

**L'Espace & Co.** est une application web conçue pour la gestion d'un espace de coworking innovant dédié aux coiffeurs indépendants. La plateforme permet aux professionnels de réserver leur poste de travail en toute autonomie, de payer en ligne et de recevoir un accès numérique sécurisé (QR code) pour contrôler les ressources de l'espace (accès, électricité, eau) pour la durée de leur location.

## 🛠️ Stack Technique

* **Back-end :** Python 3 avec le micro-framework Flask.
* **Front-end :** HTML5, CSS3, Bootstrap 5.
* **JavaScript :** FullCalendar.js pour le calendrier de réservation.
* **Base de Données :** SQLite.

## 🚀 Installation et Lancement Local (Windows)

1.  **Créez un environnement virtuel :**
    `powershell
    python -m venv venv
    `

2.  **Activez l'environnement virtuel :**
    `powershell
    .\venv\Scripts\Activate.ps1
    `
    *Note : Si vous rencontrez une erreur d'exécution de script, lancez d'abord cette commande : Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process*

3.  **Installez les dépendances :**
    `powershell
    pip install -r requirements.txt
    `

4.  **Lancez l'application :**
    `powershell
    flask run
    `
    L'application sera accessible à l'adresse [http://127.0.0.1:5000](http://127.0.0.1:5000).
