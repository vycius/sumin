# Statinių duomenų išvestis

## Vežėjų informacija

### Vežėjų informacijos atvėrimas

VINTRA saugo informaciją apie vežėjus, tačiau ši informacija nėra atverta.

Remiantis [GTFS specifikacija](https://gtfs.org/schedule/reference/#attributionstxt) šia informacija galima atverti
GTFS rinkinyje sukuriant `attributions.txt` failą su informacija apie vežėjus.

Toliau pateikiamas tokio failo pavyzdys adaptuotas pagal [Klaipėdos GTFS](http://stops.lt/klaipeda/klaipeda/gtfs.zip)
duomenų rinkinį.

:::{admonition} Informacija apie maršrutus aptarnaujančius vežėjus (GTFS attributions.txt)

```csv
route_id,organization_name,is_operator,attribution_url,attribution_email,attribution_phone
klaipeda_bus_M5,Kautra,1,https://www.kautra.lt,klaipeda@kautra.lt,861290007
klaipeda_bus_M6,Kautra,1,https://www.kautra.lt,klaipeda@kautra.lt,861290007
klaipeda_bus_M8,Ridvija,1,,,841500800
```

:::

Informacija apie vežėjus rekomenduojama atverti ir NeTEx duomenų rinkiniuose.

## Sustojimo vietos

### Visų Sustojimo vietų atvėrimas

TODO: Gerosios užsienio šalių patirtys

```csv
stop_id,stop_name,stop_lat,stop_lon,stop_code,stop_desc,zone_id,stop_url,location_type,parent_station,wheelchair_boarding,stop_timezone,vehicle_type,platform_code
3913,Stankutiškės,54.620421,25.389962,,,3913,"https://www.visimarsrutai.lt/#/stop/result?stopId=3913",,,,,,
4751,Lyta,54.698099,25.493329,,,4751,"https://www.visimarsrutai.lt/#/stop/result?stopId=4751",,,,,,
```