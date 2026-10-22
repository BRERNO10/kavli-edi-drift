# System: Quickdesign (Kameleon)

| Felt | Verdi |
| --- | --- |
| Hva det gjør | Programvare fra Domino for design av merkemeldinger og etiketter og styring av utskriften på linja. <Utdyp: hvilke linjer, skrivere og etiketter hos Kavli, og hva den får fra M3.> |
| Linje eller område | <fyll inn> |
| Eier i Kavli | <rolle> |
| Leverandør og support | <Domino eller Kameleon – avklar hvem som har supportavtalen> |
| Versjon og livsløp | <versjon>. Domino har avviklet QuickDesign-serien og oppgir Domino Automation som erstatning ([Domino](https://domino-printing.com/en-us/products/legacy/quickdesign), sjekket 2026-10-22). <Avklar supportstatus for versjonen Kavli bruker, og om utskifting er planlagt.> |
| Kjører på | <server eller tjeneste, og nett> |
| Integrasjonsmåte mot M3 | <ION data flow / EC-avtale / M3 API / fil / database / annet> |
| Tjenestekonto mot M3 | <navn på konto eller authorized app – aldri passord> |
| Logger | <hvor de ligger, hvem som har tilgang, og hvor lenge de beholdes> |
| Tåler stans i | <minutter eller timer før linja merker det> |
| Sist verifisert | Ikke verifisert – påbegynt 2026-10-22 |

## Flyter

- <Flytkortene for Quickdesign, f.eks. `docs/flyter/intern_M3-Quickdesign_<innhold>.md`>

## Konsekvens ved stans

<Hva som skjer på linja når etiketter eller merking ikke kan skrives ut, og etter hvor lang tid.>

## Manuell nødprosedyre

<Hva produksjonen gjør mens Quickdesign eller flyten står, og hvem som avgjør det.>

## Varsling og eskalering

<Hvem som varsles først, og når leverandøren kontaktes.>

## Kvalitet og sporbarhet

Quickdesign påvirker merkingen. <Fyll inn: hva som kan bli feil (f.eks. holdbarhetsdato, batch eller GTIN), hvem i kvalitet som varsles, og hvem som avgjør om varer sperres.>

## Vanlige feil

- <Feil> → `docs/runbooks/<fil>.md`

## Kilder i repoet

- `kilde/systemer/quickdesign/`
