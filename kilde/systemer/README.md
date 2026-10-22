# Interne systemer

Én mappe per system, med samme navn som systemkortet i `docs/systemer/`: `mac/`, `quickdesign/` osv.

| Innhold | Filnavn |
| --- | --- |
| Oppsettet for M3-integrasjonen i systemet – endepunkt, mappe, feltkobling, intervall – som eksport eller skjermbilde | `PRD_ÅÅÅÅ-MM-DD_oppsett_<navn>.<filtype>` |
| Grensesnittbeskrivelse og annen dokumentasjon fra leverandøren | Valgfritt |

Loggene ligger trolig i systemet eller på en server i produksjonen, og Cowork når dem ikke. Skriv i systemkortet hvor de ligger, og legg anonymiserte utdrag i `kilde/eksempler/`.

## Før du committer

Oppsettfiler fra systemene kan inneholde tilkoblingsstrenger med brukernavn og passord til databaser eller M3. Erstatt passordet med `***`, og følg sjekken i `kilde/README.md`.

## Legges ikke her

- Passord, nøkler, sertifikater eller tilkoblingsstrenger med passord
- Rå logger – bare anonymiserte utdrag, i `kilde/eksempler/`
- Databasekopier og backup, for eksempel `.bak`, `.mdf` og `.ldf`
