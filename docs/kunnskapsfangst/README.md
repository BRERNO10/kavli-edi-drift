# Kunnskapsfangst

Mål: få ned det som bare finnes hos ressursen som slutter, før siste arbeidsdag ([dato]).

Avklar først om ressursen også kjenner de interne flytene, som M3–MAC og M3–Quickdesign. Gjør den det, tas de med i øktene under. Hvis ikke: finn hvem som kjenner dem – systemeier, produksjon eller leverandør – og ta øktene for de interne flytene med dem.

## Økter

| Økt | Innhold | Varighet | Resultat |
| --- | --- | --- | --- |
| 1 | Oversikt over alle flyter: EDI-partnere og interne systemer | 60 min | Liste over flyter, partnere og systemer |
| 2 … n | Én flyt per økt, med eksporten av data flow på skjermen | 45 min | Utkast til flytkort i `docs/flyter/` |
| n + 1 … m | Ett internt system per økt: MAC, Quickdesign osv. | 45 min | Utkast til systemkort i `docs/systemer/` |
| m + 1 | De ti vanligste feilene, og hva som gjøres | 60 min | Utkast til runbooks i `docs/runbooks/` |
| m + 2 | Utløp, tilganger og kontakter | 30 min | `docs/kalender.md` og `docs/kontakter.md` |
| m + 3 | Gjennomgang av utkastene | 60 min | Rettede flytkort, systemkort og runbooks |

Spørsmålene til øktene står i `sporsmal.md`.

## Slik gjør vi det

- Ta opp øktene i Teams, med samtykke. Opptak og transkripsjon lagres i SharePoint, ikke her.
- Cowork lager første utkast til flytkort, systemkort og runbooks fra transkripsjonen. Den som kjenner flyten, retter utkastene.
- Hver flyt er ferdig når flytkortet har «Sist verifisert» med dato og navn.

## Sjekkliste

- [ ] Avklart om ressursen kjenner de interne flytene, og hvem som eventuelt gjør det
- [ ] Opptak der hver EDI-flyt gjennomgås ende til ende, fra M3 til partner
- [ ] Opptak der hver intern flyt gjennomgås fra M3 til linja, med manuell nødprosedyre
- [ ] «Topp 10 feil og hva jeg gjør da», med skjermbilder fra EC Administration, OneView og systemene
- [ ] Manuelle rutiner og faste sjekker – daglig, ukentlig og ved månedsslutt
- [ ] Skjulte avhengigheter: partnerspesifikke unntak, hardkodede verdier i mappinger, ting som ble gjort «midlertidig»
- [ ] Hvem som kontaktes eksternt, og for hva – også leverandørene av MAC og Quickdesign
- [ ] Utkastene til flytkort og systemkort gjennomgått og rettet
