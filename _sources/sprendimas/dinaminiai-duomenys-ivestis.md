# Dinaminių duomenų įvestis

## Naudojamas dinaminių duomenų formatas

Šiuo metu dinaminių duomenų įkėlimui į VINTRA naudojamas .csv formatas.
Šis formatas paplitęs tik Lietuvoje ir nėra naudojamas jokiose kitose pasaulio šalyse. Esminės naudojamo formato
trūkumai:

- Duomenis sunku integruoti į užsienio sistemas;
- Jokia užsienio sistema negeneruoja duomenų šiuo formatu;
- Sunku patikrinti duomenų kokybę, nes neegzistuoja jokių automatinių duomenų kokybės patikrinimo įrankių;
- Negriežtai apibrėžti privaloma informacija (sudaromos galimybės teikti nekokybiškus duomenis);
- Sunku išplėsti formatą (pvz., pridėti pranešimus keleiviams);
- Apsunkinama duomenų koversija į SIRI (būtiną pagal ITS
  direktyvą{cite}`directive_multimodal_travel_information_services_main`) atveriant dinaminius duomenis) arba GTFS
  Realtime formatus;

Dėl šių priežasčių siūloma keisti dinaminių duomenų įkėlimo formatą į paminėtus toliau.

## SIRI

Remianti Jungtinės Karalystės, Švedijos užsienio gerosiomis praktikomis rekomenduojama, kaip numatytąjį formatą
dinaminių duomenų įkėlimui į VINTRA naudoti SIRI formatą.

Rekomenduojama
remtis [Nordic SIRI profiliu](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370420/Nordic+SIRI+Profile) arba
Jungtinės Karalystės Bus Open Data
Service [SIRI-VM profiliu](https://www.gov.uk/government/publications/technical-guidance-publishing-location-data-using-the-bus-open-data-service-siri-vm)
transporto priemonių geografinei padėčiai įkelti.

### Transporto priemonių geografinė padėtis

https://github.com/entur/profile-examples/blob/master/siri/vehicle-monitoring/siri-vm-before-stop.xml

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Siri xmlns="http://www.siri.org.uk/siri"
      xmlns:ns2="http://www.ifopt.org.uk/acsb"
      xmlns:ns3="http://www.ifopt.org.uk/ifopt"
      xmlns:ns4="http://datex2.eu/schema/2_0RC1/2_0"
      version="2.0">
    <ServiceDelivery>
        <ResponseTimestamp>2022-07-04T12:13:39</ResponseTimestamp>
        <ProducerRef>VLN</ProducerRef>
        <VehicleMonitoringDelivery version="2.0">
            <ResponseTimestamp>2022-07-04T12:13:39</ResponseTimestamp>
            <VehicleActivity>
                <RecordedAtTime>2022-07-04T12:13:01</RecordedAtTime>
                <ValidUntilTime>2022-07-04T12:23:01</ValidUntilTime>
                <ProgressBetweenStops>
                    <LinkDistance>501</LinkDistance>
                    <Percentage>0.62</Percentage>
                </ProgressBetweenStops>
                <MonitoredVehicleJourney>
                    <LineRef>VLN:Line:54</LineRef>
                    <FramedVehicleJourneyRef>
                        <DataFrameRef>2018-07-24</DataFrameRef>
                        <DatedVehicleJourneyRef>VLN:ServiceJourney:54-1605</DatedVehicleJourneyRef>
                    </FramedVehicleJourneyRef>
                    <VehicleMode>bus</VehicleMode>
                    <OperatorRef>VLN:Operator:Transrevis</OperatorRef>
                    <Monitored>true</Monitored>
                    <DataSource>VLN</DataSource>
                    <VehicleLocation srsName="WGS84">
                        <Longitude>10.759100</Longitude>
                        <Latitude>59.937483</Latitude>
                    </VehicleLocation>
                    <Bearing>096</Bearing>
                    <Occupancy>seatsAvailable</Occupancy>
                    <Delay>PT239S</Delay>
                    <VehicleStatus>inProgress</VehicleStatus>
                    <VehicleRef>103029</VehicleRef>
                    <MonitoredCall>
                        <StopPointRef>NSR:Quay:11689</StopPointRef>
                        <StopPointName>Žaliasis tiltas</StopPointName>
                        <VehicleAtStop>false</VehicleAtStop>
                        <DestinationDisplay>Centras</DestinationDisplay>
                    </MonitoredCall>
                    <IsCompleteStopSequence>false</IsCompleteStopSequence>
                </MonitoredVehicleJourney>
            </VehicleActivity>
        </VehicleMonitoringDelivery>
    </ServiceDelivery>
</Siri>
```