
- [En Français](#Application-pour-filtrer,-télécharger-et-visualiser-les-données-Alouette-I)
- [In English](# Application-to-filter,-download-and-visualize-Alouette-I-data)

# Application pour filtrer, télécharger et visualiser les données Alouette-I


## Contexte

Le satellite Alouette-I (dates d'exploitation : 1962-1972) a été le premier satellite canadien lancé dans l'espace. L'objectif 
de son expérience principale était de comprendre la structure de la haute ionosphère. Les données de l'Alouette I 
Le satellite est constitué de centaines de milliers d'ionogrammes qui sont maintenant stockés numériquement sous forme de fichiers d'images. Pour comprendre les tendances en matière de 
les données des ionogrammes, il est nécessaire d'examiner les données à une grande échelle, ce qui n'est pas possible en examinant chaque ionogramme
 un à la fois. 

Ce projet est une application qui permet aux utilisateurs de filtrer les ionogrammes sur
 de multiples paramètres et télécharger soit les caractéristiques extraites des ionogrammes sélectionnés sous forme de CSV, soit les images des ionogrammes 
 eux-mêmes. L'application permet également aux utilisateurs de visualiser un résumé des données des ionogrammes qu'ils ont sélectionnés, à la fois sur 
 une carte et un graphique linéaire, en renonçant au téléchargement des données pour des aperçus simples. 

Ce projet peut être utilisé comme étude de cas pour le développement de futures applications de données satellitaires, de sorte que les données de
 de ces satellites peuvent être obtenus et analysés à une plus grande échelle et de manière plus conviviale.

## Démarrage rapide

Les commandes suivantes peuvent être exécutées plus facilement dans un environnement virtuel (comme conda). Il peut donc être judicieux d'installer [Anaconda] (https://www.anaconda.com/distribution/) au préalable. 

Git doit être installé. Sur une machine Windows, il est recommandé d'installer Git Bash et d'exécuter les commandes git depuis le terminal Git Bash.
Un compte GitLab qui se trouve sur le service Gitlab hébergé par Shared Services Canada est nécessaire pour cloner le dépôt. Un compte 
peut être créé ici : https://gccode.ssc-spc.gc.ca/.


Pour démarrer l'application :

        pip install -r requirements.txt
        python app.py

Des instructions d'installation distinctes pour la version de production de l'application sont fournies dans le "Guide d'installation de l'application Alouette Production.docx".

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


## Accessibilité et image de marque
 - En raison des [exigences relatives à la marque Canada.ca] (https://wet-boew.github.io/themes-dist/GCWeb/index-en.html), une grande partie du CSS de l'application devra être modifiée et l'en-tête et le pied de page du gouvernement du Canada devront être ajoutés
    - Les exigences du gouvernement du Canada seront plus strictes lorsque le site Web de la CSA sera fusionné avec Canada.ca en mars 2020
    - Pour plus d'informations sur l'image de marque du gouvernement du Canada, cliquez ici : [http://livelink/livelink/llisapi.dll?func=ll&objId=43843079&objAction=viewheader](http://livelink/livelink/llisapi.dll?func=ll&objId=43843079&objAction=viewheader)
 - En raison de la [norme du gouvernement du Canada sur l'accessibilité du Web] (https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=23601), il faudra probablement apporter des modifications au frontal ou au CSS
    - Le [Web Experience Toolkit] (https://wet-boew.github.io/v4.0-ci/index-en.html) peut être utilisé pour aider à atteindre cette norme, mais il n'est pas nécessaire
    - Vous trouverez ici d'autres notes sur l'accessibilité : [http://livelink/livelink/llisapi.dll?func=ll&objId=43801583&objAction=viewheader]([http://livelink/livelink/llisapi.dll?func=ll&objId=43801583&objAction=viewheader])
 
Il faudra apporter des modifications à app.py pour changer les couleurs et les styles des visualisations interactives ainsi que la mise en page HTML de la page. La plupart des autres changements seront simplement des CSS.

## En-tête/pied de page

- Le code de l'en-tête/du pied de page du gouvernement est enregistré dans un fichier séparé (header_footer.py), et est directement injecté dans l'application du tiret.

## Traductions

 - Les traductions sont délicates avec Dash en raison de la façon dont il rend la page. Pour savoir comment faire de nouvelles traductions, consultez [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n]([https://blog.miguelgrinberg.com/post/the-flask-

Traduit avec www.DeepL.com/Translator (version gratuite)



# Application to filter, download and visualize Alouette-I data


## Background

The Alouette-I satellite (dates of operation: 1962-1972) was the first Canadian satellite launched into space. The goal 
of its main experiment was to understand the structure of the upper ionosphere. The data from the Alouette I 
satellite consists of hundreds of thousands of ionograms now stored digitally as image files. To understand trends in 
the ionogram data, it is necessary to examine the data at a large scale that is not possible by looking at each ionogram
 one at a time. 

This project is an application that allows users to filter through ionograms on
 multiple parameters and download either the selected ionograms’ extracted features as a CSV or the ionogram images 
 themselves. The application also allows users to visualize a summary of the data from their selected ionograms on both 
 a map and a line chart, forgoing the need for downloading the data for simple insights. 

This project can be used as a case study for the development of future satellite data applications so that the data from
 from these satellites are able to be obtained and analyzed at a larger scale and in a more user-friendly way.

## Quick start

The following commands can be done more easily if in a virtual environment (like conda) so it may be a good idea to install [Anaconda](https://www.anaconda.com/distribution/) beforehand. 

Git must be installed. On a Windows machine, installing Git Bash and running git commands from the Git Bash terminal is recommended.
A GitLab account that is on the Shared Services Canada-hosted Gitlab service is required to clone the repository. An 
account can be created here: https://gccode.ssc-spc.gc.ca/.


For starting the application:

        pip install -r requirements.txt
        python app.py

Separate installation instructions for the production version of the app are provided in "Alouette Production Installation Guide.docx".

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


## Accessibility and branding
 - Due to [Canada.ca branding requirements](https://wet-boew.github.io/themes-dist/GCWeb/index-en.html), much of the CSS of the application will need to be changed and the Government of Canada header and footer will need to be added
    - There will be stricter Government of Canada requirements when the CSA website gets merged with Canada.ca in March of 2020
    - More note on Government of Canada branding can be found here: [http://livelink/livelink/llisapi.dll?func=ll&objId=43843079&objAction=viewheader](http://livelink/livelink/llisapi.dll?func=ll&objId=43843079&objAction=viewheader)
 - Due to the [Government of Canada Standard on Web Accessibility](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=23601), there will likely need to be changes to the frontend or CSS
    - The [Web Experience Toolkit](https://wet-boew.github.io/v4.0-ci/index-en.html) can be used to help reach this standard, but it is not necessary
    - More notes on accessibility can be found here: [http://livelink/livelink/llisapi.dll?func=ll&objId=43801583&objAction=viewheader]([http://livelink/livelink/llisapi.dll?func=ll&objId=43801583&objAction=viewheader])
 
There will need to be changes in app.py to change colours and styles of the interactive visualizations as well as the HTML layout of the page. Most other changes will just be CSS.

## Header/Footer

- The government header/footer code is saved in a separate file (header_footer.py), and is directly injected into the dash app.

## Translations

 - Translations are tricky with Dash due to the way it renders the page. To learn how to make new translations, consult [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n]([https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n])

 - Each text element to be translated in dash has to be given a component ID (see Dash documentation for more details on this). The component is subsequently re-rendered on language switch. 

## Downloads

- The max number of ionograms that can be downloaded at once is 100 as of now. These ionograms are currently stored in memory before being sent to the user as a zip; this method may fail for a larger download.

## Roadmap

The current and previous roadmaps can be found on livelink for reference:
[http://livelink/livelink/llisapi.dll?func=ll&objId=39628342&objAction=viewheader]([http://livelink/livelink/llisapi.dll?func=ll&objId=39628342&objAction=viewheader])



## Authors
 - Hansen Liu
 - Wasiq Mohammmad


## Acknowledgments
 - Etienne Low-Decarie
 - Jenisha Patel
 - Cooper Ang
