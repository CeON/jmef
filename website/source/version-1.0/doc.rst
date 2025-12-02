###########################
Version 1.0 - Documentation
###########################

This document contains description of every possible xml element of the Journal Metadata Exchange Format (JMEF)

.. contents::
    :local:

********
Elements
********

journal
********

Root element of JMEF xml.

.. code-block:: xml

  <journal xmlns="https://journalmetadata.org/version-1.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xsi:schemaLocation="https://journalmetadata.org/version-1.0 https://journalmetadata.org/version-1.0/jmef.xsd">
    ...
  </journal>


id
******

Various journal identifiers for internal use by systems exchanging data, e.g., for
synchronization or deduplication of harvested data.

Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

  <id type="ddh">123</id>
  <id type="doaj">6f0107092faa43e7b3232480cb89fb99</id>
  <id type="doi">10.1012/abc</id>

Attributes:
 - type - type of the identifier associated with the element

title-group
***************

Wrapper element containing informations about the journal titles

Mandatory: **Yes**

Occurrences: **1**

.. code-block:: xml

  <title-group>
    <title language-iso2="ENG">Patria Artha Technological Journal</title>
    <other-title type="translation" language-iso2="DEU">Translated title</other-title>
    <other-title type="subtitle" language-iso2="ENG">Subtitle</other-title>
    <other-title type="alternative">Alt title</other-title>
  </title-group>

title
=========

The main title of the journal

Mandatory: **Yes**

Occurrences: **1**

.. code-block:: xml

   <title language-iso2="ENG">Patria Artha Technological Journal</title>

Attributes:
 - language-iso2 - language of the title given as :ref:`ISO 639-2/T code <language-code-label>`

other-title
===============

Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

   <other-title type="translation" language-iso2="DEU">Translated title</other-title>

Attributes:
 - type (Mandatory) - Type of the title. Allowed values are: translation, subtitle, alternative, other
 - language-iso2 - language of the title given as :ref:`ISO 639-2/T code <language-code-label>`

issn
*********

International Standard Serial Number (ISSN) of the journal

Mandatory: **Yes**

Occurrences: **1-n**

.. code-block:: xml

   <issn publication-format="print">1063-777X</issn>

Attributes:
 - publication-format (Mandatory) - Format of the issn. Allowed values are: print (meaning that ISSN is for paper version of the journal) and electronic (meaning that ISSN is for the electronic media (online) version of the journal).


diamond-criteria
*****************

Journal diamond criteria as defined within the DIAMAS and CRAFT‑OA projects (see: `Operational Diamond OA Criteria for Journals <https://zenodo.org/records/12721408>`__)

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <diamond-criteria>
    <scholarly-journal value="true" />
    <community-owned value="true"/>
    <open-access-with-open-licenses value="true" />
    <no-fees value="true"/>
    <open-to-all-authors value="true" />
  </diamond-criteria>
  

scholarly-journal
=================

Status of the scholarly journal diamond criterion.


.. admonition:: Scholarly journal

  The journal should be a scholarly journal that selects papers via an explicitly described
  evaluation process before and/or after publication, in line with accepted practices in the
  relevant discipline (See also DOAS https://doi.org/10.58121/Z15S-JY03)

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <scholarly-journal value="true" />

Attributes:
 - value (Mandatory) - Whether journal fulfills scholarly journal diamond criterion. Possible values: true or false. 

community-owned
===============

Status of the community-owned diamond criterion.

.. admonition:: Community-owned

  The journal title must be owned by public or not-for-profit organisations (or parts thereof)
  whose mission includes performing or promoting research and scholarship. These include
  but are not limited to research performing organisations (RPOs), research funding
  organisations (RFOs), organisations connected to RPOs (university libraries, university
  presses, faculties, and departments), research institutes, and scholarly societies. The journal
  should explain its ownership status on its webpage.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <community-owned value="true"/>

Attributes:
 - value (Mandatory) - Whether journal fulfills community owned diamond criterion. Possible values: true or false.

open-access-with-open-licenses
==============================

Status of the open access with open licenses diamond criterion.

.. admonition:: Open Access with open licenses

  All outputs of the journal should be Open Access and carry an open license that is included
  in the article-level metadata.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <open-access-with-open-licenses value="true" />

Attributes:
 - value (Mandatory) - Whether journal fulfills community open access with open licenses criterion. Possible values: true or false.

no-fees
======================

Status of the no fees diamond criterion.

.. admonition:: No fees

  Publication in the journal is not contingent on the payment of fees of any kind (e.g. article
  processing charges or membership dues). The journal should state this as such on its
  webpage. Voluntary author contributions and donations are allowed, if this is not a
  condition for publication.

Mandatory: **No**

Occurrences: **1**


.. code-block:: xml

    <no-fees value="true"/>

Attributes:
 - value (Mandatory) - Whether journal fulfills no fees diamond criterion. Possible values: true or false. 

open-to-all-authors
===================

Status of the open to all authors diamond criterion.

.. admonition:: Open to all authors

  Authorship in the journal should not be limited to any type of affiliation. Any author can
  submit an article that is in line with the aims and scope of the journal.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <open-to-all-authors value="true" />

Attributes:
 - value (Mandatory) - Whether journal fulfills open to all authors diamond criterion. Possible values: true or false. 


organizations
*************

Organizations associated with the journal, in particular the publisher.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <organizations>
    <publisher>
      <name>British Medical Journal</name>
      <location>
        <country iso3="GBR">United Kingdom</country>
      </location>
    </publisher>
    <other-organization>
      <name>University of Science</name>
    </other-organization>
    <other-organization>
      <name>University of Science 2</name>
    </other-organization>
  </organizations>

publisher
=========

Organization publishing the journal.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <publisher>
      <name>British Medical Journal</name>
      <location>
        <country iso3="GBR">United Kingdom</country>
      </location>
    </publisher>

name
----

Name of the publisher.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <name>British Medical Journal</name>

location
---------

Information about publisher location.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <location>
    <country iso3="GBR">United Kingdom</country>
  </location>

country
~~~~~~~~~~~~~~~~~~~

Country of the publisher.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <country iso3="GBR">United Kingdom</country>

Attributes:
 - iso3 - :ref:`ISO 3166-1 alpha-3 country code <country-code-label>`

other-organization
===================

The owner of the journal, if it is different from the publisher, or other organizations associated with the journal.

Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

    <other-organization>
      <name>University of Science</name>
    </other-organization>

name
------

Name of the organization.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <name>University of Science</name>


publication-policy
******************

Element containing policies related to the publication process in the journal.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <publication-policy>
    <review-process type="peer"/>
    <languages>
      <language iso2="ENG">English</language>
      <language iso2="DEU">German</language>
      <language>Polish</language>
    </languages>
    <licenses>
      <license xlink:href="http://creativecommons.org/licenses/by-nc/4.0" />
      <license xlink:href="http://creativecommons.org/licenses/by/4.0" />
    </licenses>
  </publication-policy>

review-process
==============

Describes reviewing process used by the journal.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <review-process type="peer"/>

Attributes:
 - type - Type of the review process. Currently only **peer** is allowed (meaning that journal is peer reviewed).


languages
=========

Wrapper element for the languages in which the journal accepts article submissions.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <languages>
      <language iso2="ENG">English</language>
      <language iso2="DEU">German</language>
      <language>Polish</language>
    </languages>

language
--------

Language in which the journal accepts article submissions. If journal accepts submissions in multiple languages then this element needs to be repeated.


Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

  <language iso2="ENG">English</language>
      
Attributes:
 - iso2 - :ref:`ISO 639-2/T language code <language-code-label>`

licenses
========

Wrapper element for licenses under which the journal publishes its contents.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

    <licenses>
      <license xlink:href="http://creativecommons.org/licenses/by-nc/4.0" />
      <license xlink:href="http://creativecommons.org/licenses/by/4.0" />
      <license xlink:href="http://someothernoncclicense.com" />
    </licenses>

license
--------

License assigned under which the journal publishes its contents. If journal publishes its contents using different licenses then this element needs to be repeated.

Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

      <license xlink:href="http://creativecommons.org/licenses/by-nc/4.0" />

Attributes:
 - xlink:href - Link to webpage describing the license



self-uri
********

Link to the journal webpage (provided as an attribute)

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <self-uri xlink:href="http://ejournal.patria-artha.ac.id/index.php/patj/index" />


Attributes:
 - xlink:href - link to the journal webpage

keywords
***********

Wrapper element for journal keywords.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <keywords>
    <keyword>DNA analysis</keyword>
    <keyword>gene expression</keyword>
    <keyword>parallel cloning</keyword>
    <keyword>fluid microarray</keyword>
  </keywords>

keyword
=======

Journal keyword.

Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

  <keyword>DNA analysis</keyword>

classifications
****************

Wrapper element for journal classifications.

Mandatory: **No**

Occurrences: **1**

.. code-block:: xml

  <classifications>
    <classification type="oecd-2007">
      <class code="2.6" value="Medical engineering" />
    </classification>
  </classifications>


classification
==============



Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

    <classification type="oecd-2007">
      <class code="2.6" value="Medical engineering" />
    </classification>

Attributes:
 - type - 

class
------------------

Single entry of classification

Mandatory: **No**

Occurrences: **0-n**

.. code-block:: xml

  <class code="2.6" value="Medical engineering" />

Attributes:
 - code - 
 - value - 


.. _country-code-label:

**************
Country codes
**************

JMEF follows the ISO 3166-1 alpha-3 standard for country identification.

Below is the list of supported codes:

- **ABW** - Aruba
- **AFG** - Afghanistan
- **AGO** - Angola
- **AIA** - Anguilla
- **ALA** - Åland Islands
- **ALB** - Albania
- **AND** - Andorra
- **ARE** - United Arab Emirates
- **ARG** - Argentina
- **ARM** - Armenia
- **ASM** - American Samoa
- **ATA** - Antarctica
- **ATF** - French Southern Territories
- **ATG** - Antigua and Barbuda
- **AUS** - Australia
- **AUT** - Austria
- **AZE** - Azerbaijan
- **BDI** - Burundi
- **BEL** - Belgium
- **BEN** - Benin
- **BES** - Bonaire, Sint Eustatius and Saba
- **BFA** - Burkina Faso
- **BGD** - Bangladesh
- **BGR** - Bulgaria
- **BHR** - Bahrain
- **BHS** - Bahamas
- **BIH** - Bosnia and Herzegovina
- **BLM** - Saint Barthélemy
- **BLR** - Belarus
- **BLZ** - Belize
- **BMU** - Bermuda
- **BOL** - Bolivia, Plurinational State of
- **BRA** - Brazil
- **BRB** - Barbados
- **BRN** - Brunei Darussalam
- **BTN** - Bhutan
- **BVT** - Bouvet Island
- **BWA** - Botswana
- **CAF** - Central African Republic
- **CAN** - Canada
- **CCK** - Cocos (Keeling) Islands
- **CHE** - Switzerland
- **CHL** - Chile
- **CHN** - China
- **CIV** - Côte d'Ivoire
- **CMR** - Cameroon
- **COD** - Congo, Democratic Republic of the
- **COG** - Congo
- **COK** - Cook Islands
- **COL** - Colombia
- **COM** - Comoros
- **CPV** - Cabo Verde
- **CRI** - Costa Rica
- **CUB** - Cuba
- **CUW** - Curaçao
- **CXR** - Christmas Island
- **CYM** - Cayman Islands
- **CYP** - Cyprus
- **CZE** - Czechia
- **DEU** - Germany
- **DJI** - Djibouti
- **DMA** - Dominica
- **DNK** - Denmark
- **DOM** - Dominican Republic
- **DZA** - Algeria
- **ECU** - Ecuador
- **EGY** - Egypt
- **ERI** - Eritrea
- **ESH** - Western Sahara
- **ESP** - Spain
- **EST** - Estonia
- **ETH** - Ethiopia
- **FIN** - Finland
- **FJI** - Fiji
- **FLK** - Falkland Islands (Malvinas)
- **FRA** - France
- **FRO** - Faroe Islands
- **FSM** - Micronesia, Federated States of
- **GAB** - Gabon
- **GBR** - United Kingdom of Great Britain and Northern Ireland
- **GEO** - Georgia
- **GGY** - Guernsey
- **GHA** - Ghana
- **GIB** - Gibraltar
- **GIN** - Guinea
- **GLP** - Guadeloupe
- **GMB** - Gambia
- **GNB** - Guinea-Bissau
- **GNQ** - Equatorial Guinea
- **GRC** - Greece
- **GRD** - Grenada
- **GRL** - Greenland
- **GTM** - Guatemala
- **GUF** - French Guiana
- **GUM** - Guam
- **GUY** - Guyana
- **HKG** - Hong Kong
- **HMD** - Heard Island and McDonald Islands
- **HND** - Honduras
- **HRV** - Croatia
- **HTI** - Haiti
- **HUN** - Hungary
- **IDN** - Indonesia
- **IMN** - Isle of Man
- **IND** - India
- **IOT** - British Indian Ocean Territory
- **IRL** - Ireland
- **IRN** - Iran, Islamic Republic of
- **IRQ** - Iraq
- **ISL** - Iceland
- **ISR** - Israel
- **ITA** - Italy
- **JAM** - Jamaica
- **JEY** - Jersey
- **JOR** - Jordan
- **JPN** - Japan
- **KAZ** - Kazakhstan
- **KEN** - Kenya
- **KGZ** - Kyrgyzstan
- **KHM** - Cambodia
- **KIR** - Kiribati
- **KNA** - Saint Kitts and Nevis
- **KOR** - Korea, Republic of
- **KWT** - Kuwait
- **LAO** - Lao People's Democratic Republic
- **LBN** - Lebanon
- **LBR** - Liberia
- **LBY** - Libya
- **LCA** - Saint Lucia
- **LIE** - Liechtenstein
- **LKA** - Sri Lanka
- **LSO** - Lesotho
- **LTU** - Lithuania
- **LUX** - Luxembourg
- **LVA** - Latvia
- **MAC** - Macao
- **MAF** - Saint Martin (French part)
- **MAR** - Morocco
- **MCO** - Monaco
- **MDA** - Moldova, Republic of
- **MDG** - Madagascar
- **MDV** - Maldives
- **MEX** - Mexico
- **MHL** - Marshall Islands
- **MKD** - North Macedonia
- **MLI** - Mali
- **MLT** - Malta
- **MMR** - Myanmar
- **MNE** - Montenegro
- **MNG** - Mongolia
- **MNP** - Northern Mariana Islands
- **MOZ** - Mozambique
- **MRT** - Mauritania
- **MSR** - Montserrat
- **MTQ** - Martinique
- **MUS** - Mauritius
- **MWI** - Malawi
- **MYS** - Malaysia
- **MYT** - Mayotte
- **NAM** - Namibia
- **NCL** - New Caledonia
- **NER** - Niger
- **NFK** - Norfolk Island
- **NGA** - Nigeria
- **NIC** - Nicaragua
- **NIU** - Niue
- **NLD** - Netherlands, Kingdom of the
- **NOR** - Norway
- **NPL** - Nepal
- **NRU** - Nauru
- **NZL** - New Zealand
- **OMN** - Oman
- **PAK** - Pakistan
- **PAN** - Panama
- **PCN** - Pitcairn
- **PER** - Peru
- **PHL** - Philippines
- **PLW** - Palau
- **PNG** - Papua New Guinea
- **POL** - Poland
- **PRI** - Puerto Rico
- **PRK** - Korea, Democratic People's Republic of
- **PRT** - Portugal
- **PRY** - Paraguay
- **PSE** - Palestine, State of
- **PYF** - French Polynesia
- **QAT** - Qatar
- **REU** - Réunion
- **ROU** - Romania
- **RUS** - Russian Federation
- **RWA** - Rwanda
- **SAU** - Saudi Arabia
- **SDN** - Sudan
- **SEN** - Senegal
- **SGP** - Singapore
- **SGS** - South Georgia and the South Sandwich Islands
- **SHN** - Saint Helena, Ascension and Tristan da Cunha
- **SJM** - Svalbard and Jan Mayen
- **SLB** - Solomon Islands
- **SLE** - Sierra Leone
- **SLV** - El Salvador
- **SMR** - San Marino
- **SOM** - Somalia
- **SPM** - Saint Pierre and Miquelon
- **SRB** - Serbia
- **SSD** - South Sudan
- **STP** - Sao Tome and Principe
- **SUR** - Suriname
- **SVK** - Slovakia
- **SVN** - Slovenia
- **SWE** - Sweden
- **SWZ** - Eswatini
- **SXM** - Sint Maarten (Dutch part)
- **SYC** - Seychelles
- **SYR** - Syrian Arab Republic
- **TCA** - Turks and Caicos Islands
- **TCD** - Chad
- **TGO** - Togo
- **THA** - Thailand
- **TJK** - Tajikistan
- **TKL** - Tokelau
- **TKM** - Turkmenistan
- **TLS** - Timor-Leste
- **TON** - Tonga
- **TTO** - Trinidad and Tobago
- **TUN** - Tunisia
- **TUR** - Türkiye
- **TUV** - Tuvalu
- **TWN** - Taiwan, Province of China
- **TZA** - Tanzania, United Republic of
- **UGA** - Uganda
- **UKR** - Ukraine
- **UMI** - United States Minor Outlying Islands
- **URY** - Uruguay
- **USA** - United States of America
- **UZB** - Uzbekistan
- **VAT** - Holy See
- **VCT** - Saint Vincent and the Grenadines
- **VEN** - Venezuela, Bolivarian Republic of
- **VGB** - Virgin Islands (British)
- **VIR** - Virgin Islands (U.S.)
- **VNM** - Viet Nam
- **VUT** - Vanuatu
- **WLF** - Wallis and Futuna
- **WSM** - Samoa
- **YEM** - Yemen
- **ZAF** - South Africa
- **ZMB** - Zambia
- **ZWE** - Zimbabwe

To learn more about ISO 3166-1 alpha-3 country codes visit `Wikipedia page about ISO 3166-1 alpha-3 codes <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__.

.. _language-code-label:

**************
Language codes
**************

JMEF follows the ISO 639-2/T standard for language identification.

Below is the list of supported codes:

- **AAR** - Afar
- **ABK** - Abkhazian
- **ACE** - Achinese
- **ACH** - Acoli
- **ADA** - Adangme
- **ADY** - Adyghe
- **AFA** - Afro-Asiatic languages
- **AFH** - Afrihili
- **AFR** - Afrikaans
- **AIN** - Ainu
- **AKA** - Akan
- **AKK** - Akkadian
- **ALE** - Aleut
- **ALG** - Algonquian languages
- **ALT** - Southern Altai
- **AMH** - Amharic
- **ANG** - English, Old (ca. 450-1100)
- **ANP** - Angika
- **APA** - Apache languages
- **ARA** - Arabic
- **ARC** - Official Aramaic (700-300 BCE)
- **ARG** - Aragonese
- **ARN** - Mapudungun
- **ARP** - Arapaho
- **ART** - Artificial languages
- **ARW** - Arawak
- **ASM** - Assamese
- **AST** - Asturian
- **ATH** - Athapascan languages
- **AUS** - Australian languages
- **AVA** - Avaric
- **AVE** - Avestan
- **AWA** - Awadhi
- **AYM** - Aymara
- **AZE** - Azerbaijani
- **BAD** - Banda languages
- **BAI** - Bamileke languages
- **BAK** - Bashkir
- **BAL** - Baluchi
- **BAM** - Bambara
- **BAN** - Balinese
- **BAS** - Basa
- **BAT** - Baltic languages
- **BEJ** - Beja
- **BEL** - Belarusian
- **BEM** - Bemba
- **BEN** - Bengali
- **BER** - Berber languages
- **BHO** - Bhojpuri
- **BIH** - Bihari languages
- **BIK** - Bikol
- **BIN** - Bini
- **BIS** - Bislama
- **BLA** - Siksika
- **BNT** - Bantu languages
- **BOD** - Tibetan
- **BOS** - Bosnian
- **BRA** - Braj
- **BRE** - Breton
- **BTK** - Batak languages
- **BUA** - Buriat
- **BUG** - Buginese
- **BUL** - Bulgarian
- **BYN** - Blin
- **CAD** - Caddo
- **CAI** - Central American Indian languages
- **CAR** - Galibi Carib
- **CAT** - Catalan
- **CAU** - Caucasian languages
- **CEB** - Cebuano
- **CEL** - Celtic languages
- **CES** - Czech
- **CHA** - Chamorro
- **CHB** - Chibcha
- **CHE** - Chechen
- **CHG** - Chagatai
- **CHK** - Chuukese
- **CHM** - Mari
- **CHN** - Chinook jargon
- **CHO** - Choctaw
- **CHP** - Chipewyan
- **CHR** - Cherokee
- **CHU** - Church Slavic
- **CHV** - Chuvash
- **CHY** - Cheyenne
- **CMC** - Chamic languages
- **CNR** - Montenegrin
- **COP** - Coptic
- **COR** - Cornish
- **COS** - Corsican
- **CPE** - Creoles and pidgins, English-based
- **CPF** - Creoles and pidgins, French-based
- **CPP** - Creoles and pidgins, Portuguese-based
- **CRE** - Cree
- **CRH** - Crimean Tatar
- **CRP** - Creoles and pidgins
- **CSB** - Kashubian
- **CUS** - Cushitic languages
- **CYM** - Welsh
- **DAK** - Dakota
- **DAN** - Danish
- **DAR** - Dargwa
- **DAY** - Land Dayak languages
- **DEL** - Delaware
- **DEN** - Slave (Athapascan)
- **DEU** - German
- **DGR** - Dogrib
- **DIN** - Dinka
- **DIV** - Divehi
- **DOI** - Dogri
- **DRA** - Dravidian languages
- **DSB** - Lower Sorbian
- **DUA** - Duala
- **DUM** - Dutch, Middle (ca. 1050-1350)
- **DYU** - Dyula
- **DZO** - Dzongkha
- **EFI** - Efik
- **EGY** - Egyptian (Ancient)
- **EKA** - Ekajuk
- **ELL** - Greek, Modern (1453-)
- **ELX** - Elamite
- **ENG** - English
- **ENM** - English, Middle (1100-1500)
- **EPO** - Esperanto
- **EST** - Estonian
- **EUS** - Basque
- **EWE** - Ewe
- **EWO** - Ewondo
- **FAN** - Fang
- **FAO** - Faroese
- **FAS** - Persian
- **FAT** - Fanti
- **FIJ** - Fijian
- **FIL** - Filipino
- **FIN** - Finnish
- **FIU** - Finno-Ugrian languages
- **FON** - Phone
- **FRA** - French
- **FRM** - French, Middle (ca. 1400-1600)
- **FRO** - French, Old (842-ca. 1400)
- **FRR** - Northern Frisian
- **FRS** - Eastern Frisian
- **FRY** - Western Frisian
- **FUL** - Fulah
- **FUR** - Friulian
- **GAA** - Ga
- **GAY** - Gayo
- **GBA** - Gbaya
- **GEM** - Germanic languages
- **GEZ** - Geez
- **GIL** - Gilbertese
- **GLA** - Gaelic
- **GLE** - Irish
- **GLG** - Galician
- **GLV** - Manx
- **GMH** - German, Middle High (ca. 1050-1500)
- **GOH** - German, Old High (ca. 750-1050)
- **GON** - Gondi
- **GOR** - Gorontalo
- **GOT** - Gothic
- **GRB** - Grebo
- **GRC** - Greek, Ancient (to 1453)
- **GRN** - Guarani
- **GSW** - Swiss German
- **GUJ** - Gujarati
- **GWI** - Gwich'in
- **HAI** - Haida
- **HAT** - Haitian
- **HAU** - Hausa
- **HAW** - Hawaiian
- **HEB** - Hebrew
- **HER** - Herero
- **HIL** - Hiligaynon
- **HIM** - Himachali languages
- **HIN** - Hindi
- **HIT** - Hittite
- **HMN** - Hmong
- **HMO** - Hiri Motu
- **HRV** - Croatian
- **HSB** - Upper Sorbian
- **HUN** - Hungarian
- **HUP** - Hupa
- **HYE** - Armenian
- **IBA** - Iban
- **IBO** - Igbo
- **IDO** - Ido
- **III** - Sichuan Yi
- **IJO** - Ijo languages
- **IKU** - Inuktitut
- **ILE** - Interlingue
- **ILO** - Iloko
- **INA** - Interlingua (International Auxiliary Language Association)
- **INC** - Indic languages
- **IND** - Indonesian
- **INE** - Indo-European languages
- **INH** - Ingush
- **IPK** - Inupiaq
- **IRA** - Iranian languages
- **IRO** - Iroquoian languages
- **ISL** - Icelandic
- **ITA** - Italian
- **JAV** - Javanese
- **JBO** - Lojban
- **JPN** - Japanese
- **JPR** - Judeo-Persian
- **JRB** - Judeo-Arabic
- **KAA** - Kara-Kalpak
- **KAB** - Kabyle
- **KAC** - Kachin
- **KAL** - Kalaallisut
- **KAM** - Kamba
- **KAN** - Kannada
- **KAR** - Karen languages
- **KAS** - Kashmiri
- **KAT** - Georgian
- **KAU** - Kanuri
- **KAW** - Kawi
- **KAZ** - Kazakh
- **KBD** - Kabardian
- **KHA** - Khasi
- **KHI** - Khoisan languages
- **KHM** - Khmer
- **KHO** - Khotanese
- **KIK** - Kikuyu
- **KIN** - Kinyarwanda
- **KIR** - Kirghiz
- **KMB** - Kimbundu
- **KOK** - Konkani
- **KOM** - Komi
- **KON** - Kongo
- **KOR** - Korean
- **KOS** - Kosraean
- **KPE** - Kpelle
- **KRC** - Karachay-Balkar
- **KRL** - Karelian
- **KRO** - Kru languages
- **KRU** - Kurukh
- **KUA** - Kuanyama
- **KUM** - Kumyk
- **KUR** - Kurdish
- **KUT** - Kutenai
- **LAD** - Ladino
- **LAH** - Lahnda
- **LAM** - Lamba
- **LAO** - Lao
- **LAT** - Latin
- **LAV** - Latvian
- **LEZ** - Lezghian
- **LIM** - Limburgan
- **LIN** - Lingala
- **LIT** - Lithuanian
- **LOL** - Mongo
- **LOZ** - Lozi
- **LTZ** - Luxembourgish
- **LUA** - Luba-Lulua
- **LUB** - Luba-Katanga
- **LUG** - Ganda
- **LUI** - Luiseno
- **LUN** - Lunda
- **LUO** - Luo (Kenya and Tanzania)
- **LUS** - Lushai
- **MAD** - Madurese
- **MAG** - Magahi
- **MAH** - Marshallese
- **MAI** - Maithili
- **MAK** - Makasar
- **MAL** - Malayalam
- **MAN** - Mandingo
- **MAP** - Austronesian languages
- **MAR** - Marathi
- **MAS** - Masai
- **MDF** - Moksha
- **MDR** - Mandar
- **MEN** - Mende
- **MGA** - Irish, Middle (900-1200)
- **MIC** - Mi'kmaq
- **MIN** - Minangkabau
- **MIS** - Uncoded languages
- **MKD** - Macedonian
- **MKH** - Mon-Khmer languages
- **MLG** - Malagasy
- **MLT** - Maltese
- **MNC** - Manchu
- **MNI** - Manipuri
- **MNO** - Manobo languages
- **MOH** - Mohawk
- **MON** - Mongolian
- **MOS** - Mossi
- **MRI** - Maori
- **MSA** - Malay
- **MUL** - Multiple languages
- **MUN** - Munda languages
- **MUS** - Creek
- **MWL** - Mirandese
- **MWR** - Marwari
- **MYA** - Burmese
- **MYN** - Mayan languages
- **MYV** - Erzya
- **NAH** - Nahuatl languages
- **NAI** - North American Indian languages
- **NAP** - Neapolitan
- **NAU** - Nauru
- **NAV** - Navajo
- **NBL** - Ndebele, South
- **NDE** - Ndebele, North
- **NDO** - Ndonga
- **NDS** - Low German
- **NEP** - Nepali
- **NEW** - Nepal Bhasa
- **NIA** - Nias
- **NIC** - Niger-Kordofanian languages
- **NIU** - Niuean
- **NLD** - Dutch
- **NNO** - Norwegian Nynorsk
- **NOB** - Bokmål, Norwegian
- **NOG** - Nogai
- **NON** - Norse, Old
- **NOR** - Norwegian
- **NQO** - N'Ko
- **NSO** - Pedi
- **NUB** - Nubian languages
- **NWC** - Classical Newari
- **NYA** - Chichewa
- **NYM** - Nyamwezi
- **NYN** - Nyankole
- **NYO** - Nyoro
- **NZI** - Nzima
- **OCI** - Occitan (post 1500)
- **OJI** - Ojibwa
- **ORI** - Oriya
- **ORM** - Oromo
- **OSA** - Osage
- **OSS** - Ossetian
- **OTA** - Turkish, Ottoman (1500-1928)
- **OTO** - Otomian languages
- **PAA** - Papuan languages
- **PAG** - Pangasinan
- **PAL** - Pahlavi
- **PAM** - Pampanga
- **PAN** - Punjabi
- **PAP** - Papiamento
- **PAU** - Palauan
- **PEO** - Persian, Old (ca. 600-400 BC)
- **PHI** - Philippine languages
- **PHN** - Phoenician
- **PLI** - Pali
- **POL** - Polish
- **PON** - Pohnpeian
- **POR** - Portuguese
- **PRA** - Prakrit languages
- **PRO** - Provençal, Old (to 1500)
- **PUS** - Pashto
- **QUE** - Quechua
- **RAJ** - Rajasthani
- **RAP** - Rapanui
- **RAR** - Rarotongan
- **ROA** - Romance languages
- **ROH** - Romansh
- **ROM** - Romany
- **RON** - Romanian
- **RUN** - Rundi
- **RUP** - Aromanian
- **RUS** - Russian
- **SAD** - Sandawe
- **SAG** - Sango
- **SAH** - Yakut
- **SAI** - South American Indian languages
- **SAL** - Salishan languages
- **SAM** - Samaritan Aramaic
- **SAN** - Sanskrit
- **SAS** - Sasak
- **SAT** - Santali
- **SCN** - Sicilian
- **SCO** - Scots
- **SEL** - Selkup
- **SEM** - Semitic languages
- **SGA** - Irish, Old (to 900)
- **SGN** - Sign Languages
- **SHN** - Shan
- **SID** - Sidamo
- **SIN** - Sinhala
- **SIO** - Siouan languages
- **SIT** - Sino-Tibetan languages
- **SLA** - Slavic languages
- **SLK** - Slovak
- **SLV** - Slovenian
- **SMA** - Southern Sami
- **SME** - Northern Sami
- **SMI** - Sami languages
- **SMJ** - Lule Sami
- **SMN** - Inari Sami
- **SMO** - Samoan
- **SMS** - Skolt Sami
- **SNA** - Shona
- **SND** - Sindhi
- **SNK** - Soninke
- **SOG** - Sogdian
- **SOM** - Somali
- **SON** - Songhai languages
- **SOT** - Sotho, Southern
- **SPA** - Spanish
- **SQI** - Albanian
- **SRD** - Sardinian
- **SRN** - Sranan Tongo
- **SRP** - Serbian
- **SRR** - Serer
- **SSA** - Nilo-Saharan languages
- **SSW** - Swati
- **SUK** - Sukuma
- **SUN** - Sundanese
- **SUS** - Susu
- **SUX** - Sumerian
- **SWA** - Swahili
- **SWE** - Swedish
- **SYC** - Classical Syriac
- **SYR** - Syriac
- **TAH** - Tahitian
- **TAI** - Tai languages
- **TAM** - Tamil
- **TAT** - Tatar
- **TEL** - Telugu
- **TEM** - Timne
- **TER** - Tereno
- **TET** - Tetum
- **TGK** - Tajik
- **TGL** - Tagalog
- **THA** - Thai
- **TIG** - Tigre
- **TIR** - Tigrinya
- **TIV** - Tiv
- **TKL** - Tokelau
- **TLH** - Klingon
- **TLI** - Tlingit
- **TMH** - Tamashek
- **TOG** - Tonga (Nyasa)
- **TON** - Tonga (Tonga Islands)
- **TPI** - Tok Pisin
- **TSI** - Tsimshian
- **TSN** - Tswana
- **TSO** - Tsonga
- **TUK** - Turkmen
- **TUM** - Tumbuka
- **TUP** - Tupi languages
- **TUR** - Turkish
- **TUT** - Altaic languages
- **TVL** - Tuvalu
- **TWI** - Twi
- **TYV** - Tuvinian
- **UDM** - Udmurt
- **UGA** - Ugaritic
- **UIG** - Uighur
- **UKR** - Ukrainian
- **UMB** - Umbundu
- **UND** - Undetermined
- **URD** - Urdu
- **UZB** - Uzbek
- **VAI** - Vai
- **VEN** - Venda
- **VIE** - Vietnamese
- **VOL** - Volapük
- **VOT** - Votic
- **WAK** - Wakashan languages
- **WAL** - Wolaitta
- **WAR** - Waray
- **WAS** - Washo
- **WEN** - Sorbian languages
- **WLN** - Walloon
- **WOL** - Wolof
- **XAL** - Kalmyk
- **XHO** - Xhosa
- **YAO** - Yao
- **YAP** - Yapese
- **YID** - Yiddish
- **YOR** - Yoruba
- **YPK** - Yupik languages
- **ZAP** - Zapotec
- **ZBL** - Blissymbols
- **ZEN** - Zenaga
- **ZGH** - Standard Moroccan Tamazight
- **ZHA** - Zhuang
- **ZHO** - Chinese
- **ZND** - Zande languages
- **ZUL** - Zulu
- **ZUN** - Zuni
- **ZXX** - No linguistic content"
- **ZZA** - Zaza

To learn more about ISO 639-2 language codes visit `Wikipedia page about ISO 639-2 codes <https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes>`__.


.. note::

  Be aware that ISO 639-2 codes have two flavours: bibliographical and terminological. In JMEF the terminological codes are used. There are about 20 cases where bibliographical and terminological codes are different. For example: terminological code for Deutsch language code is **DEU** and bibliographical is **GER**






