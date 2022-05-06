# GTFS

GTFS (*General Transit Feed Specification*) yra ypač plačiai naudojamas standartas skirtas pateikti viešojo transporto
statinę informaciją. Šis formatas yra naudojamas ne tik daugybės transporto paslaugų teikėjų visame pasaulyje, tačiau ir
visų populiariausių kelionių planavimo priemonių (pvz., Google Maps Transit, Apple Maps Transit).

## Struktūra

GTFS duomenų rinkinys būna suspaustas į `.zip` failą susidedantį iš keleto `.csv` kablelių atskirtų failų. Kiekviename
iš failų saugoma informacija apie konkretų transporto sistemos elementą pvz., stoteles, maršrutus, reisus, tvarkaraštį
ir pnš.

Toliau detaliai aprašomas kiekvienas GTFS duomenų rinkinio failai{cite}`google_gtfs_reference`.

```{table} GTFS duomenų rinkinio failai
:name: gtfs-files

| Failas                                                                                           | Privalomumas         | Aprašymas                                                          |
|--------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------|
| [`agency.txt`](https://developers.google.com/transit/gtfs/reference#agencytxt)                   | Privalomas           | Informacija apie transporto paslaugų teikėjus.                     |
| [`stops.txt`](https://developers.google.com/transit/gtfs/reference#stopstxt)                     | Privalomas           | Stotelių informacija.                                              |
| [`routes.txt`](https://developers.google.com/transit/gtfs/reference#routestxt)                   | Privalomas           | Maršrutų informacija.                                              |
| [`trips.txt`](https://developers.google.com/transit/gtfs/reference#tripstxt)                     | Privalomas           | Reisų informacija.                                                 |
| [`stop_times.txt`](https://developers.google.com/transit/gtfs/reference#stop_timestxt)           | Provalomas           | Laikai, kada transporto priemonė atvyksta ir išvyksta iš stotelių. |
| [`calendar.txt`](https://developers.google.com/transit/gtfs/reference#calendartxt)               | Sąlyginai privalomas | Informacija kada paslauga yra teikiama.                            |
| [`calendar_dates.txt`](https://developers.google.com/transit/gtfs/reference#calendar_datestxt)   | Sąlyginai privalomas | Aprašo kada transporto paslaugos nėra teikiamos.                   |
| [`feed_info.txt`](https://developers.google.com/transit/gtfs/reference#feed_infotxt)             | Sąlyginai privalomas | Duomenų šaltinio informacija.                                      |
| [`fare_attributes.txt`](https://developers.google.com/transit/gtfs/reference#fare_attributestxt) | Neprivalomas         | Bilietų kainodaros informacija.                                    |
| [`fare_rules.txt`](https://developers.google.com/transit/gtfs/reference#fare_rulestxt)           | Neprivalomas         | Taisyklės aprašančios kainodaros taikymą.                          |
| [`shapes.txt`](https://developers.google.com/transit/gtfs/reference#shapestxt)                   | Neprivalomas         | Maršruto nubrėžimui žemėlapyje reikalinga informacija.             |
| [`frequencies.txt`](https://developers.google.com/transit/gtfs/reference#frequenciestxt)         | Neprivalomas         | Aprašo intervalinius maršrutus.                                    |
| [`transfers.txt`](https://developers.google.com/transit/gtfs/reference#transferstxt)             | Neprivalomas         | Taisyklės aprašančios persėdimus tarp maršrutų.                    |
| [`pathways.txt`](https://developers.google.com/transit/gtfs/reference#pathwaystxt)               | Neprivalomas         | Aprašo kelius jungiančius stoteles.                                |
| [`levels.txt`](https://developers.google.com/transit/gtfs/reference#levelstxt)                   | Neprivalomas         | Aprašo skirtingi stoties lygiai.                                   |
| [`translations.txt`](https://developers.google.com/transit/gtfs/reference#translationstxt)       | Neprivalomas         | Vertimai į kitas kalbas.                                           |
| [`attributions.txt`](https://developers.google.com/transit/gtfs/reference#attributionstxt)       | Neprivalomas         | Nurodo papildomus duomenų rinkinio atributus.                      |
```

### Ryšiai tarp duomenų rinkinio failų

```{figure} /images/standartai/gtfs/gtfs-files-relationship.png
:name: gtfs-files-relationships

Ryšiai tarp GTFS duomenų rinkinio failų{cite}`gtfs_files_relationshop`
```