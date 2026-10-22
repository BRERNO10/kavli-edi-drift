# Oppsett i Enterprise Collaborator som ikke følger med eksporten

For egendefinerte ikke-BOD-avtaler følger dette ikke med i local package, og må dokumenteres her. Lag én fil per avtale: `PRD_ÅÅÅÅ-MM-DD_ec-oppsett_<avtale>.md`.

- **Event Hub-abonnement** – kreves for utgående avtaler
- **Document** – kreves for innkommende avtaler
- **String Replacer** – hvis en mapping bruker det (gjelder også egendefinerte BOD-avtaler)

Hentes fra Enterprise Collaborator Configuration. Kilde: [Infor – Configuration Management, Enterprise Collaborator](https://docs.infor.com/m3core/2026.10/en-us/useradminlib_cloud/config_mgt_m3/bol1709935417089.html).

Ta også med status og control properties per avtale, fra EC Administration → Server → Agreement Status og Agreement Control Properties. Control properties kan inneholde miljøspesifikke verdier – sjekk for passord og nøkler før commit.
