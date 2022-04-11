# Judumo duomenų ekosistemos plėtra

Kiekvieną dieną po miestą judame mums patogiausiais būdais: vieni tą darome naudodamiesi viešuoju transportu,
dviračiais, paspirtukais, kiti automobilių dalijimosi, pavežėjimo paslaugomis. Dažnai naudojame ne vieną, o keletą
skirtingų transporto rūšių. Siekdami, kad judėjimo patirtis būtų kuo malonesnė, sklandesnė ir sutaupytume kuo daugiau
laiko pasitelkiame programas pvz., Trafi, Google Maps, Apple Maps. Visų šių programų veikimui yra reikalingi atviri,
tikslūs su judumu susiję duomenys.

## Pagrindiniai faktai
- 2019 m. Lietuva buvo **pirma ES** pagal kelionių atliktų automobiliu kiekį (90.6%){cite}`eurostat_model_split_of_passenger_transport`;
- 2019 m. Lietuva pagal automobilių skaičiaus prieaugį 1000 gyv. buvo **antra ES** (24% prieaugis 2019 m. lyginant su 2015 m.){cite}`eurostat_passenger_cars`;
- Susisiekimo ministerija koordinuoja ir leidžia teisės aktus susijusius su intelektinių transporto sistemų diegimu ir 
  naudojimu{cite}`transporto_veiklos_pagrindu_istatymas`;
- Statiniai viešojo transporto duomenys turi būti teikiami bent jau `NeTEx` formatu, o realaus laiko bent jau `SIRI`
  formatu pagal direktyvos 2010/40/ES nuostatas{cite}`directive_multimodal_travel_information_services`</cite>;
- VINTRA tvarkytojo LAKD (*VĮ Lietuvos automobilių kelių direkcija*) funkijų atlikimui nėra reikalingi viešojo 
  transporto duomenys;
- Per dieną VINTRA (visimarsrutai.lt) aplanko **apie 10 unikalių lankytojų** (TODO patikrinti su LAKD);
- VINTRA skelbiami **statiniai viešojo transporto duomenys yra pasenę** (23 savivaldybių duomenys neturi nė vieno 
  galiojančio reiso); 
- VINTRA `NeTEx` formatu pateikiami 8 Lietuvos savivaldybių viešojo transporto statiniai duomenys;
- **VINTRA neteikia jokių realaus laiko atvirų duomenų**;
- **Nė viena Lietuvos savivaldybė** neteikia viešojo transporto realaus laiko duomenų `SIRI` ar `GTFS-Realtime` 
  formatais.
- 11 savivaldybių naudojama Stops.lt sistema statiniams duomenims atiduoti palaiko tik `GTFS` formatą, o **realaus laiko 
  duomenims nepalaiko jokio standartizuoto formato**;
- Apple Maps Transit **neveikia Lietuvoje** (veikia Estijoje ir 17 kitų ES šalių);
- Google Maps Transit Lietuvoje **neturi realaus laiko atvykimų** dėl duomenų `GTFS-Realtime` formato nebuvimo;


## Projekto siekiai

Per standartizuotų judumo duomenų atvėrimą:
- Sudaryti sąlygas Lietuvos gyventojams mėgautis pačiomis patogiausiomis ir maloniausiomis kelionėmis bei keliavimo įrankiais;
- Įgalinti egzistuojančias kelionių planavimo programų pilnavertį veikimą Lietuvoje (pvz., Google Maps Transit, Apple
  Maps Transit);
- Patobulinti sąlygas Lietuvoje vystyti judumo startuolius;
- Sukurti sąlygas įgyvendinti visą Lietuvą apimančius judumo, kaip paslaugos (angl. *Mobility as a Service*) sprendimus;
- Užtikrinti darnią judumo paslaugų plėtrą Lietuvoje;

## Nauda
### Visuomenei:
- Patogesnis ir prieinamesnis keliavimas viešioju transportu;
- Sumažintas kelionės laikas (pagal realią informaciją gali koreguoti planus);
- Mažesnis laukimo laikas;

### Savivaldybėms ir transporto valdytojams:
- Išaugęs viešojo transporto naudojimas ir daugiau bilietų pardavimų;
- Lengvesnis viešojo transporto planavimas;
- Geresnis viešojo transporto vertinimas;

### Startuoliams ir akademijai:
- Nauji startuoliai grįsti atvertais duomenimis;
- Daugiau mokslinių tyrimų susijusių su transporto tinklo optimizavimu ir kokybės gerinimu;



## Nacionaliniai teisės aktai ir dokumentai

### Lietuvos susisiekimo plėtros iki 2050 m. strategija
> **1.2. tikslas. Darnus, integruotas ir įtraukus susisiekimas.** Šiuo tikslu siekiama užtikrinti, jog vartotojams būtų sudaromos sąlygos naudotis aplinkai draugiška, vartotojų poreikius atitinkančia susisiekimo sistema.

> **1.2.1. uždavinys. Vietinio (miestų ir priemiesčių) susisiekimo punktualumo, dažnumo ir išmanumo skatinimas.** Šiuo uždaviniu siekiama pritraukti gyventojus naudotis viešuoju transportu, o norint tai pasiekti būtina užtikrinti viešojo transporto patrauklumą ir patogumą vartotojui.

> **1.2.2. uždavinys. Darnaus judumo įgyvendinimo užtikrinimo ir universalaus dizaino priemonių skatinimas.** Šiuo uždaviniu siekiama įgyvendinti darnų judumą, kadangi bemotorio transporto naudojimas miestuose mažintų ŠESD, vizualinę ir triukšmo taršas, taip pat prisidėtų prie individualių automobilių skaičiaus mažinimo. Skatinant darnų judumą būtina atsižvelgti ir į riboto judumo asmenų poreikius, kad viešuoju transportu ar kitomis netaršiomis judumo alternatyvomis (įskaitant alternatyvių degalų infrastruktūra) galėtų pasinaudoti visi asmenys.

> **1.2.3. uždavinys. Integruoto regionų pasiekiamumo skatinimas.** Kadangi susisiekimas su regionais šalyje užtikrinamas nepakankamai, nėra vieningos viešojo transporto organizavimo sistemos derinant tolimąjį ir priemiestinį susisiekimą bei susisiekimą geležinkeliu, taip pat dėl mažo gyventojų skaičiaus atokiose gyvenvietėse, UPP teikimo vietų išlaikymas yra netvarus, todėl šiuo uždaviniu siekiama užtikrinti integruotą ir prieinamą paslaugų teikimą taikant modernius sprendimus regionuose.

> **1.2.4. uždavinys. Intermodalumo ir funkcinio suderinamumo skatinimas keleivių ir krovinių vežimuose.** Šiuo uždaviniu siekiama skatinti transporto rūšių integruotumą bei intermodalumą, kadangi šalyje trūksta skirtingų transporto rūšių suderinamumo, neišnaudojamas vidaus vandenų, geležinkelių transporto potencialas krovinių vežimui (kroviniai daugiausiai vežami kelių transportu, o tai lemia didesnes ŠESD emisijas), nėra vieningos viešojo transporto sistemos derinant susisiekimą skirtingomis transporto rūšimis.

### Nacionalinės susisiekimo plėtros 2014–2022 m. programa

> **Tikslas:** užtikrinti miesto ir priemiesčio įvairių rūšių viešojo transporto maršrutų suderinamumą ir didesnę jų sąveiką su privačiu transportu.
>
> **Uždavinys:** skatinti viešojo transporto naudojimą padidinus jo patrauklumą ir prieinamumą, ypač priemiesčių gyventojams, užtikrinti įvairių judumo mieste alternatyvų sąveiką; plėtoti kombinuotas viešojo ir privataus transporto sąveikos sistemas (angl. Park&Ride), taip pat taikyti kitas priemones, keičiančias visuomenės judumo įpročius ir didinančias miesto transporto darną.

> **Tikslas:** didinti krovinių ir keleivių judumą.
>
> **Uždavinys:** kurti ir diegti intelektinės transporto sistemos, technologijas, inovatyvias mobilumo paslaugas ir produktus, kurie padėtų užtikrinti geresnį keleivių ir krovinių judumą, sumažinti išmetamą šiltnamio efektą sukeliančių dujų kiekį, taip pat mažinti į aplinkos orą išmetamą teršalų kiekį.

> **Tikslas:** skatinti vietinio (miestų ir priemiesčių) transporto sistemos darnumą.
>
> **Uždavinys:** skatinti gyventojus naudotis viešuoju transportu ir didinti viešojo transporto patrauklumą, atnaujinant transporto priemones, gerinant viešojo transporto infrastruktūrą, diegiant universalaus dizaino sprendimus, didinti viešojo transporto prieinamumą, diegti viešojo transporto pirmumo sistemas ir plačiau taikyti intelektinės transporto sistemos sprendimus.

### Aštuonioliktosios Lietuvos Respublikos Vyriausybės programa

> 141.2. Darnios transporto sistemos plėtra. Plėsime elektrifikuoto geležinkelių tinklo, spartaus elektromobilių įkrovimo tinklo, dviračių ir pėsčiųjų takų ir (ar) trasų infrastruktūrą, kursime viešojo ir privataus transporto sąveikos ir darnaus judumo sistemas, gerinsime judumo sąlygas ir judumo paklausos valdymą, mažinsime transporto triukšmo taršą.


> 141.3. Užtikrinsime tolygią susisiekimo tinklo plėtrą. Susisiekimo infrastruktūrą jungsime į vieningą ir nacionaliniu mastu skirtingas transporto rūšis integruojantį tinklą. Bendradarbiaudami su savivaldybėmis stiprinsime šalies vidaus susisiekimo sistemą – didindami junglumą tarp miestų, mažindami kaimo ir mažų bei vidutinių miestų atokumą, transporto srautus miestuose, modernizuodami geležinkelių infrastruktūrą, didindami jos patrauklumą keleiviams ir kroviniams vežti. Siekdami didinti keleivių ir krovinių judumą, pagerinsime Lietuvos tarptautinį susisiekimą su Europos Sąjungos ir trečiosiomis šalimis kelių, geležinkelių, oro, jūrų ir vidaus vandenų transportu.`

> 141.5. Susisiekimo sektoriaus skaitmeninimas. Siekdami stiprinti Lietuvos transporto sektoriaus konkurencingumą, kartu su socialiniais partneriais parengsime ir įgyvendinsime Lietuvos transporto sektoriaus skaitmeninimo veiksmų planą, apimantį finansinius instrumentus e. transporto priemonių plėtrai. Imsimės regioninės lyderystės skatinti bendrus skaitmeninimo projektus su kaimyninėmis šalimis, siekdami kurti integralią ateities susisiekimo ekosistemą.

> 141.6. Diegsime automatizuotas ir išmanias eismo valdymo sistemas, kurios sudarytų sąlygas saugesniam, efektyvesniam ir tvaresniam transportui. Taikydami įvairias informacines ir ryšių technologijas visoms keleivių ir krovinių transporto rūšims, diegsime saugaus eismo gerinimo priemones, įgyvendindami valstybinę eismo saugumo programą „Vizija – nulis“. Integruosime esamas technologijas, kartu skatindami kurti naujas paslaugas susisiekimo sektoriuje, užtikrinant naujų darbo vietų kūrimą ir sektoriaus plėtrą. Skatinsime intensyvų transporto skaitmenizavimo procesą, skirtą pralaidumui didinti ir transporto rūšių ir paslaugų sąveikai gerinti, prisitaikant prie geografinių ir struktūrinių logistikos pasikeitimų.

## Užrašai

Be infrastruktūros trūkumų, judumo trukdžių taip pat kelia nepatogūs viešojo transporto maršrutai ir tvarkaraščiai,
nesusietos savivaldybių viešojo transporto sistemos arba nepakankamos paskatos ar parama reguliariai į
darbą https://ec.europa.eu/info/sites/default/files/file_import/2019-european-semester-country-report-lithuania_lt.pdf

- Data Management and Policy. Agencies must prioritize data. Just as dedicating staff and resources is crucial to the
  success of a large capital project, agency leadership must commit to and invest in the internal infrastructure that
  will support good data.
- Data Quality. No matter the quantity of available data, its usefulness ultimately hinges upon its quality. In other
  words, more is not necessarily better. The weather app on my phone shows me relative humidity, dew point, visibility,
  and pressure, but it’s of no use to me if it never accurately predicts the rain in Portland.
- Data Specifications. At the risk of sounding too “kumbaya,” we are all on the same team in the transit data world.
  That is, we all benefit when data is open and standardized. This enables industry growth and innovation. GTFS is a
  perfect example.
  https://trilliumtransit.com/2019/10/01/data-transit-riders-want/
- Viena pagrindinių priežasčių, kodėl žmonės nesinaudoja viešuoju transportu **yra informacijos apie maršrutus ir planavimo priemonių stoka**;
