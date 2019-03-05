# Projektityösuunnitelma 

* ***Jarno Wermundsen***
* ***Miika Zitting***
* ***Hannu Kankkunen***





















					
# Projektin tehtävä
Projektin tehtävänä on luoda Raspberry Pi lämpötilamittari Python ohjelmointikielellä.

# Projektin tulostavoitteet
Projektin tulostavoitteina ovat:
- Raspberry Pi toiminta lämpötilasensorin kanssa
- Python kielen osaamisen kehittyminen
- Sovellus, joka lähettää sensorin tiedot eteenpäin luettavassa muodossa
- Toistettavissa oleva projekti raportointi



# Projektin oppimistavoitteet 
Perehdytään Python kieleen ja sovelletaan opittua toimivan lopputuloksen varmistamiseksi. Tutustutaan eri vaihtoehtoihin, joilla lämpötilaa saa mitattua ja valitaan 
projektiin sopiva sensori.

# Projektin rajaus 
Pidetään projekti yksinkertaisena, jotta lopputulos vastaa tavoitetta määritellyssä ajassa. Projekti on tarkoitettu omien taitojen kartuttamiseen, ei kaupalliseen käyttöön.



# Projektin riskit ja niihin varautuminen 
Projektin riskit on kartoittettu alla olevaan taulukkoon.

*) 3 = pieni, 2 = kohtuullinen, 1 = suuri/huomattava.

| Riski | Todennäköisyys | Seuraus- vaikutus | Syyt | Syiden ennaltaehkäisy | Seurauksiin varautuminen |
| ---	 | ---	 | ---	 | ---	 | ---	 | ---	 |
| Avainhenkilö jättää projektin | 3 | 1 | Henkilökohtaiset syyt, muut opinnot, hyvä työtarjous, kuolema, muu vakava vammautuminen | Mielekkäiden työkokonaisuuksien takaaminen, nykyaikaiset välineet työlle, sitoutuminen opintojen jatkamiseen | Projektin tehtävän ja tulosten määrittely ja jako |
| Projektin tehtävä jää muun työn jalkoihin | 2 | 2 | Projektikulttuuri heikko, töiden priorisointi epäonnistunut | Keskittyminen projektin tehtävään: n. 8-10t/vko lukujärjestykseen merkittyä työaikaa, säännölliset projekti palaverit | Päätös projektin keston, tavoitteen muuttamiseksi |
| Perehtyminen ja osaaminen ei riitä | 1 | 3 | Huono materiaali, riittämätön ohjaus, täysin odottamaton ongelma | Hyvä perehtyminen ja töiden sunnittelu | Sovellusten/Osien vaihtaminen, koko alustan vaihtaminen, yhteydenotto opettajiin ja/tai asiantuntijoihin.
| Kustannusten nousu | 2 | 1 | Odottamattomia kustannuksia ilmaantuu | Huolellinen suunnittelu | Kustannusten jakaminen ja mahdollisesti ulkopuolisen rahoituksen hankkiminen |
| Osien rikkoutuminen | 2 | 1 | Huolimaton käsittely, virhe kolvaamisessa tai todella virheellinen koodi | Laitteiden ja osien huolellinen käsittely | Joitakin kriittisiä osia on käytettävissä useampia ja selvitetty mahdolliset hankintapaikat ja aikataulut |

## Projektiryhmä 
Projekti tehdään ryhmätyönä ryhmässä, johon kuuluvat 
- Miika Zitting 
- Jarno Wermundsen
- Hannu Kankkunen

Projektipäällikköä ei tarpeen erikseen nimetä, sillä työnjako ja suunnittelu hoidetaan huolellisesti ja tasa-arvoisesti.

## Projektin ympäristö 
- Raspberry Pi 3 - Raspbian käyttöjärjestelmällä
- Adafruit 16x2 LCD näyttö
- Adafruit MCP9808 Lämpötila-anturi
- Google Sheets & Google API

## Käytettävät teknologiat, menetelmät ja työkalut 
Projektissa käytämme alustana Raspberry Pi 3, johon liitämme 16x2 kokoisen LCD näytön joka tulostaa näytölle lämpötilan Raspberryyn liitetyltä lämpötila-anturilta. Osien toimivuutta hallitsemme Python ohjelmointikielellä luodulla koodilla, jolla saamme anturin lukemaan tietoja jonka koodi muuttaa tulostettavaan muotoon näyttöä varten. 
Lämpötilan mittaustulokset arkistoidaan myös Google Sheets palveluun Python koodin avulla. Google Sheetsin tulostus tapahtuu Pythoniin lisätyllä kirjastolla ja Googlen API avainten avulla.

## Projektin vaiheistus, aikataulu ja työmäärät

Projekti alkaa 28.01.2019 ja päättyy 15.05.2019. 
Käytettävissä oleva työmäärä on 8-12 tuntia/viikko.

Työmäärät ja tehtävät vaihtelevat projektin vaiheen mukaan. Viikon alussa asetamme tavoitteen joka tulisi viikon aikana saavuttaa. Työmäärät jaetaan tasaisesti projektin tekijöiden kesken, omat erikoisosaamisalueet huomioon ottaen.

Projektin alussa keskitymme tutustumaan Python ohjelmointikieleen, sekä Googlen API alustaan. Tutkimme myös millaisia osia tarvitsemme Raspberrya varten projektin onnistumiseksi. 

Työvaiheessa keskitymme koodin tuottamiseen, sekä sensorin ja näytön ohjaaminen koodin avulla. Kun olemme saaneet koodit erillisinä toimintakuntoon lähdemme kasaamaan näitä yhdeksi isommaksi kokonaisuudeksi jota Raspberry ajaisi automaattisesti käynnistyessään. 

Testausvaiheessa olemme saaneet järjestelmän toimintakuntoon ja testaamme sen toimintaa erilaisissa olosuhteissa.


## Dokumentinhallinta
Dokumenttien hallintaan käytämme GitHub palvelua, johon lisäämme kaikki raporttimme, sekä mahdollisesti käytettävät koodit. GitHub palvelussa meillä on jo luotuna Projekti repository, johon kaikilla projektiin osallistuvilla on muokkaus/julkaisu oikeudet. 


Linkki GitHubiin :
https://github.com/JarnoWer/Projekti
