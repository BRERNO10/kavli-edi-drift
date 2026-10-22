# kavli-integrasjonsdrift

Kunnskapsbase og Copilot Cowork-plugin for drift og feilsøking av integrasjonene rundt Infor M3 CloudSuite:

- **EDI** med kunder og leverandører, via Enterprise Collaborator (MEC) og ION
- **Interne flyter** mellom M3 og systemer i produksjonen, som MAC (AGV-klient) og Quickdesign (Kameleon)

Repoet er grunnlaget for AI-POC-en november 2026 – januar 2027. POC-en måles bare på EDI.

| Rolle | Navn |
| --- | --- |
| Eier | [navn] |
| Stedfortreder | [navn] |

## Struktur

```text
kavli-integrasjonsdrift/
├── kilde/              råeksporter fra PRD – redigeres ikke
│   ├── ion/            data flows, connection points, mappings, monitors, status
│   ├── ec/             egendefinerte avtaler og manuelt dokumentert oppsett
│   ├── m3/             uttrekk (CRS945, CRS949 m.m.) og spørringer
│   ├── eksempler/      anonymiserte meldinger og logger (*.anon.*)
│   ├── partnere/       MIG-er og andre dokumenter fra EDI-partnere
│   └── systemer/       oppsett og dokumentasjon for interne systemer (mac/, quickdesign/)
├── docs/               kunnskap skrevet av oss
│   ├── flyter/         ett flytkort per flyt: edi_… eller intern_…
│   ├── partnere/       ett partnerkort per EDI-partner
│   ├── systemer/       ett systemkort per internt system
│   ├── runbooks/       én fil per feiltype, felles for alle flyter
│   ├── kunnskapsfangst/
│   ├── beslutninger/
│   ├── kalender.md     utløp av sertifikater, nøkler, passord og tjenestekontoer
│   └── kontakter.md
├── plugin/             Cowork-plugin (Claude-pluginformat)
├── overgang/           skillen for den midlertidige SharePoint-løsningen
├── tester/             historiske saker med fasit
├── scripts/            bygg og sjekk av plugin
└── .github/            sjekker og bygg i GitHub Actions
```

Filer som starter med `_` er maler. Kopier dem og gi filen et nytt navn.

## Regler

1. **Bare PRD foreløpig.** Filnavn i `kilde/`: `PRD_ÅÅÅÅ-MM-DD_<type>_<navn>.<filtype>`, for eksempel `PRD_2026-10-21_dataflow_DESADV-ut.xml`.
2. **Ingen hemmeligheter.** Aldri .ionapi-filer, passord, nøkler, sertifikater eller tilkoblingsstrenger med passord. Gitleaks sjekker hver push. Slår den ut, må passordet eller nøkkelen byttes – å slette det fra historikken er ikke nok.
3. **Ingen rå meldinger eller logger med kunde-, partner- eller persondata.** Bare anonymiserte eksempler, i `kilde/eksempler/`.
4. **Råeksporter redigeres ikke.** Forklaringer og vurderinger skrives i `docs/`.
5. **Flytkort heter `edi_…` eller `intern_…`.** Bygget stopper ellers. Bruk «intern», ikke «prod», så det ikke forveksles med PRD-miljøet.
6. **Endringer går via pull request**, og sjekken `Valider` må være grønn.

## Første gang

1. Opprett et privat repo `kavli-integrasjonsdrift` i Kavli-organisasjonen, uten README.
2. Push skjelettet fra denne mappen:

   ```bash
   git init -b main
   git add .
   git commit -m "Repo-skjelett for integrasjonsdrift"
   git remote add origin https://github.com/<organisasjon>/kavli-integrasjonsdrift.git
   git push -u origin main
   ```

3. Under Settings → Branches: beskytt `main` med krav om pull request og grønn `Valider`-sjekk. Det krever GitHub Team for private repoer.
4. Fyll inn eier og stedfortreder over, team eller brukernavn i `.github/CODEOWNERS`, og bytt `ORGANISASJON` i `plugin/.claude-plugin/plugin.json`.

## Daglig bruk

| Jeg skal … | Gjør dette |
| --- | --- |
| legge inn en eksport | Se `kilde/README.md` |
| skrive ned kunnskap | Kopier malen i `docs/flyter/`, `docs/partnere/`, `docs/systemer/` eller `docs/runbooks/` |
| forberede kunnskapsfangst | Se `docs/kunnskapsfangst/` |
| teste pluginen | Se `tester/README.md` |
| lage ny plugin-versjon | Øk `version` i `plugin/.claude-plugin/plugin.json`, oppdater `CHANGELOG.md` og lag en tag `vX.Y.Z` |

Pluginen bygges i GitHub Actions (workflow «Bygg plugin»). Zip-filen lastes ned fra kjøringen, eller fra Releases når en tag er laget. Se `plugin/README.md` for opplasting i Cowork.

## Veikart

| Versjon | Innhold | Status |
| --- | --- | --- |
| v0.1 | Skillene edi-triage, intern-triage og flytkart med innebygde referanser | Under arbeid |
| v0.2 | GitHub-tilkobling med lesetilgang | Planlagt |
| v0.3 | Skillene m3-edi-oppsett og edi-avstemming | Planlagt |
| Etter POC-en | Måling av intern-triage, eller én intern flyt som pilot | Vurderes |
| Senere | edi-endring, live-data fra ION og M3 | Vurderes |
