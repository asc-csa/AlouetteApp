

![alouette satellite](alouette.jpg)

- [En Français](#Application-pour-filtrer,-télécharger-et-visualiser-les-données-Alouette-I)
- [In English](#application-to-filter--download-and-visualize-alouette-i-data)

# Application pour filtrer, télécharger et visualiser les données Alouette-I


## Contexte

Le satellite [Alouette-I](https://www.asc-csa.gc.ca/fra/satellites/alouette.asp) a été le premier satellite canadien lancé dans l'espace en 1962.  Lancés en 1969 et 1971, les satellites canadiens ISIS ont servi à l'étude de l'ionosphère et des aurores boréales. Les satellites du programme canadien ISIS ont envoyé des ondes radio de différentes fréquences dans la couche supérieure de l'atmosphère, connue sous le nom d'ionosphère, et a recueilli des données sur la profondeur de pénétration de ces ondes. Les résultats de ces expériences ont été envoyés à des stations terrestres dans le monde entier et stockés sous la forme de films, dont une portion est maintenant numérisée. 

![ionogram](ionogram.png)

Ce projet est une application qui permet aux utilisateurs de filtrer les ionogrammes sur de multiples paramètres et télécharger soit les données extraites des ionogrammes sélectionnés sous forme de CSV, soit les images des ionogrammes eux-mêmes. L'application permet également aux utilisateurs de visualiser un résumé des données des ionogrammes qu'ils ont sélectionnés, à la fois sur une carte et un graphique linéaire, évitant ainsi le téléchargement des données pour des aperçus simples. 

Vous pouvez accéder à cette micro application en direct au https://donnees-data.asc-csa.gc.ca/alouette-fr. 

![interface de l'application](appinterface.png)


## Dépendances
L'application repose sur l'architecture [App-Launcher](https://github.com/asc-csa/App-Launcher). Cette application doit être installée en premier lieu.

## Démarrage rapide

Les commandes suivantes peuvent être exécutées plus facilement dans un environnement virtuel (comme conda). Il peut donc être judicieux d'installer [Anaconda] (https://www.anaconda.com/distribution/) au préalable. 

Pour démarrer l'application :

- Créer un dossier nommé "data" et y ajouter le fichier "final_alouette_data.csv". Vous devrez aussi ajouter le fichier "config.cfg" dans le même dossier que "alouette.py". Vous trouverez ce fichier sur [Livelink](http://livelink/livelink/llisapi.dll?func=ll&objId=36908608&objAction=browse&viewType=1).

        pip install -r requirements.txt
        python alouette.py

Lors de l'exécution, l'[application locale](http://127.0.0.1:8888/alouette/) se trouve à cet endroit. Des instructions d'installation distinctes pour la version de production de l'application sont fournies dans le "Guide d'installation de l'application Alouette Production.docx".

## Construit avec

 - [Plotly Dash](https://dash.plot.ly/) - Le framework Python construit sur Flask a été utilisé pour développer l'application. Tous les composants et visualisations de l'application web sont des objets Dash qui sont créés et mis à jour dans les fonctions de rappel de l'application. Je vous recommande de consulter la documentation complète de Dash (lien) si vous n'êtes pas sûr de son fonctionnement.
 
 - [Jupyter Notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) - Utilisé pour le nettoyage des données. 


## Navigation et fichiers

 - app.py est l'application principale où chaque composant et la présentation de l'application sont définis 
 
 - controls.py contient les options pour certains des composants (par exemple, les dropdowns)

- header_footer.py contient le html pour l'en-tête et le pied de page du gouvernement du Canada. Ce html est injecté dans l'application principale.
 
 - /assets contient différents fichiers pour le style de l'application (images, redimensionnement, css)
 
 - /data contient les données csv traitées provenant du pipeline d'extraction des caractéristiques

 - /data_cleaning contient des carnets jupyter utilisés pour nettoyer les données ionogrammes extraites

 - messages.pot et /translations contient des informations sur la traduction

 - config.py précise les langues disponibles pour la traduction


## Téléchargements

Le nombre maximum d’ionogrammes pouvant être téléchargés est limité à 100. Ces ionogrammes sont actuellement stockés en mémoire avant d'être envoyés à l'utilisateur sous forme d’un fichier ZIP. Cette méthode peut échouer pour un téléchargement plus volumineux.

## Version
Ceci est la version 1.0. 

## Traductions

 - Les traductions sont délicates avec Dash en raison de la façon dont il rend la page. Pour savoir comment faire de nouvelles traductions, consultez [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n]([https://blog.miguelgrinberg.com/post/the-flask-

Traduit avec www.DeepL.com/Translator (version gratuite)


## Auteurs
 - Emiline Filion
 - Hansen Liu
 - Wasiq Mohammmad
 - Cole DeMan


## Remerciements
 - Etienne Low-Decarie
 - Jenisha Patel
 - Cooper Ang



# Application to filter, download and visualize Alouette-I data


## Background

The [Alouette-I satellite](https://www.asc-csa.gc.ca/eng/satellites/alouette.asp) was the first Canadian satellite launched into space in 1962. Launched in 1969 and 1971, Canada's International Satellites for Ionospheric Studies (ISIS) satellites were used to study the ionosphere and the aurora borealis. ISIS satellites sent radio waves of different frequencies into the topmost layer of the atmosphere, known as the ionosphere, and collected data on the depth of penetration of these waves. The results of this were sent to ground stations around the world and stored on films, a portion of which have now been digitized.

![ionogramme](ionogram.png)

This project is an application that allows users to filter through ionograms on multiple parameters and download either the selected ionograms’ extracted features as a CSV or the ionogram images  themselves. The application also allows users to visualize a summary of the data from their selected ionograms on both a map and a line chart, forgoing the need for downloading the data for simple insights. 

The live version of this micro application is available at https://donnees-data.asc-csa.gc.ca/alouette.

![app interface](appinterface_fr.png)


## Dependancies
This application is based on [App-Launcher](https://github.com/asc-csa/App-Launcher). Make sure to install App-Launcher before moving on with Alouette.

## Quick start

The following commands can be done more easily if in a virtual environment (like conda) so it may be a good idea to install [Anaconda](https://www.anaconda.com/distribution/) beforehand. 


For starting the application:
- Create a folder named "data" and add the file "final_alouette_data.csv". You will also have to add the "config.cfg" file to the same folder as the "alouette.py" file.You can find this file on [Livelink](http://livelink/livelink/llisapi.dll?func=ll&objId=36908608&objAction=browse&viewType=1).

        pip install -r requirements.txt
        python alouette.py

This is the [local instance of the application](http://127.0.0.1:8888/alouette/). Separate installation instructions for the production version of the app are provided in "Alouette Production Installation Guide.docx".

This application also requires a customized version of dash-core-components, without it the application will not meet Accessibility guidelines and may encounter errors when you attempt to run it.

The customized version of dash-core-components can be found here: https://github.com/asc-csa/dash-core-components

Once you have downloaded the repository, enter the directory. From there copy `dash_core_components` to your `site-packages` directory within your python installation and replace the existing dash-core-components directory. If you followed the directions above and used conda you will find `site-packages` in this location:
`/home/<your_username>/anaconda3/lib/python3.8/site-packages`

## Built with

 - [Plotly Dash](https://dash.plot.ly/) - The Python framework built on top of Flask used to develop the application. All components and visualizations on the web application are Dash objects that are created and updated in the callback functions in app.py. I would recommend that you look over Dash's comprehensive documentation (linked) if you are unsure how it works.
 
 - [Jupyter Notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) - Used for data cleaning. 


## Navigation and files

 - app.py is the main application where each component and the layout of the application is defined 
 
 - controls.py contains the options for the some of the components (e.g. dropdowns)

- header_footer.py contains the html for the government of Canada header and footer. This html is injected into the main app.
 
 - /assets contains various files for the styling of the application (images, resizing, css)
 
 - /data contains the processed csv data from the feature extraction pipeline

 - /data_cleaning contains jupyter notebooks used to clean the extracted ionogram data

 - messages.pot and /translations contains translation information

 - config.py specifies the languages available for translation



## Downloads

The maximum number of ionograms that can be downloaded at once is 100 as of now. These ionograms are currently stored in memory before being sent to the user as a zip; this method may fail for a larger download.

## Version
This is version 1.0. 


## Authors
 - Emiline Filion
 - Hansen Liu
 - Wasiq Mohammmad
 - Cole DeMan


## Acknowledgments
 - Etienne Low-Decarie
 - Jenisha Patel
 - Cooper Ang
