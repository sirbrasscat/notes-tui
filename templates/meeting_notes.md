---
title: "{{ title }}"
date: "{{ date }}"
category: "{{ category|default('work') }}"
tags: {{ tags|default(['meeting']) }}
status: "{{ status|default('draft') }}"
meeting_type: "{{ meeting_type|default('general') }}"
attendees: "{{ attendees|default('') }}"
location: "{{ location|default('') }}"
---

# {{ title }}

## Meeting Details

| Field | Value |
|-------|-------|
| **Type** | {{ meeting_type|default('General Meeting') }} |
| **Date** | {{ date }} |
| **Location** | {{ location|default('TBD') }} |
| **Attendees** | {{ attendees|default('') }} |

---

## Agenda

1. Opening and introductions
2. Review of previous action items
3. Main discussion topics
4. Q&A
5. Next steps and closing

---

## Discussion Notes

### Topic 1: [Agenda Item]

<!-- Capture key points, decisions, and discussion details -->

**Key Points:**
- 
- 

**Discussion:**


### Topic 2: [Agenda Item]

**Key Points:**
- 
- 

**Discussion:**


---

## Action Items

| Task | Assignee | Due Date | Status |
|------|----------|----------|--------|
| <!-- Example: Review proposal --> | <!-- Name --> | <!-- YYYY-MM-DD --> | - [ ] |
|  |  |  | - [ ] |
|  |  |  | - [ ] |
|  |  |  | - [ ] |

---

## Decisions Made

- **Decision 1:** 
  - *Rationale:* 
  - *Impact:* 

- **Decision 2:** 
  - *Rationale:* 
  - *Impact:* 

---

## Next Steps

- [ ] Schedule follow-up meeting
- [ ] Distribute meeting notes to attendees
- [ ] 
- [ ] 

**Next Meeting:**
- Date: 
- Topics: 

---

## Related Notes

- [[project-name]] - Related project documentation
- [[meeting-{{ date_ymd|default('YYYY-MM-DD') }}]] - Previous meeting
- [[team-overview]] - Team information
- [[quarterly-goals]] - Strategic objectives
