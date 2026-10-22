# Flytkort: <navn på flyt>

| Felt | Verdi |
| --- | --- |
| Flyt-ID | <f.eks. DESADV-UT> |
| Meldingstype | <DESADV / ORDERS / ORDRSP / INVOIC> |
| Retning | <inn / ut> |
| Partnere | <liste, eller «se docs/partnere/»> |
| Sist verifisert | <ÅÅÅÅ-MM-DD> av <navn> |

## Formål

<Hva flyten gjør, og hva som skjer hos partneren hvis den stopper.>

## Trigger i M3

<Hendelse eller jobb som starter flyten. Dokumentnummer og variant i CRS945. Tidspunkt hvis den går på jobbplan.>

## Steg

| # | System | Objekt (navn slik det står i systemet) | Merknad |
| --- | --- | --- | --- |
| 1 | M3 | <dokument/variant, MBM-initiator> | |
| 2 | Enterprise Collaborator | <avtale> | |
| 3 | ION | <data flow> | |
| 4 | ION | <connection point> | |
| 5 | VAN eller partner | <kanal> | |

## Forventet volum og tidsvindu

<Antall meldinger per dag eller uke, og når de normalt går.>

## Kjente feil

- <Feil> → `docs/runbooks/<fil>.md`

## Kontaktpunkter

<Partner, VAN og intern kontakt. Se også `docs/kontakter.md`.>

## Kilder i repoet

- `kilde/ion/data-flows/<fil>`
- `kilde/ec/agreements/<fil>`
