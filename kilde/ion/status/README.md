# Status i ION

Aktiv/inaktiv-status følger ikke med ION-eksportene. Lagre den her som CSV, én fil per eksportdato: `PRD_ÅÅÅÅ-MM-DD_status_ion.csv`.

Bruk kolonnene i `_mal_status.csv` (semikolon eller komma går begge):

| Kolonne | Innhold |
| --- | --- |
| type | `dataflow`, `cp` eller `monitor` |
| navn | Navnet slik det står i ION Desk |
| status | `aktiv` eller `inaktiv` |
| merknad | Hvorfor den er inaktiv, eller annet som er nyttig å vite |

Statusen hentes fra ION Desk → Connect → Active Data Flows og Active Connection Points, og Monitors & Workflows → Active Monitors.
