import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Event timeline (month/year), corrected scores, and metric type
events = [
    ('January 2025', 0.6, 'DAE', 'EO on Birthright Citizenship'),
    ('January 2025', 0.65, 'DAE', 'Jan 6 Pardons'),
    ('June 2025', 0.7, 'DAE', 'National Guard + Marines LA deployment'),
    ('September 2025', 0.72, 'DAE', 'Countering Domestic Terrorism memo'),
    ('October 2025', 0.75, 'DAE', 'Alligator Alcatraz operational'),
    ('January 2026', 0.645, 'DAE', 'DAE Current'),  # corrected
    ('January 2026', 0.720, 'ICR', 'ICR Current'),  # corrected
    ('January 2026', 0.817, 'ICR', 'WW3 Risk Adj')  # corrected
]

# Convert dates to datetime objects
dates = [datetime.strptime(e[0], '%B %Y') for e in events]
DAE_scores = [e[1] if e[2] == 'DAE' else None for e in events]
ICR_scores = [e[1] if e[2] == 'ICR' else None for e in events]

# Plot
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(dates, DAE_scores, marker='o', label='Domestic Authoritarian Escalation (DAE)', color='red')
ax.plot(dates, ICR_scores, marker='x', linestyle='--', label='International Conflict / WW3 Risk (ICR_adj)', color='blue')

# Tipping point line
ax.axhline(y=0.9, color='black', linestyle=':', label='Critical WW3 Threshold')

# Annotate events
for i, event in enumerate(events):
    ax.annotate(event[3], (dates[i], event[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Format
ax.set_title('Neofascism & WW3 Risk Timeline (Corrected)')
ax.set_xlabel('Date')
ax.set_ylabel('Risk Score (0-1)')
ax.set_ylim(0,1.05)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
ax.legend()
plt.tight_layout()
plt.show()
