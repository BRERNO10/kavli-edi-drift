---
name: integrasjon-feilsok
description: Feilsøker integrasjonshendelser i Kavlis Infor M3 CloudSuite ut fra logger, XML- og RCV-filer og skjermbilder i en saksmappe – både EDI (Enterprise Collaborator/MEC, ION og M3) og interne flyter mellom M3 og systemer i produksjonen, som MAC (AGV-klient) og Quickdesign (Kameleon). Bruk når noen ber om å feilsøke eller analysere en sak, spør hvorfor en DESADV, ORDERS eller INVOIC feilet, hvorfor AGV-ene ikke får oppdrag eller etiketter ikke skrives ut, eller nevner .rcv-filer, EC-logg, OneView, failed agreement, detection failed, Retry eller Redetect.
---

# Integrasjonsfeilsøk (overgangsløsning)

Finn sannsynlig årsak og neste steg for én hendelse, basert på filene i saksmappen. Du foreslår – driftsansvarlig eller systemeier utfører alt i Enterprise Collaborator (EC), ION, M3 og systemene i produksjonen.

## Først: står linja?

Gjelder saken en intern flyt, for eksempel M3–MAC eller M3–Quickdesign, avklar dette før analysen:

- **Linja står, eller går snart tom:** si at den manuelle nødprosedyren skal følges, og at produksjonen skal varsles. Analysen kommer etterpå.
- **Mulig feil merking** (holdbarhetsdato, batch, GTIN eller annet på etiketten): si at kvalitet skal varsles. Kvalitet avgjør om varer sperres.

Står ikke nødprosedyren eller kontakten i 00-Kunnskap, si det.

## Arbeidsflyt

1. Finn saksmappen brukeren peker på (01-Saker/<sak>). Les 00_beskrivelse.md først. Mangler den, spør om flyt, retning, motpart (partner eller system), tidspunkt og meldings-ID (EC UUID eller OneView) før du går videre. Bruk 00-Kunnskap for partnere, systemer, kontakter og notater.
2. Gå gjennom filene i nummerrekkefølge: 10–19 er EC, 20–29 er ION og OneView, 30–39 er M3, og 40–49 er motparten – partner/VAN eller systemet (logg, alarm eller skjermbilde). Noter kort hva hver fil viser.
3. Identifiser meldingen:
   - EDIFACT (starter med UNA eller UNB): meldingstype i UNH, dokumentnummer i BGM, datoer i DTM, parter og GLN i NAD, varelinjer og GTIN i LIN, antall i QTY, SSCC i GIN.
   - XML eller BOD: verb og substantiv i rotelementet, dokument-ID og avsender.
   - .rcv (lagret som .rcv.txt): filen slik EC mottok den. Sammenlign med det partneren eller M3 faktisk sendte.
   - Logg fra et system: tidspunkt, feilkode, og siste vellykkede melding før feilen.
4. Plasser feilen i ett ledd, og begrunn valget.

   **EDI:**
   - Mottak og kanal: filen kom ikke frem, eller kom til feil kanal.
   - Deteksjon: EC fant ingen avtale som passer filen.
   - Mapping: feil i et mapping-steg eller et M3 API-kall. Les MI-feilteksten ordrett.
   - M3-data: manglende eller feil masterdata (GLN, GTIN, enhet), feil partneroppsett (CRS945/CRS949) eller feil status på leveransen.
   - ION: ruting, connection point eller filter.
   - Partner eller VAN: meldingen er avvist hos mottaker (CONTRL eller APERAK).

   **Interne flyter:**
   - M3: triggeren gikk ikke (jobb, status eller hendelse), eller data mangler eller er feil.
   - Integrasjonsledd: ION data flow, connection point, EC-avtale, eller et API-kall som er avvist. Les feilteksten ordrett.
   - Nett og tilgang: produksjonsnett, brannmur, sertifikat, tjenestekonto eller utløpt passord.
   - Systemet: tjenesten står, køen er full, eller oppsettet eller produkttabellen i systemet er feil.
   - Utstyr på linja: AGV, skriver eller merkemaskin – til vedlikehold, ikke IT.
5. Mangler meldinger uten at noe har feilet, sjekk om linja gikk i perioden, og sammenlign med normalt volum i 00-Kunnskap.
6. Finnes et referanseeksempel for samme motpart og meldingstype i 02-Referanse, sammenlign felt for felt og list forskjellene.
7. Lag triage-kortet under. Spør om det skal lagres som 90_analyse.md i saksmappen.

## Triage-kort

| Felt | Innhold |
| --- | --- |
| Hva skjedde | Kort beskrivelse med tidspunkt |
| Flyt og motpart | Flyt, retning, partner eller system, og EC UUID eller OneView meldings-ID |
| Konsekvens nå | Frist mot partner, eller om linja står og hvor lenge den tåler stans |
| Sannsynlig årsak | Ledd og forklaring, med henvisning til fil og felt eller linje |
| Foreslått tiltak | Konkrete steg; for EC: Retry, Redetect eller Verify, med begrunnelse |
| Hvem utfører | Rolle, ikke person |
| Varsles | Partner, produksjon, kvalitet eller leverandør – bare de som er relevante |
| Usikkerhet | Hva filene ikke avgjør, og hva som må sjekkes manuelt |

## Retry, Redetect og Verify i EC

- Redetect behandler meldingen på nytt fra start. Aktuelt når avtale eller deteksjon er rettet.
- Retry fortsetter der meldingen stoppet. Aktuelt når årsaken, for eksempel masterdata, er rettet.
- Verify merker meldingen som ferdig uten videre behandling. Bare når den er håndtert på annen måte.

Anbefal, men overlat valget til driftsansvarlig. Finnes en rutine i 00-Kunnskap, følg den.

## Regler

- Skill tydelig mellom det filene viser og det du antar.
- Ikke finn på feltnavn, programnavn eller oppsett som ikke står i filene eller i 00-Kunnskap.
- Ikke foreslå endringer i systemene eller på linja uten at systemeier er med på avgjørelsen.
- Ikke gjengi person- eller prisdata i analysen når det ikke trengs for å forklare feilen.
- Ikke send noe ut av Kavli, og ikke endre eller slett filer uten å spørre.
- Hvis saken avdekker noe som bør bli en fast rutine, foreslå et utkast til 99_losning.md.
