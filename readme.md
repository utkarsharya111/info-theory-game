1. Setting Up the Production Space
Production State Space: Let 
Ω
Ω be the set of all possible ways of producing a good (or set of goods). Each 
𝜔
∈
Ω
ω∈Ω corresponds to a specific “strategy” or “method” (e.g., combination of technologies, inputs, and processes).

Probability Distribution: At time 
𝑡
t, our knowledge about the best production methods is summarized by a distribution

𝑝
(
𝜔
;
𝑡
)
for
  
𝜔
∈
Ω
.
p(ω;t)forω∈Ω.
If 
𝑝
(
𝜔
;
𝑡
)
p(ω;t) is broad and flat, it means we’re very uncertain about which method is best.
If 
𝑝
(
𝜔
;
𝑡
)
p(ω;t) is peaked around a few states, we’ve identified (and are applying) the most efficient methods with high probability.
Shannon Entropy: The entropy of this distribution is

𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
  
=
  
−
∑
𝜔
∈
Ω
 
𝑝
(
𝜔
;
𝑡
)
 
ln
⁡
 
𝑝
(
𝜔
;
𝑡
)
.
H(p(ω;t))=− 
ω∈Ω
∑
​
 p(ω;t)lnp(ω;t).
A higher 
𝐻
H indicates more uncertainty (less knowledge).
A lower 
𝐻
H indicates more certainty (more knowledge about which methods truly work best).
2. Defining the Knowledge Stock 
𝐾
(
𝑡
)
K(t)
We want to translate “reduced entropy” into “increased knowledge.” One common approach:

Maximum Entropy, 
𝐻
m
a
x
H 
max
​
 : Assume there’s a baseline or “ignorant” distribution (maybe uniform if 
Ω
Ω is finite). That maximum entropy is 
𝐻
m
a
x
H 
max
​
 .

Knowledge Stock: Define

𝐾
(
𝑡
)
  
=
  
𝐻
m
a
x
  
−
  
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
.
K(t)=H 
max
​
 −H(p(ω;t)).
If 
𝑝
(
𝜔
;
𝑡
)
p(ω;t) is still spread out, 
𝐻
H is large, so 
𝐾
(
𝑡
)
K(t) is small.
If 
𝑝
(
𝜔
;
𝑡
)
p(ω;t) collapses around the best states, 
𝐻
H is small, so 
𝐾
(
𝑡
)
K(t) is large.
Essentially, 
𝐾
(
𝑡
)
K(t) measures how much uncertainty we’ve eliminated about production methods.

3. Linking Knowledge to TFP
In standard macroeconomics, we often have a production function:

𝑌
(
𝑡
)
  
=
  
𝐴
(
𝑡
)
 
𝐹
(
𝐾
(
𝑡
)
,
𝐿
(
𝑡
)
)
,
Y(t)=A(t)F(K(t),L(t)),
where

𝑌
Y is output,
𝐾
K is physical capital,
𝐿
L is labor,
𝐴
(
𝑡
)
A(t) is total factor productivity (TFP).
3.1 TFP as an Exponential of Knowledge
We let TFP be an exponential function of the knowledge stock:

𝐴
(
𝑡
)
  
=
  
exp
⁡
 ⁣
(
𝛼
 
𝐾
(
𝑡
)
)
,
A(t)=exp(αK(t)),
where 
𝛼
>
0
α>0 is a constant scale factor. Substituting 
𝐾
(
𝑡
)
=
𝐻
m
a
x
−
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
K(t)=H 
max
​
 −H(p(ω;t)):

𝐴
(
𝑡
)
=
exp
⁡
 ⁣
(
𝛼
 
[
 
𝐻
m
a
x
−
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
]
)
=
exp
⁡
(
𝛼
 
𝐻
m
a
x
)
  
×
  
exp
⁡
 ⁣
(
−
 
𝛼
 
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
)
.
A(t)=exp(α[H 
max
​
 −H(p(ω;t))])=exp(αH 
max
​
 )×exp(−αH(p(ω;t))).
If entropy 
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
H(p(ω;t)) drops, TFP rises exponentially.
If we know exactly which 
𝜔
ω is optimal (i.e., 
𝐻
=
0
H=0), then 
𝐾
(
𝑡
)
=
𝐻
m
a
x
K(t)=H 
max
​
 , so TFP is at its highest possible level (given 
𝛼
α).
Interpretation
exp
⁡
(
𝛼
 
𝐾
(
𝑡
)
)
exp(αK(t)) means each additional “unit” of knowledge can multiply your effective productivity.
As you become more certain about the best production methods (entropy goes down), your productivity soars.
4. Time Prices and Wages
Now, time prices measure how many hours of work it costs to buy a good 
𝑔
g. Formally:

𝜋
𝑔
(
𝑡
)
  
=
  
𝑃
𝑔
(
𝑡
)
𝑤
(
𝑡
)
,
π 
g
​
 (t)= 
w(t)
P 
g
​
 (t)
​
 ,
where 
𝑃
𝑔
(
𝑡
)
P 
g
​
 (t) is the nominal money price of good 
𝑔
g, and 
𝑤
(
𝑡
)
w(t) is the nominal wage (income per hour).

Wage typically relates to marginal product of labor (MPL) in a competitive market. For the Cobb–Douglas style function, we can show:

𝑤
𝑟
(
𝑡
)
=
∂
𝑌
(
𝑡
)
∂
𝐿
(
𝑡
)
  
=
  
(
1
−
𝛽
)
 
exp
⁡
 ⁣
(
𝛼
 
𝐾
(
𝑡
)
)
 
𝐾
(
𝑡
)
𝛽
𝐿
(
𝑡
)
𝛽
.
w 
r
​
 (t)= 
∂L(t)
∂Y(t)
​
 =(1−β)exp(αK(t)) 
L(t) 
β
 
K(t) 
β
 
​
 .
That’s the real wage (in units of output). The nominal wage just multiplies by some price index.

As 
𝐾
(
𝑡
)
K(t) increases (entropy drops), the real wage grows—leading to a lower 
𝜋
𝑔
(
𝑡
)
π 
g
​
 (t) if nominal prices don’t rise as fast as wages.

In simpler algebraic terms, if 
𝜋
𝑔
(
𝑡
)
∝
exp
⁡
(
−
 
𝛿
 
𝐾
(
𝑡
)
)
π 
g
​
 (t)∝exp(−δK(t)), that means each increase in knowledge shrinks the time price exponentially.

5. Knowledge Accumulation via Entropy Reduction
5.1 Growth of 
𝐾
(
𝑡
)
K(t)
We might posit a simple dynamic:

𝑑
𝐾
(
𝑡
)
𝑑
𝑡
  
=
  
𝛾
 
𝑁
(
𝑡
)
 
[
𝐾
(
𝑡
)
]
𝜃
,
dt
dK(t)
​
 =γN(t)[K(t)] 
θ
 ,
where:

𝑁
(
𝑡
)
N(t) is the population (or number of innovators),
𝜃
θ is an exponent for knowledge spillovers,
𝛾
>
0
γ>0 is a base innovation rate.
As knowledge grows, we discover more about which 
𝜔
ω yields high output, so 
𝑝
(
𝜔
;
𝑡
)
p(ω;t) “collapses” around that method, lowering entropy.

5.2 Entropy to Knowledge Relation
Recall:

𝐾
(
𝑡
)
=
𝐻
m
a
x
−
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
.
K(t)=H 
max
​
 −H(p(ω;t)).
If we interpret discovering new knowledge as reducing 
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
H(p(ω;t)), then each “successful innovation” is akin to mutual information gained about the best state 
𝜔
ω. That’s the direct link between an information-theoretic concept (entropy) and an economic concept (knowledge stock).

6. Putting It All Together
Entropy High → 
𝐾
(
𝑡
)
K(t) Low → TFP 
𝐴
(
𝑡
)
A(t) Low → Lower wages, higher time prices.
Entropy Falls → 
𝐾
(
𝑡
)
K(t) Rises → TFP 
𝐴
(
𝑡
)
A(t) Rises → Higher wages, lower time prices.
In diagrammatic form:

Lower 
𝐻
H (less uncertainty)
↓
↓
Higher 
𝐾
(
𝑡
)
K(t) (bigger knowledge stock)
↓
↓
Higher 
𝐴
(
𝑡
)
A(t) (TFP)
↓
↓
Higher real wages / productivity
↓
↓
Lower 
𝜋
𝑔
(
𝑡
)
π 
g
​
 (t) (time price)
↓
↓
Freed resources → further R&D → even lower entropy.
This feedback loop can drive a “superabundance” scenario where each new insight multiplies the effect of previous insights. Population growth can accelerate this if more individuals contribute to knowledge discovery.

7. Example: A Minimal System of Equations
For completeness, let’s write a short system:

Knowledge Stock vs. Entropy

𝐾
(
𝑡
)
=
𝐻
m
a
x
−
𝐻
(
𝑝
(
𝜔
;
𝑡
)
)
.
K(t)=H 
max
​
 −H(p(ω;t)).
TFP from Knowledge

𝐴
(
𝑡
)
=
exp
⁡
 ⁣
(
𝛼
 
𝐾
(
𝑡
)
)
.
A(t)=exp(αK(t)).
Production Function

𝑌
(
𝑡
)
=
𝐴
(
𝑡
)
 
𝐾
(
𝑡
)
𝛽
 
𝐿
(
𝑡
)
1
−
𝛽
.
Y(t)=A(t)K(t) 
β
 L(t) 
1−β
 .
Wage 
(
assuming competition
)
(assuming competition)

𝑤
𝑟
(
𝑡
)
=
(
1
−
𝛽
)
 
exp
⁡
 ⁣
(
𝛼
 
𝐾
(
𝑡
)
)
 
𝐾
(
𝑡
)
𝛽
𝐿
(
𝑡
)
𝛽
.
w 
r
​
 (t)=(1−β)exp(αK(t)) 
L(t) 
β
 
K(t) 
β
 
​
 .
Time Price of Good 
𝑔
g

𝜋
𝑔
(
𝑡
)
=
𝑃
𝑔
(
𝑡
)
𝑤
(
𝑡
)
  
∝
  
exp
⁡
(
−
 
𝛿
 
𝐾
(
𝑡
)
)
,
π 
g
​
 (t)= 
w(t)
P 
g
​
 (t)
​
 ∝exp(−δK(t)),
for some constant 
𝛿
>
0
δ>0.

Knowledge Growth

𝑑
𝐾
(
𝑡
)
𝑑
𝑡
=
𝛾
 
𝑁
(
𝑡
)
 
[
𝐾
(
𝑡
)
]
𝜃
.
dt
dK(t)
​
 =γN(t)[K(t)] 
θ
 .
One could then show how 
𝐾
(
𝑡
)
K(t) evolves from near zero (high entropy) to a large value (low entropy), pushing time prices ever downward.

8. Summary
Entropy captures uncertainty about which production methods are optimal.
Knowledge 
𝐾
(
𝑡
)
K(t) is basically how much of that uncertainty is eliminated.
TFP 
𝐴
(
𝑡
)
A(t) rises as knowledge accumulates (entropy falls).
Higher TFP translates into cheaper goods in labor-time units—i.e., time prices fall.
A simple model with 
𝐾
(
𝑡
)
=
𝐻
m
a
x
−
𝐻
(
𝑝
)
K(t)=H 
max
​
 −H(p) plus an exponential TFP function merges Shannon Entropy with economic growth mechanics.