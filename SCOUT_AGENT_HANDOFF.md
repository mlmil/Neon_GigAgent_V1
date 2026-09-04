# Neon_Gig_Agent_v1 Handoff

Date: 2026-09-03

## Mission

`Neon_Gig_Agent_v1` (Scout Agent) finds possible new Neon Blonde venues before they become confirmed bookings.

This is a prospecting lane only. It does not own confirmed gigs, payouts, venue folders for active gigs, Band Sheet publishing, calendar updates, or venue-facing email sends.

## Current Folder

```text
/Volumes/VADER/Manifold/Neon_Blonde/Scout Agent/
```

Current files:

```text
SCOUT_AGENT.md
SCOUT_AGENT_HANDOFF.md
scout-leads.csv
do-not-contact.csv
regions/
  ventura-county.md
  santa-barbara-county.md
  la-valley.md
  central-coast.md
```

## Repo Context

Neon V2 repo:

```text
/Volumes/VADER/Manifold/Neon_Blonde/Repos/Neon_v2
```

Useful repo files:

```text
references/agent-ecosystem.md
references/automation-map.md
docs/superpowers/specs/2026-06-08-neon-v2-brainstorm-todo.md
scripts/scout_agent_tool.py
schemas/scout_leads_schema.json
```

Validate the Scout lead CSV with:

```bash
cd /Volumes/VADER/Manifold/Neon_Blonde/Repos/Neon_v2
python3 scripts/scout_agent_tool.py "/Volumes/VADER/Manifold/Neon_Blonde/Scout Agent/scout-leads.csv"
```

## Boundaries

Allowed:

- Research public venue calendars.
- Research public venue social posts.
- Research public event listings.
- Research public schedules for similar local bands.
- Find public booking contact pages or public booking emails.
- Add/update rows in `scout-leads.csv`.
- Add notes to regional research files.
- Produce weekly Scout reports.

Not allowed without Mike approval:

- Send outreach.
- Update Google Calendar.
- Publish or edit the Band Sheet.
- Update WordPress.
- Create active gig folders in `/Volumes/VADER/Manifold/Neon_Blonde/Venues`.
- Mark a venue as booked.
- Share files with venues.
- Add private phone numbers or private contact info.

Hard rule:

```text
Scout lead = prospect only.
Confirmed gig = calendar event exists or Mike explicitly confirms it.
```

## Target Regions (Reach: San Francisco to San Diego)

Priority 1 (Core Home Circuit & High Venue Density):

- Ventura County
- Santa Barbara County
- Malibu & Calabasas

Priority 2 (Secondary & Connecting Corridors):

- San Fernando Valley
- LA County / Los Angeles
- Orange County

Priority 3 (Destination / Extended Reach Corridors):

- San Diego County (South Anchor)
- Central Coast / SLO / Paso Robles (Mid-Coast)
- San Francisco & Bay Area (North Anchor)

## Source Rules

Use public sources only:

- Venue websites
- Venue event calendars
- Public venue Instagram/Facebook posts
- Public local event calendars
- Public band websites
- Public booking/contact pages
- Parks & Recreation department websites (Concerts in the Park)
- Chamber of Commerce / Downtown Association event listings
- Festival vendor/entertainment application pages
- Community/Fraternal organization calendars (Elks, Moose, VFW)
- Yacht/Country club public event pages

Do not use:

- Private groups
- Login-only pages
- Paywalled sources
- Scraping that bypasses access controls
- Personal/private contact lists unless Mike explicitly provides them for Scout use

## Lead CSV Schema

Main lead file:

```text
/Volumes/VADER/Manifold/Neon_Blonde/Scout Agent/scout-leads.csv
```

Columns:

```text
lead_id
venue_name
city
county
region_priority
status
lead_score
gig_type
source_type
source_url
similar_bands_seen
booking_contact_name
booking_contact_email
booking_contact_phone
lead_owner
next_action
follow_up_date
last_checked
notes
```

Allowed gig types (for `gig_type` column):

```text
club
festival
municipal
private_club
```

Allowed statuses:

```text
discovered
researching
qualified
ready_to_contact
contacted
follow_up
warm
not_a_fit
booked
converted_to_venue_agent
```

Default lead owner:

```text
unassigned
```

Known booking leads:

- Mike Miller
- Alfred Morlaes

Curtis Clyde may occasionally lead a booking, but do not assign him unless Mike says so or the source clearly shows Curtis leading that contact.

## Lead Scoring

Use a simple 0-100 score.

Suggested scoring:

- +25 venue regularly books live bands
- +20 similar bands have played there
- +15 target region fit
- +15 clear public booking contact
- +10 music style fits Neon Blonde
- +10 likely room/pay supports a six-piece band
- +15 municipal, festival, or private club event (usually higher budget)
- +5 useful notes or warm connection found

Subtract:

- -20 no clear contact path
- -20 only DJs/acoustic/original-only programming
- -15 too far for normal routing
- -15 one-off event with no recurring music program
- -50 listed in `do-not-contact.csv`

Score bands:

```text
80-100 = high-priority lead
60-79 = qualified
40-59 = research more
0-39 = weak or not a fit
```

## Similar-Band Signal

Track bands that suggest a venue is a fit for Neon Blonde.

Examples of useful signals:

- Local cover bands
- 80s/new-wave/post-punk adjacent bands
- Danceable bar/event bands
- Bands playing Ventura/Santa Barbara/LA County venues with similar audience fit

Put those names in `similar_bands_seen`.

## Weekly Report Format

Create weekly reports in:

```text
/Volumes/VADER/Manifold/Neon_Blonde/Scout Agent/reports/
```

File name:

```text
YYYY-MM-DD-scout-report.md
```

Report sections:

```text
# Scout Agent Weekly Report

## Top 10 New Leads

## Best 3 To Contact First

## Similar Bands / Venue Signals

## Follow-Ups Due

## Dead Ends / Not A Fit

## Needs Mike Decision
```

## Graduation Rules

Scout -> Booking Pipeline:

- Lead is qualified or ready_to_contact.
- There is a clear public contact path.
- Mike or Alfred should review outreach.

Scout -> Venue Agent:

- Calendar event exists, or Mike explicitly confirms the venue/gig.
- Create or update the active venue workflow outside Scout.

Never move straight from Scout to confirmed booking without Mike approval.

## First Task For Next Agent

1. Validate `scout-leads.csv`.
2. Review region files for target areas.
3. Add 10 public-source venue leads from Ventura County and Santa Barbara County.
4. Include at least one source URL per lead.
5. Score each lead.
6. Mark the 3 best as `ready_to_contact`.
7. Write the first weekly report.

## Current Stop Point

Scout Agent folder exists and schema is defined.

No live scraping automation is installed yet.

No outreach automation is approved.

The next useful build is a Scout lead collection workflow that creates or updates `scout-leads.csv` from public research, then validates it with `scripts/scout_agent_tool.py`.
