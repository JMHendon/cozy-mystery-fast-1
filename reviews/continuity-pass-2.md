---
document: continuity pass 2 (seams between the four Rev 1 revisers)
scope: manuscript/ch01–ch44 after Rev 1 (R1 Ch 1–9, R2 Ch 10–22, R3 Ch 23–33, R4 Ch 34–44, with the Ch 41/42 swap)
checked_against: reviews/editorial-letter-rev1.md (governs), the four rev1 logs, reviews/continuity-pass-1.md, foundation/mystery-spine.md, foundation/style-guide.md
method: I read all 44 chapters in order, in full. Then I ran targeted greps for every device budget, capped phrase, time, count and pre-click leak, and checked them against the drafts (reviews/draft1-full.md) wherever a callback's source was in doubt.
supersedes: continuity-pass-1.md §4. Where the two disagree, the ledger in §4 below governs.
---

# Continuity Pass 2

Every edit is surgical, from one word to one sentence. No plot was added, and the solution and the clue emphasis are unchanged. Nothing makes Hollis more conspicuous before Ch 32. Book total after this pass: **80,896 words** (`wc -w`), inside the letter's 80,000–82,000 target. Headings are correct and sequential in all 44 files (`# Chapter N` / `## Title`), Ch 41 is **Keys** and Ch 42 is **Daylight**, and `compile.py` sorts by filename.

## 1. Changes made

| Ch | Before → After | Why |
|---|---|---|
| 24 | June: "I get to decide where it goes." → "I get to decide where it goes. **I said not in public. Mattie sent me the video before first period.**" | **Orphaned setup.** R3 cut this line without logging it. That left June's Ch 18 condition ("Don't do it in public"), which Archie breaks in Ch 19, unregistered anywhere in the book. This restores Pass 1's fix (+11 words). |
| 25 | Teddy: the card "went out with the drives on **Monday**" → "on **Sunday**" | Ch 27 has Brannock say that on *Sunday* Teddy told him the card "had gone to Los Angeles." Teddy's lie now holds steady. (This was pre-existing, but the Ch 27 rewrite exposed it.) |
| 26 | June: Kev "Six hundred and **four** thousand this morning" (Wed) → "Six hundred and **thirty** thousand this morning" | Ch 21 (Tue) already gives 604,000. Without the change his count stalls for a day while the letter's point is that it's climbing. Ch 27's "six hundred thousand new reasons" still fits. |
| 28 | June's face "lit up all at once… **the way his own face must have lit on a kitchen floor in 1982 with a silver dollar coming out of his ear**" (and "before she could stop it") → "And then it lit up all at once, the whole of it." | **Cross-range repeated image.** Ch 44's "struck match — the way his own must have been when he was four years old… *Watch closely, Sparrow*" is the payoff. Ch 28 had already spent the same comparison. The cut also removes an Act II body-before-mind formula and a manner clause. |
| 33 | Archie's assembly quotes *Hollis already gave me the speech.* → *Hollis already sat at this table and gave me the whole thing again.* | **Quote to a line that isn't there.** The italics present it as Shannon's words, but Ch 13 never says "the speech." It now matches what she actually said in Ch 13. |
| 34 | Dale "had been a Knox County deputy for **twenty years** before he came to Merrow in 2010" → "for **more than twenty years**" | **Arithmetic seam, Ch 15 vs Ch 34.** Dale was already a deputy in 1988 (Ch 15), and 2010 − 20 = 1990. |
| 34 | Brannock: "until we've been through that **shed**" → "that **house**" | Nobody on the page has mentioned a shed yet. Tess hasn't opened the confession, and the shed first appears in Ch 35. The warrant line ("House and outbuildings") stays. |
| 34 | Tess's drive-by: "a weathered Cape with a blue door **and a big front border dug over to bare earth**" → "a weathered Cape with a blue door" | **The turned bed must first appear in Ch 35** (A5, and the brief for this pass). Ch 35's "dug over its whole length to bare brown earth" is now the bed's only appearance before the confession. |
| 35 | Hollis "looked at him **a second longer than she needed to**" → "She looked at him." | The same phrase closes a beat in Ch 32 (June), three chapters earlier, in another reviser's range (it also appears in Ch 5). The plain version is stronger here. |
| 35 | "**Mattie Pinkham and three of her cousins** on ladders" at 8 a.m. Friday → "**three of the Pinkham cousins** on ladders" | Friday is a school day. Ch 37 has June driven to school that morning, and Mattie is her classmate. Ch 31 already uses "three of the Pinkham cousins." |
| 41 | Hollis's ring of keys "in the pocket of his buffalo-check coat" → "hooked on his belt under his buffalo-check coat" | Ch 39 makes it a ring "the size of a dinner plate" with a hundred keys, which won't fit in a coat pocket. Same logic as Pass 1's poster-tube fix. "Knocking against his hip" later in the chapter now reads correctly. |
| 41 | Lorelei died "**two floors down** in this same building" → "**downstairs** in this same building" | She died in the ER at Pen Bay in Rockport (Ch 9), and Hollis is in room 214. Nobody on the page knows the floor count. |
| 43 | Tess: "I'm not going to tell you what you risked, either. **Bev's told you.**" → "…either. **You know.**" | **Orphaned callback.** No chapter, in any draft, has Bev telling Archie off for the risk. In Ch 39 she says "Drink that. Then go," and in Ch 42 she serves pie. |

## 2. Brief checklist, verified with no change needed

**Callbacks**
- **Sparrow source.** Planted in Ch 12: Sunday, Ivy's binder, the pink FAIRWEATHER, A. tab, a Nov 1988 *Packet* photocopy, highlighted, read upside down from the wall. It pays off in Ch 24 (Tuesday turret, refuses at S-P-A) and Ch 44 ("read it upside down, from a wall, behind a pink tab"). June's microfilm copy in Ch 44 pays off Ch 32's "The *Packet*'s on microfilm… Deb opens at nine." Ch 10's "Then show it to me" is answered by Ch 12's "It was research."
- **Library card.**
  - Ch 5 runs in date order: H. Coombs 2/79, R. Thibodeau 4/79, W. Calloway 11/88, H. Pelletier 3/92, M. Pinkham 6/95, H. Langley 12/03, then J. Fairweather ×3.
  - Ch 32 ("H. Langley, twelve, oh-three. The last name before mine") and Ch 35 ("H. Langley, December 2003") both match.
  - The Langley line gets no arrow, and Deb's comment is about Pinkham.
- **Ch 17 photo.**
  - Ch 17: piano crowded with photos, the Ford story, then "Danny. My son." and the waistcoat handed over the cat's head.
  - Ch 32 matches exactly. There is no costume rack and no man in oilskins.
  - Ch 33's "a boy on a dock with a mackerel" matches. Bev's "ate a whole blueberry pie… when he was twelve" agrees with the photo's age.
  - Ch 41 doesn't recall the photo.
- **Thermos.** It is left by the wall (Ch 7). Vivienne bags it Saturday night and leaves it on the hall table (Ch 10). It is returned a little after noon Sunday, count 61 (Ch 12). Bev washes it "cups and all" Sunday afternoon (Ch 14). Ch 16 has "went home in your mother's handbag… washed it yesterday afternoon." No Dale, hearse window or "evidence man" remains anywhere.
- **Tess's call (Ch 29 → Ch 34).** The call is Wednesday night, off the record ("This call isn't happening"): the AG files tomorrow, the jail at ten, "I believe you." Ch 34's "believed the magician since Wednesday… against orders, in a call she would never log" matches.
- **Dale's history.** Ch 15 has him as a Knox County deputy in 1988 (softball sweatshirt, 2004). Ch 34 has him on the county in 2003 and at Merrow PD from 2010. The span is fixed above.
- **Ivy's release.** Ch 41: "Ivy Crane walked out at ten." Ch 42: "two hours out of Knox County Jail" at 12:15. Ch 35: "would walk out tomorrow morning." No "eight" or "eleven" release time is left on the page.
- **Saturday flow.** Statement at 8 (Ch 41). Ivy out at 10. Tess in the dooryard at 10:30, then Pen Bay, twenty minutes, and "The Galley." The fog burns off by 9, and Tess drops him at the wharf at noon (Ch 42). Ivy arrives 12:15, Warren 12:30, the liars' table leaves at 1. Archie walks home and sleeps three hours with the cat (Ch 43). Memorial at 5. June went to the library with Mattie in the afternoon, home at 6 (Ch 44). Supper at 7. Malvolio arrived at midnight Friday (Ch 41's "Dale says…", Ch 44).
- **Hollis's method (Ch 41 against Ch 7 and Ch 26).**
  - Ch 7 plants the crew's black stage gloves, worn while lighting the candles, the open-flame permit in her name, and the tray, water glasses and horn slid "on her way off."
  - Ch 26 has the tall pillar candle in the middle of the table, "the polished curve of the trumpet right beside it," Hollis walking off with her tray, and the flare at 7:51:10.
  - Ch 28 has the shoebox of crew gloves from the booth, and Ch 37 has black cotton gloves in the shed.
  - Ch 41's "a hand from the horn on purpose," "Black cotton, out of the crew's box," the finger cot, the tin under the tray, the funnel lift and the fire-hold failsafe are all consistent with these. Ch 24 has Archie say he saw it "from the back of the room," which matches "I watched you… I was looking right at you."
- **Kayla, the cruiser and the fire escape.**
  - Ch 31: the marshal's order, and the door wedged with a program.
  - Ch 34: Brannock sets Bissonnette in plain clothes from 5 and a car on Main Street.
  - Ch 36: Archie sees the cruiser at 5:30 and Kayla at 6:45 "with the balcony stairs at her elbow," and is relieved. He knows nothing of the door.
  - Ch 37: "I had the balcony stairs, Sarge"; warrant at 6:40.
  - Ch 41: Kayla's phone call at 6:45 and the cruiser "when I came in."
- **Vivienne and Ozzie.**
  - The undertow runs through Ch 28 (phone face down), Ch 29 (pantry calls, "nobody"), Ch 31 ("out is a complete sentence") and Ch 32 (coat smelling of fried clams).
  - It resolves in Ch 33 (Lobster Pound, Lincolnville; "Ozzie." / "Ozzie.").
  - Ch 27's "fresh on Saturday morning" monkshood fits with Ch 2 and Ch 16's Thursday jug as a second cutting she reported herself.
- **Kev.** Subscribers run 11,400 (Fri) → ~600,000 (Tue a.m., Ch 20) → 604,000 (Tue 10 a.m., Ch 21) → 630,000 (Wed, Ch 26) → "six hundred thousand new reasons" (Wed, Ch 27). He is never formally cleared, and Ch 27's witness warning blocks Archie's plan to question him.
- **Glass Box.**
  - Ch 25 defines the effect and plants the room-service fries ("*Magic, Junebug*").
  - Ch 26: "Eleven months… Henderson."
  - Ch 28: June cites the napkin.
  - Ch 44: the landing, the two-word answer refused, four minutes, the method unheard, "eleven months of Lenny in a garage in Henderson, Nevada."
  - Knowers on the page: Lenny, two stagehands, Archie, Teddy and June.

**No orphaned payoffs remain.** I checked:
- "foot taller," "vulture," the turned bed in Ch 17 and Ch 33
- "You didn't feel me take it"
- the "stagehand" line (Ch 41's is Hollis's own, not a callback to the cut Ch 22 line)
- "Hear me out"/"No" (Ch 11, 14)
- "Grandma's in the chair anyway"
- "the words he'd taught her on Wednesday night"
- "I did that once this week. In a diner"
- "the voice from the parking lot" (Ch 29 → 27)
- Lionel
- "Correct answer"
- Hollis's "a queen" (Ch 35 → 36)
- "Mattie has the cue book… Thursday"
- "That's twice"

**Device budgets (whole book)**

| Device | Where | Budget |
|---|---|---|
| Coin walk | Ch 10, 17, 24, 31 | OK |
| Card from nowhere | Ch 13 (ace of spades, queen of hearts), Ch 28 (jack of clubs). R2 cut Ch 21's apport. | Within 13/21/28 |
| Lifts | Ch 4 (pen), Ch 20 (notebook, caught), Ch 43 (Tess, the watch). Ch 21 is now a request ("lend me that"), and Ch 36 says "no lifting tonight." | OK |
| "Holy Houdini" | Ch 22 only | OK |
| Tess laughs | Ch 11 only. Ch 43's "almost smiled" and "almost certain she was smiling" are not laughs. | OK |
| Watch-winding | Ch 11, 18, 25, 32, never twice in a chapter | OK |
| "X stopped." one-liners | At most one punch per chapter. Ch 32's second "stopped" is June pausing at the stairs, not a punch. | OK |
| Body-before-mind | Act I: Ch 1's grin. Act II: Ch 11 (Tess's laugh "got out before anyone could stop it"), which is protected. Act III: Ch 38's cloak fold. Ch 44's recollection of the same fold is the payoff, not a new instance. | OK |

**Capped phrases (letter C38 and others)**

| Phrase | Where | Cap |
|---|---|---|
| "Second and a half" | Ch 4 only | OK |
| Presidential dating | Carter (Ch 1), Obama (Ch 3) | OK |
| "Struck match" | Ch 44 only | OK |
| "Pushed straight through" | Ch 3 only | OK |
| "Meant it so much" | Ch 5 only | OK |
| "1994" | None left | OK |
| "In half, and in half again" | Ch 19 only | OK |
| "Hear me out" | Ch 11, 14 | OK |
| "Four sweaters" | Ch 1 origin, Ch 2 callback. Ch 29's "all three" and Ch 44's "one sweater fewer" are different jokes. | OK |
| Merrow Light "every six seconds" | Ch 2 only | OK |
| "For a long moment" | None | OK |
| "Something went across / face did something" | None | OK |
| "Very X and very Y" | None | OK |

**Chapter endings**
- The bell buoy closes Ch 2, 33 and 43, which is within the limit of five.
- Epigram or harbor endings are about 7 of 44, well under a third.

**No early solution**
- Before Ch 32 there is no Langley outside the memorial list (Ch 3) and the card (Ch 5).
- "Danny" appears only as "Danny. My son." (Ch 17).
- There is no Hollis monkshood, border, shed, jar or finger cot, and no "a foot taller."
- After this pass the turned bed first appears in Ch 35.

## 3. Issues found but not fixed (and why)

1. **"Thirty thousand people"** appears in Ch 5, 14 and 36, as Archie's career yardstick. It isn't capped by the letter, and each use does different work. It's a trim candidate for the line edit.
2. **"A second/moment longer than (s)he needed to"** now appears in Ch 5, 15 and 32. These are three ranges and three different scenes, so I left them for the line edit.
3. **Ch 7 against Ch 26 order.** Ch 7's bustle paragraph lists Hollis lighting candles before Kev's phone. The B-roll in Ch 26 has Kev at 7:46 and candles at 7:48. Ch 7 is a deliberately unordered "dozen people doing a dozen things" from the back of the hall (letter A4), and the B-roll governs.
4. **Ch 38: "She didn't use it for a private sitting again for three years."** Archie infers this from Ivy's "November 2003" plus Kev's "to oh-six." It's consistent with the A6 blur, so I left it.
5. **Ch 43: Brannock spoke "this morning at the command post."** Saturday is crowded (statement at 8 at Pen Bay, Rockland at 10), but an early-morning command-post moment still fits. Left.
6. **Ch 42:** the poster tube Archie has had "under his arm all morning" isn't mentioned at Pen Bay in Ch 41. It's harmless. Left.
7. **Ch 41: Hollis's "unlocking the radiators"** is odd wording ("bleeding" is the idiom). It's R4's line, a word choice, not a seam. Flag for the line edit.
8. **Ch 41/42: "from closer than Knox County."** Merrow is itself in Knox County, so this reads as Hollis's dry reference to the county jail. Left as character voice.
9. **Rosie** is a ladybug "since Thursday" (Ch 13) and a lobster on Halloween (Ch 36, 39). This is pre-existing (Pass 1 #2) and not a contradiction.
10. **Hollis as godmother** is first stated in Ch 41 (Ch 13 shows only "Aunt Hollis"). This follows from A5 cutting "I'm Rosie's godmother" from Ch 17. It isn't a contradiction, and the spine's clue list (#10) is now stale on this point.
11. **Spine is stale.** It still lists clue 1c ("a foot taller"), clue 11 (the bed in Ch 17), clue 13 (the family laughs it off) and "the bail commissioner at 8." The page governs. Planners should update the spine before Book 2 work.

## 4. Continuity ledger (rely on this; supersedes Pass 1 §4)

### Fixed facts

**Ages and people**
- Archie is 47, and was 10 in 1988 (second row, left aisle). Others: June 16, Vivienne 73, Lenny 70, Tess 38, Walt 74 (chief 1981–2010), Hollis 66 (29 in 1988), Lorelei 58 (started at 26, "thirty years on the road"), Ivy 29 (7 in Nov 2003, plant since 12), Shannon 34, Liam 7, Rosie 4, Kev 31, Warren 61, Dale 63, Bev 67, Ozzie 70.
- **Dale:** a Knox County deputy from before 1988 (the Gus search). On the county in 2003. Merrow PD from 2010, the year Walt retired.
- **Hollis** married Peter Langley in 1983. Danny drowned at the quarry in Aug 2001, aged 15. Peter was lost on Shag Ledge on 11/18/03. She was "Hollis Langley" socially until after Peter's death, and "Mrs. Tibbetts" at school always. The séance unit ran about 2004 to 2020 ("sixteen years"). She wrote to Marchand in **May** to *expose* Lorelei, after seeing the Gloucester widow episode. The town signed in **July**, and Shannon was contacted about two weeks later. Hollis is Rosie's godmother ("Aunt Hollis").

**The library card (Ch 5, in date order)**
- H. Coombs 2/79 (Deb's mother-in-law, the Grange table-tipping)
- R. Thibodeau 4/79 (Bev's father-in-law, cribbage)
- W. Calloway 11/88
- H. Pelletier 3/92 (the minister's wife)
- M. Pinkham 6/95 (Dale's cousin's girl, an A)
- H. Langley 12/03
- J. Fairweather: Sept, Oct, Oct

**The memorial**
- Ch 3 reads the names *without years*: Arthur Coombs, Robert and James Haskell, Peter Langley, Dennis Pinkham, and below them THOMAS MAYO.
- The years come from the stone in Ch 32 (1978, 1991, 2003).
- Ch 43 adds that names have been cut "since 1847."

**Objects and props**
- **The Sparrow source:** the *Merrow Packet*, Nov 1988: "his grandson, Archie, whom he called his 'little sparrow.'" It's a photocopy in Ivy's binder behind a pink tab (Ch 12), and June's microfilm copy (Ch 44). The trunk page is a separate 1988 *Packet* page (Ch 2).
- **Monkshood at Fairweather House:** Gus's stand along the fence. Vivienne cut it for a jug on Thursday (Ch 2, 16) and cut fresh on Saturday morning, which she told police herself (Ch 27).
- **Thermos:** Ch 7 by the wall → Vivienne's bag, Saturday night → hall table → back to Bev a little after noon Sunday → washed Sunday afternoon.
- **Gus's watch:** a steel Hamilton with a cracked crystal, loses four minutes a day. Wound in Ch 11, 18, 25 and 32. Tess lifts it in the water in Ch 38 and returns it in Ch 43.
- **The trap, the Chair and the crawlspace** are as in Pass 1. Practice rig: rope and counterweight (Ch 29). The stage uses Gus's 1951 iron lever (Ch 40).
- **Light board:** 280 cues. Q.142 is the Sparrows. The cue-book drawer is "not the cough drops." Mattie was shown the board on Thursday.
- **Glass Box:** a clear case on a bright stage, then empty, with Archie on a plane to June's Boston debate final. Built over 11 months in Henderson, NV. The method is known to Lenny, two stagehands, Archie, Teddy (napkin NDA, Ch 25) and June (Ch 44). The reader never hears it.
- **Posters:** Gus's, on loan since 1985, now Vivienne's.
  - Sold in September: WALKS THROUGH WALLS ($1,150), RADIO'S MASTER OF MYSTERY (1949, $1,400, Connecticut), SAWS A LADY IN HALF (1966, $975, Ohio).
  - HALLOWEEN AT THE OPERA HOUSE (1962) was listed Saturday at 6:48 and ended Sunday at 12:04.
  - The first two were bought back (Philadelphia, Connecticut) and given to Warren for Carol in Ch 42.
- **Trunk:** SPARROW, opened by June on Saturday night (Ch 44). Inside: opera gloves, cards, the "You remembered" note, and the Key West postcard, MAR 14 1996.

**Kev and the Trumpet Hiatus**
- **Kev's channel:** 11,400 Fri → ~600,000 Tue a.m. → 604,000 Tue 10 a.m. → 630,000 Wed. Ads turned on Sunday night, and a mattress sponsor.
- **The Trumpet Hiatus** is fan lore: "oh-three or oh-four… to oh-six" (Ch 21). Ivy fixes the start at Nov 2003 (Ch 30). Archie says "three years" (Ch 38).

### Device and phrase budgets (final)
- Coin walk: Ch 10, 17, 24, 31. Card from nowhere: Ch 13, 28. Lifts: Ch 4, 20 (caught), 43 (Tess). "Holy Houdini": Ch 22. Tess laughs: Ch 11. Watch-winding: Ch 11, 18, 25, 32.
- Wild theories: #1 rum-runners (Ch 11), #2 Baja (Ch 14), #3 Warren at the table plus Kev the plant (Ch 18–20), #4 Kev as likeliest (Ch 26, with June).
- Liars' table count: 59 (Ch 3), 61 (Ch 12), 62 (Ch 15), 63 (Ch 19), 64 with Elwin's nod (Ch 28), 66 "Morning, Archie," unheard (Ch 33). A chair pulled out on Saturday (Ch 42). Pickle is Lionel (Ch 36).
- Bell-buoy chapter closers: Ch 2, 33, 43.

### Timeline (changes from Pass 1 marked ▲)

**Thu Oct 23**
- Straitjacket escape, 2:11. The walkthrough. The $2M bet.
- ▲ Ch 1: "Everybody in Merrow *probably* knows about the trunk" (said, not believed).
- Harold. Vivienne's jug of Gus's monkshood.
- ▲ The "foot taller" line is gone. The *Packet* trunk page brings relief, then unease (Ch 2).
- Marco at the walkthrough (gaffer tape; ▲ Hollis watches his lens flare off the horn, Ch 41).
- 1:05 a.m.: LORELEI on the dials.

**Fri Oct 24**
- 6:30, Galley (count 59): the spoon; "Page one-twelve."
- Memorial with Shannon. ▲ Her contact came "in the summer."
- Sea View: lift #1.
- Afternoon: Warren borrows Hollis's key and takes the 1962 poster.
- 4:30, library: the card; June's pass.
- 8 p.m., Spindrift: "last season"; "thirty years on the road."
- About 9, Shannon's 4th reading. About 9:30, Kev in the prop room.

**Sat Oct 25**
- Thermos at 6.
- 7:20: ▲ Ivy lays out the props alone (Ch 7).
- 7:30: controls. 7:35:12: the toot. 7:38: the whisper. About 7:41: tea, cut.
- 7:43:50: Ivy places the rod (B-roll).
- 7:45–7:55: Archie at the back with Dale.
- B-roll: 7:46 Kev, 7:47 Warren down (Dale at the stair door until 7:57), 7:48 Hollis with candles and water, 7:51:10–7:51:50 the pan, Teddy's call, the horn slid.
- 7:55: Archie sits. 7:58: return. 7:59: Kev's camera. 8:00: dark. 8:17:04: the ringed hand. About 8:28: the horn falls; the wipe.
- 9:40: death (ER, Rockport / Pen Bay). 10:05: Tess.
- ▲ Vivienne bags the thermos. About 11: Archie drops Ivy at the Spindrift.

**Sun Oct 26**
- 7: pancakes; coin walk.
- 7 a.m.: Hollis at Shannon's ("the whole thing again").
- 9:58: walkthrough: hairpin, rum-runners, cone demo, Tess laughs, Hollis's answers, the remote. ▲ Archie *chooses* to pick up the remote.
- A little after noon: thermos returned (count 61).
- 1 p.m., Captain's Suite: binder taken. ▲ Archie sees the *Packet* Sparrow line. Coat returned.
- 4 p.m., Shannon's: cards. ▲ Liam's question.
- Autopsy at 4 in Augusta. Bev washes the thermos in the afternoon.
- 8 p.m.: poker.
- ▲ **9:30 p.m.: Warren walks into Tess's command post** (Dale's back office) and discloses everything. This supersedes Pass 1's "4 p.m."
- Later Sunday: the hatbox goes to Pru's safe.

**Mon Oct 27** (teacher-workshop day)
- 5:30: hauling (count 62). Harold is female. ▲ Dale: a Knox County deputy in 1988, out on a Coombs boat.
- Prelim blood result: aconite. It's a homicide.
- 2 p.m.: Brannock; the heater kept; ▲ "went home in your mother's handbag."
- 6 p.m., Pudding Lane: chowder, coin walk, Malvolio, Hollis in the booth in 1988. ▲ Crowded piano; "Danny. My son." ▲ No vulture speech, no border.
- About 9:30: June, Harborview.

**Tue Oct 28**
- 7: Galley (count 63). ▲ The theory is now Warren at the table, 7:38–7:47.
- 7:30, wharf: lift #2. ▲ Tess dismisses it on *her* theory (ingestion; Warren never near it) plus Dale's observation and Warren's Sunday-night disclosure.
- 9: scene released.
- 10, Kev: raps, glove, horn. ▲ The handle is borrowed, not lifted. ▲ Hiatus blurred. Poster line; coat left on the chair; footage.
- About 2:10: lab, "Holy Houdini," statement until 5:26.
- 5:31: running (Ch 23). About 6: Ivy arrested; Okafor.
- 10 p.m.: family meeting. ▲ No one comments on Hollis. ▲ June: "I said not in public. Mattie sent me the video." S-P-A, stop. Teddy's 9:05 flight.

**Wed Oct 29**
- June skips school.
- 7:50, Owls Head: the Glass Box for the card. ▲ Teddy: "went out with the drives on Sunday."
- 11, opera house: the B-roll walked once (Ch 26). ▲ Four names, no comment on Hollis. ▲ Kev the likeliest (630,000 subscribers). ▲ "It puts your mother at the table." Coat retrieved.
- 2 p.m., the lot: ▲ Brannock presses on Vivienne. ▲ The fast tox and the slow DNA explained. ▲ Archie refuses to name anyone. No-contact order.
- 4–8, Paint Day: count 64. ▲ Vivienne turns Ozzie's phone face down. 6:45: gloves. 7:15: oath.
- 10 p.m.: the Method. ▲ **Tess's off-the-record call** (murder charge tomorrow, jail at 10, "I believe you").

**Thu Oct 30**
- 10 a.m., jail: ▲ Ivy fixes "Two thousand three. November." Hatbox release signed. Tess in the corridor; Okafor tells her "a man in Maine."
- AG files murder. ▲ Tess remembers the by-complainant files Thursday afternoon.
- 6–8:15, dress rehearsal:
  - Fire door wedged.
  - Mattie and the cue book.
  - The Chair.
  - ▲ Archie hears Rosie and Hollis from the booth steps and goes back down.
  - ▲ Vivienne: "out is a complete sentence."
  - Cue question asked at 8:15.
- 9:04: Pru. 9:30 to about 3: the hatbox. ▲ Vivienne home first (fried clams). June to bed about 1:30; watch wound at 2.
- ▲ **Thursday night:** Vivienne and Ozzie at the Lobster Pound, Lincolnville. Hollis writes her confession.

**Fri Oct 31, Halloween**
- 4:50–5:15, Galley: ▲ Bev reveals Ozzie. "That's Hollis." The 10 p.m. deadline. "Morning, Archie" (66), unheard.
- 7: breakfast. June driven to school.
- 8: opera house (▲ Pinkham cousins on the ladders; Hollis).
- ▲ Dale finds the basement key Friday morning. 11:00: the 2003 drawer. 12:20: LANGLEY, H.
- Noon: Archie at Sea View (Carol's card). About 1–2: Tess at Sea View, "That's the trumpet woman." ▲ Tess remembers the signed eight-by-ten: *You're right. Don't tell anyone. — A.F.*
- 2:30: Hollis home.
- 3:00, Pudding Lane: ▲ the bed first seen (dug over, dahlias); ▲ chamomile accepted and drunk; the envelope; June's jacket.
- 3:15: Tess drives past (▲ house only). 3:40: *Intermission. Please.*
- 5: Kayla in plain clothes; cruiser on Main Street (▲ Archie sees it at 5:30 and is relieved).
- 6:40: warrant executed (blue jar, black cotton gloves). ▲ 6:45: Kayla's call; Hollis sees her look up.
- 7: show. About 8:15: intermission. ▲ "I'm going. I'm breaking my promise." June: "Go."
- 8:25–8:50: the bell buoy. ▲ "He decided." Line, collar, watch.
- About 8:55: the wharf, Miranda, keys. About 9:05–9:10: the Chair, "You're late."
- Midnight: Dale brings Malvolio.

**Sat Nov 1** (▲ restructured by the swap)
- 8: Hollis's formal statement at Pen Bay.
- **10: Ivy released** (Rockland). Tess drops her at the Spindrift.
- 10:30: Tess collects Archie (fever, cough, keys on his belt).
- About 11, Pen Bay room 214 (**Ch 41, Keys**):
  - The rest of the story: the May letter, July, September.
  - ▲ The method shown with a lunch menu and a water cup.
  - "Nobody looks at the stagehand"; "You did."
  - ▲ Why the bell: Kayla's look, the cruiser, "tell Peter first."
  - Apology for Ivy; "Ask me in a year."
  - Bequests: the Players, Rosie ("Ask Shannon, not Vivienne"), Malvolio.
  - Gus's wink at Walt.
- Noon–1, Galley (**Ch 42, Daylight**):
  - The liars' chair; pie.
  - 12:15: Ivy repays Shannon $1,050. ▲ Archie delivers Hollis's apology. Vermont.
  - ▲ Shannon on the godmother question: "We'll see after that."
  - 12:30: Warren, the posters for Carol.
  - 1: "Correct answer."
- About 1:30–4:30: Archie sleeps (the cat). June and Mattie at the library microfilm (Deb opens for them).
- 5, memorial (Ch 43):
  - Peter's notebook from the piano bench.
  - ▲ Tess's rebuke: what it was like, her hand on his collar.
  - Consult offer; "Yes"; the watch; "Don't tell anyone."
- 7, supper (Ch 44): both pies. ▲ The Glass Box told to June on the turret landing. June opens SPARROW. The note, the 1996 postcard, the folded cloak. "Get your coat."
