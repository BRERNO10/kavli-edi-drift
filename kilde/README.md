# kilde/ – råeksporter

Alt her er eksportert fra **PRD** og lagres uendret. Forklaringer og vurderinger skrives i `docs/`.

## Filnavn

`PRD_ÅÅÅÅ-MM-DD_<type>_<navn>.<filtype>`, der datoen er eksportdatoen. Eksempel: `PRD_2026-10-21_dataflow_DESADV-ut.xml`.

| Type | Mappe | Hentes fra |
| --- | --- | --- |
| `dataflow` | `ion/data-flows/` | ION Desk → Connect → Data Flows → Export. Eksporter hele flyten, så følger connection points og mappinger med. |
| `cp` | `ion/connection-points/` | ION Desk → Connect → Connection Points → Export. Bare de som ikke er med i en eksportert flyt. |
| `mapping` | `ion/mappings/` | ION Desk → Connect → Mappings → Export, for mappinger som ikke fulgte med flyten. |
| `monitor` | `ion/monitors/` | ION Desk → Monitors & Workflows → Export (monitors og activation policies). |
| `schema` | `ion/object-schemas/` | ION Desk → Data Catalog → Object Schemas (egendefinerte dokumenter). |
| `status` | `ion/status/` | Active Data Flows og Active Connection Points. Se `ion/status/README.md`. |
| `agreement` | `ec/agreements/` | Configuration Management → local package med Custom Agreements. |
| `ec-oppsett` | `ec/configuration/` | Skrives manuelt. Se `ec/configuration/README.md`. |
| `crs945` o.l. | `m3/uttrekk/` | Listen eksportert fra H5 eller Compass, lagret som CSV. |
| `oppsett` | `systemer/<system>/` | Oppsettet for M3-integrasjonen i et internt system, som eksport eller skjermbilde. Se `systemer/README.md`. |

Aktiv/inaktiv-status følger ikke med eksportene fra ION, og må derfor lagres separat i `ion/status/`. Det gjelder også data flows og connection points for de interne flytene.

Dokumenter fra partnere og leverandører, i `partnere/` og `systemer/`, trenger ikke følge navneregelen.

## Før du committer

1. Åpne filen og søk etter `password`, `passwd`, `pwd`, `secret`, `key`, `token`, `connectionstring`, `"cs"` og `"sask"`.
2. Finner du et passord eller en nøkkel: erstatt verdien med `***`, og skriv det i commit-meldingen.
3. Sjekk at filnavnet starter med `PRD_` og eksportdatoen.

Gitleaks sjekker også hver push, men da ligger filen allerede i historikken. Den manuelle sjekken før commit er derfor den viktigste.

## Legges ikke her

- .ionapi-filer, tjenestekontoer, sertifikater eller nøkler
- Rå meldinger og logger med kunde-, partner- eller persondata – bare anonymiserte eksempler i `eksempler/`
- Databasekopier og backup fra systemene
