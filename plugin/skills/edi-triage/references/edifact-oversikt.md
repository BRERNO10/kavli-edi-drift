# EDIFACT – rask oversikt

Generell referanse for EANCOM-meldinger. Partnerens MIG (`docs/partnere/` og `kilde/partnere/`) gjelder alltid foran denne.

## Konvolutt

| Segment | Betydning |
| --- | --- |
| UNA | Angir skilletegn – valgfritt |
| UNB | Utvekslingshode: avsender- og mottaker-ID (ofte GLN), dato og tid, kontrollreferanse |
| UNH | Meldingshode: meldingsreferanse og type, f.eks. `DESADV:D:96A:UN:EAN005` |
| UNT | Meldingshale: antall segmenter og meldingsreferanse – må stemme med UNH |
| UNZ | Utvekslingshale: antall meldinger og kontrollreferanse – må stemme med UNB |

## Vanlige segmenter

| Segment | Bruk | Vanlige koder |
| --- | --- | --- |
| BGM | Dokumenttype og nummer | 220 = ordre, 231 = ordresvar, 351 = leveringsmelding (DESADV), 380 = faktura |
| DTM | Datoer | 137 = dokumentdato, 2 = ønsket leveringsdato, 11 = forsendelsesdato, 17 = estimert leveringsdato |
| DTM-format | Datoformat | 102 = ÅÅÅÅMMDD, 203 = ÅÅÅÅMMDDTTMM |
| RFF | Referanser | ON = kundens ordrenummer |
| NAD | Parter | BY = kjøper, SU = leverandør, DP = leveringssted, IV = fakturamottaker |
| CPS / PAC | Pakkehierarki og antall kolli | |
| GIN | Identifikasjon av kolli | BJ = SSCC (18 siffer) |
| LIN | Varelinje | Artikkelnummer med kode EN (eldre EANCOM) eller SRV (EANCOM 2002) = GTIN |
| QTY | Antall | 21 = bestilt, 12 = sendt (DESADV), 47 = fakturert |

## Kvitteringer

| Melding | Betydning |
| --- | --- |
| CONTRL | Syntakskvittering: meldingen er mottatt og lest, eller avvist på grunn av syntaksfeil |
| APERAK | Applikasjonssvar: mottakers system har godtatt eller avvist innholdet |

## Vanlige feil

- GLN i UNB eller NAD som mottakeren ikke kjenner igjen
- GTIN i LIN som ikke finnes hos mottakeren, eller feil enhet
- SSCC i GIN som mangler, er duplisert eller ikke har 18 siffer
- Antall i UNT eller UNZ som ikke stemmer – ofte en avkuttet eller manuelt endret fil
- Feil datoformat i DTM

## XML og BOD fra ION

Rotelementet viser verb og substantiv, for eksempel `SyncSalesOrder`. `ApplicationArea` inneholder avsender (`Sender/LogicalID`), tidspunkt og `BODID`.
