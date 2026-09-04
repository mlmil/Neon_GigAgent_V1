# Neon_GigAgent_V1

`Neon_Gig_Agent_v1` is the dedicated venue prospecting and lead discovery agent for **Neon Blonde** (a 6-piece energetic retro, dance, and rock party band).

## Overview

Scout Agent identifies, qualifies, scores, and tracks potential live music venues, private clubs, festival stages, and municipal concert series before they enter the booking pipeline.

### Target Regions (Reach: San Francisco to San Diego)
- **Priority 1**: Ventura County, Santa Barbara County, Malibu & Calabasas (High venue density & core circuit)
- **Priority 2**: San Fernando Valley, Greater Los Angeles, Orange County
- **Priority 3**: San Diego County, Central Coast, San Francisco & Bay Area (Destination & tour runs)

---

## Directory Structure

```text
Neon_GigAgent_V1/
├── SCOUT_AGENT.md                 # Operating Handbook & Rules
├── SCOUT_AGENT_HANDOFF.md         # Context & Agent Handoff
├── scout-leads.csv                # Primary Leads Database
├── do-not-contact.csv             # Excluded / Blacklisted Venues
├── schemas/
│   └── scout_leads_schema.json    # JSON Schema definition
├── scripts/
│   └── scout_agent_tool.py        # CLI validator, scorer, and report generator
├── regions/                       # Regional dossiers & notes
│   ├── malibu-calabasas.md        # Priority 1
│   ├── ventura-county.md          # Priority 1
│   ├── santa-barbara-county.md    # Priority 1
│   ├── la-valley.md               # Priority 2
│   └── central-coast.md           # Priority 3
├── reports/                       # Weekly generated Scout reports
├── tests/                         # Unit tests
└── ai/                            # Worklog system & project context
```

---

## Quick Start & Commands

```bash
# 1. Validate leads database
python3 scripts/scout_agent_tool.py scout-leads.csv

# 2. Print summary breakdown
python3 scripts/scout_agent_tool.py --summary scout-leads.csv

# 3. Generate weekly Scout markdown report
python3 scripts/scout_agent_tool.py --report scout-leads.csv

# 4. Run test suite
python3 -m unittest discover -s tests -p 'test_*.py'
```

---

## Safety & Boundaries

- **Scout scope**: Prospecting and intelligence only.
- **Protected actions**: Outreach sends, booking confirmations, rate negotiations, and calendar updates require band leadership (Mike Miller) approval.
