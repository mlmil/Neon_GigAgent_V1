# Neon_Gig_Agent_v1 — Brainstorming Session

**Date**: 2026-09-03  
**Bot / Agent**: `Neon_Gig_Agent_v1` (Scout Agent Lane for Neon Blonde)  
**Corridor Reach**: San Francisco to San Diego  
**Contributors**:
- [x] **Antigravity** (Architectural Blueprints, Unorthodox Intelligence, Scraping Pipelines, Contact Discovery & Prototypes)
- [ ] **Codex** (Pending next session)
- [ ] **Claude** (Pending subsequent session)

---

# Part 1: Antigravity Deep Brainstorm

## 1. Executive Summary & Vision

To keep Neon Blonde booked across high-yield venues along the 500-mile coastal corridor from San Francisco to San Diego, `Neon_Gig_Agent_v1` must move beyond passive directory lookups. It should operate as an **autonomous radar system** combining:
1. **Unorthodox Signal Mining** (Liquor licenses, sound engineer networks, municipal permit filings).
2. **Social Media & Peer Band Scraping** (Flyer OCR, venue location tags, schedule monitoring).
3. **Automated Contact Waterfall Enrichment** (Zero-touch email/phone discovery for talent buyers).
4. **Strategic Penetration Plays** (Turnkey theme packages, peer band co-billing, emergency slot fill-ins).

---

## 2. Unorthodox & Non-Obvious Venue Discovery Angles

### Angle A: California ABC Liquor License & Entertainment Endorsement Mining
- **Concept**: The California Department of Alcoholic Beverage Control (ABC) publishes weekly public records of new applications, license transfers, and premises updates (specifically **Type 47** - On-Sale General Eating Place and **Type 48** - On-Sale General Public Premises).
- **The Signal**: Whenever a restaurant, brewery, or saloon applies for or transfers a Type 47/48 license with an **Entertainment / Live Music Endorsement**, it reveals newly opening or renovating venues **2 to 4 months before they officially announce entertainment schedules**.
- **Scout Play**: Target new liquor license filings in Malibu, Calabasas, Ventura, Santa Barbara, Orange County, and San Diego to pitch Neon Blonde as the opening-month headliner.

### Angle B: Live Sound Engineer & Production Rental Tag Mining
- **Concept**: Bands often forget to tag venues, but **Front-of-House (FOH) sound engineers, lighting designers, and gear rental companies** (e.g. staging/PA rental houses in Ventura, LA, OC, SD) constantly post behind-the-scenes Instagram stories and posts tagging the exact private estates, wineries, yacht clubs, and corporate retreats where they provide staging.
- **The Signal**: Scraping mentions from a curated list of 30+ SoCal/NorCal production techs uncovers private high-budget venues that never appear on public music blogs.

### Angle C: Municipal Council Agendas & Special Event Noise Permit Filings
- **Concept**: Cities along the SF-to-SD corridor (Ventura, Malibu, Calabasas, Thousand Oaks, Newport Beach, Carlsbad, etc.) require public filings for outdoor live amplified music permits, street closures, and park festivals.
- **The Signal**: Scraping municipal agenda PDFs for terms like *"Amplified Sound Permit"*, *"Summer Concert Series Contract"*, or *"Downtown Festival Entertainment"* surfaces municipal opportunities 6 months before public call-for-artist announcements.

### Angle D: Yelp & Google Maps Review NLP Sentiment Extraction
- **Concept**: Many high-capacity restaurants, beach bars, and breweries have great live music but terrible websites that don't maintain a music calendar.
- **The Signal**: Querying Google Maps and Yelp APIs across target zip codes with regex filters:
  - `"live band" AND ("dance floor" OR "Saturday night" OR "cover band" OR "80s")`
  - Score venues based on review frequency mentioning live music energy and room size.

### Angle E: Winery & Luxury Estate Preferred Vendor Lists
- **Concept**: High-budget private event hubs in Malibu, Santa Ynez, Paso Robles, and Napa maintain public "Preferred Vendor PDFs" for wedding and corporate event planners.
- **The Signal**: Scraping `/preferred-vendors`, `/private-events`, and `/corporate-retreats` extracts the direct names and emails of Event Directors and Entertainment Coordinators.

---

## 3. Social Media & Peer Band Scraping Architecture

### A. The "Peer Band Radar" (Competitor / Complementary Band Tracking)
By tracking where peer 80s/retro/party bands play, `Neon_Gig_Agent_v1` automatically discovers rooms with verified audience appetite, budget, and staging for a 6-piece live band.

#### Key Watchlist Bands (SF to SD Corridor):
1. **The Spazmatics** (80s New Wave / Retro) — SoCal / Statewide
2. **Fast Times** (80s Rock / Dance) — LA / Ventura / OC
3. **The Molly Ringwald Project** (80s Tribute) — Santa Barbara / Central Coast
4. **Twisted Gypsy** (Fleetwood Mac / Classic Pop-Rock) — SoCal Circuit
5. **Area 51** (Funk / Dance / Party) — Santa Barbara / Ventura
6. **The 805s** (Party Covers) — Ventura County / Conejo Valley
7. **Flashback Heart Attack** (80s Party Rock) — Orange County / Newport
8. **The Cheezies / Radio Rebels** (Retro Party) — San Diego County
9. **Super Diamond** (Neil Diamond / Retro) — SF Bay Area / Statewide
10. **Tainted Love** (80s Tribute) — San Francisco / Northern California

### B. Instagram Public Flyer Ingestion & Vision/OCR Pipeline
```text
Instagram Public Profile / Tagged Feed
                 │
                 ▼
     [Post & Image Fetcher]
                 │
                 ▼
  [Multimodal LLM / OCR Extractor]
  Extract:
  - Venue Name & City
  - Performance Date & Time
  - Co-billing / Opener Acts
  - Ticket Price / Cover
                 │
                 ▼
    [Venue Cross-Reference]
  Is venue in scout-leads.csv?
     ├─ Yes ──> Update last_checked & similar_bands_seen
     └─ No  ──> Create new lead (status: discovered)
```

### C. Municipal "Concerts in the Park" & Festival Harvester
A dedicated crawler targeting 40+ city Parks & Recreation portals along the SF-to-SD corridor:
- **Scrape Targets**:
  - Pleasant Valley Rec & Park (Camarillo)
  - Conejo Rec & Park District (Thousand Oaks)
  - City of Calabasas Community Services
  - City of Santa Barbara Parks & Rec
  - City of Newport Beach Cultural Arts
  - City of Carlsbad Cultural Arts (TGIF Concerts)
  - City of San Mateo / San Rafael Summer Series
- **Key Pattern Matches**: `"Call for Bands"`, `"Entertainment Application"`, `"Performer Submission"`, `"Submission Deadline"`.

---

## 4. Contact Discovery & Waterfall Enrichment

When a venue is discovered, `Neon_Gig_Agent_v1` runs a 5-tier waterfall to locate the talent buyer's direct email and phone number:

```text
[New Venue Lead]
       │
       ├─► Tier 1: Website Direct Scraping (/booking, /contact, /entertainment, mailto: links, schema.org)
       │
       ├─► Tier 2: Instagram Bio & Action Buttons (extract business email/phone buttons & bio text)
       │
       ├─► Tier 3: Search Engine Dorking (e.g. `site:linkedin.com/in ("Talent Buyer" OR "Booking") "Venue Name"`)
       │
       ├─► Tier 4: Email Permutation & MX Ping (booking@domain.com, events@domain.com, gm@domain.com)
       │
       └─► Tier 5: Fallback to Public Phone & In-Person Pitch Script
```

---

## 5. Strategic Venue Penetration Plays

### Play 1: The "Proven Room Fit" Pitch
- *Approach*: Pitching a talent buyer by referencing peer bands that had successful nights:
  > *"We noticed Fast Times and The Molly Ringwald Project always pack your dance floor. Neon Blonde delivers that exact high-octane 80s/retro party energy with a full 6-piece lineup..."*

### Play 2: The "Turnkey Theme Night" Package
- *Approach*: Instead of asking for a generic gig, pitch a ready-to-run event:
  > *"Neon Blonde presents 'Totally 80s Neon Night' — complete with promotional digital flyer package, customized social media ad assets, interval retro dance playlists, and stage lighting."*

### Play 3: Emergency "Open Slot" Arbitrage
- *Approach*: When the radar detects a scheduled band cancel on social media or a venue calendar shows an open Saturday within the next 3 weeks, trigger an immediate high-priority alert to Mike:
  > *"Alert: Sagebrush Cantina has an open Saturday slot on Oct 18. Instant pitch draft ready for review."*

---

## 6. Prototyping & Architecture Code Sketches

### Prototype A: Municipal Application & Event Harvester (`scripts/scout_municipal_crawler.py`)
```python
"""Prototype: Municipal Concerts in the Park Crawler."""
import re
import urllib.request
from bs4 import BeautifulSoup

MUNICIPAL_TARGETS = [
    {"city": "Camarillo", "url": "https://www.pvrpd.org/concerts-in-the-park", "county": "Ventura"},
    {"city": "Thousand Oaks", "url": "https://www.crpd.org/events/summer-concerts-in-the-park/", "county": "Ventura"},
    {"city": "Calabasas", "url": "https://www.cityofcalabasas.com/community/community-events", "county": "LA"},
    {"city": "Carlsbad", "url": "https://www.carlsbadca.gov/departments/cultural-arts/tgif-concerts-in-the-parks", "county": "San Diego"},
]

def scan_municipal_portal(target: dict) -> dict:
    req = urllib.request.Request(target["url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text()
            
            # Look for application windows & performer calls
            deadline_match = re.search(r"(deadline|apply by|applications due)[:\s]+([A-Za-z]+ \d{1,2},? \d{4})", text, re.IGNORECASE)
            email_match = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
            
            return {
                "city": target["city"],
                "county": target["county"],
                "has_call_for_bands": bool(re.search(r"performer|band submission|call for artists|entertainment application", text, re.IGNORECASE)),
                "deadline": deadline_match.group(0) if deadline_match else "Check portal",
                "contacts": list(set(email_match))[:3],
                "status": "qualified"
            }
    except Exception as e:
        return {"city": target["city"], "error": str(e)}
```

### Prototype B: Automated Pitch Draft Generator (`scripts/scout_agent_tool.py --draft-pitch`)
```python
def generate_pitch_draft(lead: dict) -> str:
    """Generate personalized outreach pitch for Mike's review."""
    return f"""Subject: Live Music Booking Inquiry: Neon Blonde at {lead['venue_name']}

Hi {lead.get('booking_contact_name') or 'Booking Team'},

Hope you're having a great week!

I'm reaching out on behalf of Neon Blonde, a high-energy 6-piece retro, 80s dance, and rock party band based in Southern California. 

We love the live music energy at {lead['venue_name']}—especially seeing great crowds for acts like {lead.get('similar_bands_seen') or 'top local party bands'}. Neon Blonde brings that exact high-octane dance floor experience with full dynamic sound, female & male dual lead vocals, and a polished retro setlist (covering Prince, Madonna, Duran Duran, The Cure, Journey, and 80s dance classics).

You can check out our live video promo reel and EPK here:
👉 [Neon Blonde Promo Video & EPK Link]

We are currently booking our spring/summer dates across the coastal circuit and would love to discuss open dates for {lead['venue_name']}.

Are you currently booking upcoming weekend dates for {lead.get('city', 'your area')}?

Best regards,

Mike Miller
Neon Blonde
(805) XXX-XXXX | booking@neonblondeband.com
"""
```

---

## 7. Antigravity Sign-Off

Brainstorm completed and architectural blueprints drafted.  
Signed,  
**Antigravity Agent**  
*Deepmind Agentic Coding Team*  
*Timestamp: 2026-09-03T20:53:00-07:00*

---

# Part 2: Handoff & Prompt for Codex

> [!IMPORTANT]
> **Prompt for Codex**:
> 
> *"Hello Codex! Antigravity has established the initial operational foundation for `Neon_Gig_Agent_v1` across the San Francisco to San Diego reach, and completed Part 1 of this Brainstorming Session covering unorthodox venue discovery, social media scraping architectures, peer band radar tracking, contact waterflow enrichment, and penetration strategies.*
> 
> *Now it's your turn in **Part 2** to build upon this doc. Please:*
> 1. *Review Antigravity's blueprints and add your deep engineering and systems perspective.*
> 2. *Propose concrete technical implementations or enhancements for the scrapers, data models, or API integrations (e.g. headless scraping resilience, proxy rotation, Instagram rate-limit bypass strategies, schema migrations, or database backing).*
> 3. *Brainstorm additional creative venue discovery channels or algorithms (e.g., Spotify local playlist mining, craft brewery network crawlers, private golf/yacht club directories).*
> 4. *Design a specific feature or CLI expansion for `scripts/scout_agent_tool.py` and provide code prototypes.*
> 5. *Sign off as **Codex** and write a prompt for the next agent (**Claude**)."*

---

# Part 3: Codex Brainstorm (Pending)
*(To be populated by Codex in the next session)*

---

# Part 4: Claude Brainstorm (Pending)
*(To be populated by Claude in the subsequent session)*
