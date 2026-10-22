---
name: flytkart
description: Forklarer hvordan Kavlis integrasjonsflyter rundt Infor M3 CloudSuite henger sammen – EDI med kunder og leverandører via Enterprise Collaborator og ION, og interne flyter mellom M3 og systemer i produksjonen, som MAC (AGV-klient) og Quickdesign – og hva som rammes når et ledd stopper. Bruk når noen spør hvordan en flyt går, hvilke partnere som får DESADV, hvilke flyter eller systemer som bruker en connection point, avtale eller API, eller hva som påvirkes hvis ION, en kanal, et system eller en partner er nede. Ikke for feilsøking av én konkret feil – da gjelder edi-triage eller intern-triage.
---

# Flytkart (Kavli)

Gi oversikt over integrasjonsflytene og avhengighetene mellom dem, både EDI og interne flyter i produksjonen. Feilsøking av en konkret hendelse hører til edi-triage eller intern-triage.

## Kunnskapsgrunnlag

- `references/gen-flyter.md` – alle flytkort, EDI (`edi_…`) og interne (`intern_…`), med steg og objektnavn
- `references/gen-partnere.md` – EDI-partnere og meldingstyper
- `references/gen-systemer.md` – interne systemer: integrasjonsmåte, konsekvens ved stans og hvor lenge linja tåler stans
- `references/gen-status.md` – hvilke flyter, connection points og monitors som er aktive i ION
- `references/gen-kilde-indeks.md` – eksporter i repoet, med dato

Filene starter med byggedato. Oppgi alltid datoen på kunnskapen du bygger på.

## Arbeidsflyt

1. Finn flyten eller objektet spørsmålet gjelder: navn, meldingstype, partner, system, avtale, connection point eller API.
2. For «hvordan går flyten»:
   - EDI: beskriv stegene fra trigger i M3 (dokument og variant i CRS945) via EC-avtale og ION data flow til connection point og partner, med objektnavn.
   - Intern: beskriv stegene fra trigger i M3 via integrasjonsleddet (ION, EC eller API) til systemet og linja, med objektnavn.
3. For «hva rammes»: finn alle flyter som bruker objektet, både EDI og interne. Ta med status fra `gen-status.md` og konsekvens ved stans – frist mot partner for EDI, og hvor lenge linja tåler stans for interne flyter. List flytene med kortest tid før konsekvens først.
4. Oppgi «Sist verifisert» for hvert flytkort og systemkort, og datoen på statuslisten. Stemmer ikke flytkort og eksport overens, påpek avviket.

## Svarformat

Kort forklaring, deretter en tabell:

| Flyt | Type | Motpart | Retning | Objekter | Status | Konsekvens ved stans | Sist verifisert |
| --- | --- | --- | --- | --- | --- | --- | --- |

Type er EDI eller intern. Motpart er partneren eller systemet.

## Regler

- Bruk bare objektnavn som står i kunnskapsgrunnlaget. Mangler noe, si det rett ut.
- Ikke anbefal endringer i oppsettet. Slike spørsmål følges opp av driftsansvarlig eller systemeier.
