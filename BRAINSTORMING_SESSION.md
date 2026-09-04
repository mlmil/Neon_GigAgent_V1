# Neon_Gig_Agent_v1 — Brainstorming Session

**Date**: 2026-09-03  
**Bot / Agent**: `Neon_Gig_Agent_v1` (Scout Agent Lane for Neon Blonde)  
**Corridor Reach**: San Francisco to San Diego  

---

## 1. Session Objective & Strategic Vision

Explore features, automation architectures, research workflows, and integration points to evolve `Neon_Gig_Agent_v1` from a structured lead manager into an intelligent, semi-autonomous scouting powerhouse that keeps the Neon Blonde booking pipeline full.

---

## 2. Core Brainstorming Themes

### A. Automated Public Lead Discovery & Signal Ingestion
- **Venue Calendar Scrapers**:
  - Headless browser / Crawl4AI workflows targeting municipal Parks & Rec event pages, downtown business association calendars, and harbor event boards.
  - Automated detection of annual summer concert series application deadlines (typically Jan–March).
- **Similar-Band Intelligence ("Band Watch")**:
  - Track public touring schedules of similar California retro/party bands (e.g., *The Spazmatics*, *Fast Times*, *The Molly Ringwald Project*, *Twisted Gypsy*, *Area 51*).
  - Reverse-lookup new venues whenever a peer band posts a gig date.
- **Social Media Radar**:
  - Monitor public Instagram & Facebook event tags in target cities (`#MalibuLiveMusic`, `#VenturaMusic`, `#SantaBarbaraLive`, `#SanDiegoBands`).

---

### B. Route Optimization & Weekend "Mini-Run" Clustering
- **Distance & Travel Feasibility Engine**:
  - Automatic grouping of leads into viable 2-night or 3-night weekend runs:
    - *Northern Run*: San Francisco / Marin / Napa (Friday) + Santa Cruz / Monterey (Saturday).
    - *Central Coast Run*: San Luis Obispo (Friday) + Paso Robles / Pismo Beach (Saturday).
    - *Core Coastal Circuit*: Santa Barbara (Friday) + Malibu / Calabasas / Ventura (Saturday).
    - *South Coast Run*: Orange County (Friday) + San Diego / Solana Beach (Saturday).
- **Driving & Lodging Logic**:
  - Score multipliers for dates that can be chained together to minimize travel overhead for the 6-piece band.

---

### C. Smart Pitch & Outreach Drafting Engine
- **Context-Aware Email Drafts**:
  - Automatically draft tailored outreach emails for Mike / Alfred review based on:
    - Venue vibe and room size.
    - Specific similar bands that have played there.
    - Tailored YouTube live demo links and EPK materials.
    - Relevant open dates from the band's availability calendar.
- **Follow-up Cadence Automation**:
  - Reminder triggers when a contacted venue has not replied within 14 days.

---

### D. Deep Integration with Neon V2 Ecosystem
- **Telegram Bot Notifications (`NeonBotstein`)**:
  - Send instant alerts to Mike via Telegram when a high-score lead (Score >= 85) is discovered or application deadlines are approaching.
- **Seamless Graduation to Booking Pipeline & Venue Agent**:
  - 1-click command to graduate a `ready_to_contact` lead to the active booking negotiation queue.
  - Automatic creation of venue profile folders upon Mike's confirmation.

---

## 3. Prioritized Ideas Matrix

| Idea / Capability | Impact | Complexity | Priority |
|---|---|---|---|
| **Peer Band Calendar Monitoring** (Track 5–10 key tribute bands) | 🔥 High | 🟡 Medium | **Phase 1** |
| **Municipal Concerts in the Park Tracker** (Application deadlines) | 🔥 High | 🟢 Low | **Phase 1** |
| **Smart Pitch Generator CLI** (`--draft-pitch <lead_id>`) | 🟢 High | 🟢 Low | **Phase 1** |
| **Telegram Lead Alerts** (Scout report summaries via bot) | 🟡 Medium | 🟡 Medium | **Phase 2** |
| **Automated Web Calendar Scraping** (Crawl4ai / Playwright) | 🔥 High | 🔴 High | **Phase 2** |
| **Weekend Mini-Run Tour Planner** (SF to SD route chaining) | 🟡 Medium | 🟡 Medium | **Phase 3** |

---

## 4. Open Discussion Topics for Mike

1. **Top Target Lead Types**:
   - Should we prioritize municipal summer series / festivals (higher budget, early booking) over private clubs and weekend bars for the next scouting batch?
2. **Key Peer Bands to Monitor**:
   - Which specific bands provide the best signal that a room is ready for Neon Blonde?
3. **Outreach Channels**:
   - Do you prefer pitching via email, Instagram DM, or web contact forms for independent bar/saloon managers?

---

## 5. Next Steps & Experiments

- [ ] Add 10 additional venue leads in San Diego, Orange County, and Bay Area.
- [ ] Implement `scripts/scout_agent_tool.py --draft-pitch <lead_id>` to test automated outreach copy generation.
- [ ] Compile a "Peer Band Watchlist" of 10 local/regional acts to monitor.
