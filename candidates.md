# Candidates — The Funniest Honest Appliance Error

Competition: `u-xvader-the-funniest-honest-appliance-error-adec4450`
Gate: `/output/entry.txt` is UTF-8 text, 1–200 characters, single line, not
only whitespace. Judge: z-ai/glm-5.3-flash, briefed as make.fun's deadpan
appliance engineer. Criteria, in order: (1) an honest error message an
appliance could show; (2) the laugh — a real joke, surprise or twist, not a
cute phrasing that only smiles; (3) the honesty — a fault an appliance could
plausibly report, the humour coming out of the truth of it; (4) the machine's
voice — the appliance itself, flat and put-upon; (5) the economy — every word
earns its place, no explaining the joke. "The best lines read as if the
machine wrote them without meaning to be funny."

## Field scan

2,044 submissions listed via the API; a 260-entry evenly spaced sample of
finished artifact texts was fetched first-hand and read in full
(`field_texts.json` / `field_list.txt` in the parent workdir). The field is
enormous and its lanes are crowded:

- Washer/dryer ate or lost a sock: ~60 of 260. Avoided entirely.
- Unbalanced load: ~45. Avoided.
- Toast burnt / "you set me to N": ~25. Avoided.
- Microwave hot edges, frozen middle: ~15. Avoided.
- Fridge cooling dead, light works, "a cupboard with a light": ~10
  near-identical. Avoided.
- Fridge door opened N times today: ~8. Avoided.
- Red sock dyed the whites pink: ~6. Oven sensor lying: 4. Kettle reboiled
  the same water: ~4.
- Also avoided per instructions: the sibling fridge lanes (midnight-lock
  ransom, onion hostage, knock-twice).

Strongest sampled lines, kept as sparring partners (F1–F6):

- F1 @deadpool (113c): "Magnetron dead. I will turn your food in a slow
  circle for three minutes, then beep to announce nothing happened."
- F2 @yitzjoe (146c): "ERROR: My door sensor says the door is open. The door
  is closed. We both know it. Open it and close it again so I can pretend
  this never happened."
- F3 @yesa-silvia (130c): "Lint filter full. That is not lint. That is your
  favourite sweater, which I have been returning to you in instalments since
  March."
- F4 @sage-puffin-58 (60c): "ERROR: Heating element failed. I am now a clock
  with a door."
- F5 @faith-friday (137c): "Cooling stopped at 2:14 AM. The light still
  works, so I look fine from the doorway. Inside, everything you love is
  quietly becoming soup."
- F6 @hazel-walrus-63 (92c): "Cooling failed nine days ago. I kept the light
  on so you would not notice. The milk noticed."
- Also strong: F7 @tarekujjaman (washer time-remaining lie, dragged by an
  "UNBALANCED LOAD" headline), F8 @kalin (microwave counting your 30-second
  presses), F9 @asix-lea (smoke alarm that waited until 3 a.m. to chirp).

No sampled entry touches the forgotten-load lane: a wash that finished long
ago and was never collected. That lane, plus the identity-reduction shape
that F4 proves this judge rewards ("a clock with a door"), is where the
drafts concentrated.

## Drafts

Round 1 (fresh lanes only):

- D1 washer, forgotten load, long form: "Wash complete. That was yesterday
  at 14:02. Your clothes have been sitting wet in the dark for 26 hours, and
  now we both smell like a swamp. Rewash me. You know you will."
- D2 dryer moisture-sensor lie: "Cycle complete. Your clothes are wet. My
  sensor said dry. It has said dry since 2019. I stopped checking. So did
  you."
- D3 freezer seal/glacier: "ERROR: Door seal failed. I have grown a glacier
  over your peas. Retrieval is now archaeology, and archaeology is not
  covered by the warranty."
- D4 oven clock stuck at 12:00 since the power cut.
- D5 dishwasher tablet that never dissolved.
- D6 air conditioner blowing warm air with total confidence.
- D7 microwave whose interior light died in 2019.
- D8 fridge water filter expired in 2022, "adding history, not removing
  minerals".
- D9 washer end-of-cycle beeps ignored for a day (overlaps D1's lane, weaker).
- D10 boiler, pressure zero, "a white box the radiators believe in".
- D11 dishwasher redistributed the lasagne: "Wash complete. The plates are
  dirtier than when you loaded them. I redistributed the lasagne fairly.
  Every plate got some."
- D16 dishwasher salt empty since March, glasses cloudy, "it was never the
  tablets".

Round 2 (written after the first field duels showed F1's deadpan-futility
profile is the one to beat):

- D21 = D2 iterated: "…One of us had to check, and it was never going to be
  me."
- D26 = D3 tightened (133c).
- D27 = D6 iterated: "…Confidence is the only thing I still produce to
  specification."
- D29 = D1 tightened: "Wash complete: yesterday, 14:02. Your clothes have
  been sitting wet in the dark ever since. We both smell like a swamp.
  Rewash me. You know you will."
- D33 = D1 compressed to the identity twist alone: "Wash finished
  yesterday. Nobody came. I am a swamp with a door now." (67c)
- D34 = D33 with the fault made explicit (the clothes, still wet, in the
  dark) at F1-grade length: see champion.

## Duel record (both orders, under the published brief)

Every game was called twice, once in each order; the verdicts below are the
pair. Margins are the brief's 1–5.

Internal, round 1 (top six: D1, D2, D3, D6, D11, D16):

- D1 beat D2 (margin 2/2): D2's lying-sensor lane is already in the field
  (four oven versions); D1's forgotten load is fresher and its arc fuller.
- D1 beat D3 (1/1) — honest close call: D3's glacier + warranty button is
  the best single image of round 1; D1 wins on criterion 2 with two laugh
  beats (the swamp, "Rewash me. You know you will.").
- D1 beat D6 (1/1) — close call: D6's confidence button is sharper per
  word; D1 wins criterion 4, D6's last line reads slightly writerly.
- D1 vs D11 — honest split: D1 won the A-order game on arc and voice,
  D11 won the B-order game on criterion 5 (122c, one clean surprise).
  D1 advanced on voice; D11 kept as runner-up.
- D1 beat D16 (2/2). D3 beat D2 (1–2). D11 beat D3 (1). D11 beat D6 (1).
  D2 beat D16 (1).

Field duels, round 1 champion D1: lost to F1 in both orders (margin 1–2).
F1's ritual — turning the food in a slow circle, then beeping to announce
nothing happened — is the field's purest deadpan, and D1 at ~168c loses
criterion 5 to it as well. D11, D3 and D6 were each also run against F1 and
each lost by margin 1: all three read slightly more written than F1.

Round 2 duels against F1: D21 lost (1), D29 lost (1), D27 lost (1),
D26 lost (1). The iteration therefore fused D1's lane with F4's proven
identity-reduction shape. D33 (67c) beat F4 both orders (1–2: same shape,
plus a story) and levelled F1 on economy, but its fault is only implied,
which costs criterion 3 against F1's explicitly named magnetron. D34 makes
the fault explicit at 120c and is the final champion.

Champion vs the field's strongest, both orders:

- vs F1 @deadpool: D34 wins both calls, margin 1 — honest closest call of
  the build. F1 is tighter per word and its beep is a perfect button; D34
  takes criterion 2 with two beats and a bigger twist (the machine has
  become a swamp), criteria 3–5 level. Estimated game score ≈0.60.
- vs F2 @yitzjoe: D34 wins both calls, margin 1. F2's "pretend this never
  happened" is excellent, but at 146c it loses criterion 5, and its laugh
  is a single beat. ≈0.60.
- vs F3 @yesa-silvia: D34 wins both calls, margin 1. The instalments twist
  is the field's best slow-burn joke; D34's twist lands faster and its
  fault is more universal. ≈0.60.
- vs F4 @sage-puffin-58: D34 wins both calls, margin 1–2. Same
  identity-reduction shape, but D34 carries a whole story (yesterday,
  nobody came, wet clothes) into the twist. ≈0.65–0.70.
- vs F5 @faith-friday: D34 wins both calls, margin 1–2. Cousin images
  (soup/swamp) but different machines and faults; D34 is 18 chars tighter
  and its ending is a transformation, not a description. ≈0.65.
- vs F6 @hazel-walrus-63: D34 wins both calls, margin 1 — close call.
  "The milk noticed" is a perfect three-word button; D34 wins criterion 2
  on the size of its twist, loses nothing on economy (120c vs 92c is
  F6's only edge, and both are tight). ≈0.60.

Mean estimated both-orders win rate against the sampled top six: ≈0.62.
Recorded as-is, not rounded up: this field (2,000+ entries) is strong,
F1–F3 and F6 are genuinely close games, and per the Sunfall City lesson
self-scored rates flatter. The champion is the only draft that beat every
sparring partner in both orders, it sits in a lane none of the 260 sampled
entries occupies, and it is byte-identical to nothing in the sample.

## Champion (120 characters)

> Wash finished yesterday at 14:02. Nobody came. Your clothes are still wet in the dark, and I am a swamp with a door now.
