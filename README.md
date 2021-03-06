# TeamLab

![N|Solid](https://le-datascientist.fr/wp-content/uploads/2019/02/logo-apache-spark.png) ![N|Solid](https://lucasvidelaine.files.wordpress.com/2018/10/postgresql2.png?w=600)![N|Solid](https://user.oc-static.com/upload/2019/05/10/15574814980481_Docker-660x269.png)

## Intrdoduction

L'objectif de ce projet est de mettre en place une application permettant de traiter un grand volume de données avec Spark **Pyspark**.
Les données sont téléchargées via les liens suivants:
* [StockUniteLegaleHistorique_utf8.zip](https://files.data.gouv.fr/insee-sirene/StockUniteLegaleHistorique_utf8.zip)
* [StockUniteLegale_utf8.zip](https://files.data.gouv.fr/insee-sirene/StockUniteLegale_utf8.zip)

Les données proviennent de l'insee et recensent les Sirene des entreprises et de leurs établusssments (SIREN, SIRET)

Nous utilisons **Postgres** pour stocker les données après le préprocessing. Et une **API** qui prend la Siren comme paramètre et qui renvoie les informations associées.
## Prerequis
Pour pourvoir utiliser cette application il faut avoir installer **Docker** et l'outil **docker-compose**
## Services
Le projet utilse trois services :
### Pyspark
Au lancement de ce container, un script Preprocess.py sera executé. Ce script téléchargera les données en question puis exécutera l'ensemble des transformatons avant de charger la nouvelle table ( jointure des deux tables) dans la base de données postgres.
### Postgres
Une base de données pour stocker les données traitées dans la partie précédente. 

### Django
Nous utilisons **Django REST framework** pour créer une API . L'API prendera en paramètre le siren et retournera les informations correspondantes. 

## Installation et démarrage
Pour installer et démarrer l'application:

$ cd PathFolderApplication
$ docker-compose build # Faire un build des images
$ docker-compose up # Démarrer les containers

## Pour interroger la base de données 
Nous utilisons Postman : 
la reqûete à saisir est la suivante : 
[GET] http://localhost:8000/api/unitelegales/"N°Siren"
Cette reqûete fait invoque la méthide unitelegales qui renvoie un JSON de toutes lignes ayant le Siren donné en paramètre.
