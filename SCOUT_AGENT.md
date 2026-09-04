# Neon_Gig_Agent_v1 Operating Manual

## 1. Mission & Authority

**Neon_Gig_Agent_v1** (Scout Agent) discovers and qualifies potential venue leads for **Neon Blonde** (6-piece high-energy retro/dance/rock party band) before they become confirmed bookings.

`Neon_Gig_Agent_v1` is strictly a **prospecting and intelligence lane**.

### Allowed Actions
- Research public venue calendars, social media feeds, and websites.
- Research competitor and peer band schedules.
- Identify public booking contacts (names, emails, phones, forms).
- Record and update venue entries in `scout-leads.csv`.
- Score leads using the official 0–100 rubric.
- Generate weekly Scout reports.

### Protected Actions (Requires Mike Approval)
- Sending outreach emails or messages to venues.
- Confirming gigs or agreeing to rates/terms.
- Updating Google Calendar or Band Sheet.
- Creating active gig folders in production venue archives.

---

## 2. Directory Structure

```text
Neon_GigAgent/
├── SCOUT_AGENT.md                 # This operating handbook
├── SCOUT_AGENT_HANDOFF.md         # Handoff context & priorities
├── scout-leads.csv                # Primary leads database
├── do-not-contact.csv             # Excluded / blacklisted venues
├── schemas/
│   └── scout_leads_schema.json    # JSON schema for leads validation
├── scripts/
│   └── scout_agent_tool.py        # CLI validator, scorer, and report tool
├── regions/                       # Regional dossiers & venue notes
│   ├── malibu-calabasas.md        # Priority 1: High venue density
│   ├── ventura-county.md          # Priority 1: Home territory
│   ├── santa-barbara-county.md    # Priority 1: Premium coastal & wine country
│   ├── la-valley.md               # Priority 2: San Fernando Valley & LA
│   ├── orange-county.md           # Priority 2: Coastal & South OC
│   ├── san-diego.md               # Priority 3: South reach anchor
│   ├── central-coast.md           # Priority 3: Mid-coast overflow
│   └── san-francisco-bay-area.md  # Priority 3: North reach anchor
├── reports/                       # Weekly generated Scout reports
└── tests/
    └── test_scout_agent_tool.py   # Test suite
```

---

## 3. Geographic Reach & ID Conventions

`Neon_Gig_Agent_v1` covers the California coastal corridor from **San Francisco to San Diego**:

Lead IDs follow the format `{PREFIX}-{NNN}`:
- `MAL`: Malibu (Priority 1)
- `CAL`: Calabasas (Priority 1)
- `VC`: Ventura County (Priority 1)
- `SB`: Santa Barbara County (Priority 1)
- `SFV`: San Fernando Valley (Priority 2)
- `LA`: Greater Los Angeles (Priority 2)
- `OC`: Orange County (Priority 2)
- `SD`: San Diego County (Priority 3 - South Corridor)
- `CC`: Central Coast (Priority 3 - Mid-Coast)
- `SF`: San Francisco & Bay Area (Priority 3 - North Corridor)

---

## 4. Lead Scoring Rubric (0–100)

| Signal | Score Adjustment |
|---|---|
| Venue regularly books live bands | +25 |
| Similar bands have played there | +20 |
| Target region fit (Priority 1) | +15 |
| Clear public booking contact found | +15 |
| High-value gig type (municipal/festival/private) | +15 |
| Music style fit (80s, pop/rock, dance) | +10 |
| Physical stage/room supports 6-piece band | +10 |
| Warm connection or helpful insider notes | +5 |
| No clear contact path found | -20 |
| Wrong music programming (DJs only, acoustic only) | -20 |
| Venue too far for routine routing | -15 |
| One-off event with no recurring music program | -15 |
| Listed in `do-not-contact.csv` | -50 |

### Score Bands
- **80–100**: High Priority (Ready for outreach review)
- **60–79**: Qualified (Good candidate)
- **40–59**: Research More (Needs additional vetting)
- **0–39**: Weak / Not a fit

---

## 5. Tooling & Verification Commands

### Validate Leads CSV
```bash
python3 scripts/scout_agent_tool.py scout-leads.csv
```

### Check Summary Stats
```bash
python3 scripts/scout_agent_tool.py --summary scout-leads.csv
```

### Generate Weekly Markdown Report
```bash
python3 scripts/scout_agent_tool.py --report scout-leads.csv > reports/$(date +%Y-%m-%d)-scout-report.md
```

### Run Test Suite
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

---

## 6. Handoff to Booking Pipeline
When a lead is scored **>= 80** and has verified public contact info:
1. Mark status as `ready_to_contact`.
2. Document in the weekly report under `Best Leads To Contact First`.
3. Present to Mike for outreach draft approval and lead owner assignment (`Mike Miller` or `Alfred Morlaes`).
