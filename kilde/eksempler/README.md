# Anonymiserte eksempler

Kjente gode meldinger og logger, og typiske feilede, å sammenligne mot. Bare anonymiserte filer:

- **EDI:** `<partner>_<meldingstype>_<OK|FEIL>.anon.txt` for EDIFACT og RCV, `.anon.xml` for XML.
- **Interne flyter:** `<system>_<flyt>_<OK|FEIL>.anon.<filtype>`, for eksempel `mac_<flyt>_FEIL.anon.log`.
- Fjern personnavn, brukernavn, telefonnumre, e-postadresser og priser. GLN, GTIN, batch, datoer og strukturen beholdes, siden de trengs for å forstå feil.
- `.gitignore` stopper rå meldinger og logger (`*.rcv`, `*.edi`, `*.log`). Bare filer med `.anon.` i navnet slipper gjennom.
