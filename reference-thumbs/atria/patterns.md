# Atria — vizualų paternai (Tom Crosshill / PL recruitment, 87 creatives)

Šaltinis: tryatria.com workspace, brand "Tom Crosshill", board "PL recruitment"
PDF: `Atria _ The AI ad engine that grows your revenue.pdf` (2026-04-05, 11:50)
Crops: `page-1-grid.png`, `page-2-grid.png`, `page-{1,2}-col-{1..5}.png`

## Brand profilis

Tas pats segmentas kaip Kapitał Życia — finansinė edukacija lenkų rinkai, recruitment'as / ETF investavimo mokymai.
Auditorija plati (P1-P5 personos perdengiamos), primary pitch — "stop kaupti į ZUS, pradėk investuoti".

## Spalvos (Atria favorites)

| Spalva | Hex (apytiksliai) | Kur naudojama |
|---|---|---|
| Bright green | `#00B14F` / `#27D17C` | Statement cards, CTA blokai |
| Forest green | `#0E5C2F` | Premium serif quote BG |
| Warning yellow | `#F4D33E` | "ULTIMATE GUIDE" cards, attention-grabbers |
| Burgundy / wine | `#4A1E2A` | Premium testimonial / quote BG |
| Dark purple | `#3B2A4A` | Niche statement cards |
| Cream / off-white | `#F5EFE3` / `#FBF6EC` | Soft card pages |
| Pure black | `#0F0F0F` | Headlines on cream/yellow |

**Insight:** Atria nebijo CIRKULIUOTI sodriom solid spalvom. Kapital Życia šablonas šiuo metu fokusuojasi į green-deep + cream — verta pridėti **yellow alarm** ir **burgundy premium** variantus dėl scroll-stopping galios.

## Layout šeimos (rastos Atria 87 creatives)

### A. Bright-green statement (pure typography)
- Vientisas šviesiai žalias BG (#00B14F)
- 2-4 žodžių mega headline juodu/baltu, Anton-style
- Mažas creator headshot kampe (opt.)
- Pavyzdžiai: "EVERYONE should learn how to invest", "20 YEARS OF INVESTING IN 90 MINUTES"
- **KZ pritaikymas:** AD7 broad offer + AD5 korpo offer

### B. Yellow alarm card
- Warning yellow BG (#F4D33E)
- "ULTIMATE GUIDE" / "BECOME AN X" tipo headline
- Strong contrast — black bold text
- Daugiausia naudojama feed (4:5)
- **KZ pritaikymas:** AD2 ZUS Math, AD3 OC Commission Trap

### C. Burgundy quote / testimonial
- Tamsus wine BG (#4A1E2A) arba dark purple
- Serif italic quote ("WHAT IF YOU COULD RETIRE EARLY?")
- Maža attribution apačioje
- Premium "invitation" feel
- **KZ pritaikymas:** AD7C "the offer" watercolor variantas, AD4C agent nieruchomości

### D. Creator-face UGC
- Light/dark BG + bald guy pusinis portretas
- Text overlay viršuje + CTA apačioje
- Apie 30% Tom Crosshill ads turi jo veidą
- **KZ pritaikymas:** Reikia placeholder'io recruiter veidui — dabar nėra. Galima panaudoti silhouette ar generic biznesmen photo
- *Sprendimas:* nepasisavinti — KZ nestato vieno žmogaus brand'o, palikti type-only / iliustracijas

### E. Phone-checklist mockup
- Kreminis BG
- Phone frame + screenshot iš formų / checklistų
- "Schedule a 1:1 call" stilistika
- **KZ pritaikymas:** CTA-fokusuotos iteracijos (ypač "Aplikuj" close), AD7

### F. Lifestyle photo + text overlay
- Outdoor scene, kalnai, gamta, kavinė
- Text apačioje white-over-photo
- Aspirational vibe
- **KZ pritaikymas:** Jau yra `hero-photo` — KEEP, prisitvarkyti su Warsaw lifestyle nuotraukom

### G. Stat-wake-up dark
- Tamsus žalias arba juodas BG
- Mega skaičius (% ar PLN) + 1 sakinys explanation
- Mažas brand mark apačioje
- **KZ pritaikymas:** Jau yra `mega-number` — sustiprinti su yellow alert variantu (žr. B)

## Hook formulės (iš matomų Atria headline'ų)

| Formulė | Atria pavyzdys | KZ adapt |
|---|---|---|
| "Does this sound like you?" | "DOES THIS SOUND LIKE YOU?" | "Czy to brzmi znajomo?" |
| Aspiracinis "What if" | "WHAT IF YOU COULD RETIRE EARLY?" | "A GDYBYŚ MÓGŁ ODEJŚĆ Z BANKU W TYM ROKU?" |
| Listicle "Reason why" | "REASON WHY MOST NEVER RETIRE EARLY" | "POWÓD, DLA KTÓREGO 95% DORADCÓW REZYGNUJE" |
| Compression value | "20 YEARS OF INVESTING IN 90 MINUTES" | "10 LAT KARIERY UBEZPIECZENIOWEJ W 1 ROZMOWIE" |
| Direct CTA mockup | "Schedule a 1:1 call with my team" | "Umów rozmowę z naszym recruiterem" |
| Regret / FOMO | "I WISH I started YEARS ago..." | "Żałuję, że nie zacząłem 10 lat temu" |
| Controversial | "EVERYONE should learn how to invest" | "KAŻDY doradca powinien sprawdzić tę matematykę" |
| Authority frame | "BECOME AN ETF INVESTOR / ULTIMATE GUIDE" | "ZOSTAŃ PRAWDZIWYM DORADCĄ / KOMPLETNY PRZEWODNIK" |

## Konkretūs naujumai generator.py

1. **Pridėti CSS klasę `.ad.yellow`** — warning yellow BG (#F4D33E), juodas tekstas
2. **Pridėti CSS klasę `.ad.burgundy`** — wine BG (#4A1E2A), serif italic headline
3. **Naujas layout `bright-statement`** — full-color bg, no image, mega Anton headline (vienas žodis arba dviejų)
4. **Naujas layout `yellow-alarm`** — yellow BG su "ULTIMATE GUIDE" / "POWÓD WHY" framing
5. **Naujas layout `burgundy-quote`** — wine BG su Playfair italic + creator attribution
6. **Naujas layout `phone-mockup`** — kreminis BG su CSS-only telefono frame'u + faked checklist
7. **Hook varijavimas** — kiekvienam AD koncepcijai 3 iteracijoms suteikti 3 skirtingas hook formules iš lentelės virš

## Layout reassignment (dabartiniai vs Atria-influenced)

| AD | Iter | DABAR | NAUJAS |
|----|------|-------|--------|
| 1A | split-screen | KEEP |
| 1B | ugc-story | KEEP |
| 1C | bold-statement | **bright-statement** (zaliąja BG) |
| 2A | handwritten-notes | KEEP |
| 2B | mega-number | **yellow-alarm** (`#F4D33E` BG) |
| 2C | redacted-doc | KEEP |
| 3A | chalkboard | KEEP |
| 3B | ugc-story | KEEP |
| 3C | split-screen | **yellow-alarm** ("ULTIMATE GUIDE OC TRAP") |
| 4A | hero-photo | KEEP |
| 4B | handwritten-notes | KEEP |
| 4C | watercolor | **burgundy-quote** (premium "invitation") |
| 5A | hero-photo | KEEP |
| 5B | bold-statement | **bright-statement** |
| 5C | bold-numbered | KEEP |
| 6A | stamp-badge | KEEP |
| 6B | ugc-story | KEEP |
| 6C | bold-statement | **bright-statement** |
| 7A | watercolor | **burgundy-quote** |
| 7B | mega-number | **phone-mockup** (CTA-focused) |
| 7C | bold-numbered | **yellow-alarm** ("OFERTA POWODU") |

## Ko NEDAryti iš Atria

- **Necituoti Tom Crosshill** ar jokio kito žmogaus vardu — KZ ne creator brand'as
- **Nedėti to paties bald-guy stock photo** — atrodo kaip kopija, plagijavimas
- **Nepervaryt yellow** — max 1-2 yellow ads per koncepciją (3 iter), ne visi
- **Nepalikti per atspalvių** — jei dedi burgundy, pasirink consistent #4A1E2A, ne 5 skirtingus tonus
- **Nemiti €/PLN konvertavimo** — visada PLN su disclaimer'iu (Lenkijos rinka)
