# 0002 – Interne integrasjoner i samme repo og plugin

| Felt | Verdi |
| --- | --- |
| Dato | 2026-10-22 |
| Status | Foreslått |
| Besluttet av | [navn] |

## Bakgrunn

I tillegg til EDI har Kavli interne integrasjoner mellom M3 og systemer i produksjonen, blant annet M3 til MAC (AGV-klient) og M3 til Quickdesign (Kameleon). Alle flytene starter i M3, og de som går via ION eller Enterprise Collaborator deler infrastruktur med EDI.

## Beslutning

- Repo og plugin dekker både EDI og interne flyter, og heter `kavli-integrasjonsdrift` (var `kavli-edi-drift`).
- `kilde/ion/`, `kilde/ec/`, `kilde/m3/` og `docs/runbooks/` er felles. Nytt er `kilde/systemer/` og `docs/systemer/`, med ett systemkort per system.
- Flytkort heter `edi_…` eller `intern_…`. «Intern» brukes i stedet for «prod», så det ikke forveksles med PRD-miljøet.
- Feilsøkingen er delt i edi-triage og intern-triage, fordi den er ulik. Flytkart (var edi-flytkart) dekker alle flyter, så det finnes ett sted å se hva som rammes når et ledd stopper.
- Overgangsskillen heter `integrasjon-feilsok` (var `edi-feilsok`) og dekker begge.
- Stans i interne flyter varsles fra ION-monitorer eller systemenes egne alarmer, direkte til den som har ansvar for linja. AI brukes til diagnosen, ikke som første varsling.
- POC-en måles bare på EDI. Interne flyter tas inn i målingen etterpå, eller én av dem som pilot hvis sakshistorikken viser at de feiler oftere.

## Alternativer som ble vurdert

- **Eget repo for interne integrasjoner:** gir to sett med eksporter fra ION, EC og M3, og ingen samlet oversikt over hva som rammes når et felles ledd stopper.
- **Én triage-skill for alt:** feilsøkingen og hastegraden er ulik, og POC-målingen for EDI ville blitt blandet med de interne flytene.

## Konsekvenser

- Navnet byttes før første push, mens repoet er tomt.
- Kunnskapsfangsten må avklare om ressursen som slutter også kjenner de interne flytene.
- Loggene fra MAC og Quickdesign ligger trolig i produksjonsnettet, som Cowork ikke når. De må hentes ut og legges ved saken.
