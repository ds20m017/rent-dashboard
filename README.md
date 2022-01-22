# Rent-dashboard

# Wohnsituation Österreich

Wohnen ist ein zentrales Thema in jedem Industriestaat. Wachsende Bevöklerung bei gleichbleibende Verfügbarkeit der Fläche führt zu einer Knappheit an Wohnraum. 
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

![image](https://user-images.githubusercontent.com/46869155/150642828-a855c4a4-def8-4b78-ac3c-a7d894284fe1.png)

Dabei kann zwischen verschiedenen Bundesländer unterschieden werden. Einige Berechnungen sind vorab schon fixiert.

Technsich befindet sich das ganze im frontend Folder.

## Backend

Das Backend ist über http://rent-dashboard-backend.azurewebsites.net/ erreichbar.

Folgende Endpoint existieren:

* /averageSpace
* /averagePrice
* /averagePricePerMeter
* /averageRooms
* /medianPriceLegal
* /medianPriceLegalPerMeter
* /predictPrice mit Variablen
  * state
  * size
