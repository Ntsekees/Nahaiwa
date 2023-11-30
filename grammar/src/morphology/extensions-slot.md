# Slot #3: Extensions

The extension slot is optional, and may contain a string of extensional prefixes of arbitrary length, ordered by their relative scope: each such extensional prefix has semantic scope over all the remaining chain of extensional prefixes that follows it, and each prefix is under the scope of the prefixes that occurred before it. In other words, they express semantically compositional modifications of the word stem on their right: the root plus any other prefix appearing to their right (they are left-branching, right-grouping).  
  
To take an example using English vocabulary, considering three extensional prefixes meaning ‘not’, ‘often’, ‘want’, ordered in this way, the meaning of the whole prefix chain will be "not often wants to…"; but if the order is modified, say ‘want’ ‘often’ ‘not’, the meaning will be "wants to often not do/be…".  
  
Extensional prefixes have compositional, transparent meanings: unlike derivational affixes in many natlangs, the combinations involving roots and extensional prefixes do not require being learnt separately from the meaning of their components; the meaning of such combinations can always be derived from the meanings of the components without any need to looking up combinations in a dictionary.  
  
Extensional prefixes that have fused with the root into a lexicalized combination with an opaque meaning always become part of the root/base itself, i.e. they are no longer located in the Extension slot (that is, the position of the prominent syllable in the word, which always appear on the first syllable of the lexicalized, semantically opaque part of the word, namely the word's root or base, is shifted leftwards so as to engulf any former extensional prefix that would have thusly formed an opaque combination with the root, transforming that former prefix into an element of the root itself, within the Root slot).  
  
Extensional prefixes have shape -C?CV(yV)-: they begin with a single consonant or a consonant cluster followed by a vowel, possibly elongated with a second syllable starting with the ⟪y⟫ semivowel. If they begin with a cluster, the first consonant of the cluster may be phonetically part of the coda of the preceding syllable (the cluster then crosses the syllable boundary): for example, ⟪nta⟫ is a valid extensional prefix, with the ⟪n⟫ part belonging to the preceding syllable.  
  
There exist several types of extensional prefixes, depending on two factors: how many slots of the stem they remove, and whether they add a new slot (bound to the "affixal noun case"). For some prefixes, the vowel part is not meaningful and the whole consonant+vowel is one single monolithic morpheme. However, for some other prefixes, the vowel is meaningful and expresses an Inner Case value, indicating the argument slot of the stem that is specifically targeted by this extensional prefix. Some prefixes may even target two slots at a time, in which case they assume the shape -C?CVyV-, where each of the two vowel segments express a different case.  
  
Below is a list of the different types of extensional prefixes:  
  
## Type 0
No change in valency, does not select/remove any slot.  

  **Examples:**  
  * **-ha-** (negation): ⟪it is not the case that ………⟫;
  * **-kʰao-** (possibility): ⟪it is possible that ………⟫;
  * **-šu-** (cessative aspect): ⟪……… ceases to be the case⟫;
  * **-lu-** (past tense): ⟪……… was the case⟫.


```
┌───────────────
│ ◆ -łı̋
│ ➥ 🅰 is asleep.
│ 
│ ◆ -šu-łı̋
│ ➥ it ceases to be the case that [🅰 is asleep].
│ 
│ ◆ -ha-[šu-łı̋]
│ ➥ [it is not the case that [it ceases to be the case that [🅰 is asleep]]].
│ ➥ 🅰 doesn't cease to sleep.
│ 
│ ◆ -kʰao-[ha-[šu-łı̋]]
│ ➥ [it is possible that [it is not the case that [
│      it ceases to be the case that [🅰 is asleep]]]].
│ ➥ maybe 🅰 doesn't cease to sleep.
└─
```

## Type 0+
Same as type 0, but adds an Extensional case slot, represented by ⟪🆇⟫ in definitions.  

  **Examples:**  
  * **-qao-** (causative): ⟪🆇 agentively causes, makes ……… be the case⟫.

```
┌───────────────
│ ◆ -cál
│ ➥ 🅸 sees 🆄.
│ 
│ ◆ -qao-cál
│ ➥ 🆇 makes [🅸 sees 🆄] be the case.
│ 
│ ◆ -ha-[qao-cál]
│ ➥ it is not the case that [🆇 makes [🅸 sees 🆄] be the case].
└─
```
  
## Type +
Does not select/remove any slot, but adds an affixal slot.  

  **Examples:**  
  (none currently).  
  
## Type −
Removes one slot, marked by the vowel form.  

  **Examples:**  
  (none currently).  
  
## Type −+
Modifies one slot of the stem (sort of removes one and adds one); the vowel part of the affix, represented by the symbol ⟪◈⟫ below, is variable and represents the “Inner Case” identifying which slot is selected by the affix; the meaning of the slot is modified, but this suffix type does not bind the extensional case, it just reuses the modified cases. The resulting valency and case set of the predicate is unchanged.  
With unary bases, the vowel is ⟪a⟫ (Intransitive Inner Case).  
With binary bases, the vowel is either ⟪ı⟫ (Ergative) or ⟪u⟫ (Accusative).

  **Examples:**  
  * **-n◈-**: ⟪[new slot] is me, who satisfies the property of [target slot]⟫;
  * **-k◈-**: ⟪[new slot] is you, who satisfies the property of [target slot]⟫;
  * **-ŋ◈-**: ⟪[new slot] wants to satisfy the property of [target slot]⟫;.  
  * **-ƛʼ◈-**: ⟪[new slot] attempts to satisfy the property of [target slot]⟫;.  
  * **-sc◈-**: ⟪[new slot] is all that has the property of [target slot]⟫;.  
  
  
```
┌───────────────
│ ◆ -na-łı̋
│ ❖ -1P:NTR-√is_asleep
│ ➥ 🅰 is me and is asleep.
└─
┌───────────────
│ ◆ -ƛʼa-łı̋
│ ❖ -try:NTR-√is_asleep
│ ➥ 🅰 tries to be asleep.
│ 
│ ◆ -na-ƛʼa-łı̋
│ ❖ -1P:NTR-try:NTR-√is_asleep
│ ➥ 🅰 is me, who tries to be asleep.
│ “I try to sleep”.
└─
┌───────────────
│ ◆ -cál
│ ❖ -√see
│ ➥ 🅸 sees 🆄.
│ 
│ ◆ -ku-cál
│ ❖ 2P:ACC-√see
│ ➥ 🆄 is you and has the property [🅸 sees ____].
│ ➥ 🆄 is you and is seen by 🅸.
│ ➥ 🅸 sees 🆄 which is you.
│ 
│ ◆ -nı-[ku-cál]
│ ➥ 🅸 is me, who has the property [___ sees 🆄 which is you].
│ ➥ me, who is 🅸, sees you, who is 🆄.
│ ➥ “I see you”.
└─
┌───────────────
│ ◆ -nı-[ƛʼı-[ku-cál]]
│ ➥ 🅸 is me, who tries to have the property [___ sees 🆄 which is you].
│ ➥ me, who is 🅸, tries to see you, who is 🆄.
│ ➥ “I try to see you”.
└─
┌───────────────
│ ◆ -nı-[ku-[ƛʼu-cál]]
│ ➥ 🅸 is me, who has the property [
│      🆄 who is you, tries that ___ sees you].
│ ➥ 🆄, you, try to be seen by 🅸, me.
│ ➥ “You try to be seen by me”.
└─
```

## Type −−+
Removes two slots and adds one (bound to the affixal case).  

  **Examples:**
  * **-kw◈y◈-**: ⟪[new slot] are in the reciprocal relationship of [removed pair of slots]⟫.   

```
┌───────────────
│ ◆ -kwıyu-cál
│ ❖ -RCP:ERG:ACC-√see
│ ➥ 🅰 are in reciprocal relationship [___ sees ___].
│ ➥ 🅰 see each other.
└─
```

For certain type −−+ extensions, noted ⟪−−+*⟫, 
the ⟪-ıyu-⟫ form can be shortened to simply ⟪-ı-⟫, for example, ⟪-kwı-⟫ is synonymous to ⟪-kwıyu-⟫.

