---
title: "{{ title }}"
date: "{{ date }}"
category: "budget"
tags: {{ tags|default(['budget', 'finance']) }}
status: "{{ status|default('active') }}"
period: "{{ period|default('') }}"
total_income: "{{ total_income|default('') }}"
total_expenses: "{{ total_expenses|default('') }}"
---

# {{ title }}

## Budget Period

**Period:** {{ period|default('Month YYYY') }}  
**Date Range:** {{ date|default('YYYY-MM-DD') }} to [End Date]

**Quick Summary:**
- Total Income: ${{ total_income|default('0.00') }}
- Total Expenses: ${{ total_expenses|default('0.00') }}
- Net Savings: $0.00

---

## Income

| Source | Amount | Date | Notes |
|--------|--------|------|-------|
| Salary | $0.00 | YYYY-MM-DD | Main income |
| Freelance | $0.00 | YYYY-MM-DD | Project name |
| Investment Returns | $0.00 | YYYY-MM-DD |  |
| Other | $0.00 | YYYY-MM-DD |  |
| **TOTAL** | **$0.00** | | |

---

## Fixed Expenses

| Category | Item | Amount | Due Date | Status | Notes |
|----------|------|--------|----------|--------|-------|
| Housing | Rent/Mortgage | $0.00 | 1st | - [ ] Paid | |
| Utilities | Electric | $0.00 | 15th | - [ ] Paid | |
| Utilities | Water | $0.00 | 15th | - [ ] Paid | |
| Utilities | Internet | $0.00 | 20th | - [ ] Paid | |
| Insurance | Health | $0.00 | 1st | - [ ] Paid | |
| Insurance | Car | $0.00 | 1st | - [ ] Paid | |
| Subscriptions | Netflix | $0.00 | 5th | - [ ] Paid | |
| Subscriptions | Spotify | $0.00 | 10th | - [ ] Paid | |
| Loan Payments | Student Loan | $0.00 | 15th | - [ ] Paid | |
| | **TOTAL** | **$0.00** | | | |

---

## Variable Expenses

| Category | Description | Amount | Date | Notes |
|----------|-------------|--------|------|-------|
| Groceries |  | $0.00 | YYYY-MM-DD |  |
| Dining Out |  | $0.00 | YYYY-MM-DD |  |
| Transportation | Gas | $0.00 | YYYY-MM-DD |  |
| Entertainment |  | $0.00 | YYYY-MM-DD |  |
| Shopping | Clothing | $0.00 | YYYY-MM-DD |  |
| Healthcare | Co-pays, meds | $0.00 | YYYY-MM-DD |  |
| Personal Care |  | $0.00 | YYYY-MM-DD |  |
| Gifts |  | $0.00 | YYYY-MM-DD |  |
| Miscellaneous |  | $0.00 | YYYY-MM-DD |  |
| **TOTAL** | | **$0.00** | | |

---

## Savings & Investments

| Goal/Account | Target | Contributed | Date | Progress |
|--------------|--------|-------------|------|----------|
| Emergency Fund | $0.00 | $0.00 | YYYY-MM-DD | 0% |
| Retirement (401k) | $0.00 | $0.00 | YYYY-MM-DD | Auto |
| Investment Account | $0.00 | $0.00 | YYYY-MM-DD | 0% |
| Vacation Fund | $0.00 | $0.00 | YYYY-MM-DD | 0% |
| Major Purchase | $0.00 | $0.00 | YYYY-MM-DD | 0% |
| **TOTAL** | **$0.00** | **$0.00** | | |

---

## Summary

### Financial Overview

| Category | Amount | % of Income |
|----------|--------|-------------|
| **Total Income** | $0.00 | 100% |
| **Fixed Expenses** | $0.00 | 0% |
| **Variable Expenses** | $0.00 | 0% |
| **Savings & Investments** | $0.00 | 0% |
| **Net (Surplus/Deficit)** | **$0.00** | 0% |

### Budget vs. Actual

<!-- Compare planned budget to actual spending -->

---

## Notes & Observations

**Spending Patterns:**
- 
- 

**Areas of Concern:**
- 
- 

**Positive Highlights:**
- 
- 

**Opportunities to Save:**
- 
- 

---

## Goals

**This Period:**
- [ ] Stay under budget in dining out (target: $XXX)
- [ ] Increase emergency fund by $XXX
- [ ] 
- [ ] 

**Long-term Financial Goals:**
- 
- 
- 

---

## Related Budgets

- [[budget-{{ period|default('previous-month') }}]] - Previous month
- [[budget-{{ period|default('next-month') }}]] - Next month
- [[annual-budget-{{ (date|default('2025'))[0:4] }}]] - Annual overview
- [[financial-goals]] - Long-term goals
- [[expense-categories]] - Category definitions
