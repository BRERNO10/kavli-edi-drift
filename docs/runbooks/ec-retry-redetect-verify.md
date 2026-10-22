# Runbook: Feilede meldinger i Enterprise Collaborator – Retry, Redetect eller Verify

| Felt | Verdi |
| --- | --- |
| Gjelder | Alle flyter gjennom Enterprise Collaborator |
| Hvor det vises | EC Administration → Messages → Retry/Redetect |
| Sist verifisert | 2026-10-21 mot Infor-dokumentasjon. Kavlis egen rutine er ikke lagt inn ennå. |

## Symptom

En melding har feilet i Enterprise Collaborator (EC) og ligger i Retry/Redetect-visningen.

## Velg handling

| Handling | Hva den gjør | Bruk når |
| --- | --- | --- |
| Redetect | Behandler meldingen på nytt fra start | Avtale eller deteksjon er rettet |
| Retry | Fortsetter der meldingen stoppet | Årsaken er rettet, for eksempel masterdata i M3 |
| Verify | Merker meldingen som ferdig uten videre behandling | Meldingen er håndtert på annen måte |

## Sjekk

1. Les feilteksten i meldingsdetaljene. Feil fra et M3 API-kall (MI) står der ordrett.
2. Rett årsaken før Retry eller Redetect, ellers feiler meldingen på nytt.
3. Meldinger du har kjørt Retry eller Redetect på, forsvinner fra listen. Feiler de på nytt, dukker de opp igjen med ny status.

## Merk

- Visningen viser alle feilede meldinger unntatt status **Received failed** og **Messages Rejected**. De må følges opp separat.
- EC beholder vellykkede meldinger i 30 dager og feilede i 60 dager. Lagre det som trengs til en sak før det slettes.

## Eskaler når

<Fylles ut i kunnskapsfangsten.>

Kilde: [Infor – Processing failed messages](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/aer1498545343201.html)
