# Tester

Historiske saker med fasit, brukt til å måle om pluginen stiller riktig diagnose.

| Filnavn | Område | Skill |
| --- | --- | --- |
| `T01-<kort-navn>.md` | EDI | edi-triage |
| `I01-<kort-navn>.md` | Interne flyter | intern-triage |

Suksesskriteriet i POC-en er riktig diagnose i minst 8 av 10 EDI-saker (T-filene). I-filene telles for seg, så resultatet for EDI ikke blandes med de interne flytene.

## Lag en test

1. Kopier `_mal.md` til `T01-<kort-navn>.md` eller `I01-<kort-navn>.md`.
2. Legg anonymiserte inputfiler i `kilde/eksempler/` og henvis til dem.
3. Skriv fasit: hvilket ledd feilen lå i, årsaken og riktig tiltak.

## Kjør testene

1. Start en ny samtale i Cowork for hver test, med pluginen aktiv.
2. Legg ved inputfilene og skriv: «Bruk edi-triage på denne saken» eller «Bruk intern-triage på denne saken».
3. Sammenlign triage-kortet med fasit. Noter resultat, modell og kreditter i testfilen – Cowork viser kreditter per oppgave.

Kjør alle testene på nytt når en ny plugin-versjon er bygget, så ser vi om endringen har gjort ting bedre eller verre.
