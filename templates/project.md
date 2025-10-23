---
title: "{{ title }}"
date: "{{ date }}"
category: "{{ category|default('work') }}"
tags: {{ tags|default(['project']) }}
status: "{{ status|default('planning') }}"
start_date: "{{ start_date|default('') }}"
end_date: "{{ end_date|default('') }}"
priority: "{{ priority|default('medium') }}"
owner: "{{ owner|default('') }}"
---

# {{ title }}

## Project Overview

**Status:** {{ status|default('Planning') }} | **Priority:** {{ priority|default('Medium') }} | **Owner:** {{ owner|default('TBD') }}

**Start Date:** {{ start_date|default('YYYY-MM-DD') }}  
**Target End Date:** {{ end_date|default('YYYY-MM-DD') }}

### Description

<!-- Provide a high-level description of the project -->



### Objectives

**Primary Goals:**
1. 
2. 
3. 

**Success Metrics:**
- 
- 
- 

---

## Stakeholders

| Role | Name | Responsibility | Contact |
|------|------|----------------|---------|
| Project Owner | {{ owner|default('') }} | Overall accountability |  |
| Team Lead |  | Technical leadership |  |
| Developer |  | Implementation |  |
| Designer |  | UI/UX design |  |
| Stakeholder |  | Approval & feedback |  |

---

## Timeline

| Milestone | Target Date | Status | Notes |
|-----------|-------------|--------|-------|
| Project Kickoff | {{ start_date|default('YYYY-MM-DD') }} | - [ ] |  |
| Requirements Complete |  | - [ ] |  |
| Design Phase Complete |  | - [ ] |  |
| Development Sprint 1 |  | - [ ] |  |
| Testing & QA |  | - [ ] |  |
| Launch | {{ end_date|default('YYYY-MM-DD') }} | - [ ] |  |
| Post-Launch Review |  | - [ ] |  |

---

## Scope

### In Scope

**Included Features:**
- 
- 
- 

**Deliverables:**
- 
- 
- 

### Out of Scope

**Explicitly Excluded:**
- 
- 
- 

**Future Considerations:**
- 
- 

---

## Tasks

### Planning Phase
- [ ] Define project requirements
- [ ] Identify stakeholders
- [ ] Create project timeline
- [ ] Secure resources and budget

### Design Phase
- [ ] Create wireframes/mockups
- [ ] Review and approve designs
- [ ] Define technical architecture

### Development Phase
- [ ] Set up development environment
- [ ] Implement core features
- [ ] Code review and testing
- [ ] Documentation

### Testing Phase
- [ ] Unit testing
- [ ] Integration testing
- [ ] User acceptance testing (UAT)
- [ ] Bug fixes

### Launch Phase
- [ ] Deploy to production
- [ ] Monitor performance
- [ ] User training/documentation
- [ ] Post-launch support

---

## Resources

**Documentation:**
- [[project-requirements]] - Detailed requirements
- [[technical-spec]] - Technical specifications
- [[design-mockups]] - Design files

**External Links:**
- [Repository](https://github.com/org/repo)
- [Project Board](https://example.com/board)
- [Design Files](https://example.com/designs)

**Tools & Technologies:**
- 
- 
- 

---

## Progress Updates

<!-- Add newest updates at the top -->

### {{ date|default('YYYY-MM-DD') }} - Initial Planning

- Created project documentation
- Defined initial scope and objectives
- Next steps: [describe]

### YYYY-MM-DD - Update Title

**Completed:**
- 
- 

**In Progress:**
- 
- 

**Blockers:**
- 
- 

**Next Steps:**
- 
- 

---

## Risks & Issues

| Risk/Issue | Severity | Impact | Mitigation Strategy | Status |
|------------|----------|--------|---------------------|--------|
| Example: Timeline too aggressive | High | Delayed launch | Add buffer time, prioritize features | - [ ] Resolved |
|  |  |  |  | - [ ] Resolved |
|  |  |  |  | - [ ] Resolved |

**Active Blockers:**
- 
- 

---

## Success Criteria

**Project will be considered successful when:**

1. ✅ 
2. ✅ 
3. ✅ 
4. ✅ 

**Key Performance Indicators (KPIs):**
- Metric 1: Target value
- Metric 2: Target value
- Metric 3: Target value

---

## Related Projects

- [[parent-project]] - Parent initiative
- [[related-project-1]] - Similar project
- [[meeting-notes-kickoff]] - Kickoff meeting notes
- [[team-overview]] - Team information
- [[quarterly-goals]] - Strategic alignment

---

## Notes

**Lessons Learned:**
- 
- 

**Ideas for Improvement:**
- 
- 

**Retrospective Items:**
- 
- 
