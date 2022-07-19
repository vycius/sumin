# Nacionalinis sustojimo punktų registras

Nacionalinis sustojimo punktų (stotelių) registras - tai duomenų bazė, kurioje yra saugoma informacija apie visas
šalyje esančius viešojo transporto sustojimo punktus.

Tokia duomenų bazė padeda išvengti stotelių duplikavimo tarp transporto paslaugų teikėjų, suteikia galimybę valdyti
stotelių atnaujinimo procesą (pvz., pavadinimo keitimą, stotelės vietos keitimą) valdyti vienoje vietoje ir leidžia
naujiems operatoriams lengviau planuoti bei nustatyti maršrutus. Tokius registrus
turi [Jungtinė Karalystė](https://publish.bus-data.dft.gov.uk/guidance/local-authority-requirements/?section=naptan),
[Švedija](https://www.trafiklab.se/api/trafiklab-apis/stops-data/)
, [Norvegija](https://developer.entur.org/stops-and-timetable-data) ir daugybė kitų šalių.

## Esama situacija

### VINTRA

Artimiausias nacionalinių sustojimo punktų registro atitikmuo yra VINTRA. GTFS ir NeTEx duomenų formatais galima
gauti informacija apie visas Lietuvoje egzistuojančias viešojo transporto stoteles, autobusų ir geležinkelių stotis
ir pnš.

Pagal viešojo transporto kelionių duomenų kaupimo tvarkos aprašą{cite}`sumin_vintra_duomenu_kaupimo_tvarka` su
stotelėmis, stotimis ir kitais maršruto punktais susijusią informaciją turi teikti:

- Lietuvos transporto saugos administracija;
- Lietuvos automobilių kelių direkcija;
- Savivaldybių institucijos arba jų įgaliotos įstaigos, valdančios ir organizuojančios keleivių vežimą vietinio
  (miesto ar priemiestinio) reguliariojo susisiekimo maršrutais;
- Vežėjai, teikiantys keleivių vežimo viešuoju geležinkelių transportu paslaugas;
- Vežėjai, teikiantys keleivių vežimo viešuoju vidaus vandenų transportu paslaugas;

2022 m. liepos 19 d. VINTRA buvo saugoma informacija apie 25 256 sustojimo vietas (iš jų 13 177 grįžta GTFS duomenų
rinkinyje).

### LAKIS

LAKIS sistemoje saugomos autobusų 18 022 sustojimo aikštelės esančios valstybiniuose
keliuose{cite}`lakis_autobusu_stoteles`. Iš LAKIS gražinama informacija apima kelio numerį, vietą kelyje, pusę ir 
pnš. Atvirų duomenų pavidalu iš LAKIS nėra gražinamas stotelės pavadinimas. 







