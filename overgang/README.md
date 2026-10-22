# Overgang: feilsøking fra SharePoint

Skillen `integrasjon-feilsok/` brukes sammen med en SharePoint-mappe for feilsøk til pluginen er klar. Den dekker både EDI og de interne flytene i produksjonen, og er ikke avhengig av hva kanalen heter. Foreslått navn er «Integrasjon-feilsøk».

Skillen lastes opp i Cowork under Customize → Skills → Add → Upload skill, og deles med teamet.

## Saksmapper

Én mappe per hendelse under `01-Saker/`, med flytnavnet i mappenavnet:

- EDI: `2026-10-15_DESADV-ut_<partner>_<kort-tekst>`
- Intern: `2026-10-21_M3-MAC_<kort-tekst>`

| Filer | Innhold | Eksempel |
| --- | --- | --- |
| `00_beskrivelse.md` | Hva, når, hvem, frist, flyt, motpart og meldings-ID. Mal: `_mal_00_beskrivelse.md`, som legges i `03-Maler`. | |
| `10–19` | Enterprise Collaborator | `10_ec_<uuid>.rcv.txt`, `11_ec_logg.txt` |
| `20–29` | ION og OneView | `20_oneview_<id>.xml`, `21_oneview_tidslinje.png` |
| `30–39` | M3 | `30_m3_<program>.png` |
| `40–49` | Motparten: svar fra partner eller VAN, eller logg, alarm og skjermbilder fra systemet | `40_partner_svar.txt`, `40_mac.log`, `41_quickdesign_alarm.png` |
| `90_analyse.md` | Skrevet av AI | |
| `99_losning.md` | Skrevet av den som løste saken | |

RCV- og EDIFACT-filer lagres med `.txt` til slutt, for eksempel `10_ec_<uuid>.rcv.txt`, fordi Cowork ikke leser .rcv og .edi. Logger kan beholde `.log`.

Kopier systemkortene fra `docs/systemer/` til `00-Kunnskap` når de er fylt ut, så skillen finner nødprosedyre og kontakter.

## Bytte fra edi-feilsok

Skillen het tidligere `edi-feilsok`. Er den lastet opp i Cowork, slett den når `integrasjon-feilsok` er lastet opp, så to skills ikke konkurrerer om de samme forespørslene.

## Når pluginen er i bruk

Når plugin v0.1 med edi-triage og intern-triage er tatt i bruk: fjern delingen av integrasjon-feilsok og slett den.
