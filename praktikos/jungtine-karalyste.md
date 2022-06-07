# Jungtinė Karalystė

2017 m. išleistas autobusų paslaugų teikimo įstatymas (
angl. *[Bus Services Act](https://www.legislation.gov.uk/ukpga/2017/21/contents)*) reikalauja, kad visi
vietinių autobusų operatoriai teiktų tvarkraščių, tarifų ir transporto priemonės buvimo vietos informaciją į
centrinę
sistemą (angl. *[Bus Open Data Service](https://data.bus-data.dft.gov.uk/guidance/requirements/?section=overview)*).

Šių duomenų teikimui buvo numatyti pereinamieji laikotarpiai, kurie vaizduojami toliau esančioje
lentelėje{cite}`uk_bus_open_service_developer_documentation`.

```{table} Duomenų teikimo pereinamsis laikotarpis visiems vietinių autobusų operatoriams

| Data                   | Aprašymas                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------|
| 2020 m. gruodžio 31 d. | Privaloma teikti tvarkaraščių informaciją                                                      |
| 2021 m. sausio 7 d.    | Privaloma teikti transporto priemonės buvimo vietos ir pagrindius tarifų bei bilietų duomenis. |
| 2023 m. sausio 7 d.    | Privaloma teikti išplėstinius bilietų kainų ir bilietų duomenis.                               |
```

## Informacija apie transporto operatorius

Juntinė Karalystė [specialiame puslapyje](https://data.bus-data.dft.gov.uk/operators/) pateikia informaciją apie
kiekvieną šalyje veikiantį transporto operatorių, jo licenzijos numerį bei atvirų duomenų nuorodos susijusios
su tvarkaraščiais, transporto priemonės buvimo vieta bei tarifais.

```{figure} ../images/gerosios-praktikos/united-kingdom/operator-profiles.png

Informacija apie transporto operatorius.
```

## Statiniai duomenys

```{table} Statinių duomenų teikimas ir atviri duomenys

| Tipas         | Duomenų teikimo formatas | Atvirų duomenų formatas | Atnaujinimo dažnumas |
|---------------|--------------------------|-------------------------|----------------------|
| Tvarkaraščiai | TransXChange             | GTFS ir TransXChange    | Kartą per 24 val.    |
| Tarifai       | NeTEx                    | NeTEx                   | Kartą per 24 val.    |
```

Verta pastebėti, kad transporto operatoriai tvarkaraščių duomenis
teikia [TransXChange](https://www.gov.uk/government/collections/transxchange) formatu. Šis formatas yra būdingas tik
Jungtinei Karalystei bei yra ypač panašus į NeTEx ir paremtas Transmodel.

## Dinaminiai duomenys

Transporto operatoriai informaciją apie transporto priemonių buvimo vietos teikia SIRI-VM
formatu{cite}`uk_bus_open_service_developer_documentation`. Toliau pateikiama lentelė kokie duomenys
privalo būti teikiami{cite}`uk_bods_bus_operator_requirements`.

```{table} Dinaminių duomenų teikimo privalomumas transporto operatoriams (SIRI-VM)

| SIRI-VM profilio laukelis   | Aprašymas                                       |
|-----------------------------|-------------------------------------------------|
| Bearing                     | Azimutas                                        |
| BlockRef                    | Bloko identifikatorius                          |
| DestinationRef              | Paskirties stotelės identifikatorius            |
| DirectionRef                | Reiso kryptis                                   |
| LineRef                     | Maršruto identifikatorius                       |
| OperatorRef                 | Operatoriaus identifikatorius                   |
| OriginName                  | Pirmosios stotelės pavadinimas                  |
| OriginRef                   | Pirmosios reiso stotelės identifikatorius       |
| ProducerRef                 | Duomenų rinkinio generatoriaus identifikatorius |
| PublishedLineName           | Maršruto pavadinimas                            |
| RecordedAtTime              | Pozicijos gavimo data ir laikas                 |
| Speed                       | Transporto priemonės greitis                    |
| ValidUntilTime              | Pozicijos galiojimo data ir laikas              |
| VehicleJourneyRef           | Reiso identifikatorius                          |
| VehicleLocation (Lat, Long) | Transporto priemonės pozicija                   |
| VehicleRef                  | Transporto priemonės identifikatorius.          |
```

### Ativiri duomenys

Visi dinaminiai viešojo transporto duomenys yra atviri ir prieinami
per *[Bus Open Data Service](https://data.bus-data.dft.gov.uk/avl/download/#)* dviem formatais: SIRI-Lite ir GTFS
Realtime.

```{figure} ../images/gerosios-praktikos/united-kingdom/location-data.png

Atvirai prieinami dinaminiai viešojo transporto duomenys.
```

:::{admonition} SIRI VM (Vehicle Monitoring) gražinamų duomenų pavzydys
:class: tip, dropdown

```xml

<Siri xmlns="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.siri.org.uk/siri http://www.siri.org.uk/schema/2.0/xsd/siri.xsd" version="2.0">
    <ServiceDelivery>
        <ResponseTimestamp>2022-06-07T08:51:02.550066+00:00</ResponseTimestamp>
        <ProducerRef>ItoWorld</ProducerRef>
        <VehicleMonitoringDelivery>
            <ResponseTimestamp>2022-06-07T08:51:02.550066+00:00</ResponseTimestamp>
            <RequestMessageRef>1a4d0e6a-23a3-4a30-a582-47e5e2a664da</RequestMessageRef>
            <ValidUntil>2022-06-07T08:56:02.550066+00:00</ValidUntil>
            <ShortestPossibleCycle>PT5S</ShortestPossibleCycle>
            <VehicleActivity>
                <RecordedAtTime>2022-06-07T08:50:39+00:00</RecordedAtTime>
                <ItemIdentifier>de1f2149-64f0-4ce0-9174-fb89379272bb</ItemIdentifier>
                <ValidUntilTime>2022-06-07T08:56:02.550587</ValidUntilTime>
                <MonitoredVehicleJourney>
                    <LineRef>891</LineRef>
                    <DirectionRef>outbound</DirectionRef>
                    <FramedVehicleJourneyRef>
                        <DataFrameRef>2022-06-07</DataFrameRef>
                        <DatedVehicleJourneyRef>0925</DatedVehicleJourneyRef>
                    </FramedVehicleJourneyRef>
                    <PublishedLineName>891</PublishedLineName>
                    <OperatorRef>BANG</OperatorRef>
                    <OriginRef>43000700104</OriginRef>
                    <OriginName>Wolverhampton_Bus_Station</OriginName>
                    <DestinationRef>3590E106500</DestinationRef>
                    <DestinationName>TELFORD_Bus_Station</DestinationName>
                    <OriginAimedDepartureTime>2022-06-07T09:25:00+00:00</OriginAimedDepartureTime>
                    <DestinationAimedArrivalTime>2022-06-07T10:22:00+00:00</DestinationAimedArrivalTime>
                    <VehicleLocation>
                        <Longitude>-2.209715</Longitude>
                        <Latitude>52.614723</Latitude>
                    </VehicleLocation>
                    <Bearing>312.0</Bearing>
                    <BlockRef>8912</BlockRef>
                    <VehicleRef>YX60FUE</VehicleRef>
                </MonitoredVehicleJourney>
                <Extensions>
                    <VehicleJourney>
                        <Operational>
                            <TicketMachine>
                                <TicketMachineServiceCode>891</TicketMachineServiceCode>
                                <JourneyCode>0925</JourneyCode>
                            </TicketMachine>
                        </Operational>
                        <VehicleUniqueId>14</VehicleUniqueId>
                    </VehicleJourney>
                </Extensions>
            </VehicleActivity>
        </VehicleMonitoringDelivery>
    </ServiceDelivery>
</Siri>
```
:::