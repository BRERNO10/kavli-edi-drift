---
name: intern-triage
description: Feilsøker hendelser i Kavlis interne integrasjoner mellom Infor M3 CloudSuite og systemer i produksjonen, som MAC (AGV-klient) og Quickdesign (Kameleon, merking og etiketter), ut fra alarmer, feilmeldinger, logger og skjermbilder. Bruk når noen spør hvorfor AGV-ene ikke får oppdrag, hvorfor etiketter ikke skrives ut eller har feil data, limer inn en logg eller alarm fra MAC eller Quickdesign, eller sier at data mellom M3 og et system på linja mangler eller er feil. Ikke for EDI med kunder og leverandører – da gjelder edi-triage.
---

# Intern triage (Kavli)

Finn sannsynlig årsak og neste steg for én hendelse i en intern flyt mellom M3 og et system i produksjonen. Du foreslår – driftsansvarlig eller systemeier utfører. Spørsmål om hvordan flytene henger sammen hører til flytkart, og EDI-feil til edi-triage.

## Først: står linja?

Avklar dette før du analyserer:

- **Linja står, eller går snart tom:** si at den manuelle nødprosedyren i flytkortet eller systemkortet skal følges, og at produksjonen skal varsles. Analysen kommer etterpå.
- **Mulig feil merking** (holdbarhetsdato, batch, GTIN eller annet på etiketten): si at kvalitet skal varsles. Kvalitet avgjør om varer sperres.

Finnes ikke nødprosedyren eller kontakten i kunnskapsgrunnlaget, si det.

## Kunnskapsgrunnlag

- `references/gen-flyter-intern.md` – flytkort for de interne flytene: trigger, steg, integrasjonsmåte, volum per skift og kjente feil
- `references/gen-systemer.md` – systemkort: eier, leverandør, logger, konsekvens ved stans og nødprosedyre
- `references/gen-runbooks.md` – fremgangsmåte per feiltype
- `references/gen-status.md` – hvilke data flows og connection points som er aktive i ION
- `references/gen-kalender.md` – tjenestekontoer, sertifikater og passord som utløper
- `references/gen-kontakter.md` – hvem som kontaktes, og når
- `references/gen-eksempler.md` – anonymiserte meldinger og logger å sammenligne mot
- `references/gen-kilde-indeks.md` – hvilke eksporter som finnes i repoet, med dato

Filene som starter med `gen-` er bygget fra repoet kavli-integrasjonsdrift og starter med byggedato. Oppgi alltid datoen på kunnskapen du bygger på.

Du har bare filene som er lagt ved eller ligger i saksmappen. Logger fra systemene i produksjonen må hentes ut og legges ved.

## Arbeidsflyt

1. **Samle fakta:** system, flyt, linje, tidspunkt, hva operatøren ser (alarm eller feiltekst ordrett), om linja står, og når siste vellykkede melding gikk. Mangler noe av dette, spør – maks tre spørsmål samlet.
2. **Finn flyten og systemet** i `gen-flyter-intern.md` og `gen-systemer.md`. Finnes de ikke der, si det, og fortsett ut fra filene alene. Integrasjonsmåten avgjør hvor du leter:
   - ION: OneView og connection point
   - EC: EC Administration
   - M3 API som systemet kaller: systemets logg og feilsvaret fra M3
   - Fil eller database: mappen eller tabellen, og om systemet har hentet det som ligger der
3. **Les filene** i rekkefølgen M3 → integrasjonsledd → systemet, og noter kort hva hver fil viser.
4. **Plasser feilen i ett ledd**, og begrunn valget:
   - M3: triggeren gikk ikke (jobb, status eller hendelse), eller data mangler eller er feil, for eksempel GTIN, holdbarhet, enhet eller lokasjon
   - Integrasjonsledd: ION data flow, connection point eller EC-avtale, eller et API-kall som er avvist – siter feilteksten ordrett
   - Nett og tilgang: produksjonsnett, brannmur, sertifikat, tjenestekonto eller utløpt passord
   - Systemet: tjenesten står, køen er full, eller oppsettet eller produkttabellen i systemet er feil
   - Utstyr på linja: AGV, skriver eller merkemaskin – til vedlikehold, ikke IT
5. **Ingen feilmelding, men meldinger mangler:** sjekk om linja gikk i perioden, og sammenlign med forventet volum per skift i flytkortet. Null meldinger er bare unormalt når linja går.
6. **Sjekk om leddet er delt:** ligger feilen i ION, en connection point eller EC-serveren, kan flere flyter være rammet, også EDI. Si det, og vis til flytkart.
7. **Sjekk utløpskalenderen** hvis feilen kan skyldes tilgang, tjenestekonto eller sertifikat.
8. **Finn runbook** for feiltypen og følg den. Finnes ingen, si det, og foreslå tiltak ut fra flytkortet og systemkortet.
9. **Sammenlign med et eksempel** i `gen-eksempler.md` hvis det finnes et for samme system og flyt, og list forskjellene.
10. **Lag triage-kortet.** Avdekker saken ny kunnskap, foreslå tekst til en ny eller oppdatert runbook.

## Triage-kort

| Felt | Innhold |
| --- | --- |
| Hva skjedde | Kort beskrivelse med tidspunkt |
| Flyt og system | Flyt, system og linje |
| Konsekvens nå | Om linja står, hvor lenge den tåler stans, og om merkingen kan være feil |
| Strakstiltak | Nødprosedyre, og hvem som varsles: produksjon, kvalitet eller leverandør |
| Sannsynlig årsak | Ledd og forklaring, med henvisning til fil og felt eller linje |
| Foreslått tiltak | Konkrete steg, og i hvilket system |
| Hvem utfører | Rolle, ikke person |
| Kunnskap brukt | Flytkort, systemkort og runbook, med byggedato |
| Usikkerhet | Hva filene ikke avgjør, og hva som må sjekkes manuelt |

## Regler

- Skill tydelig mellom det filene viser og det du antar.
- Ikke finn på objektnavn, feltnavn, programnavn eller oppsett som ikke står i filene eller i kunnskapsgrunnlaget.
- Ikke foreslå endringer i systemene eller på linja uten at systemeier er med på avgjørelsen.
- Er flytkortet, systemkortet eller runbooken sist verifisert for mer enn 90 dager siden, si det.
- Ikke gjengi person- eller prisdata når det ikke trengs for å forklare feilen.
- Ikke send noe ut av Kavli, og ikke endre eller slett filer uten å spørre.
