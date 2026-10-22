# Flytkort

Ett flytkort per flyt. Navnet avgjør hvilken skill som får kortet:

| Filnavn | Mal | Brukes av |
| --- | --- | --- |
| `edi_<meldingstype>-<retning>.md`, f.eks. `edi_DESADV-ut.md` | `_mal_edi.md` | edi-triage og flytkart |
| `intern_<fra>-<til>_<innhold>.md`, f.eks. `intern_M3-MAC_<innhold>.md` | `_mal_intern.md` | intern-triage og flytkart |

Gjelder en EDI-flyt bare én partner, legg partneren til slutt: `edi_DESADV-ut_<partner>.md`.

Bygget stopper hvis et flytkort ikke starter med `edi_` eller `intern_`, med små bokstaver. Bruk «intern», ikke «prod», så det ikke forveksles med PRD-miljøet.

Et flytkort er ferdig når «Sist verifisert» har dato og navn.
