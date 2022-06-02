# Norvegija

Nacionalinis Novergijos viešojo transporto duomenų registras ([ENTUR](https://developer.entur.org/pages-intro-overview))
susideda iš daugiau nei 60 transporto operatorių, beveik 60 000 stotelių ir informacijos apie daugiau nei 3 tūkst.
maršrutų su daugiau nei 21 tūkst. kasdienių išvykimų{cite}`entur_about`. Šis registras yra valdomas „Entur AS“
bendrovės, kuri yra įkurta 2016 m. Norvegijos transporto ir ryšių ministerijos. ENTUR ne tik atsakinga už viešojo
transporto duomenis, tačiau ir valdo traukinių bilietų pardavimo sistemą bei kuria skaitmeninius produktus lengvesniam
kelionių planavimui.

## Duomenų prieinamumas

Visi duomenys yra prieinami visiškai nemokamai
pagal [Norvegijos atvirosios vyriausybės duomenų licenciją](https://data.norge.no/nlod/en/2.0/) (angl. *Norwegian
Licence for Open Government Data*).

## Nacionalinis stotelių registras

[Nacionalinis stotelių registras](https://stoppested.entur.org) yra centrinė duomenų bazė, kurioje yra saugoma su
stotelėmis susijusi informacija. Šiuos duomenis valdo savivaldybės (norv. *fylkeskommune*), o visą informaciją
administruoja ENTUR.

Pagrindinis nacionlinio stotelių registro tikslas yra išvengti stotelių duplikavimo tarp transporto paslaugų teikėjų ir
padėti naujiems operatoriams lengviau planuoti bei nustatyti maršrutus. Tai užtikrina, kad visi duomenų teikėjai ir
transporto operatoriai į ENTUR teikia duomenis su tais pačiais stotelių identifikatoriais. Pagrindinė registre saugoma
informacija yra stotelės identifikatorius, pavadinimas, geografinė padėtis, tačiau taip pat tvarkomi ir kiti duomenys,
pvz., stotelės prieinamumas asmeniui turinčiam judėjimo negalią.

```{figure} ../images/gerosios-praktikos/norvegija/entur-stop-registry.png
:name: entur-stop-registry

Novergijos nacionalinis stotelių registras.
```

## Statiniai duomenys

Statiniai duomenys yra prieinami tiek NeTEx, tiek GTFS formatais. GTFS formatas turi du tipus: „pilną“ (angl. *
extended*) ir pagrindinį (angl. *basic*). Visi duomenų teikėjai privalo teikti statinius duomenis NeTEx formatu
pagal [Norvegišką NeTEX profilį](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile).

[ENTUR](https://developer.entur.org/stops-and-timetable-data) yra prieinami tiek atskirų duomenų teikėjų, tiek visos
šalies viešojo transporto statiniai duomenų rinkinio failai.

```{figure} ../images/gerosios-praktikos/norvegija/entur-static-files.png
:name: entur-static-data-files

ENTUR statiniai viešojo transporto duomenų rinkiniai.
```

## Dinaminiai duomenys

ENTUR taip pat teikia visą Novegijos apimančius viešojo transporto dinaminius
duomenis. [Dinaminiai duomenys](https://developer.entur.org/pages-real-time-intro) yra prieinami SIRI XML, SIRI Lite (
REST) ir GTFS Realtime formatais.

### SIRI

Norvegijos dinaminiai duomenys
atitinka [Norvegišką SIRI profilį](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370420/Norwegian+SIRI+profile)

#### ET – Estimated Timetable

Kiekvienos viešojo transporto kelionės suplanuoti, faktiniai ir prognozuojami išvykimo laikai, atšaukimai.

:::{admonition} Novergijos SIRI Estimated Timetable (ET) duomenų kontrakto pavyzdys
:class: tip, dropdown

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Siri xmlns="http://www.siri.org.uk/siri" xmlns:ns2="http://www.ifopt.org.uk/acsb"
      xmlns:ns3="http://www.ifopt.org.uk/ifopt" xmlns:ns4="http://datex2.eu/schema/2_0RC1/2_0" version="2.0">
    <ServiceDelivery>
        <ResponseTimestamp>2022-06-01T17:45:04.47352847+02:00</ResponseTimestamp>
        <ProducerRef>ENT</ProducerRef>
        <EstimatedTimetableDelivery version="2.0">
            <ResponseTimestamp>2022-06-01T17:45:04.473537687+02:00</ResponseTimestamp>
            <EstimatedJourneyVersionFrame>
                <RecordedAtTime>2022-06-01T17:45:04.473531413+02:00</RecordedAtTime>
                <EstimatedVehicleJourney>
                    <RecordedAtTime>2022-06-01T16:13:54.653+02:00</RecordedAtTime>
                    <LineRef>RUT:Line:310</LineRef>
                    <DirectionRef>2</DirectionRef>
                    <FramedVehicleJourneyRef>
                        <DataFrameRef>2022-06-01</DataFrameRef>
                        <DatedVehicleJourneyRef>RUT:ServiceJourney:310-166441-22091263</DatedVehicleJourneyRef>
                    </FramedVehicleJourneyRef>
                    <OperatorRef>norgesbuss</OperatorRef>
                    <Monitored>true</Monitored>
                    <DataSource>RUT</DataSource>
                    <BlockRef>12005-2022-06-01</BlockRef>
                    <VehicleRef>YV3U1W12XK1197095</VehicleRef>
                    <EstimatedCalls>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9910</StopPointRef>
                            <Order>1</Order>
                            <StopPointName>Vallerudtoppen</StopPointName>
                            <DestinationDisplay>Fjerdingby</DestinationDisplay>
                            <AimedDepartureTime>2022-06-01T18:56:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T18:56:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9897</StopPointRef>
                            <Order>2</Order>
                            <StopPointName>Vallerudlia</StopPointName>
                            <AimedArrivalTime>2022-06-01T18:57:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T18:57:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T18:57:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T18:57:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9891</StopPointRef>
                            <Order>3</Order>
                            <StopPointName>Rasta skole</StopPointName>
                            <AimedArrivalTime>2022-06-01T18:58:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T18:58:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T18:58:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T18:58:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:10005</StopPointRef>
                            <Order>4</Order>
                            <StopPointName>Glenneveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T18:59:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T18:59:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T18:59:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T18:59:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9811</StopPointRef>
                            <Order>5</Order>
                            <StopPointName>Lørenskog sentrum</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:05:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:05:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:05:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:05:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9870</StopPointRef>
                            <Order>6</Order>
                            <StopPointName>Knatten</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:06:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:06:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:06:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:06:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9944</StopPointRef>
                            <Order>7</Order>
                            <StopPointName>Kloppaveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:08:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:08:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:08:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:08:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9840</StopPointRef>
                            <Order>8</Order>
                            <StopPointName>Ahus</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:09:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:09:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:10:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:10:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9928</StopPointRef>
                            <Order>9</Order>
                            <StopPointName>Vittenberg</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:13:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:13:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:13:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:13:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:10058</StopPointRef>
                            <Order>10</Order>
                            <StopPointName>Strømsbergveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:14:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:14:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:14:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:14:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:10061</StopPointRef>
                            <Order>11</Order>
                            <StopPointName>Stasjonsveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:15:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:15:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:15:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:15:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:10072</StopPointRef>
                            <Order>12</Order>
                            <StopPointName>Frydenbergveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:16:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:16:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:16:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:16:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9422</StopPointRef>
                            <Order>13</Order>
                            <StopPointName>Kurlandsveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:17:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:17:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:17:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:17:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9419</StopPointRef>
                            <Order>14</Order>
                            <StopPointName>Torgenholtet</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:18:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:18:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:18:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:18:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9394</StopPointRef>
                            <Order>15</Order>
                            <StopPointName>Løvenstad senter</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:19:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:19:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:19:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:19:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9391</StopPointRef>
                            <Order>16</Order>
                            <StopPointName>Skytilveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:20:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:20:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:20:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:20:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9388</StopPointRef>
                            <Order>17</Order>
                            <StopPointName>Sæterveien</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:21:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:21:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:21:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:21:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9289</StopPointRef>
                            <Order>18</Order>
                            <StopPointName>Furukollen</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:22:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:22:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:22:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:22:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9352</StopPointRef>
                            <Order>19</Order>
                            <StopPointName>Petrinehøy</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:23:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:23:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:23:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:23:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9348</StopPointRef>
                            <Order>20</Order>
                            <StopPointName>Rud skole</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:24:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:24:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:24:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:24:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9328</StopPointRef>
                            <Order>21</Order>
                            <StopPointName>Hagastubakken</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:26:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:26:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:26:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:26:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9335</StopPointRef>
                            <Order>22</Order>
                            <StopPointName>Øgardshøgda</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:27:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:27:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:27:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:27:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9339</StopPointRef>
                            <Order>23</Order>
                            <StopPointName>Norum</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:28:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:28:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:28:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:28:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9343</StopPointRef>
                            <Order>24</Order>
                            <StopPointName>Dovre fabrikker</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:29:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:29:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:29:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:29:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9313</StopPointRef>
                            <Order>25</Order>
                            <StopPointName>Rælingen rådhus</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:31:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:31:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:31:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:31:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9306</StopPointRef>
                            <Order>26</Order>
                            <StopPointName>Marikollen</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:32:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:32:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <AimedDepartureTime>2022-06-01T19:32:00+02:00</AimedDepartureTime>
                            <ExpectedDepartureTime>2022-06-01T19:32:00+02:00</ExpectedDepartureTime>
                            <DepartureStatus>onTime</DepartureStatus>
                        </EstimatedCall>
                        <EstimatedCall>
                            <StopPointRef>NSR:Quay:9298</StopPointRef>
                            <Order>27</Order>
                            <StopPointName>Fjerdingby</StopPointName>
                            <AimedArrivalTime>2022-06-01T19:35:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-06-01T19:35:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                        </EstimatedCall>
                    </EstimatedCalls>
                    <IsCompleteStopSequence>true</IsCompleteStopSequence>
                </EstimatedVehicleJourney>
            </EstimatedJourneyVersionFrame>
        </EstimatedTimetableDelivery>
    </ServiceDelivery>
</Siri>
```

:::

#### VM – Vehicle Monitoring

Realaus laiko transporto priemonės pozicijos duomenys su nukrypimas nuo tvarkaraščio.

:::{admonition} Novergijos SIRI Vehicle Monitoring (VM) duomenų kontrakto pavyzdys
:class: tip, dropdown

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Siri xmlns="http://www.siri.org.uk/siri" xmlns:ns2="http://www.ifopt.org.uk/acsb"
      xmlns:ns3="http://www.ifopt.org.uk/ifopt" xmlns:ns4="http://datex2.eu/schema/2_0RC1/2_0" version="2.0">
    <ServiceDelivery>
        <ResponseTimestamp>2022-05-13T13:52:40.491112194+02:00</ResponseTimestamp>
        <ProducerRef>ENT</ProducerRef>
        <RequestMessageRef>757c9284-0f12-4a46-a557-33a19e80119b</RequestMessageRef>
        <MoreData>true</MoreData>
        <VehicleMonitoringDelivery version="2.0">
            <ResponseTimestamp>2022-05-13T13:52:40.49125405+02:00</ResponseTimestamp>
            <VehicleActivity>
                <RecordedAtTime>2022-05-13T13:52:17.047+02:00</RecordedAtTime>
                <ValidUntilTime>2022-05-13T14:23:00+02:00</ValidUntilTime>
                <VehicleMonitoringRef>753233</VehicleMonitoringRef>
                <ProgressBetweenStops/>
                <MonitoredVehicleJourney>
                    <LineRef>VKT:Line:701328</LineRef>
                    <DirectionRef>Inbound</DirectionRef>
                    <FramedVehicleJourneyRef>
                        <DataFrameRef>2022-05-13</DataFrameRef>
                        <DatedVehicleJourneyRef>572-13281328-75-1254-20220513-2171</DatedVehicleJourneyRef>
                    </FramedVehicleJourneyRef>
                    <JourneyPatternRef>572-1254-505</JourneyPatternRef>
                    <JourneyPatternName>505</JourneyPatternName>
                    <VehicleMode>bus</VehicleMode>
                    <PublishedLineName>1328</PublishedLineName>
                    <DirectionName>Inbound</DirectionName>
                    <OperatorRef xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                 xsi:type="OperationalUnitRefStructure">70
                    </OperatorRef>
                    <OriginRef>NSR:StopPlace:17977</OriginRef>
                    <OriginName>Lardal skole</OriginName>
                    <DestinationRef>NSR:StopPlace:17446</DestinationRef>
                    <DestinationName>Helgeland-Steinsholt</DestinationName>
                    <Monitored>true</Monitored>
                    <DataSource>VKT</DataSource>
                    <VehicleLocation>
                        <Longitude>9.9569589</Longitude>
                        <Latitude>59.4009118</Latitude>
                    </VehicleLocation>
                    <LocationRecordedAtTime>2022-05-13T13:52:17.047+02:00</LocationRecordedAtTime>
                    <Bearing>273.0</Bearing>
                    <Delay>PT0S</Delay>
                    <VehicleStatus>inProgress</VehicleStatus>
                    <VehicleJourneyRef>13281328</VehicleJourneyRef>
                    <VehicleRef>753233</VehicleRef>
                    <OnwardCalls>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31438</StopPointRef>
                            <VisitNumber>1</VisitNumber>
                            <Order>1</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Lardal skole
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>noAlighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:15:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:15:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">0
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31441</StopPointRef>
                            <VisitNumber>2</VisitNumber>
                            <Order>2</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Lardal ungdomsskole
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:18:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:18:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:18:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:18:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">1
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>0728004001</StopPointRef>
                            <VisitNumber>3</VisitNumber>
                            <Order>3</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Hukstrøm bru
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:20:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:20:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:20:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:20:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">1
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33650</StopPointRef>
                            <VisitNumber>4</VisitNumber>
                            <Order>4</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Berg Svarstad
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:21:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:21:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:21:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:21:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33713</StopPointRef>
                            <VisitNumber>5</VisitNumber>
                            <Order>5</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Gavelstad
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:23:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:23:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:23:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:23:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32887</StopPointRef>
                            <VisitNumber>6</VisitNumber>
                            <Order>6</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Hvaal nord
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:23:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:23:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:23:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:23:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32880</StopPointRef>
                            <VisitNumber>7</VisitNumber>
                            <Order>7</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Hvaal
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:24:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:24:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:24:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:24:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33811</StopPointRef>
                            <VisitNumber>8</VisitNumber>
                            <Order>8</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Bjærtnes
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:25:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:25:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:25:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:25:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33874</StopPointRef>
                            <VisitNumber>9</VisitNumber>
                            <Order>9</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Glenne Østsideveien
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:26:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:26:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:26:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:26:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31975</StopPointRef>
                            <VisitNumber>10</VisitNumber>
                            <Order>10</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Holtan
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:27:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:27:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:27:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:27:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32407</StopPointRef>
                            <VisitNumber>11</VisitNumber>
                            <Order>11</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Kongelf
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:28:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:28:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:28:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:28:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31488</StopPointRef>
                            <VisitNumber>12</VisitNumber>
                            <Order>12</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Helgeland
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:30:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:30:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:30:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:30:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:34047</StopPointRef>
                            <VisitNumber>13</VisitNumber>
                            <Order>13</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Brekka snuplass
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:33:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:33:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:33:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:33:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">0
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31487</StopPointRef>
                            <VisitNumber>14</VisitNumber>
                            <Order>14</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Helgeland
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:36:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:36:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:36:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:36:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">1
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31004</StopPointRef>
                            <VisitNumber>15</VisitNumber>
                            <Order>15</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Gåserud
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:39:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:39:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:39:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:39:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33538</StopPointRef>
                            <VisitNumber>16</VisitNumber>
                            <Order>16</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Eide
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:40:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:40:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:40:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:40:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32740</StopPointRef>
                            <VisitNumber>17</VisitNumber>
                            <Order>17</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Styrvoll
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:41:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:41:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:41:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:41:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32832</StopPointRef>
                            <VisitNumber>18</VisitNumber>
                            <Order>18</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Svartangveien
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:41:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:41:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:41:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:41:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33202</StopPointRef>
                            <VisitNumber>19</VisitNumber>
                            <Order>19</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Dalen Hanevoll
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:42:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:42:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:42:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:42:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33400</StopPointRef>
                            <VisitNumber>20</VisitNumber>
                            <Order>20</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Duvholt
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:43:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:43:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:43:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:43:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">1
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31197</StopPointRef>
                            <VisitNumber>21</VisitNumber>
                            <Order>21</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Hanevoll
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:45:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:45:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:45:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:45:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:34037</StopPointRef>
                            <VisitNumber>22</VisitNumber>
                            <Order>22</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Breidablikk Steinsholt
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:46:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:46:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:46:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:46:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">0
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32517</StopPointRef>
                            <VisitNumber>23</VisitNumber>
                            <Order>23</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Steinsholt
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:48:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:48:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:48:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:48:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33157</StopPointRef>
                            <VisitNumber>24</VisitNumber>
                            <Order>24</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Thyge
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:51:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:51:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:51:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:51:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">1
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32527</StopPointRef>
                            <VisitNumber>25</VisitNumber>
                            <Order>25</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Steinsholt Stranda
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:52:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:52:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:52:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:52:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:32541</StopPointRef>
                            <VisitNumber>26</VisitNumber>
                            <Order>26</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Steinsholtmoen
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:53:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:53:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:53:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:53:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:30836</StopPointRef>
                            <VisitNumber>27</VisitNumber>
                            <Order>27</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Røsholtmoen
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:53:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:53:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:53:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:53:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33710</StopPointRef>
                            <VisitNumber>28</VisitNumber>
                            <Order>28</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Berganmoen
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:54:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:54:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:54:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:54:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:33714</StopPointRef>
                            <VisitNumber>29</VisitNumber>
                            <Order>29</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Berganmoen industri
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:54:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:54:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:54:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:54:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:31496</StopPointRef>
                            <VisitNumber>30</VisitNumber>
                            <Order>30</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Virgenes
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:55:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:55:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <AimedDepartureTime>2022-05-13T14:55:00+02:00</AimedDepartureTime>
                            <EarliestExpectedDepartureTime>2022-05-13T14:55:00+02:00</EarliestExpectedDepartureTime>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>boarding</DepartureBoardingActivity>
                        </OnwardCall>
                        <OnwardCall>
                            <StopPointRef>NSR:Quay:30493</StopPointRef>
                            <VisitNumber>31</VisitNumber>
                            <Order>31</Order>
                            <StopPointName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                           xsi:type="DefaultedTextStructure">Rambo
                            </StopPointName>
                            <VehicleAtStop>false</VehicleAtStop>
                            <AimedArrivalTime>2022-05-13T14:56:00+02:00</AimedArrivalTime>
                            <ExpectedArrivalTime>2022-05-13T14:56:00+02:00</ExpectedArrivalTime>
                            <ArrivalStatus>onTime</ArrivalStatus>
                            <ArrivalBoardingActivity>alighting</ArrivalBoardingActivity>
                            <DeparturePlatformName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                                   xsi:type="DefaultedTextStructure">2
                            </DeparturePlatformName>
                            <DepartureBoardingActivity>noBoarding</DepartureBoardingActivity>
                        </OnwardCall>
                    </OnwardCalls>
                </MonitoredVehicleJourney>
            </VehicleActivity>
        </VehicleMonitoringDelivery>
    </ServiceDelivery>
</Siri>
```

:::

#### SX – Situation Exchange

Tekstiniai pranešimai susieti su maršrutais, reisais, stotelėmis rodomi keleiviams.

:::{admonition} Norvegijos SIRI Situation Exchange (SX) duomenų kontrakto pavyzdys
:class: tip, dropdown

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Siri xmlns="http://www.siri.org.uk/siri" xmlns:ns2="http://www.ifopt.org.uk/acsb"
      xmlns:ns3="http://www.ifopt.org.uk/ifopt" xmlns:ns4="http://datex2.eu/schema/2_0RC1/2_0" version="2.0">
    <ServiceDelivery>
        <ResponseTimestamp>2022-05-13T13:51:12.156961772+02:00</ResponseTimestamp>
        <ProducerRef>ENT</ProducerRef>
        <RequestMessageRef>757c9284-0f12-4a46-a557-33a19e80119b</RequestMessageRef>
        <MoreData>false</MoreData>
        <SituationExchangeDelivery>
            <ResponseTimestamp>2022-05-13T13:51:12.156974389+02:00</ResponseTimestamp>
            <Situations>
                <PtSituationElement>
                    <CreationTime>2022-05-13T13:48:46.955+02:00</CreationTime>
                    <ParticipantRef>RUT</ParticipantRef>
                    <SituationNumber>RUT:SituationNumber:533766</SituationNumber>
                    <Source>
                        <SourceType>directReport</SourceType>
                    </Source>
                    <Progress>open</Progress>
                    <ValidityPeriod>
                        <StartTime>2022-05-13T13:38:00+02:00</StartTime>
                        <EndTime>2022-05-13T14:34:00+02:00</EndTime>
                    </ValidityPeriod>
                    <UndefinedReason></UndefinedReason>
                    <Severity>normal</Severity>
                    <ReportType>incident</ReportType>
                    <Keywords></Keywords>
                    <Summary xml:lang="NO">Forsinket ca. 10 minutter</Summary>
                    <Summary xml:lang="EN">Delayed</Summary>
                    <Description xml:lang="NO">Forsinkelsen skyldes mye trafikk og kø.</Description>
                    <Description xml:lang="EN">The departure from Voksen skog at 13:38 towards Kværnerbyen is about 10
                        minutes delayed.
                    </Description>
                    <Affects>
                        <VehicleJourneys>
                            <AffectedVehicleJourney>
                                <VehicleJourneyRef>RUT:ServiceJourney:32-163399-21485514</VehicleJourneyRef>
                            </AffectedVehicleJourney>
                        </VehicleJourneys>
                    </Affects>
                </PtSituationElement>
                <PtSituationElement>
                    <CreationTime>2022-05-13T13:49:26.054+02:00</CreationTime>
                    <ParticipantRef>RUT</ParticipantRef>
                    <SituationNumber>RUT:SituationNumber:533767</SituationNumber>
                    <Source>
                        <SourceType>directReport</SourceType>
                    </Source>
                    <Progress>open</Progress>
                    <ValidityPeriod>
                        <StartTime>2022-05-13T13:45:00+02:00</StartTime>
                        <EndTime>2022-05-13T14:13:00+02:00</EndTime>
                    </ValidityPeriod>
                    <UndefinedReason></UndefinedReason>
                    <Severity>normal</Severity>
                    <ReportType>incident</ReportType>
                    <Keywords></Keywords>
                    <Summary xml:lang="NO">Forsinket ca. 5 minutter</Summary>
                    <Summary xml:lang="EN">Delayed</Summary>
                    <Description xml:lang="NO">Forsinkelsen skyldes mye trafikk og kø.</Description>
                    <Description xml:lang="EN">The departure from Ullerntoppen at 13:45 towards Majorstuen is about 5
                        minutes delayed.
                    </Description>
                    <Affects>
                        <VehicleJourneys>
                            <AffectedVehicleJourney>
                                <VehicleJourneyRef>RUT:ServiceJourney:46-164389-22218648</VehicleJourneyRef>
                            </AffectedVehicleJourney>
                        </VehicleJourneys>
                    </Affects>
                </PtSituationElement>
            </Situations>
        </SituationExchangeDelivery>
    </ServiceDelivery>
</Siri>
```

:::

### GTFS Realtime

#### Trip updates

:::{admonition} Novergijos GTFS Realtime Trip updates duomenų kontrakto pavyzdys
:class: tip, dropdown

```json
{
  "header": {
    "gtfs_realtime_version": "1.0",
    "incrementality": "FULL_DATASET",
    "timestamp": "1652696355"
  },
  "entity": [
    {
      "id": "VYB:ServiceJourney:a743888f8852ea12a49e41c7801854237e703b74-2022-05-16",
      "trip_update": {
        "trip": {
          "trip_id": "VYB:ServiceJourney:a743888f8852ea12a49e41c7801854237e703b74",
          "route_id": "VYB:Line:22"
        },
        "stop_time_update": [
          {
            "stop_sequence": 0,
            "departure": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:99391"
          },
          {
            "stop_sequence": 1,
            "arrival": {
              "delay": 0
            },
            "departure": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:101311"
          },
          {
            "stop_sequence": 2,
            "arrival": {
              "delay": 0
            },
            "departure": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:99400"
          },
          {
            "stop_sequence": 3,
            "arrival": {
              "delay": 0
            },
            "departure": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:99392"
          },
          {
            "stop_sequence": 4,
            "arrival": {
              "delay": 0
            },
            "departure": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:101350"
          },
          {
            "stop_sequence": 5,
            "arrival": {
              "delay": 0
            },
            "departure": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:99397"
          },
          {
            "stop_sequence": 6,
            "arrival": {
              "delay": 0
            },
            "stop_id": "NSR:Quay:99376"
          }
        ]
      }
    }
  ]
}
```

:::

#### Vehicle positions

:::{admonition} Novergijos GTFS Realtime Vehicle positions duomenų kontrakto pavyzdys
:class: tip, dropdown

```json
{
  "header": {
    "gtfs_realtime_version": "1.0",
    "incrementality": "FULL_DATASET",
    "timestamp": "1652695735"
  },
  "entity": [
    {
      "id": "VYB:VehicleRef:1950290",
      "vehicle": {
        "trip": {
          "trip_id": "VYB:ServiceJourney:a3a92fe030416ab91414e80dbf9c406e9222768d",
          "route_id": "VYB:Line:26"
        },
        "position": {
          "latitude": 59.391876,
          "longitude": 16.471745,
          "bearing": 0.0,
          "odometer": 0.0,
          "speed": 0.0
        },
        "timestamp": "1652695730",
        "congestion_level": "RUNNING_SMOOTHLY",
        "vehicle": {
          "id": "VYB:VehicleRef:1950290"
        }
      }
    }
  ]
}
```

:::

#### Service alerts

:::{admonition} Novergijos GTFS Realtime Service alerts duomenų kontrakto pavyzdys
:class: tip, dropdown

```json
{
  "header": {
    "gtfs_realtime_version": "1.0",
    "incrementality": "FULL_DATASET",
    "timestamp": "1652696516"
  },
  "entity": [
    {
      "id": "RUT:SituationNumber:504908",
      "alert": {
        "active_period": [
          {
            "start": "1620784800",
            "end": "1683928740"
          }
        ],
        "informed_entity": [
          {
            "route_id": "RUT:Line:23",
            "stop_id": "NSR:Quay:11067"
          },
          {
            "route_id": "RUT:Line:24",
            "stop_id": "NSR:Quay:11067"
          }
        ],
        "header_text": {
          "translation": [
            {
              "text": "Holdeplass Sinsenveien \u00f8stg\u00e5ende er flyttet",
              "language": "no"
            },
            {
              "text": "Stop Sinsenveien eastbound is moved",
              "language": "en"
            }
          ]
        },
        "description_text": {
          "translation": [
            {
              "text": "Fra 12 mai: Holdeplass Sinsenveien retning \u00f8st er flyttet ca. 150 meter tilbake. Avviket er planlagt \u00e5 vare i ca. 2 \u00e5r.",
              "language": "no"
            },
            {
              "text": "From 12 May. Stop Sinsenveien direction east is moved approx. 150 backwards. The discrepancy is scheduled to end approx. 2 years.",
              "language": "en"
            }
          ]
        }
      }
    }
  ]
}
```

:::

## Naudingos nuorodos

- [Novegiško SIRI profilio formato pavydžiai](https://github.com/entur/profile-norway-examples/tree/master/siri/)