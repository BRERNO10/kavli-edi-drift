# 0001 – Oppsett av AI-POC for EDI-drift

| Felt | Verdi |
| --- | --- |
| Dato | 2026-10-21 |
| Status | Rammer vedtatt (IT-IB 21.10.2026). Tekniske valg foreslått. Utvidet av 0002. |
| Besluttet av | [navn] |

## Bakgrunn

Kavli mister en ressurs med inngående kunnskap om EDI-integrasjonene i Infor M3 CloudSuite. POC-en tester om Copilot Cowork kan ta over førstelinje feilsøking og overvåking av flytene. Kostnadsramme ca. 20 000 kr, november 2026 – januar 2027.

## Beslutning

- Kunnskapen samles i dette private repoet og pakkes som plugin i Copilot Cowork.
- Bare PRD eksporteres foreløpig. TST tas inn ved behov for sammenligning eller støtte til endringer.
- Inntil pluginen er klar brukes en SharePoint-mappe per hendelse og skillen edi-feilsok (`overgang/`).
- Plugin v0.1 har bare skills med innebygde referanser. GitHub-tilkoblingen kommer i v0.2, når OAuth-registreringen er på plass.
- AI foreslår, mennesker utfører. Ingen skrivetilgang til ION, Enterprise Collaborator eller M3.
- Hemmelighetsskanning med gitleaks i GitHub Actions, i stedet for GitHub Secret Protection, som er et betalt tillegg for private repoer.

## Konsekvenser

- Interne timer: ca. 80 i IT og 10–15 fra ressursen som slutter.
- Referansene i pluginen er et øyeblikksbilde. Ny versjon må bygges når `docs/` endres.
