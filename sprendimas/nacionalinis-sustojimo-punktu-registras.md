# Nacionalinis stotelių registras

Nacionalinis stotelių registras - tai duomenų bazė, kurioje yra saugoma informacija apie visas
šalyje esančius viešojo transporto sustojimo punktus (stoteles).

Tokia duomenų bazė padeda išvengti stotelių duplikavimo tarp transporto paslaugų teikėjų, suteikia galimybę
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

### Stotelės iš savivaldybių GTFS duomenų rinkinių

Dalis savivaldybi duomenų į VINTRA yra importuojami automatiškai. Kartu su GTFS failais į VINTRA patenka ir
savivaldybių stotelės. Toliau esančioje lentelėje vaizduojama kiek stotelių turi savivaldybių GTFS failai.

```{table} Stotelių kiekis skirtingų savivaldybių GTFS failuose (2022-07-27)

| Savivaldybė       | Stotelių kiekis |
|-------------------|-----------------|
| Vilniaus m. sav.  | 1503            |
| Kauno m. sav.     | 886             |
| Klaipėdos m. sav. | 652             |
| Šiaulių m. sav.   | 490             |
| Panevėžio m. sav. | 236             |
| Alytaus m. sav.   | 196             |
| Druskininkų sav.  | 149             |
```

### Stotelių išvestis iš VINTRA

#### GTFS

```{table} VINTRA GTFS duomenų rinkinio pavyzdys
|   stop_id | stop_name   |   stop_lat |   stop_lon | stop_code   | stop_desc   |   zone_id | stop_url                                               | location_type   | parent_station   | wheelchair_boarding   | stop_direction   | stop_timezone   | vehicle_type   | platform_code   |
|----------:|:------------|-----------:|-----------:|:------------|:------------|----------:|:-------------------------------------------------------|:----------------|:-----------------|:----------------------|:-----------------|:----------------|:---------------|:----------------|
|     14146 | Pakuršėnis  |    56.0177 |    22.9544 |             |             |     14146 | http://www.visimarsrutai.lt/#/stop/result?stopId=14146 |                 |                  |                       |                  |                 |                |                 |
|     14165 | Šakyna      |    56.1809 |    23.1237 |             |             |     14165 | http://www.visimarsrutai.lt/#/stop/result?stopId=14165 |                 |                  |                       |                  |                 |                |                 |
|     14172 | Micaičiai   |    55.9729 |    22.9161 |             |             |     14172 | http://www.visimarsrutai.lt/#/stop/result?stopId=14172 |                 |                  |                       |                  |                 |                |                 |
|     14675 | Gedinčiai   |    56.0345 |    22.9309 |             |             |     14675 | http://www.visimarsrutai.lt/#/stop/result?stopId=14675 |                 |                  |                       |                  |                 |                |                 |
|     15298 | Sutkūnai    |    55.9744 |    23.3285 |             |             |     15298 | http://www.visimarsrutai.lt/#/stop/result?stopId=15298 |                 |                  |                       |                  |                 |                |                 |
```

#### NeTEx

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:ns2="http://www.opengis.net/gml/3.2"
                     xmlns:ns3="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                     version="1" xsi:schemaLocation="">
    <PublicationTimestamp>2022-07-23T00:40:00.238</PublicationTimestamp>
    <ParticipantRef>VTR</ParticipantRef>
    <dataObjects>
        <SiteFrame modification="new" version="1" id="VTR:SiteFrame:2229">
            <FrameDefaults>
                <DefaultLocale>
                    <TimeZone>Europe/Vilnius</TimeZone>
                </DefaultLocale>
                <DefaultLocationSystem>WGS84</DefaultLocationSystem>
            </FrameDefaults>
            <stopPlaces>
                <StopPlace created="2015-05-25T16:19:43" changed="2019-05-11T02:15:34" modification="revise"
                           version="10024" id="VTR:StopPlaceElement:10024">
                    <ValidBetween>
                        <FromDate>2019-05-11T02:15:34</FromDate>
                    </ValidBetween>
                    <keyList>
                        <KeyValue>
                            <Key>DATA_SOURCE_TYPE</Key>
                            <Value>LAKIS</Value>
                        </KeyValue>
                    </keyList>
                    <Name lang="lt">Pušalotas</Name>
                    <Centroid>
                        <Location>
                            <Longitude>24.240047</Longitude>
                            <Latitude>55.936714</Latitude>
                        </Location>
                    </Centroid>
                    <TransportMode>bus</TransportMode>
                    <StopPlaceType>onstreetBus</StopPlaceType>
                    <Weighting>interchangeAllowed</Weighting>
                    <quays>
                        <Quay modification="new" version="10024" id="VTR:Quay:10024">
                            <Centroid>
                                <Location>
                                    <Longitude>24.240047</Longitude>
                                    <Latitude>55.936714</Latitude>
                                </Location>
                            </Centroid>
                        </Quay>
                    </quays>
                </StopPlace>
            </stopPlaces>
        </SiteFrame>
    </dataObjects>
</PublicationDelivery>
```

## Problemos ir galimybės

### Stotelių duomenų rinkinys

Nei iš VINTRA, nei iš LAKIS negalima pasiimti visų Lietuvoje esančių stotelių (apimančių pilną stotelių informaciją).
VINTRA NeTEx ir GTFS duomenų rinkiniuose atiduodamos tik stotelės turinčios priskirtų maršrutų.

### Prieinamumo informacija

VINTRA negražina jokios informacijos apie stotelės prieinamumą (GTFS atributas _wheelchair_boarding_,
NeTEx _AccessibilityAssessment_). Dėl šios priežasties Ssecialiųjų poreikių turinčių žmonių susisiekimas viešuoju
transportu yra apsunkinamas.

### Išvykimo aikštelė ar platforma

VINTRA tolimojo susisiekimo maršrutai yra susisiejami su stotimis. Toks susiejimas keleiviui nesuteikia informacijos
apie tai į kurią aikštelę atvyks tolimojo susisiekimo autobusas (analogiškai nėra informacijos ir apie traukinių
platformas).

```{figure} ../images/sprendimai/stoteles/vilniaus-autobusu-stotis-aiksteles.jpg

Vilniaus autobusų stoties aikštelės. [Šaltinis](https://www.lrytas.lt/auto/rinka/2022/01/19/news/spaudziant-11-laipsniu-salciui-autobusu-dvi-valandas-keliavo-be-sildymo-bendrove-paaiskino-kas-nutiko-22094617)
```

```{figure} ../images/sprendimai/stoteles/google-maps-platform-information.png

Google Maps išvykimo platformos informacija Londoje, Jungtinėje Karalystėje
```

### Stotelės krypties nustatymas

Tokio paties stotelės pavadinimo abiejose kelio pusėse atveju yra

## Sustojimo punktų modeliavimas

Stotelių registras turėtų būti modeliuojamos pagal Transmodel ir NeTEx duomenų modelį.

```{figure} ../images/sprendimai/stoteles/netex/stopplace-datamodel.png

NeTEx duomenų modelis sustojimo punktui (angl. _stop place_). [Šaltinis](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728596522/Data+models#Stops)
```

### Punktas (StopPlace)

Sustojimas apibrėžiamas pavadinimu, transporto ir sustojimo vietos tipu bei turi turėti apibrėžtą prieinamumo
informaciją.

```xml Hello

<StopPlace version="any" id="NSR:StopPlace:10000000">
    <!-- Punkto pavadinimas (VINTRA atitikmuo) -->
    <Name>Fabijoniškės</Name>
    <!-- Sustojimo prieinamumo informacija: punktas prieinamas asmeniui   -->
    <AccessibilityAssessment version="any" id="NSR:AccessibilityAssessment:1">
        <MobilityImpairedAccess>true</MobilityImpairedAccess>
        <limitations>
            <!-- Minimum requirements to UU-information -->
            <AccessibilityLimitation>
                <WheelchairAccess>true</WheelchairAccess>
                <StepFreeAccess>true</StepFreeAccess>
            </AccessibilityLimitation>
        </limitations>
    </AccessibilityAssessment>
    <Covered>outdoors</Covered>
    <placeEquipments>
        <PassengerInformationEquipment id="NSR:PassengerInformationEquipment" version="any">
            <PassengerInformationFacilityList>passengerInformationDisplay</PassengerInformationFacilityList>
        </PassengerInformationEquipment>
        <GeneralSign id="NSR:GeneralSign:1" version="any">
            <PrivateCode>512</PrivateCode>
            <SignContentType>transportMode</SignContentType>
        </GeneralSign>
    </placeEquipments>
    <TransportMode>bus</TransportMode>
    <StopPlaceType>onstreetBus</StopPlaceType>
    <quays>
        <!--- see its own description below -->
    </quays>
</StopPlace>
```

- Punktas ([StopPlace](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728727661/stops#StopPlace)) -
- Punkto vieta ([Quay](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728727661/stops#Quay)) - tiksli vieta, 
  kurioje transporto priemonės sustoja, o keliautojai įlipa arba išlipa;