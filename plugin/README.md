# Cowork-plugin: kavli-integrasjonsdrift

Pluginen gir Copilot Cowork Kavlis kunnskap om integrasjonene rundt M3: EDI-flytene og de interne flytene i produksjonen. Den er laget i Claude-pluginformat, som Cowork konverterer ved opplasting.

| Skill | Brukes når |
| --- | --- |
| edi-triage | En konkret EDI-feil, et varsel eller en feilmelding skal forstås og løses |
| intern-triage | En feil i en intern flyt mellom M3 og et system i produksjonen, som MAC eller Quickdesign |
| flytkart | Spørsmål om hvordan flytene henger sammen, og hva som rammes når et ledd stopper – både EDI og interne flyter |

## Referanser

Filer i `skills/*/references/` som starter med `gen-` bygges fra `docs/` og `kilde/` av `scripts/generer_referanser.py`. De committes ikke. Faste referanser, som `edifact-oversikt.md`, ligger i repoet.

| Referanse | Bygges fra | Brukes av |
| --- | --- | --- |
| `gen-flyter-edi.md` | `docs/flyter/edi_*.md` | edi-triage |
| `gen-flyter-intern.md` | `docs/flyter/intern_*.md` | intern-triage |
| `gen-flyter.md` | alle flytkort | flytkart |
| `gen-partnere.md` | `docs/partnere/` | edi-triage, flytkart |
| `gen-systemer.md` | `docs/systemer/` | intern-triage, flytkart |
| `gen-status.md` | `kilde/ion/status/` | intern-triage, flytkart |
| `gen-runbooks.md`, `gen-kalender.md`, `gen-kontakter.md` | `docs/` | edi-triage, intern-triage |
| `gen-eksempler.md` | `kilde/eksempler/` | edi-triage, intern-triage |
| `gen-kilde-indeks.md` | `kilde/` | alle |

## Bygg

- **I GitHub:** Actions → «Bygg plugin» → Run workflow. Zip-filen ligger som artefakt på kjøringen. En tag `vX.Y.Z` lager i tillegg en release med zip-filen.
- **Lokalt:** `python scripts/bygg_plugin.py` lager `dist/kavli-integrasjonsdrift-<versjon>.zip`.

Bygget stopper hvis et flytkort ikke heter `edi_…` eller `intern_…`, eller hvis en skill bryter grensene i Cowork: maks 20 skills per plugin, maks 20 tilleggsfiler per skill, 5 MB per fil og 10 MB totalt, navn lik mappenavnet i kebab-case, og beskrivelse på maks 1 024 tegn. Grensene sjekkes av `scripts/sjekk_grenser.py`.

## Ta i bruk i Cowork (v0.1)

1. Eieren laster opp zip-filen: Customize → Plugins → Upload plugin.
2. Del med teamet i Share-dialogen: Specific users in your organization.
3. Ved ny versjon: last opp den nye zip-filen og velg Re-share.
4. Fjern delingen av overgangsskillen integrasjon-feilsok når triage-skillene er i bruk.

La ikke flere laste opp den samme pakken. Cowork tillater bare én eier per manifest-ID i tenanten.

## Senere

- **v0.2 – GitHub-tilkobling med lesetilgang:** Krever en OAuth-app i GitHub og en OAuth client registration i Teams Developer Portal. Kopier deretter `connectors/github.mcp.json` til `.mcp.json` i denne mappen. Endepunktet `/mcp/readonly` avviser alle skriveoperasjoner.
- **Distribusjon fra admin:** Konverter zip-filen til en Microsoft 365-pakke og last den opp i Microsoft 365 admin center. Testet med Agents Toolkit CLI 1.1.18:

  ```bash
  npm install -g @microsoft/m365agentstoolkit-cli
  atk import openplugin --path <utpakket plugin-zip> --output m365-prosjekt \
    --privacy-url <Kavlis personvernerklæring> --terms-url <URL til vilkår>
  atk package --manifest-file m365-prosjekt/appPackage/manifest.json \
    --output-package-file m365-prosjekt/appPackage/build/appPackage.zip \
    --output-folder m365-prosjekt/appPackage/build
  ```

  Manifestet får versjon `devPreview`. Krever admin center versjon 1.28, må `manifestVersion` og `$schema` endres i `manifest.json`.
- **Flere skills:** m3-edi-oppsett, edi-avstemming og edi-endring.

Kilde: [Build plugins for Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development)
