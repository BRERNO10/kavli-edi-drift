# System: <navn>

| Felt | Verdi |
| --- | --- |
| Hva det gjør | <kort beskrivelse> |
| Linje eller område | |
| Eier i Kavli | <rolle> |
| Leverandør og support | <leverandør, avtale og kanal – se `docs/kontakter.md`> |
| Versjon og livsløp | <versjon, supportstatus hos leverandøren, planlagt utskifting> |
| Kjører på | <server eller tjeneste, og nett> |
| Integrasjonsmåte mot M3 | <ION data flow / EC-avtale / M3 API / fil / database / annet> |
| Tjenestekonto mot M3 | <navn på konto eller authorized app – aldri passord. Utløp i `docs/kalender.md`> |
| Logger | <hvor de ligger, hvem som har tilgang, og hvor lenge de beholdes> |
| Tåler stans i | <minutter eller timer før linja merker det> |
| Sist verifisert | <ÅÅÅÅ-MM-DD> av <navn> |

## Flyter

- `docs/flyter/intern_<…>.md`

## Konsekvens ved stans

<Hva som skjer på linja, og etter hvor lang tid.>

## Manuell nødprosedyre

<Hva produksjonen gjør mens systemet eller flyten står, og hvem som avgjør det.>

## Varsling og eskalering

<Hvem som varsles først, for eksempel vakt eller skiftleder, og når leverandøren kontaktes. Se `docs/kontakter.md`.>

## Kvalitet og sporbarhet

<Fylles ut for systemer som påvirker merking eller sporbarhet: hva som kan bli feil (f.eks. holdbarhetsdato, batch eller GTIN), hvem i kvalitet som varsles, og hvem som avgjør om varer sperres.>

## Vanlige feil

- <Feil> → `docs/runbooks/<fil>.md`

## Kilder i repoet

- `kilde/systemer/<system>/`
