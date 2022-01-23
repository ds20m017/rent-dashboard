# Rent-dashboard

# Wohnsituation Österreich

Wohnen ist ein zentrales Thema in jedem Industriestaat. Wachsende Bevölkerung bei gleichbleibende Verfügbarkeit der Fläche führt zu einer Knappheit an Wohnraum. 
Der Wohnraum ist ein wesentlicher Bestandteil des Lebensstandard der Menschen. Insofern werden in regelmäßigen Abständen Berichte über die aktuelle Situation veröffentlicht:

https://www.derstandard.at/story/2000132589738/mietenanstieg-im-vorigen-jahrzehnt-doppelt-so-stark-wie-inflation

https://oesterreich.orf.at/stories/3138925/

## Zielsetzung

Das Ziel ist es, einen **dauerhaften** Überblick über die Wohnsitutation von Österreich. Es soll zu jederzeit möglich sein, ein Einblick über die Situation von Österreich zu bekommen, anstatt auf unregelmäßig erscheinende Berichte mit unbekannter Gültigkeitsdauer zurückgreifen zu müssen.


## Methodik

Die Zielsetzung wird durch ein interaktives Dashboard erfüllt. 

Die Daten für dieses Dashboard werden von eine REST API https://rent-dashboard-backend.azurewebsites.net/ bezogen.


## Frontend 

Das Frontend ist interaktiv und kann über http://rent-dashboard.azurewebsites.net/ erreicht werden.

![image](https://user-images.githubusercontent.com/46869155/150642660-43ef15bb-4cfd-46fb-89f3-6b8c51a6f5dd.png)

Es kann ein Zoom in oder Zoom out in den Grafiken durchgeführt werden und über die Dropdowns können verschiedene Kategorien selektiert werden.

Über das ML-Modell kann eine ungefähre Vorhersage über die monatlichen Kosten, abhängig von der qm Anzahl getroffen werden:

![image](https://user-images.githubusercontent.com/46869155/150684970-2693dbd2-4f30-4d98-92e6-f2254d07b745.png)


Dabei kann zwischen verschiedenen Bundesländer unterschieden werden. Einige Berechnungen sind vorab schon fixiert.

Technisch befindet sich das ganze im frontend Folder.

## Backend

Das Backend ist über http://rent-dashboard-backend.azurewebsites.net/ erreichbar.

Folgende Endpoint existieren:

* /averageSpace
* /averagePrice
* /averagePricePerMeter
* /averageOperatingCost
* /averageOperatingCostPerMeter
* /averageRooms
* /medianPriceLegal
* /medianPriceLegalPerMeter
* /predictPrice mit Variablen
  * state
  * size
* /predictOperatingCost mit Variablen
  * state
  * size
  
## Modelle

Beide Modelle sind Regression Forest Modelle welche im Backend implemntiert sind und über die APIs predictPrice und predictOperatingCost angesteuert werden können.

* rentRegressionForest.pkl
* operatingCostRegressionForest.pkl

## Infrastructure

Github Repository: https://github.com/ds20m017/rent-dashboard

Github Action:     https://github.com/ds20m017/rent-dashboard/blob/main/.github/workflows/main.yml

Docker Frontend:         https://github.com/ds20m017/rent-dashboard/blob/main/frontend/Dockerfile 

Docker Backend:         https://github.com/ds20m017/rent-dashboard/blob/main/backend/Dockerfile    

Frontend:          http://rent-dashboard.azurewebsites.net/

Backend:           http://rent-dashboard-backend.azurewebsites.net/
