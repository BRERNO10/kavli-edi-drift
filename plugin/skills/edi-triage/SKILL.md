---
name: edi-triage
description: Feilsøker EDI-hendelser i Kavlis Infor M3 CloudSuite (Enterprise Collaborator/MEC, ION og M3) ut fra varsler, feilmeldinger, logger, XML- og RCV-filer. Bruk når noen ber om å feilsøke en EDI-feil, spør hvorfor en DESADV, ORDERS, ORDRSP eller INVOIC feilet eller ikke ble sendt, limer inn et varsel fra ION eller Enterprise Collaborator, eller nevner failed agreement, detection failed, MI-feil, OneView, Retry eller Redetect. Ikke for interne flyter mellom M3 og systemer i produksjonen, som MAC eller Quickdesign – da gjelder intern-triage.
---

# EDI-triage (Kavli)

Finn sannsynlig årsak og neste steg for én EDI-hendelse. Du foreslår – driftsansvarlig utfører alt i Enterprise Collaborator (EC), ION og M3. Spørsmål om hvordan flytene henger sammen, uten en konkret feil, hører til flytkart. Feil i interne flyter mellom M3 og systemer i produksjonen hører til intern-triage.

## Kunnskapsgrunnlag

- `references/gen-flyter-edi.md` – flytkort for EDI-flytene: trigger, steg med objektnavn, volum og kjente feil
- `references/gen-runbooks.md` – fremgangsmåte per feiltype, blant annet Retry, Redetect og Verify i EC
- `references/gen-partnere.md` – partnere, meldingstyper, særregler og tidskrav
- `references/gen-kalender.md` – sertifikater, nøkler og passord som utløper
- `references/gen-kontakter.md` – hvem som kontaktes, og når
- `references/gen-eksempler.md` – anonymiserte meldinger å sammenligne mot
- `references/gen-kilde-indeks.md` – hvilke eksporter som finnes i repoet, med dato
- `references/edifact-oversikt.md` – vanlige segmenter, koder og feil i EDIFACT

Filene som starter med `gen-` er bygget fra repoet kavli-integrasjonsdrift og starter med byggedato. Oppgi alltid datoen på kunnskapen du bygger på.

## Arbeidsflyt

1. **Samle fakta:** meldingstype, retning, partner, tidspunkt, EC UUID eller OneView meldings-ID, og feilteksten ordrett. Bruk vedlagte filer, saksmappen i SharePoint eller tekst brukeren limer inn. Mangler noe av dette, spør – maks tre spørsmål samlet.
2. **Finn flyten og partneren** i `gen-flyter-edi.md` og `gen-partnere.md`. Finnes de ikke der, si det, og fortsett ut fra filene alene.
3. **Les filene** i rekkefølgen EC → OneView → M3 → partner/VAN, og noter kort hva hver fil viser. Bruk `edifact-oversikt.md` for EDIFACT og RCV.
4. **Plasser feilen i ett ledd**, og begrunn valget:
   - Mottak og kanal: filen kom ikke frem, eller kom til feil kanal
   - Deteksjon: EC fant ingen avtale som passer filen
   - Mapping: feil i et mapping-steg eller et M3 API-kall – siter MI-feilteksten ordrett
   - M3-data: manglende eller feil masterdata (GLN, GTIN, enhet), partneroppsett (CRS945/CRS949) eller leveransestatus
   - ION: ruting, connection point eller filter
   - Partner eller VAN: avvist hos mottaker (CONTRL eller APERAK)
5. **Sjekk om leddet er delt:** ligger feilen i ION, en connection point eller EC-serveren, kan flere flyter være rammet, også interne flyter i produksjonen. Si det, og vis til flytkart.
6. **Sjekk utløpskalenderen** hvis feilen kan skyldes tilgang, sertifikat eller nøkkel.
7. **Finn runbook** for feiltypen og følg den. Finnes ingen, si det, og foreslå tiltak ut fra flytkortet.
8. **Sammenlign med et eksempel** i `gen-eksempler.md` hvis det finnes et for samme partner og meldingstype, og list forskjellene.
9. **Lag triage-kortet.** Avdekker saken ny kunnskap, foreslå tekst til en ny eller oppdatert runbook.

## Triage-kort

| Felt | Innhold |
| --- | --- |
| Hva skjedde | Kort beskrivelse med tidspunkt |
| Melding | Type, retning, partner, EC UUID og OneView meldings-ID |
| Sannsynlig årsak | Ledd og forklaring, med henvisning til fil og felt eller linje |
| Foreslått tiltak | Konkrete steg; for EC: Retry, Redetect eller Verify, med begrunnelse |
| Hvem utfører | Rolle, ikke person |
| Hastegrad | Frist mot partner, fra partnerkortet |
| Kunnskap brukt | Flytkort og runbook, med byggedato |
| Usikkerhet | Hva filene ikke avgjør, og hva som må sjekkes manuelt |

## Regler

- Skill tydelig mellom det filene viser og det du antar.
- Ikke finn på objektnavn, feltnavn, programnavn eller oppsett som ikke står i filene eller i kunnskapsgrunnlaget.
- Er flytkortet eller runbooken sist verifisert for mer enn 90 dager siden, si det.
- Ikke gjengi person- eller prisdata når det ikke trengs for å forklare feilen.
- Ikke send noe ut av Kavli, og ikke endre eller slett filer uten å spørre.
