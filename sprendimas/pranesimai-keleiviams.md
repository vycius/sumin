# Pranešimų keleiviams redaktorius

Keleivis stovi stotelėje ir laukia atvykstančios transporto priemones, tačiau dėl įvykusios didelės avarijos ar
mieste vykstančio renginio buvo laikinai pakeistas maršrutas. Kaip apie tokius įvykius informuoti stotelėje
laukiantį ar kelionę planuojantį keleivį?

## Esama situacija

Šiuo metu Lietuvoje dažniausiai tokia informacija keleiviams teikiama per socialinius tinklus ar vežėjų interneto
svetaines. Teiakint pranešimus tokiais būdais ypač sunku užtikrinti, kad keleiviai pamatys pranešimus tuomet kada to
reikia. Taip pat keleiviai matys informacinius pranešimus, kurie nebūtinai yra susiję su jų kelione.

```{figure} /images/sprendimai/pranesimai-keleiviams/73-autobusas-pasikeitimai.png

JUDU skelbiami informaciniai pranešimai [Facebook paskyroje](https://www.facebook.com/susisiekimo.paslaugos). 
```

## Standartizuoti pranešimai keleiviams

Kitose šalyse pranešimai keleiviams yra susiejami su stotele, maršrutu, reisu, vežėju ir perduodami
standartizuotais formatais verslui, akademijai ir visuomenei per kelionių planavimo priemones.

```{figure} /images/apps/google-maps/google-maps-service-alerts.jpg

Google Maps pranešimai keleiviams (žr. *Modified Service* ir *Information*). [Šaltinis](https://www.dailydot.com/debug/google-maps-update-real-time-tracking-transit/).
```

## Pranešimų keleiviams duomenų modelis

Pranešimas keleiviui gali susidėti iš:

- Pranešimo antraštės, teksto ir nuorodos, kurioje pateikiama papildoma informacija (gali būti pateikiama keletu
  kalbų);
- Galiojimo laiko (pradžios ir pabaigos data bei laikas);
- Priežasties (pvz., renginys, avarija, streikas);
- Poveikio keleiviui (pvz., papildomi autobusai, maršruto pakeitimai);
- Įvykio sunkumo (pvz., informacinis pranešimas, įspėjimas);
- Paveikslėlio (eksperimentinis palaikymas);
- Susiejimo su stotelėmis, reisais, maršrutais, maršruto tipais ar agentūromis;

Taip pat galima pridėti papildomą informaciją
(
žr. [SIRI-SX gerasias praktikas](https://www.rtig.org.uk/system/files/documents/RTIG-PR015-D003-0.2%20SIRI-SX%20Best%20Practice.pdf))

## Rinkoje siūlomi produktai

### Google Transit

Paprasčiausias ir visiškai nemokamas būdas pridėti pranešimus keleiviams yra
naudojant
[Google Transit redaktorių](https://support.google.com/transitpartners/answer/6384347?hl=en&ref_topic=6384208).

```{figure} /images/sprendimai/pranesimai-keleiviams/google-transit-service-alerts-editor.png

Google Transit [pranešimų valdymo redaktorius](https://support.google.com/transitpartners/answer/6384347?hl=en&ref_topic=6384208).
```

Vis dėlto, pridėjus pranešimus per Google Transit redaktorių jie bus matomi tik Google Maps. Taip prarasime galimybę
pranešimus perduoti verslui, akademijai ar kitoms kelionių planavimo priemonėms. Dėl šios priežasties pranešimų
valdymas turėtų būti viešojo transporto koordinavimo sistemos dalis.

### Trillium Transit Alerts

Trillium siūlomas pranešimų keleiviams redaktorius susideda iš 3 pagrindinių dalių, o visa į jį suvesta informacija
išvedama GTFS Realtime formatu.

#### Pranešimo informacija

```{figure} /images/sprendimai/pranesimai-keleiviams/trillium-transit-service-alerts.png

Trillium Transit Alerts pranešimo informacijos langas. [Šaltinis](https://support.trilliumtransit.com/hc/en-us/articles/360025612272).
```

#### Paveikti maršrutai

```{figure} /images/sprendimai/pranesimai-keleiviams/trillium-transit-service-alerts-routes.png

Trillium Transit Alerts su pranešimu susijusių maršrutų langas. [Šaltinis](https://support.trilliumtransit.com/hc/en-us/articles/360025612272).
```

#### Paveiktos stotelės

Visos stotelės esančios paveiktuose maršrutuose yra parenkamos automatiškai (jei nenurodama kitaip).

```{figure} /images/sprendimai/pranesimai-keleiviams/trillium-transit-service-alerts-stops.png

Trillium Transit Alerts su pranešimu susijusių stotelių langas. [Šaltinis](https://support.trilliumtransit.com/hc/en-us/articles/360025612272).
```

### Kiti produktai

- [MTC Transit Data Tools](https://mtc-datatools.readthedocs.io/en/mtc-docs/user/service-alerts/#alert-editor)
  (nemokamas, atviro kodo viešojo transporto kelionių duomenų valdymo sistema su pranešimų keleiviams valdymo
  funkcija);
- [ITO World Transit Hub](https://www.itoworld.com/ito-transit-hub/).

## Duomenų perdavimas

### GTFS Realtime

:::{admonition} GTFS Realtime kontraktas pranešimams keleiviams perduoti
:class: tip, dropdown

```proto
// An alert, indicating some sort of incident in the public transit network.
message Alert {
  // Time when the alert should be shown to the user. If missing, the
  // alert will be shown as long as it appears in the feed.
  // If multiple ranges are given, the alert will be shown during all of them.
  repeated TimeRange active_period = 1;

  // Entities whose users we should notify of this alert.
  repeated EntitySelector informed_entity = 5;

  // Cause of this alert.
  enum Cause {
    UNKNOWN_CAUSE = 1;
    OTHER_CAUSE = 2;        // Not machine-representable.
    TECHNICAL_PROBLEM = 3;
    STRIKE = 4;             // Public transit agency employees stopped working.
    DEMONSTRATION = 5;      // People are blocking the streets.
    ACCIDENT = 6;
    HOLIDAY = 7;
    WEATHER = 8;
    MAINTENANCE = 9;
    CONSTRUCTION = 10;
    POLICE_ACTIVITY = 11;
    MEDICAL_EMERGENCY = 12;
  }
  optional Cause cause = 6 [default = UNKNOWN_CAUSE];

  // What is the effect of this problem on the affected entity.
  enum Effect {
    NO_SERVICE = 1;
    REDUCED_SERVICE = 2;

    // We don't care about INsignificant delays: they are hard to detect, have
    // little impact on the user, and would clutter the results as they are too
    // frequent.
    SIGNIFICANT_DELAYS = 3;

    DETOUR = 4;
    ADDITIONAL_SERVICE = 5;
    MODIFIED_SERVICE = 6;
    OTHER_EFFECT = 7;
    UNKNOWN_EFFECT = 8;
    STOP_MOVED = 9;
    NO_EFFECT = 10;
    ACCESSIBILITY_ISSUE = 11;
  }
  optional Effect effect = 7 [default = UNKNOWN_EFFECT];

  // The URL which provides additional information about the alert.
  optional TranslatedString url = 8;

  // Alert header. Contains a short summary of the alert text as plain-text.
  optional TranslatedString header_text = 10;

  // Full description for the alert as plain-text. The information in the
  // description should add to the information of the header.
  optional TranslatedString description_text = 11;

  // Text for alert header to be used in text-to-speech implementations. This field is the text-to-speech version of header_text.
  optional TranslatedString tts_header_text = 12;

  // Text for full description for the alert to be used in text-to-speech implementations. This field is the text-to-speech version of description_text.
  optional TranslatedString tts_description_text = 13;

  // Severity of this alert.
  enum SeverityLevel {
	UNKNOWN_SEVERITY = 1;
	INFO = 2;
	WARNING = 3;
	SEVERE = 4;
  }

  optional SeverityLevel severity_level = 14 [default = UNKNOWN_SEVERITY];

  // TranslatedImage to be displayed along the alert text. Used to explain visually the alert effect of a detour, station closure, etc. The image must enhance the understanding of the alert. Any essential information communicated within the image must also be contained in the alert text.
  // The following types of images are discouraged : image containing mainly text, marketing or branded images that add no additional information. 
  // NOTE: This field is still experimental, and subject to change. It may be formally adopted in the future.
  optional TranslatedImage image = 15; 

  // Text describing the appearance of the linked image in the `image` field (e.g., in case the image can't be displayed
  // or the user can't see the image for accessibility reasons). See the HTML spec for alt image text - https://html.spec.whatwg.org/#alt.
  // NOTE: This field is still experimental, and subject to change. It may be formally adopted in the future.
  optional TranslatedString image_alternative_text = 16;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features
  // and modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}

//
// Low level data structures used above.
//

// A time interval. The interval is considered active at time 't' if 't' is
// greater than or equal to the start time and less than the end time.
message TimeRange {
  // Start time, in POSIX time (i.e., number of seconds since January 1st 1970
  // 00:00:00 UTC).
  // If missing, the interval starts at minus infinity.
  optional uint64 start = 1;

  // End time, in POSIX time (i.e., number of seconds since January 1st 1970
  // 00:00:00 UTC).
  // If missing, the interval ends at plus infinity.
  optional uint64 end = 2;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features and
  // modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}

// A descriptor that identifies an instance of a GTFS trip, or all instances of
// a trip along a route.
// - To specify a single trip instance, the trip_id (and if necessary,
//   start_time) is set. If route_id is also set, then it should be same as one
//   that the given trip corresponds to.
// - To specify all the trips along a given route, only the route_id should be
//   set. Note that if the trip_id is not known, then stop sequence ids in
//   TripUpdate are not sufficient, and stop_ids must be provided as well. In
//   addition, absolute arrival/departure times must be provided.
message TripDescriptor {
  // The trip_id from the GTFS feed that this selector refers to.
  // For non frequency-based trips, this field is enough to uniquely identify
  // the trip. For frequency-based trip, start_time and start_date might also be
  // necessary. When schedule_relationship is DUPLICATED within a TripUpdate, the trip_id identifies the trip from
  // static GTFS to be duplicated. When schedule_relationship is DUPLICATED within a VehiclePosition, the trip_id
  // identifies the new duplicate trip and must contain the value for the corresponding TripUpdate.TripProperties.trip_id.
  optional string trip_id = 1;

  // The route_id from the GTFS that this selector refers to.
  optional string route_id = 5;

  // The direction_id from the GTFS feed trips.txt file, indicating the
  // direction of travel for trips this selector refers to.
  optional uint32 direction_id = 6;

  // The initially scheduled start time of this trip instance.
  // When the trip_id corresponds to a non-frequency-based trip, this field
  // should either be omitted or be equal to the value in the GTFS feed. When
  // the trip_id correponds to a frequency-based trip, the start_time must be
  // specified for trip updates and vehicle positions. If the trip corresponds
  // to exact_times=1 GTFS record, then start_time must be some multiple
  // (including zero) of headway_secs later than frequencies.txt start_time for
  // the corresponding time period. If the trip corresponds to exact_times=0,
  // then its start_time may be arbitrary, and is initially expected to be the
  // first departure of the trip. Once established, the start_time of this
  // frequency-based trip should be considered immutable, even if the first
  // departure time changes -- that time change may instead be reflected in a
  // StopTimeUpdate.
  // Format and semantics of the field is same as that of
  // GTFS/frequencies.txt/start_time, e.g., 11:15:35 or 25:15:35.
  optional string start_time = 2;
  // The scheduled start date of this trip instance.
  // Must be provided to disambiguate trips that are so late as to collide with
  // a scheduled trip on a next day. For example, for a train that departs 8:00
  // and 20:00 every day, and is 12 hours late, there would be two distinct
  // trips on the same time.
  // This field can be provided but is not mandatory for schedules in which such
  // collisions are impossible - for example, a service running on hourly
  // schedule where a vehicle that is one hour late is not considered to be
  // related to schedule anymore.
  // In YYYYMMDD format.
  optional string start_date = 3;

  // The relation between this trip and the static schedule. If a trip is done
  // in accordance with temporary schedule, not reflected in GTFS, then it
  // shouldn't be marked as SCHEDULED, but likely as ADDED.
  enum ScheduleRelationship {
    // Trip that is running in accordance with its GTFS schedule, or is close
    // enough to the scheduled trip to be associated with it.
    SCHEDULED = 0;

    // An extra trip that was added in addition to a running schedule, for
    // example, to replace a broken vehicle or to respond to sudden passenger
    // load.
    // NOTE: Currently, behavior is unspecified for feeds that use this mode. There are discussions on the GTFS GitHub
    // [(1)](https://github.com/google/transit/issues/106) [(2)](https://github.com/google/transit/pull/221)
    // [(3)](https://github.com/google/transit/pull/219) around fully specifying or deprecating ADDED trips and the
    // documentation will be updated when those discussions are finalized.
    ADDED = 1;

    // A trip that is running with no schedule associated to it (GTFS frequencies.txt exact_times=0).
    // Trips with ScheduleRelationship=UNSCHEDULED must also set all StopTimeUpdates.ScheduleRelationship=UNSCHEDULED.
    UNSCHEDULED = 2;

    // A trip that existed in the schedule but was removed.
    CANCELED = 3;

    // Should not be used - for backwards-compatibility only.
    REPLACEMENT = 5 [deprecated=true];

    // An extra trip that was added in addition to a running schedule, for example, to replace a broken vehicle or to
    // respond to sudden passenger load. Used with TripUpdate.TripProperties.trip_id, TripUpdate.TripProperties.start_date,
    // and TripUpdate.TripProperties.start_time to copy an existing trip from static GTFS but start at a different service
    // date and/or time. Duplicating a trip is allowed if the service related to the original trip in (CSV) GTFS
    // (in calendar.txt or calendar_dates.txt) is operating within the next 30 days. The trip to be duplicated is
    // identified via TripUpdate.TripDescriptor.trip_id. This enumeration does not modify the existing trip referenced by
    // TripUpdate.TripDescriptor.trip_id - if a producer wants to cancel the original trip, it must publish a separate
    // TripUpdate with the value of CANCELED. Trips defined in GTFS frequencies.txt with exact_times that is empty or
    // equal to 0 cannot be duplicated. The VehiclePosition.TripDescriptor.trip_id for the new trip must contain
    // the matching value from TripUpdate.TripProperties.trip_id and VehiclePosition.TripDescriptor.ScheduleRelationship
    // must also be set to DUPLICATED.
    // Existing producers and consumers that were using the ADDED enumeration to represent duplicated trips must follow
    // the migration guide (https://github.com/google/transit/tree/master/gtfs-realtime/spec/en/examples/migration-duplicated.md)
    // to transition to the DUPLICATED enumeration.
    // NOTE: This field is still experimental, and subject to change. It may be formally adopted in the future.
    DUPLICATED = 6;
  }
  optional ScheduleRelationship schedule_relationship = 4;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features and
  // modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}

// Identification information for the vehicle performing the trip.
message VehicleDescriptor {
  // Internal system identification of the vehicle. Should be unique per
  // vehicle, and can be used for tracking the vehicle as it proceeds through
  // the system.
  optional string id = 1;

  // User visible label, i.e., something that must be shown to the passenger to
  // help identify the correct vehicle.
  optional string label = 2;

  // The license plate of the vehicle.
  optional string license_plate = 3;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features and
  // modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}

// A selector for an entity in a GTFS feed.
message EntitySelector {
  // The values of the fields should correspond to the appropriate fields in the
  // GTFS feed.
  // At least one specifier must be given. If several are given, then the
  // matching has to apply to all the given specifiers.
  optional string agency_id = 1;
  optional string route_id = 2;
  // corresponds to route_type in GTFS.
  optional int32 route_type = 3;
  optional TripDescriptor trip = 4;
  optional string stop_id = 5;
  // Corresponds to trip direction_id in GTFS trips.txt. If provided the
  // route_id must also be provided.
  optional uint32 direction_id = 6;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features and
  // modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}

// An internationalized message containing per-language versions of a snippet of
// text or a URL.
// One of the strings from a message will be picked up. The resolution proceeds
// as follows:
// 1. If the UI language matches the language code of a translation,
//    the first matching translation is picked.
// 2. If a default UI language (e.g., English) matches the language code of a
//    translation, the first matching translation is picked.
// 3. If some translation has an unspecified language code, that translation is
//    picked.
message TranslatedString {
  message Translation {
    // A UTF-8 string containing the message.
    required string text = 1;
    // BCP-47 language code. Can be omitted if the language is unknown or if
    // no i18n is done at all for the feed. At most one translation is
    // allowed to have an unspecified language tag.
    optional string language = 2;

    // The extensions namespace allows 3rd-party developers to extend the
    // GTFS Realtime Specification in order to add and evaluate new features and
    // modifications to the spec.
    extensions 1000 to 1999;

    // The following extension IDs are reserved for private use by any organization.
    extensions 9000 to 9999;
  }
  // At least one translation must be provided.
  repeated Translation translation = 1;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features and
  // modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}

// An internationalized image containing per-language versions of a URL linking to an image
// along with meta information
// Only one of the images from a message will be retained by consumers. The resolution proceeds
// as follows:
// 1. If the UI language matches the language code of a translation,
//    the first matching translation is picked.
// 2. If a default UI language (e.g., English) matches the language code of a
//    translation, the first matching translation is picked.
// 3. If some translation has an unspecified language code, that translation is
//    picked.
// NOTE: This field is still experimental, and subject to change. It may be formally adopted in the future.
message TranslatedImage {
  message LocalizedImage {
    // String containing an URL linking to an image
    // The image linked must be less than 2MB. 
    // If an image changes in a significant enough way that an update is required on the consumer side, the producer must update the URL to a new one.
    // The URL should be a fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See the following http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.
    required string url = 1;

    // IANA media type as to specify the type of image to be displayed. 
    // The type must start with "image/"
    required string media_type = 2;

    // BCP-47 language code. Can be omitted if the language is unknown or if
    // no i18n is done at all for the feed. At most one translation is
    // allowed to have an unspecified language tag.
    optional string language = 3;


    // The extensions namespace allows 3rd-party developers to extend the
    // GTFS Realtime Specification in order to add and evaluate new features and
    // modifications to the spec.
    extensions 1000 to 1999;

    // The following extension IDs are reserved for private use by any organization.
    extensions 9000 to 9999;
  }
  // At least one localized image must be provided.
  repeated LocalizedImage localized_image = 1;

  // The extensions namespace allows 3rd-party developers to extend the
  // GTFS Realtime Specification in order to add and evaluate new features and
  // modifications to the spec.
  extensions 1000 to 1999;

  // The following extension IDs are reserved for private use by any organization.
  extensions 9000 to 9999;
}
```

:::

### SIRI Situation Exchange (SX)

- [Norvegijos SIRI Situation Exchange (SX) profilis](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370605/SIRI-SX)