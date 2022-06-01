# Duomenų teikimas

Visų savivivaldybių ir vežėjų viešojo keleivinio transporto duomenys yra kaupiami „Vintra“ informacinėje sistemoje
(Viešojo transporto kelionių duomenų informacinėje sistemoje, toliau VINTRA). Tai informacinė sistema į kurią patenka
duomenys apie stotis, stoteles, maršrutus, maršrutų trasos trajektorijas, reisus, tvarkaraščius, vežėjus, tarifus,
realaus laiko transporto priemonių geografinę padėtį ir kt.

> 13<sup>1</sup> straipnis 3 dalis: **Viešojo keleivinio transporto kelionių duomenys kaupiami viešojo transporto
> kelionių duomenų informacinėje sistemoje**, kurios valdytoją paskiria Vyriausybė ar jos įgaliota institucija. Viešojo
> transporto kelionių duomenų kaupimo tvarką nustato Vyriausybė ar jos įgaliota institucija. **Vežėjai ir savivaldybės
> teikia viešojo transporto kelionių duomenis, susijusius su tvarkaraščiais ir tarifais**, ir informuoja duomenų
> tvarkytoją
> apie jų pasikeitimus.
>
> -- <cite>Lietuvos Respublikos transporto veiklos pagrindų
> įstatymas{cite}`transporto_veiklos_pagrindu_istatymas`</cite>

Pagal transporto veiklos pagrindų įstatymą{cite}`transporto_veiklos_pagrindu_istatymas` ir viešojo transporto kelionių
duomenų kaupimo tvarkos aprašą{cite}`sumin_vintra_duomenu_kaupimo_tvarka` (priimtą 2014-05-21) keleiviai ne tik
turėtų gauti informaciją
apie viešojo keleivinio transporto maršrutus, tvarkaraščius, tarifus visoje Lietuvoje, tačiau ir stovėdami bet kurioje
Lietuvos viešojo transporto stotelėje ar stotyje realiu laiku telefone turėtų matyti atvykstant į autobusą bei žinoti
kiek faktiškai jis vėluos.

# Duomenų teikimo privalomumas

Keleivinio transporto duomenis į VINTRA privalomai teikia{cite}`sumin_vintra_duomenu_kaupimo_tvarka`:

1. Lietuvos automobilių kelių direkcija prie Susisiekimo ministerijos;
2. Lietuvos transporto saugos administracija, valdanti ir organizuojanti keleivių vežimą tolimojo ir tarptautinio
   reguliariojo susisiekimo maršrutais;
3. Savivaldybių institucijos arba jų įgaliotos įstaigos, valdančios ir organizuojančios keleivių vežimą vietinio (miesto
   ar priemiestinio) reguliariojo susisiekimo maršrutais;
4. Oro ir jūrų uostus valdančios įmonės;
5. Vežėjai, teikiantys keleivių vežimo viešuoju geležinkelių transportu paslaugas;
6. Vežėjai, teikiantys keleivių vežimo viešuoju jūrų ir vidaus vandenų transportu paslaugas;
7. Vežėjai, teikiantys keleivių vežimo reguliariojo susisiekimo kelių transporto maršrutais paslaugas ir turintys
   atitinkamą paslaugų teikimo licenciją arba leidimą.

Toliau pateikiama lentelė, kurioje vaizduojama kokie duomenys turi būti teikiami pagal transporto
rūšį{cite}`sumin_vintra_duomenu_kaupimo_tvarka`:

```{table} Į VINTRA teikiami duomenys pagal transporto rūšį remiantis duomenų kaupimo tvarkos aprašu
:name: vintra-transport-types-by-law

| Rūšis                                               | Stotys, stotelės ir kiti maršrutų punktai | Maršruto trasos trajektorija | Maršrutai | Reisai | Tvarkaraščiai | Vežėjai | Tarifai ir kainoraščiai | Transporto priemonių geografinė padėtis |
|-----------------------------------------------------|-------------------------------------------|------------------------------|-----------|--------|---------------|---------|-------------------------|-----------------------------------------|
| Vietinis reguliarusis susiekimas                    | ✔️                                        | ✔️                           | ✔️        | ✔️     | ✔️            | ✔️      | ✔️                      | ✔️                                      |
| Tolimasis ir tarptautinis reguliarusis susisiekimas | ✔️                                        | ✔️                           | ✔️        | ✔️     | ✔️            | ✔️      | ✔️                      | ✔️                                      |
| Keleiviniai traukiniai                              | ✔️                                        | ✔️                           | ✔️        | ✔️     | ✔️            | ✔️      | ✔️                      | ✔️                                      |
| Vidaus vandenų susisiekimas                         | ✔️                                        | ✔️                           | ✔️        | ✔️     | ✔️            | ✔️      | ✔️                      |                                         |
| Jūrų transportu susisiekimas                        |                                           |                              | ✔️        | ✔️     | ✔️            | ✔️      |                         |                                         |
| Lėktuvai                                            |                                           |                              | ✔️        | ✔️     | ✔️            | ✔️      |                         |                                         |
```

## VINTRA

VINTRA projekta startavo 2015 m. liepos 15 d., kaip yra centrinė vieta į kurią vežėjai ir savivaldybės
teikia viešojo transporto kelionių duomenis{cite}`transporto_veiklos_pagrindu_istatymas`. VINTRA yra skirta
„centralizuotai kaupti maršrutų, maršrutų punktų ir reisų duomenis ir vykdyti maršrutų skirtingomis viešojo transporto
rūšimis planavimą Lietuvos Respublikoje“{cite}`vintra_system`.

VINTRA informacinės sistemos sukūrimas kainavo daugiau nei 1 mln. eurų{cite}`vintra_price`, o palaikymo kaštai siekia
apie 24 tūkst. eurų be PVM per metus. Esamas VINTRA techninis tvarkytojas yra Lietuvos automobilių kelių direkcija.

### Esminės duomenų kaupimo problemos
Šiuo metu VINTRA esantys duomenys yra nepilni, dažnai nepilni, nepatikimi ar net 

- Daugiau nei trečdalio Lietuvos savivaldybių vietinio reguliariojo susisiekimo statinių duomenų iš viso nėra (21 
  savivaldybės);
- Didelės dalies savivaldybių duomenys yra nepilni, nėra reguliariai atnaujinami, yra nebeaktualūs, nėra patikimi ar 
  net klaidina keleivius (bent 14 savivaldybių);
- 7 iš 60 savivaldybių teikia vietinio reguliariojo susisiekimo transporto pozicijų duomenis, kurie būtų susieti su 
  konkrečiais reisais;
- 1 iš 37 tolimojo susisiekimo vežėjų teikia transporto pozicijų duomenis į VINTRA;
- VINTRA nėra kelionių duomenų, kuriuos privalo teikti Susisiekimo ministerijai pavaldžios institucijos pvz., 
  Lietuvos geležinkeliai, Smiltynės perkėla, Lietuvos oro uostai ir kt..


Toliau esančioje lentelėje vaizduojami pagrindiniai duomenų teikėjai ir jų į VINTRA teikiami duomenys. 

```{table} Pagrindiniai duomenų kelionių duomenų teikėjai ir jų teikiami duomenys (2022 gegužės 20 d.). 
:name: data-in-vintra

| Duomenų teikėjas                 | Statiniai duomenys    | Transporto priemonių pozicijos |
|----------------------------------|-----------------------|--------------------------------|
| Vietinis reguliarusis susiekimas | 39 iš 60 savivaldybių | 7 iš 60 savivaldybių           |
| Tolimasis susisiekimas           | 37 iš 37 vežėjų       | 1 iš 37 vežėjų                 |
| Lietuvos geležinkeliai           | Duomenų nėra          | Neteikiama                     |
| Smiltynės perkėla                | Duomenų nėra          | Neprivalo teikti               |
| Lietuvos oro uostai              | Duomenų nėra          | Neprivalo teikti               |
```