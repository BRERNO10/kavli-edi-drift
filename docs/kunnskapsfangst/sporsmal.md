# Spørsmål til kunnskapsfangsten

## Per EDI-flyt

1. Hva starter flyten – hendelse, jobb eller utskrift av dokument? Hvilket dokument og hvilken variant i CRS945?
2. Når på døgnet går den, og hvor mange meldinger er normalt?
3. Hvilke partnere bruker den, og hvilke unntak finnes per partner?
4. Hvilke EC-avtaler, ION-flyter og connection points er med? Er noen inaktive, og i så fall hvorfor?
5. Hva feiler oftest? Hvordan oppdager du det i dag – varsel, partner som ringer, eller noe du sjekker selv?
6. Hva gjør du steg for steg når det feiler? Når velger du Retry, Redetect eller Verify?
7. Hvem kontakter du – internt, hos Infor, hos VAN-leverandøren eller hos partneren?
8. Finnes det hardkodede verdier, midlertidige løsninger eller ting som ikke må røres?
9. Er det jobber som må gå i en bestemt rekkefølge for at flyten skal fungere?

## Per intern flyt eller system

1. Hva sender M3 til systemet, og hva sendes tilbake?
2. Hvordan går flyten: ION data flow, EC-avtale, M3 API som systemet kaller selv, fil eller database? Er det et mellomledd på en lokal server?
3. Hva starter flyten – hendelse i M3, jobb, eller at systemet henter selv? Hvor ofte?
4. Hvor mange meldinger er normalt per skift, og når går linja (skift, helg, vedlikeholdsstans)?
5. Hva skjer på linja når flyten stopper, og etter hvor lang tid?
6. Finnes en manuell nødprosedyre? Hvem avgjør at den tas i bruk?
7. Hvordan oppdages feil i dag – ION-monitor, alarm i systemet, eller at produksjonen ringer? Hvem får varselet, også utenom arbeidstid?
8. Hvor ligger loggene, hvem har tilgang, og hvor lenge beholdes de?
9. Hvilke M3-data må være riktige for at flyten skal virke, for eksempel GTIN, holdbarhet, enhet eller lokasjon?
10. Hvilken tjenestekonto bruker systemet mot M3, og utløper passord eller sertifikat?
11. Hvem er leverandør, hva dekker supportavtalen, og hvem i Kavli eier systemet?
12. For merking: hva kan bli feil på etiketten, og hvem i kvalitet varsles da?

## Felles

1. Hvilke sertifikater, nøkler og passord utløper, når, og hvordan fornyes de?
2. Hvilke tilganger og roller trenger den som overtar (for eksempel M3EC-Administrator)?
3. Hvilke e-postadresser eller kanaler får varsler i dag – for EDI og for de interne flytene?
4. Hvor ligger dokumentasjon, MIG-er og testrutiner fra partnerne og leverandørene?
5. Hva ville du forbedret hvis du hadde hatt mer tid?
