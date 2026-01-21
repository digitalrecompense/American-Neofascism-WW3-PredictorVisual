# Components


## A. Domestic Authoritarian Escalation (DAE)

| Metric / Indicator                        | Weight | Score (0–1) | Weighted |
| ----------------------------------------- | ------ | ----------- | -------- |
| Pretext Expansion (DOJ/White House memos) | 0.15   | 0.9         | 0.135    |
| ICE & Detention Capacity                  | 0.20   | 0.85        | 0.170    |
| Military Deployments                      | 0.20   | 0.75        | 0.150    |
| Political Actor Protection (pardons)      | 0.10   | 0.95        | 0.095    |
| FBI / DOJ Capture                         | 0.15   | 0.8         | 0.120    |
| Legal / Political Pushback                | −0.05  | 0.5         | −0.025   |
| Missing Lethal Authorization              | −0.10  | 0           | 0        |

DAE Weighted Sum:
0.135 + 0.170 + 0.150 + 0.095 + 0.120 − 0.025 = 0.645

Scale note: DAE ∈ [−0.1, 0.77] given weights; can be normalized to 0–1 for easier interpretation if desired.


## B. International Conflict / WW3 Risk (ICR)

| Metric / Indicator              | Weight | Score (0–1) | Weighted |
| ------------------------------- | ------ | ----------- | -------- |
| Direct Threats to Allies        | 0.25   | 0.95        | 0.2375   |
| Military Signaling              | 0.20   | 0.7         | 0.140    |
| International Condemnation      | 0.10   | 0.85        | 0.085    |
| Historical Escalation Behavior  | 0.20   | 0.9         | 0.180    |
| Escalation Feedback Loops       | 0.15   | 0.65        | 0.0975   |
| Diplomatic Restraint            | −0.10  | 0.2         | −0.020   |
| Nuclear / Strategic Weapons Use | −0.10  | 0           | 0        |

ICR Weighted Sum:
0.2375 + 0.140 + 0.085 + 0.180 + 0.0975 − 0.020 = 0.720


## C. Coupled Risk Adjustment (ICR_adj)

To account for domestic authoritarian influence:

DEM (Domestic Escalation Multiplier) = DAE × 0.15 = 0.645 × 0.15 = 0.09675

Adjusted risk: ICR_adj = ICR + DEM = 0.720 + 0.09675 ≈ 0.817

Interpretation: On a 0–1 normalized scale, ICR_adj ≈ 0.82, high but not a literal probability of WW3. It represents elevated risk given current trends.


## D. Visualization / Heat Map Concept

X-axis: DAE (0–1)

Y-axis: ICR_adj (0–1)

Zones:

Green: Low risk
Yellow: Medium / Watch
Red: High risk (DAE > 0.6 & ICR_adj > 0.7)
Current Position:

DAE = 0.645

ICR_adj = 0.817
→ Falls in Red / Extreme Alert Zone.

| Event                                    | DAE Modifier | ICR Modifier | Result                       |
| ---------------------------------------- | ------------ | ------------ | ---------------------------- |
| New EO authorizing domestic lethal force | +0.15        | +0.05        | DAE → 0.795, ICR_adj → 0.867 |
| Confirmed nuclear alert                  | 0            | +0.10        | ICR_adj → 0.917              |
| New ICE political-target detainee        | +0.05        | 0            | DAE → 0.695                  |
| Major international retaliation          | 0            | +0.10        | ICR_adj → 0.917              |

All updates additive; scale remains 0–1.

<br>

<br>

✅ Key corrections made:

###### -All weighted sums recalculated accurately.
###### DEM added correctly.
###### Explicit notes that 0–1 scale ≠ literal probability.
###### Event-driven updates corrected.
###### DAE/ICR now internally consistent.
