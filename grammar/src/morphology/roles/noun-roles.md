# Noun roles

 
With noun roles, as well as adjectival and adverbial roles, Slot 2 is subdivised into the following subslots:  
  
```  
┌────┬───────┬──────────────────────────────┐  
│ №  │ Form  │  Name                        │  
├────┼───────┼──────────────────────────────┤  
│ 2a │  C    │  Outer Case                  │  
├────┼───────┼──────────────────────────────┤  
│ 2b │ Vy/Vw │  Determinacy                 │  
├────┼───────┼──────────────────────────────┤  
│ 2c │ V(ʼV) │  Inner Case OR Subordinator  │  
└────┴───────┴──────────────────────────────┘  
```  
  
There are two kinds of cases:  
• Core cases, which indicate which slot of the predicate is selected;  
• Adjunct cases, which are of circumstantial nature.  
  
Nouns bear two case affixes:  
• The outer case, or external case, indicates the relationship between the noun and the main verb of the clause;  
• The inner case, or internal case, indicates which argument slot of the predicate represented by the noun's root is used for defining the noun (for example, with the root ‘to eat’, which expresses a binary relation between two participants, each represented by a case —the eater and the eaten thing—, selecting the first slot would yield a noun ‘eater’, whilst selecting the second case would yield a noun ‘eaten thing’).  
  
Instead of an inner case value, slot 2c may contain one of several Subordinator values (those will be covered later).  
  
The outer case is represented by a consonantal prefix, followed by a vocalic affix indicating the second case. A further optional -Vy- or -Vw- affix, the Determinacy affix, may optionally occur in between them (its purpose will be explained later on).  
  
The language exhibits an extended form of the tripartite alignment. Word roots represent predicates with an arity/valency between zero and four, i.e. governing at most four different arguments. Each predicate arity has its own set of case affixes: unary predicates govern only one case, binary predicates have two, ternary predicates have three, and so on. Predicates of a certain arity cannot govern case affixes belonging to a different arity: there is a form of agreement between cases and predicate arity.  
  
Core noun case affixes:  
  
OC ≝ External/outer case  
IC ≝ Internal/inner case  
  
```  
┌─────────────┬─────┬─────┐  
│ Arity       │ OC  │ IC  │  
├─────────────┼─────┼─────┤  
│ Unary:      │  t  │  a  │  
├─────────────┼─────┼─────┤  
│ Binary:     │  c  │  ı  │  
│             │  k  │  u  │  
├─────────────┼─────┼─────┤  
│ Ternary:    │  p  │  e  │  
│             │  č  │  ï  │  
│             │  q  │  o  │  
├─────────────┼─────┼─────┤  
│ Quaternary: │  pʰ │ aʼa │  
│             │  cʰ │ eʼe │  
│             │  čʰ │ ïʼï │  
│             │  qʰ │ oʼo │  
└─────────────┴─────┴─────┘  
```  
  
Other core cases:  
```  
┌─────────────┬─────┬─────┐  
│ DP:         │  tʼ │ uʼa │  
│ Affixal:    │  kʼ │ aı  │   
│ Eventive:   │  š  │ aï  │  
│ Situative:  │  tʰ │ uʼı │  
└─────────────┴─────┴─────┘  
```  
  
For binary, ternary an quaternary predicates, the cases shown in the table are ordered according to an animacy or temporal/causal hierarchy: the first participant is the most animate, or the one triggering or exercicing the most control over the event described by the predicate, or occasionally, in the case of stative relations, it may be the largest or most concrete participants. Abstract propositions, properties and relations have lowest rank in this hierarchy, and will typically be associated with the last cases of each case list.  
  
Below is an explanation of the functions of the other core cases mentioned in the second table above.  
  
• The Dislocated Predicate (DP) Case is governed exclusively by the predicate application root ⟪-tʰá⟫; it marks the noun phrase representing the predicate that is to be applied, ‘unboxed’, by the dummy applicator verb based on the ⟪-tʰá⟫ root, which also takes as its arguments all the arguments required by the applied predicate:  
```  
┌───────────────  
│ ◆ Aıtʰá tatʼí tʼoıtʼınucál.  =  Aınucál catʼí.  
│ ❖ ASR-has_property INTR-INTR-bird  
│   DP-UTC-lambda_1:ERG-me:NOM-see_stimulus  
│ ➥ A bird has the property of seeing me.  =  A bird sees me.  
└─  
```  
  
⸨Note: the predicate applicator root will maybe be replaced with one different applicator root for each allowed arities.⸩  
  
• The Affixal Case is governed by certain extentional prefixes, which intoduces a new participant to the relationship expressed by the verb. For example, a causative extensional prefix will adds a ‘causer’ participant, which will then be accessible via the Affixal Case.  
  
• The Eventive Case may appear with pretty much any verb; it marks a noun that refers to a spatiotemporal event corresponding to the abstract proposition expressed by the verb.  
  
• The Situative Case marks nouns referring to a world or a volume of spacetime within which the proposition expressed by the verb is true. For it to apply, the event and the target spacetime area must be entirely encompassed by the referent of the marked noun.  
  
  
Non-core (adjunct) cases:  
```  
┌───────────────┬─────┬─────┐  
│ Topical       │  r  │     │  
│ Pendent       │  ƛ  │     │  
│ Instrumental  │  ƛʼ │ ıʼa │  
│ SP Locative   │  s  │ eı  │  
└───────────────┴─────┴─────┘  
```  
  
• The Topical Case marks the topic of the sentence. ⸨Note: it might become deprecated soon.⸩  
  
• The Pendent Case introduces a noun phrase without stating any relation between it and the current clause, and binds it to the Pendent pronoun (whose root form is ⟪-ƛá⟫ and whose extensional form is ⟪-ƛ◈-⟫, with ⟪◈⟫ representing an Inner Case vowel). This allows the introduced noun phrase (now bound to the pendent pronoun) to be used latter, possibly in a subordinate clause not yet opened. This is especially useful for expressing quantification binding a variable that is not used in the same clause as the one in which the quantifier appears, but rather in a more deeply nested clause:  
```  
┌───────────────  
│ ◆ Inıŋıwá ƛeyahakú koıtʼıƛucál. (= Inıŋıcál keyahakú.)  
│ ❖ ASR.SEN-want:ERG-has_property  
│   PND-UQZ-INTR-not-universal_property  
│   NOM-UTC-lambda_1:ERG-PND_PN:NOM-see  
│ ➥ Not everything is such that I want to see them.  
└─  
```  
  
• The Instrumental Case marks a noun referring to an instrument used by the referent of the most animate slot of the verb (e.g. the ⟪c-⟫ Case slot of binary predicates, the ⟪p-⟫ case slot of ternary predicates…) for achieving the action described by the current clause.  
  
• The Spatiotemporal Locative Case marks nouns referring to a volume of spacetime where the event described is taking place. For it to apply, the event and the target spacetime area must simply overlap, the event needs not be entirely encompassed by that area.  
  
  
Subordinator values (slot 2c):  
```  
┌──────────────────────────┬─────┐  
│ Relative clause          │ eo  │  
│ Plain content clause     │ ao  │  
│ Polarity clause          │ ea  │  
│ Unary template clause #1 │ oı  │  
│ Unary template clause #2 │ ██  │  
│ Binary Template Clause   │ oa  │  
│ Ternary Template Clause  │ ıʼı │  
│ Quaternary Template Cl.  │ uʼu │  
└──────────────────────────┴─────┘  
```  
  
These morphemes occupy the same slot as Inner Cases (slot 2c), but are not true Cases. They turn the words which bear them into ‘participles’, words that have the special syntactic effect of opening a whole subordinate clause (which may be exited for returning to the outer clause by using an appropriate Binding proclitic; see the section `§§§ Binding Slot`). The participle can assume any syntactic roles which normal contentives can assume via outer case inflection: a participle bearing a noun case will be a “noun participle”, with an adverbial case it will be an “adverbial participle”, and so on. Even if all these morphemes cause the opening of a subordinate clause, they differ in what kind of clause is created.  
In addition to occurring in slot 2c, Subordinators may also occur as extensional prefixes (introduced later in this document), with a glottal stop ⟪ʼ⟫ prefixed to their vocalic form (for example, ⟪-ʼao-⟫ for the plain content clause subordinator).  
  
Relative clauses are clauses that refer to one of the participants (called the ‘antecedant’) mentioned within the clause and represented by the ‘resumptive pronoun’ (whose root form is ⟪-tá⟫ and whose extensional form is ⟪-t◈-⟫); the relative clause describes its antecedent, and the whole relative clause's referent is the antecedent itself.  
  
Content clauses, on the other hand, do not involve any resumptive pronoun, and the referent of a content clause is the abstract proposition described by the clause.  
  
Template clauses are similar to content clauses but contain ‘blanks’, parts that have been abstracted away, similarly to blanks in a form, ready to be filled in. A template clause defines a predicate, and each ‘blank’ corresponds to one of the argument slots of the predicate.  
Each such blank or slot is represented by a so-called ‘lambda pronoun’ (named after lambda calculus).  
There is one vocalic morpheme for each predicate arity, and each arity has its own set of lambda pronouns. Additionally, there are two different morphemes for unary predicates, they only differ in having a different lambda pronoun.  
  
```  
┌─────────────────────────┬─────┬─────────────────────────────────┐  
│ Function                │ V   │ Lambda pronoun set              │  
├─────────────────────────┼─────┼──────────────────┬──────────────┤  
│ Unary Template Clause 1 │ oı  │ -tʼá             │ -tʼ◈-        │  
│ Unary Template Clause 2 │ ea  │ -ltʼá            │ -ltʼ◈-       │  
│ Binary Template Clause  │ oa  │ -cʼí, -kʼú       │ -cʼ◈-, -kʼ◈- │  
│ Ternary Template Clause │ ıʼı │ -pʼé, -čʼı̋, -qʼó └──────────────┤  
│ Quaternary Template Cl. │ uʼu │ -pʰáʼa, -cʰéʼe, -čʰı̋ʼï, -qʰóʼo  │  
└─────────────────────────┴─────┴─────────────────────────────────┘  
```  
  
The lambda pronouns are shown in their contentive root form, with equivalent extensional prefix forms in the right-hand square (with ⟪◈⟫ standing for an Inner Case vocalic affix); only the unary and binary templates have extensional prefix forms for their lambda pronouns, as they are the most frequent in usage.  
It is noteworthy that the consonant of the lambda pronouns is the same as that of corresponding outer case's consonantal morpheme, and the vowel is likewise the same as the vowel of the corresponding inner case.  
  
```  
  ┌───────────────  
  │ ◆ Aŋkıpθú koacʼıtʰú kaoθıkʼutwá.  
  │ ❖ ASR.INF-12-ERG-√differ  ACC-BTC-BL1-ERG-√find_likely  
  │   ACC-PCCS-you_know_what-ERG-BL2-√intend  
  │ ➥ We (me+you) differ in what we think he intends to do.  
  └─  
```  
  
⸨TODO: More usage example sentences.⸩  
  
  
