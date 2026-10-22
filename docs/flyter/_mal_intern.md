# Flytkort: <fra> → <til>: <innhold>

| Felt | Verdi |
| --- | --- |
| Flyt-ID | <f.eks. M3-MAC-…> |
| Fra → til | <f.eks. M3 → MAC, eller MAC → M3> |
| Innhold | <hva som sendes: oppdrag, ordre, etikettdata, kvittering …> |
| Integrasjonsmåte | <ION data flow / EC-avtale / M3 API kalt av systemet / fil / database / annet> |
| System | `docs/systemer/<system>.md` |
| Linje eller område | <hvor i produksjonen flyten brukes> |
| Tåler stans i | <minutter eller timer før linja merker det> |
| Sist verifisert | <ÅÅÅÅ-MM-DD> av <navn> |

## Formål

<Hva flyten gjør, og hva som skjer på linja hvis den stopper.>

## Trigger

<Hendelse i M3, jobb, eller at systemet henter selv. Hvor ofte.>

## Steg

| # | System | Objekt (navn slik det står i systemet) | Merknad |
| --- | --- | --- | --- |
| 1 | M3 | <program, API eller hendelse> | |
| 2 | <ION / EC / ION API> | <data flow, avtale, connection point eller API> | |
| 3 | <system> | <tjeneste, kø, mappe eller tabell> | |
| 4 | Linja | <AGV, skriver eller merkemaskin> | |

## Forventet volum

<Antall meldinger per skift, og når linja går. Null meldinger er bare unormalt når linja går.>

## Varsling

<Hvordan stans oppdages i dag: ION-monitor, alarm i systemet eller melding fra produksjonen. Hvem varselet går til, også utenom arbeidstid.>

## Manuell nødprosedyre

<Hva linja gjør mens flyten står, og hvem som avgjør det. Henvis til systemkortet hvis den står der.>

## Kjente feil

- <Feil> → `docs/runbooks/<fil>.md`

## Kilder i repoet

- `kilde/ion/data-flows/<fil>`
- `kilde/systemer/<system>/<fil>`
