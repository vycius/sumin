# Švedija

„[Trafiklab](https://www.trafiklab.se/api/)“ galima rasti daugybę skirtingų viešojo transporto kelionių duomenų API ir
duomenų rinkinių. Visi duomenų rinkiniai yra prieinami pagal [CC0 1.0 Universali (CC0 1.0) Priskyrimas Viešajai
sričiai](https://creativecommons.org/publicdomain/zero/1.0/deed.lt) licenciją. Siekiant gauti duomenų rinkinius yra
būtina registracija.

## Stotelių duomenys

Stotelių duomenų rinkinys ([Stops data](https://www.trafiklab.se/api/trafiklab-apis/stops-data/)) apima visas
Švedijoje esančias viešojo transporto stoteles NeTEx formatu (su papildomais atributais) bei yra atnaujinamas kiekvienos
dienos ryte.

:::{admonition} Gražinamų stotelių pavyzdys NeTEx formatu.  
:class: tip, dropdown

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:ns2="http://www.opengis.net/gml/3.2"
                     xmlns:ns3="http://www.siri.org.uk/siri" version="1.11:NO-NeTEx-networktimetable:1.3">
    <PublicationTimestamp>2022-07-26T07:50:00</PublicationTimestamp>
    <ParticipantRef>SAM</ParticipantRef>
    <dataObjects>
        <SiteFrame version="20220726075000" id="SE:050:SiteFrame:1">
            <ValidBetween>
                <FromDate>2005-01-01T00:00:00</FromDate>
            </ValidBetween>
            <codespaces>
                <Codespace id="50">
                    <Xmlns>50</Xmlns>
                    <XmlnsUrl>http://www.samtrafiken.se/ns/Samtrafiken</XmlnsUrl>
                </Codespace>
            </codespaces>
            <FrameDefaults>
                <DefaultLocale>
                    <TimeZone>Europe/Stockholm</TimeZone>
                    <DefaultLanguage>se</DefaultLanguage>
                </DefaultLocale>
                <DefaultLocationSystem>4326</DefaultLocationSystem>
            </FrameDefaults>
            <stopPlaces>
                <StopPlace version="20120623" id="SE:050:StopPlace:1">
                    <ValidBetween>
                        <FromDate>2012-06-23T00:00:00</FromDate>
                    </ValidBetween>
                    <keyList>
                        <KeyValue>
                            <Key>owner</Key>
                            <Value>1</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>data-from</Key>
                            <Value>1</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>rikshallplats</Key>
                            <Value>740000001</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>trafikverket-name</Key>
                            <Value>Stockholms central</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>trafikverket-signature</Key>
                            <Value>CST</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>stip.StopArea.DefaultInterchangeDurationSeconds</Key>
                            <Value>0</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>local-name</Key>
                            <Value>3:9021003191303000:Vasagatan (Stockholm)|3:9021003191709000:Stockholm Central
                                (Stockholm)|1:9021001005011000:Stockholms central|20:9021020899005000:Stockholm C
                                (Tåg)|8:9021008199001000:Stockholm Cityterminalen|74:9021074000010000:Stockholms
                                central|100:9021074000001000:Stockholm Centralstation|172:9021172055861000:Stockholm
                                Central
                            </Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>local-gid</Key>
                            <Value>
                                3:9021003191303000|3:9021003191709000|1:9021001005011000|20:9021020899005000|8:9021008199001000|74:9021074000010000|100:9021074000001000|172:9021172055861000
                            </Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>local-number</Key>
                            <Value>3:191303|3:191709|1:5011|20:899005|8:199001|74:10|100:1|172:55861</Value>
                        </KeyValue>
                    </keyList>
                    <Name>Stockholm Centralstation</Name>
                    <ShortName>Stockholms C</ShortName>
                    <PrivateCode>1</PrivateCode>
                    <Centroid>
                        <Location>
                            <Longitude>18.057845</Longitude>
                            <Latitude>59.329520</Latitude>
                        </Location>
                    </Centroid>
                    <alternativeNames>
                        <AlternativeName>
                            <Abbreviation>CST</Abbreviation>
                        </AlternativeName>
                    </alternativeNames>
                    <TransportMode>rail</TransportMode>
                    <StopPlaceType>railStation</StopPlaceType>
                    <Weighting>preferredInterchange</Weighting>
                </StopPlace>
                <StopPlace version="20120623" id="SE:050:StopPlace:1_1">
                    <ValidBetween>
                        <FromDate>2012-06-23T00:00:00</FromDate>
                    </ValidBetween>
                    <keyList>
                        <KeyValue>
                            <Key>owner</Key>
                            <Value>1</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>data-from</Key>
                            <Value>1</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>rikshallplats</Key>
                            <Value>740000001</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>trafikverket-name</Key>
                            <Value>Stockholms central</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>trafikverket-signature</Key>
                            <Value>CST</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>stip.StopArea.DefaultInterchangeDurationSeconds</Key>
                            <Value>0</Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>local-name</Key>
                            <Value>3:9021003191303000:Vasagatan (Stockholm)|3:9021003191709000:Stockholm Central
                                (Stockholm)|1:9021001005011000:Stockholms central|20:9021020899005000:Stockholm C
                                (Tåg)|8:9021008199001000:Stockholm Cityterminalen|74:9021074000010000:Stockholms
                                central|100:9021074000001000:Stockholm Centralstation|172:9021172055861000:Stockholm
                                Central
                            </Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>local-gid</Key>
                            <Value>
                                3:9021003191303000|3:9021003191709000|1:9021001005011000|20:9021020899005000|8:9021008199001000|74:9021074000010000|100:9021074000001000|172:9021172055861000
                            </Value>
                        </KeyValue>
                        <KeyValue>
                            <Key>local-number</Key>
                            <Value>3:191303|3:191709|1:5011|20:899005|8:199001|74:10|100:1|172:55861</Value>
                        </KeyValue>
                    </keyList>
                    <Name>Stockholm Centralstation</Name>
                    <ShortName>Stockholms C</ShortName>
                    <PrivateCode>1</PrivateCode>
                    <Centroid>
                        <Location>
                            <Longitude>18.057845</Longitude>
                            <Latitude>59.329520</Latitude>
                        </Location>
                    </Centroid>
                    <alternativeNames>
                        <AlternativeName>
                            <Abbreviation>CST</Abbreviation>
                        </AlternativeName>
                    </alternativeNames>
                    <ParentSiteRef ref="SE:050:StopPlace:1"/>
                    <TransportMode>bus</TransportMode>
                    <StopPlaceType>onstreetBus</StopPlaceType>
                    <Weighting>preferredInterchange</Weighting>
                    <quays>
                        <Quay version="20210307" id="SE:050:Quay:5021">
                            <keyList>
                                <KeyValue>
                                    <Key>stip.StopPoint.ExistsFromDate</Key>
                                    <Value>2021-03-07</Value>
                                </KeyValue>
                                <KeyValue>
                                    <Key>stip.StopPoint.ExistsUpToDate</Key>
                                    <Value>null</Value>
                                </KeyValue>
                                <KeyValue>
                                    <Key>local-journeypatternpoint-gid</Key>
                                    <Value>3:9025003019130301|8:9025008019900101|74:9025074000010070</Value>
                                </KeyValue>
                                <KeyValue>
                                    <Key>local-stoppoint-gid</Key>
                                    <Value>3:9022003191303001|8:9022008199001001|74:9022074000010070</Value>
                                </KeyValue>
                                <KeyValue>
                                    <Key>local-designation</Key>
                                    <Value>3:A|8:A|74:7</Value>
                                </KeyValue>
                            </keyList>
                            <Name>Stockholm C Vasagatan</Name>
                            <ShortName>Stockholm C Vasa</ShortName>
                            <PrivateCode>1</PrivateCode>
                            <Centroid>
                                <Location>
                                    <Longitude>18.059323</Longitude>
                                    <Latitude>59.330532</Latitude>
                                </Location>
                            </Centroid>
                            <PublicCode>A</PublicCode>
                        </Quay>
                    </quays>
                </StopPlace>
            </stopPlaces>
        </SiteFrame>
    </dataObjects>
</PublicationDelivery>
```

:::

## GTFS Sverige 2

[GTFS Sverige 2](https://www.trafiklab.se/api/trafiklab-apis/gtfs-sverige-2/) apima visos Švedijos viešojo
transporto kelionių statinius ir istorinius duomenis. Šis rinkinys prieinamas GTFS formatu ir yra mažiau detalus nei
regioniniai duomenų rinkiniai prieinami NeTEx formatu.

Taip pat GTFS Sverige 2 apima istorinius statinius viešojo transporto kelionių duomenis GTFS formatu. Istoriniai
duomenų rinkiniai GTFS formatu yra sukuriami kiekvieną kartą atnaujinus statinius duomenis.

## GTFS Regional

[GTFS Regional](https://www.trafiklab.se/api/trafiklab-apis/gtfs-regional/) yra viešojo transporto kelionių statinių
duomenų rinkinys GTFS formatu bei dinaminiai realaus laiko duomenų rinkinys GTFS Realtime fomatu. Kiekviename
duomenų rinkinyje yra konkretaus regiono arba operatoriaus duomenys. Verta pastebėti, kad kiekvienas duomenų
šaltinis naudoja skirtingus stotelių identifikatorius.

## NeTEx Regional

[NeTEx Regional](https://www.trafiklab.se/api/trafiklab-apis/netex-regional/) yra analogiškas GTFS Regional, tik
duomenys yra prieinami NeTEx formatu bei šiuo formatu grįžta papildomi duomenys, kurių negalima pateikti GTFS formatu.

[Dinaminiai realaus laiko duomenys](https://www.trafiklab.se/api/trafiklab-apis/netex-regional/siri/) prieinami SIRI 2.0
formatu. Duomenų rinkinys remiasi
[Norvegijos SIRI profiliu](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370420/Norwegian+SIRI+profile).

## GTFS Sweden 3

[GTFS Sweden 3](https://www.trafiklab.se/api/trafiklab-apis/gtfs-sweden/) yra GTFS duomenų rinkinys apimantis didžiąją
dalį Švedijos viešojo transporto kelionių duomenų. GTFS
duomenų rinkinys yra prieinamas, kaip vienas GTFS duomenų failas.

Taip pat yra prieinami dinaminai realaus laiko duomenys GTFS Realtime formatu. Šie duomenys apima transporto
priemonių geografinės padėties pozicijos, prognozuojamus atvykimo laikus bei pranešimus keleivius. Šie duomenys dėl
greitaveikos priežasčių yra išskirti į atskirų regionų ar operatorių dinaminių realaus laiko duomenų rinkinius.

## NeTEx Sweden

[NeTEx Sweden](https://www.trafiklab.se/api/trafiklab-apis/netex-sweden/) yra duomenų rinkinys apimantis didžiąją dalį
Švedijos viešojo transporto kelionių duomenų NeTEx
formatu. Duomenų rinkinys yra prieinamas, kaip vienas NeTEx duomenų failas. Šis duomenų rinkinys yra analogiškas
GTFS Sweden 3, tik duomenys yra prieinami NeTEx formatu bei šiuo formatu grįžta papildomi duomenys, kurių negalima
pateikti GTFS formatu.

## KoDa (istoriniai duomenys)

[KoDa (Kollektivtrafikens Datalabb)](https://www.trafiklab.se/api/trafiklab-apis/koda/) pagrindinis tikslas rinkti,
saugoti ir teikti istorinius statinius bei dinaminius duomenis. Istoriniai statiniai viešojo transporto
kelionių duomenys yra prieinami GTFS formatu, dinaminiai - GTFS Realtikme formatu. Šie duomenų rinkiniai yra
teikiami pagal operatorių ir datą. Šie duomenys leidžia atlikti istorinę duomenų analizę, kurti dirbtiniu intelektu
grįstus modelius bei naudoti duomenis siekiant priimti geresnius sprendimus.

Istorinius duomenis galima pasiimti ne tik per API. Duomenys taip pat saugomi _Apache Cassandra_ duomenų bazėje.
Siekiant palengvinti duomenų analizę taip pat gali būti suteikta prieiga prie KoDa JupyterHub.

## Kiti duomenys ar duomenų rinkiniai

- [Trafikverket Open API](https://www.trafiklab.se/api/trafiklab-apis/trafikverket/) - API skirta informacijai apie
  skirta informacijai apie kelių ir geležinkelių eismą
  gauti.
- [SL's APIs](https://www.trafiklab.se/api/trafiklab-apis/sl/) - API skirtas gauti informaciją apie planuojamą ir
  realaus laiko eismą.
- [Oxyfi-Realtidspositionering](https://www.trafiklab.se/api/trafiklab-apis/oxyfi/) - realaus laiko traukinių
  pozicijų duomenys gaunami per Web Socket protokolą;

## Naudingos nuorodos

- [Techninis Samtrafiken atvirų duomenų vadovas](https://samtrafiken.atlassian.net/wiki/spaces/SamtrafikenOpenData/overview?homepageId=992739505)