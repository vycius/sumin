# NeTEx

NeTEx (angl. *Network Timetable Exchange*) - [Europos standartizacijos komiteto](https://www.cencenelec.eu) sukurtas
standartas skirtas viešojo transporto duomenų apsikeitimui. Šis formatas turi būti naudojamas visų Europos operatorių
pagal
direktyvą [dėl informacijos apie keliavimą daugiarūšiu transportu paslaugų teikimo (2010/40/ES)](https://eur-lex.europa.eu/legal-content/LT/TXT/HTML/?uri=CELEX:32017R1926&from=LT)
siekiant integruoti skirtingas Europos Sąjungos transporto sistemas.

## Naudojimo ES šalyse privalomumas

NeTEx formatas turi būti naudojamas visų ES šalių. Toliau pateikiama ištrauka iš 2010/40/ES direktyvos.


> (16) dėl keitimosi statiniais reguliariojo susisiekimo, pvz., viešojo transporto, tolimojo susisiekimo autobusų ir
> jūrlaivių, įskaitant keltus, duomenimis pasakytina, kad tokiems duomenims nacionaliniuose prieigos punktuose **turėtų
būti naudojamas Europos standartizacijos komiteto nustatytas keitimosi duomenimis standartas NeTEx CEN/TS 16614**,
> grindžiamas koncepciniu transporto pamatinių duomenų modeliu EN 12896:2006 ir paskesnėmis atnaujintomis jo
> redakcijomis,
> arba kitoks kompiuterio skaitomas formatas, kurio visiškas suderinamumas būtų užtikrintas iki sutarto termino.
>
> -- <cite>Europos Parlamento ir Tarybos direktyvos 2010/40/ES nuostatos dėl informacijos apie keliavimą daugiarūšiu
> transportu paslaugų teikimo{cite}`directive_multimodal_travel_information_services`</cite>

## Skirtumai lyginant su GTFS

NeTEx ir GTFS formatus galime laikyti vienas kitą papildančiais ir apimančiais skirtingus duomenų valdymo proceso
etapus. Lyginant su GTFS formatu NeTEx gali pateikti išsamesnę informaciją apie viešojo transporto sistemą pvz.,
platesnę informaciją apie infrastruktūrą, tvarkaraščius, kainodarą, persėdimus ir t.t. NeTEx naudoja XML (angl. *
Extensible Markup Language*) formatą duomenims perduoti. Verta pastebėti, kad iš NeTEx formato automatiniu būdų galima
sugeneruoti GTFS formatą (tačiau atvirkščia konversija nėra įmanoma){cite}`netex_comparison_to_other_formats`.

TODO:
Factsheet https://www.transmodel-cen.eu/wp-content/uploads/2017/07/Mobility-Factsheet-Road-Initiatives_DIGITALISATION_v4-1.pdf

## Pateikiama informacija

NeTEx yra ganėtinai sudėtingas formatas grįstas [koncepciniu transporto pamatinių duomenų modeliu (angl. *
Transmodel*)](https://www.transmodel-cen.eu). Toliau pateikiama pagrindinė informacija, kuri gali būti perduodama
naudojantis šiuo formatu{cite}`mobi_data_lab_data_sharing_standarts`:

- Viešojo transporto tvarkaraščiai, stotelės, maršrutai;
- Transporto operatoriaus informacija;
- Dienos, kuriomis teikiamos paslaugos ir taikomos išimtys (pvz., švenčių dienomis);
- Sudėtingi maršrutai (pvz., žiediniai maršrutai)
- Sudėtinės kelionės perlipant į kitas transporto priemones;
- Bilietų tipai (pvz., vienkartiniai bilietai, dienos bilietai, sezoniniai bilietai)
- Bilietų tarifų taikymas (pvz., fiksuoti tarifai, zoniniai tarifai);
- Duomenys apie paslaugų prieinamumą;
