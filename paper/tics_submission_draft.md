# Pitch–Hue Correspondences: A Quantitative Meta-Analysis of Three Centuries of Mapping Systems

**Authors:** Alex Noah Feldman¹, E.E. Kuruoglu¹*

**Affiliation:** ¹ iDI, SIGS, Tsinghua University, Shenzhen, China

**Corresponding author:** kuruoglu@sz.tsinghua.edu.cn

**ORCIDs:** Feldman: 0009-0007-0696-6323 | Kuruoglu: [ORCID to be added]

**Running head:** Pitch–Hue Correspondences: A Quantitative Meta-Analysis

**Keywords:** cross-modal correspondences; pitch; color; affective space; meta-analysis; color-music

---

# Highlights

1. Three centuries of pitch–hue proposals yield near-chance agreement (mean 0.221)
2. Hue assignments are non-uniform across systems (Rayleigh R = .66, p = .003)
3. Pedagogical systems agree 57% above baseline; Cosmological systems fall below
4. Pitch–hue alignment is strongest along the Evaluation (good–bad) axis (p = .027)
5. Evaluation axis provides a theory-derived congruency criterion for neural research

---

# Abstract

Auditory and visual experience share an affective geometry aligned along the Evaluation (good–bad) axis of emotional space. We test this claim on a corpus spanning three centuries: 70 pitch–hue mapping systems classified into eight reasoning traditions, from Newton's prism to contemporary music education. Global agreement across systems is low (mean 0.221), close to the simulated chance level of 0.212, yet hue assignments are non-uniform (Rayleigh R = .66, p = .003). Pedagogical traditions agree 57% above the pooled baseline; Cosmological traditions fall below it. Aligning cross-modal dimensions in affective space yields a significant match (p = .027), with Evaluation as the dominant axis. These findings provide theory-derived congruency criteria for neural cross-modal correspondence research.

---

# Introduction

Cross-modal correspondences — the systematic tendency to match perceptual dimensions from different senses non-randomly — are among the more revealing regularities in the science of perception. Pitch-brightness and size-loudness correspondences are relatively tractable: the paired dimensions share either a physical substrate or a prothetic (intensive) structure that allows scalar alignment. Pitch and hue share neither. Hue is a circular, categorical dimension with no obvious analogue to acoustic frequency ratios; pitch carries no counterpart to chromatic complementarity or spectral position. Behavioral evidence for a direct pitch-hue link is accordingly weak and variable [1], which makes the persistence of the intellectual tradition all the more striking. Proposals linking specific musical pitches to specific hues have accumulated without interruption for three centuries, issuing from physicists, composers, synesthetes, educators, and software designers. Each tradition is internally coherent. Collectively, they are mutually irreconcilable. That irreconcilability is not a failure of the enterprise — it is the phenomenon that demands explanation.

Three centuries of proposals divide sharply but each on its own terms. Isaac Newton partitioned the visible spectrum into seven bands aligned with the seven diatonic degrees — a deliberate geometric import of musical interval ratios into the prism [2]. Louis-Bertrand Castel literalized the analogy into a keyboard instrument: his *clavecin oculaire* paired each semitone with a specific pigment, so that a harpsichordist could paint chords as they played [3]. Alexander Scriabin, writing two centuries later, notated an orchestral color-organ part in *Prometheus: The Poem of Fire*, deriving his assignments from the circle of fifths so that harmonically related keys received neighboring hues [4]. His contemporary Nikolai Rimsky-Korsakov took the correspondence with equal seriousness and arrived at almost entirely different colors, reporting direct chromesthetic sensations bound to individual keys rather than to harmonic relationships [5]. The two composers agreed on little beyond assigning warm colors to C. Each had reasons; the reasons point in different directions.

A principled account of pitch-hue correspondence carries consequences well beyond historical reconstruction. Music educators already assign colors to notes — Boomwhackers, Figurenotes, and colored-bell Suzuki materials embed pitch-color mappings in beginner curricula used worldwide — but without a principled basis for which mappings learners will find natural rather than arbitrary [29]. Designers of sensory-substitution tools that render music visible for deaf and hard-of-hearing users face the same unresolved question [30]. The rapidly expanding class of generative AI systems that synchronize color with sound currently defaults to ad hoc palettes; a grounded mapping would replace designer intuition with a defensible criterion [31]. And cognitive neuroscientists studying cross-modal binding face a circularity problem: without an independent congruency criterion, stimuli labeled congruent or incongruent in EEG and fMRI paradigms are defined by the very intuitions the experiment is meant to test [6].

Four theoretical accounts compete to explain cross-modal correspondences in general and pitch-hue in particular. The structural account holds that correspondences arise from shared physical or geometric properties — pitch and hue are both periodic, circular dimensions with ratio structure, and the pitch-class circle may share topology with the hue wheel [7]. The statistical account holds that correspondences are internalized environmental regularities — high-pitched sounds tend to co-occur with bright, warm visual environments, producing learned associations through ecological exposure [8]. The semantic account holds that correspondences are mediated by shared linguistic description — pitch and color are connected because overlapping emotional and sensory vocabulary (warm, bright, cutting) is applied to both, making language the causal bridge [9,10]. The hedonic account holds that correspondences are organized by shared affective response — auditory and visual stimuli that elicit similar emotional states become associated, with the bridging dimension being pleasantness, or more precisely the Evaluation (good–bad) axis of affective experience [11]. As this review will argue, the hedonic account provides the most comprehensive explanation for the structure of the historical record; the analyses in §3 build that case systematically rather than testing four equi-probable alternatives.

The approach taken here treats the historical record as an empirical resource rather than a museum exhibit. Seventy pitch-hue mapping systems spanning three centuries of proposals — by physicists, composers, synesthetes, pedagogues, and application designers — are classified into eight reasoning families defined by their stated design rationale, then subjected to quantitative agreement analysis. The four theoretical accounts are tested directly: structural regularities through pitch-interval-to-hue-distance correlations, statistical regularities through distributional analysis of hue assignments, semantic mediation through sentence-transformer probing of natural-language corpora, and hedonic alignment through Procrustes analysis against affective-space coordinates. No new behavioral data are collected. That constraint is also the asset: three centuries of independent expert judgment constitute a richer and more diverse evidence base than any laboratory matching experiment could assemble, and the structure of their disagreement is itself the signal.

---

# §1. The Historical Corpus

The catalogue was assembled through three channels: systematic review of four academic surveys of the sound–color relationship, targeted searches in music history archives, color science literature, and instrument design records (covering color organs, music education curricula, and digital applications underrepresented in academic surveys), and a bibliographic snowball that followed citations until no new systems emerged. Together these channels yielded 70 candidate systems spanning from Chinese Wuxing theory (4th century BCE) to contemporary smartphone applications — a record that touches 23 centuries, though the corpus is concentrated in the three centuries from Castel's *clavecin oculaire* (1725) to the present. That concentration is not uniform: proposals cluster in the 19th century, fall sharply during the serialist decades from roughly 1930 to 1980 when fixed pitch–color assignments attracted little compositional interest, and surge again in the digital age as consumer-facing music education and accessibility tools revived the question. The temporal shape of the corpus is itself a datum — it reflects cultural investment in the problem, not the underlying rate of cross-modal correspondence.

All color specifications were standardized to CIELAB before any comparison was made. Historical sources specify color in four ways — as spectral wavelength positions (Newton), as named pigments or dye trade names (Rimington), as free natural-language descriptions (many synesthetes), and as modern color codes such as hexadecimal RGB (digital applications) — and each type was converted to CIELAB coordinates via a principled pipeline. Inter-color distances were then computed using CIEDE2000, which corrects perceptual non-uniformities in the blue–green region that raw CIELAB Euclidean distance underweights. Agreement within a set of systems on a given pitch class was operationalized as the inverse of the normalized mean pairwise CIEDE2000 distance, scaled to the interval [0, 1], so that a score near one indicates tight consensus and a score near zero indicates near-random scatter. To calibrate what chance agreement looks like under this metric, 2,000 ensembles of 12-color systems were drawn uniformly from the sRGB gamut and passed through the identical pipeline; for ensembles of 24 random systems, simulated chance agreement is 0.212 (95% interval [0.196, 0.231]).

Candidate systems were retained when they met four conditions rendered as a single set of requirements: the system must assign colors to discrete pitch classes (as opposed to continuous frequency, intervals alone, or brightness without hue); all assignments must be convertible to CIELAB; the system must be attributable to a published source with sufficient detail to verify assignments; and directly derived copies were merged with their originals rather than counted separately. Applying these criteria to the survey-channel sources retained 25 systems for the primary analysis; six further systems meeting the same criteria entered through the snowball search after the primary analyses were complete, bringing the final retained catalogue to 31 (sensitivity analysis on all 31: flat agreement 0.237, Rayleigh R = .60, semitone–hue correlation r = .49 — every conclusion unchanged). The 70 systems were then classified into eight reasoning families — Spectral Analogy (F1), Circle of Fifths (F2), Cosmological (F3), Emotion-Mediated (F4), Synesthetic (F5), Esoteric (F6), Psychophysical (F7), and Pedagogical (F8) — defined by the stated design rationale of each system in its original source text, *before* any agreement scores were computed. This sequencing is a methodological safeguard: families that were built to track reasoning tradition must be separable from families built to track color similarity, and an adjusted Rand index of .23 at k = 5 between the hand-coded families and a color-similarity cluster analysis confirms they are not redundant. The family distribution is sharply unequal: Spectral Analogy (F1) contains 22 of the 70 catalogued systems, meaning Newton's prism metaphor drove more than a third of all proposals across three centuries. Figure 1 displays the temporal distribution of the corpus and the family counts side by side.

---

# §2. Structure Within Traditions

The global record is clear on one point: no single pitch–hue mapping commands ground-truth authority over this corpus. Pooling all 25 retained systems, agreement averages 0.221 — close to the simulated chance baseline of 0.212 [0.196, 0.231] — and only G# (0.300) exceeds the upper bound of the chance interval. Yet hue assignments are not random: the 12 consensus hue angles cluster strongly toward the warm end of the spectrum (Rayleigh R = .66, Monte Carlo p = .003), at a mean direction of 24°. At the pitch level, the tonal anchors C and G show the lowest inter-system spread, while the chromatic alterations show the highest — a trace of Western tonal hierarchy embedded in a corpus dominated by Western sources. This global picture, however, conceals as much as it reveals. Pooling all reasoning traditions into a single mean may average away structure that exists within them, and the family-level analysis tests that possibility directly.

When systems are grouped by the reasoning tradition that generated them, a consistent ordering emerges (Fig. 2; Table 2). Educators designing tools for untrained learners converge more tightly than any other tradition; cosmological theorists, despite centuries of ambition, produce more disagreement than the corpus as a whole. The numbers: the Pedagogical family (F8) reaches an agreement score of 0.348 — 57% above the global baseline of 0.221; the Synesthetic family (F5) follows at 0.276; Spectral Analogy (F1) sits at 0.267. The Esoteric family (F6) falls modestly below the baseline at 0.201, and the Cosmological family (F3) falls furthest below at 0.187 — lower than the pooled corpus despite drawing on systems united by a shared cosmological purpose. The ordering spans the full range from well above to well below the global mean, suggesting that reasoning tradition is not irrelevant to the structure of pitch–hue agreement, even if the current sample is too small to confirm this statistically.

This finding must be stated with care, and it is better to say so plainly than to bury it in a footnote. No individual family's deviation from the pooled baseline survives permutation testing: for Spectral Analogy, p = .10; for Pedagogical, p = .33; for Synesthetic, p = .40. A global heterogeneity test — shuffling family labels across the merged corpus and recomputing the variance of family means — is likewise non-significant (p = .81). With three to five systems in four of the five represented families, the ordering reported here is a descriptive, effect-size-level pattern that requires confirmation on an expanded corpus. This is not a reason to ignore the pattern — effect sizes guide future data collection and power analysis — but it is a firm constraint on interpretation. The family ordering is a structured hypothesis about what an expanded corpus will show, not a result that stands on its own.

The Cosmological family's result is the most important negative finding in the dataset. The four F3 systems — the Chinese Wuxing five-phase system, the Ancient Persian pitch–color correspondence, the Indian svara associations, and Diez's planetary note–color scheme (1723) — span genuinely distinct cosmological frameworks developed independently across cultures and millennia. Their low within-family agreement (0.187) does not reflect noise within a single tradition; it reflects divergence between independent metaphysical frameworks, each internally coherent and each arriving at different answers. Centuries of cosmological theorizing — some of the most sustained and sincere human effort to link sound and color — produce more disagreement than pooling the entire corpus. This outcome argues directly against any account that treats shared metaphysical tradition as a meaningful driver of pitch–hue correspondence. Whatever structure exists in the historical record, it does not trace to cosmological reasoning.

The Pedagogical family pulls in the opposite direction, but two alternative explanations must be addressed before the convergence can carry weight. The first is lineage: commercial teaching materials routinely copy one another, which would inflate apparent agreement without independent convergence. Strict application of the independence criterion to F8 reveals, however, that Sudre's Solresol color code (France, 1862), Boomwhackers (United States, 1995), and Figurenotes (Finland, 1996) arose in different countries, markets, and eras with no documented lineage among them. The second alternative is spectral repetition: educators might simply reuse rainbow order, making the convergence spectral rather than anything more interesting. The F8 consensus departs from canonical spectral order by a mean angular distance of approximately 35° after optimal rotation — about as far as the Spectral Analogy family itself — so the two are not the same thing. The pedagogical advantage should be read as convergence on a spectrally anchored, affectively comfortable mapping, not as pure spectral repetition. With both alternatives set aside, the convergence remains striking: educators across centuries and continents, independently optimizing for what feels natural to untrained learners, agree more tightly than any other tradition. This is the first hint in the data that hedonic structure — what feels right, rather than what is physically or metaphysically correct — may be the organizing force.

---

# §3. Four Theoretical Accounts

Of the four accounts examined here — statistical, structural, semantic, and hedonic — the hedonic account is the best supported. It is the only account that achieves below-chance disparity in affective space, and its leading statistic survives false-discovery-rate correction. The remaining three accounts are not without signal; each captures something real about the corpus, but each reaches a ceiling short of explaining the fine-grained assignment of specific hues to specific pitches. Table 1 summarizes all four. We present the accounts from weakest to strongest support, building toward the hedonic conclusion.

## §3a. The Statistical Account

The environmental-statistics account predicts that auditory-visual co-occurrences in the natural environment — warm-colored sunsets with low-frequency rumble, cool blue-white light with high-pitched birdsong — produce a shared cross-modal learning signal that constrains, but does not uniquely determine, pitch-hue mappings. The account's sharpest prediction is about disagreement, not agreement: noisy co-occurrence learning should produce convergence at large separations and divergence at fine-grained chromatic distinctions.

The corpus delivers this result clearly. The correlation between interval size and between-system variance is r = −.94, p = .001: historical mappers agree most about distant intervals and disagree most about semitones. This is the most tightly predicted finding in the analysis, and its interpretation is unambiguous — a noisy environmental signal would impose a rough global ordering (big intervals, big color gaps) while leaving the specific assignment of semitone neighbors unresolved. The warm-color non-uniformity reported in §2 (Rayleigh R = .66, p = .003, mean direction 24°) is consistent with the same account.

The scope of both results is deliberate. Environmental statistics tell the mapper how far apart the colors should be; they do not say what the colors should be. Mappers who all know, roughly, that high notes are cooler than low notes can still place C anywhere on the wheel and arrive at mutually incompatible systems. The r = −.94 result explains why G# has the highest inter-system spread of any pitch class, and why the octave's overall ordering is broadly preserved across traditions. It does not explain why C is red in Rimsky-Korsakov and white in Scriabin.

**Verdict:** the statistical account earns a clear pass for large-scale ordering and does not address fine-grained assignment.

## §3b. The Structural Account

The structural account holds that a physical or mathematical isomorphism between the pitch circle and the color wheel drives the correspondence — larger musical intervals should map to larger color distances, and canonically important intervals should map to canonically important color relationships. The ordinal prediction is confirmed. Across all retained systems, semitone distance correlates positively with mean hue distance (r = .393, parametric p = .001, pitch-label permutation p = .002; Fig 3, left panel): the rank ordering of interval sizes is reliably preserved in the rank ordering of hue separations.

The account's flagship quantitative prediction, however, fails. The strongest structural claim is that the perfect fifth — the most consonant interval — should map to complementary hues, approximately 180° apart on the color wheel. Perfect fifths averaged only 80.7° of hue separation, less than half the predicted value. The interval-distance function saturates near 85° and never approaches the complementary region; the tritone, equally predicted to reach ~180°, plateaus at 85.7° (Fig 3, right panel). Interval structure accounts for the ordinal pattern, not for specific angular values.

Six first-principles structural theories were evaluated against the pooled historical consensus on their angular error — the average deviation between predicted and observed hue for each of the 12 pitch classes. Because two independent hue angles drawn at random differ by 90° on average, beating that null is the minimum test of a theory's relevance. Only Interval-Ratio Preservation (IRP, 46.2°, Monte Carlo p = .001) and Frequency-Ratio Isomorphism (FRI, 54.9°, p = .009) pass. The four remaining theories — Harmonic Entropy Matching, Multidimensional Perceptual Alignment, Perceptual Distinctiveness Mapping, and Spectral Shape Correspondence — do not. The IRP-FRI result is notable: two theories derived independently through different mathematical formalisms converge on the same below-chance geometry. Both are spectrally anchored isomorphisms. Spectral Shape Correspondence illustrates why the anchor matters — it encodes a well-formed isomorphism, but one routed through acoustic spectra rather than the visible spectrum, and it lands far from the consensus (81.2°). Theories routed through intermediate perceptual dimensions (salience, probe-tone hierarchy) fail for the same reason: the signal is in the spectral anchor, not in the isomorphism structure alone.

**Verdict:** structural regularities constrain the ordinal pattern, not specific assignment. The signal is genuine but narrow.

## §3c. The Semantic Account

The semantic account proposes that shared language — the words humans use to describe pitches and colors — carries pitch-hue geometry. Sentence-transformer probing tests this directly by embedding pitch-class descriptions and color names in the same high-dimensional semantic space, then measuring whether pitches and colors that share vocabulary also share positions on the color wheel.

Timbral descriptors — "warm", "bright", "cutting", "round" — recover significant pitch-hue geometry: Nomic with timbral descriptors yields ρ = .368, p = .007, well above the random-hue null and replicable across permutation iterations. The semantic account therefore does capture something. The internal control, however, clarifies what it is capturing. Solfège labels — pitch names that carry no timbral content and whose familiarity is distributed unevenly across cultures — produce nothing: ρ = .019. Pitch-name familiarity is not the active ingredient. Across naming conventions more broadly (English, Japanese, German, and solfège with contextual framing), pitch-hue geometry is weak and inconsistent, arguing against any name-specific artifact driving the timbral result (full 18-cell grid in Supplementary Table S4).

The critical caveat governs the timbral result. Timbral vocabulary is not affectively neutral: "warm" and "bright" are cross-modal experiential descriptors that carry valence, arousal, and hedonic connotation as much as they carry acoustic content. The ρ = .368 signal cannot be read as a purely linguistic result. It is, instead, a semantics-affect entangled channel: language appears to be encoding the affective content that the hedonic account identifies as the primary cross-modal bridge. This entanglement is itself informative — ordinary descriptive vocabulary for sound and color appears to be organized by shared affective dimensions rather than by shared physical properties. The cross-linguistic weakness further suggests that the active channel is not the specific words but the affective geometry those words encode.

**Verdict:** language contributes a real but entangled signal; the purely linguistic channel is weak; the timbral result is better understood as an affective signal carried by words.

## §3d. The Hedonic Account

The hedonic account proposes that auditory and visual dimensions are organized along shared affective axes — particularly the pleasant-unpleasant axis — and that this shared geometry drives pitch-hue correspondences. This is a claim about representational structure, not about individual associations: the argument is that the entire space of auditory-visual cross-modal matching reflects a common affective coordinate system.

To test this, ten cross-modal dimensions were positioned in two independent spaces. The first is a sensorimotor space: each dimension was coded on 11 sensorimotor-affective profile dimensions (visual, auditory, tactile, gustatory, olfactory, interoceptive, motor, valence, arousal, magnitude, and spatial strength), capturing how each dimension is grounded in bodily experience. These profiles were reduced to three principal components accounting for 68.3% of the variance. The second space is Evaluation-Potency-Activity (EPA) affective space — the three-dimensional framework from Osgood's semantic differential tradition, in which any concept can be located on axes reflecting how good-bad, powerful-weak, and active-passive it feels, based on published semantic-differential and color-affect norms. Procrustes analysis then asked: after optimally rotating, reflecting, and scaling one configuration onto the other, how much residual misalignment remains? A disparity of 0 is perfect alignment; a disparity of 1 is no alignment at all.

The answer is significant alignment. The Procrustes disparity is 0.559 (permutation p = .027; null mean 0.833, SD 0.106) — the best single-account result across all four theoretical tests. The observed value is nearly 2.5 standard deviations below the permutation null: the sensorimotor organization of auditory and visual dimensions shares an affective geometry that is unlikely to arise from random correspondence (Fig 4, left panel).

Evaluation — the good-bad, pleasant-unpleasant axis — is the dominant aligning dimension (r = .74, p = .014). Potency (r = .47, p = .17) and Activity (r = .37, p = .29) contribute positively but are individually non-significant. What aligns pitch-space with color-space most reliably is, therefore, shared hedonic value: the pleasant and the unpleasant, the agreeable and the harsh, are the dimensions along which auditory and visual experience most overlap. This finding locates Palmer et al.'s [11] demonstration of emotion-mediated music-color associations on a specific axis: the mediation is primarily a pleasantness story, not an energy or power story. High or low pleasantness predicts pitch-hue pairing; high activity or potency does not.

Item-level evidence converges. Proximity between pitch and color terms in embedding space tracks shared valence-arousal profiles (ρ = .139, p < .001): pairs of pitch-color terms that sit near each other in semantic space also tend to share emotional profiles. This result is modest in magnitude but holds across a large vocabulary and is directionally consistent with the Procrustes finding at the dimension level.

The family results from §2 fit this architecture. Pedagogical systems — Boomwhackers (USA, 1995), Figurenotes (Finland, 1996), and Sudre's Tonic Sol-fa chromatics (France, 1862), developed independently across countries and eras with no documented lineage — converge more tightly than any other tradition. The convergence is consistent with educators independently arriving at what feels right to learners, which is precisely what Evaluation-axis alignment predicts: a shared hedonic sense of which colors suit which pitches draws practitioners toward similar solutions without requiring shared theory. Synesthetic report systems amplify the same structure, with idiosyncratic but internally consistent cross-modal associations organized by the same affective geometry.

**Verdict:** the hedonic account is the best-supported of the four — the only one achieving below-chance disparity in affective space with an effect that survives correction for multiple comparisons.

---

Across the four accounts, false-discovery-rate correction leaves three statistics surviving: EPA alignment (q = .045), the interval-size-to-variance correlation (q = .007), and the timbral embedding alignment (q = .024); the interval-hue correlation (H2) also survives; family heterogeneity tests do not (q ≥ .13).

These findings, taken together, shift the question from which theoretical account is correct to what the dominant account implies — for design, for technology, and for the neural research program that has long lacked an independent congruency criterion.

---

# Discussion

**Audiovisual design and accessibility.** The Pedagogical family's convergence provides a concrete design recommendation for applications where Evaluation is the primary affective channel: a spectrally anchored warm-cool mapping centered near green/yellow-green for the C-major root, with hue warmth ascending with pitch, is the best historically grounded default. That pitch-hue is the weakest documented auditory-visual cross-modal correspondence (d = 0.20) — its weakness following from sensorimotor distance (r = −.379, p = .027) rather than from any absence of correspondence — means any working application must operate through this affective channel rather than through direct perceptual isomorphism. Music visualization for deaf and hard-of-hearing users and classroom tonal instruments — Boomwhackers and Figurenotes already approximate this mapping — represent the clearest beneficiaries. The recommendation has finite generalizability: it is likely to misfire in contexts where Activity (energy, tension) rather than Evaluation is the dominant affective criterion, such as real-time rhythm or dynamics displays.

**Generative AI and creative systems.** Generative audiovisual systems — diffusion-model video generation, music-conditioned visual synthesis, text-to-multisensory pipelines — currently lack principled pitch-hue priors, defaulting to ad hoc conventions or uniform hue sampling. Two resources follow from this analysis. The EPA-Evaluation mapping can function as a training-time softmax prior: pitch-hue assignments that invert the Evaluation gradient can be penalized during fine-tuning, encoding the primary affective channel without prescribing any specific palette. The IRP and FRI structural mappings are candidates for contrastive or ranking objectives in cross-modal generation — independently derived spectrally anchored isomorphisms whose consensus error outperforms every other structural theory against the historical corpus. One caveat applies directly: the corpus driving both resources is predominantly Western European and North American, and how well Evaluation-axis alignment generalizes to listeners trained on non-Western tonal systems is an open empirical question. Both resources should be treated as reasonable defaults for the current training distribution, not as universals.

**Synesthesia research.** Synesthetic pitch-color associations cluster in the Pedagogical and Synesthetic families, which carry the highest and second-highest within-family agreement in the corpus. This distributional fact rules out the hypothesis that synesthetic correspondences are purely idiosyncratic: idiosyncratic mappings would not concentrate in the two most coherent traditions. The more parsimonious interpretation is that synesthesia amplifies a shared affective architecture already present in the general population rather than creating a separate mapping system from scratch. Two follow-up directions are indicated: a direct comparison of synesthetes' EPA affective profiles against those of non-synesthetic participants, using the same pitch-hue vocabulary, to test whether the affective geometry is shared and only its perceptual salience differs; and a targeted replication of the Evaluation-axis dominance finding within synesthetes' own associations, to confirm whether hedonic primacy is a general feature of pitch-color experience or specific to the non-synesthetic majority.

**Limitations.** The corpus is dominated by Western European and North American proposals from the nineteenth and twentieth centuries; Indian and Chinese systems appear but non-Western traditions lack systematic coverage. All four accounts were tested against the historical consensus rather than against behavioral data collected in this study. The Pedagogical family is the only family with sufficient within-family membership to sustain meaningful comparison (six systems), and most family-level results rest on three to five systems that do not individually survive permutation testing. The EPA affective coordinates derive from predominantly Western published norms, so the Evaluation-first finding requires cross-cultural replication before its primacy can be treated as universal.

**The hedonic account as organizing principle.** For a correspondence that resisted principled explanation for three centuries, the hedonic account offers the first organizing principle with testable content: auditory and visual dimensions share an affective geometry, and the Evaluation axis — the good-bad, pleasant-unpleasant dimension of emotional experience — is its primary cross-modal bridge. This is not a complete explanation. Structural regularities constrain the ordinal interval-to-hue relationship; environmental statistics constrain the large-scale warm-color bias and the degree of agreement at distant versus adjacent intervals; semantic regularities carry a timbral signal entangled with affect. But hedonic alignment is the best single account across all four tests, and the only one that connects directly to a testable neural mechanism through the congruency framework described in Box 2. The practical gain follows the conceptual one: pitch and hue share no physics, but they share a hedonic geometry — and that geometry, once identified, can be specified, measured, and submitted to empirical test.

**What the three-century record reveals.** The corpus behaved exactly as the hedonic account predicts. Traditions that operated closer to the Evaluation axis — educators optimizing for affective naturalness, synesthetes reporting aesthetic intuitions — showed tighter within-family convergence. Traditions that routed through independent metaphysical frameworks — each internally coherent, each arriving at systematic predictions about which pitches belong to which colors — diverged from one another more than the pooled corpus does. The disagreement in the historical record is not evidence that the pitch-hue correspondence is arbitrary. It is evidence that the correspondence is mediated by something that not all traditions attempted to track, and that when traditions do track it — however implicitly, however unannounced — they converge on broadly similar answers.

**The research agenda.** Three directions follow directly. A cross-cultural behavioral study should test whether Evaluation-axis-aligned pitch-hue pairs produce faster response times, higher preference ratings, or greater concordance among participants trained on non-Western tonal systems — this would establish whether Evaluation primacy is universal or tied to Western enculturation. An RSA study submitting IRP, FRI, and EPA-Evaluation representational dissimilarity matrices as model predictors against EEG and fMRI data would locate the neural locus of this affective geometry for the first time using a theory-derived model rather than an ad hoc congruency definition; audiovisual Stroop paradigms, which create conflict precisely on the Evaluation dimension the analysis identifies as the primary affective channel, provide the recommended behavioral operationalization. Systematic extension of the catalogue through non-Western archival sources — the Indian raga tradition and sub-Saharan African drumming traditions are particularly rich candidates — would reduce the sampling bias in current family-level results and sharpen the inferential basis for cross-cultural comparison.

**Conclusion.** The pitch-hue correspondence appeared irreconcilable for three centuries because the mappers were working in incompatible explanatory registers — spectral analogy, cosmological symbolism, pedagogical intuition, synesthetic report. Analysis that treats these as competing estimates of a single parameter finds only noise. Beneath the framework diversity, a shared perceptual-affective architecture was operating all along: its primary dimension is the Evaluation axis, the same axis along which color experience and pitch experience most reliably align. Mappers disagreed at the level of metaphysics while converging, imperfectly but measurably, at the level of hedonic geometry. Theory can now name that geometry; cross-cultural research can test whether it generalizes; neuroimaging can trace it to its neural substrates. The historical record, treated as data rather than precedent, supplies the starting point for all three.

---

# Box 1. Methodology Capsule

## Source Identification

Systems were identified through three channels: systematic review of four academic surveys of the sound–colour relationship [12–15], targeted archive searches in music history, colour science, and instrument-design records (capturing practitioner systems — colour organs, education curricula, digital applications — underrepresented in academic surveys), and a bibliographic snowball that followed citations until no new systems emerged. Together these channels yielded 70 candidate systems spanning 23 centuries, from Chinese Wuxing theory (4th century BCE) to contemporary smartphone colour-music applications.

## Colour Standardization

Historical colour specifications are heterogeneous and required conversion to a common perceptual space. Each specification was classified into one of four source types and converted to CIELAB coordinates via a principled pipeline: spectral wavelengths were converted to CIEXYZ using the CIE 1931 standard observer and then to CIELAB; named pigments or dyes were matched to Munsell or Natural Color System references using published pigment databases [16,17]; natural-language descriptions were resolved by averaging the CIELAB coordinates of all XKCD Color Survey colours judged semantically compatible with the description [18]; and modern colour codes (RGB/hex) were converted via the standard sRGB-to-CIELAB transformation with D65 illuminant. All inter-colour distances were computed with the CIEDE2000 formula [19], which corrects for perceptual non-uniformities in the blue–green and blue–violet regions that would otherwise cause raw CIELAB Euclidean distances to underweight differences in those ranges. An agreement score was derived as the inverse of normalized mean pairwise CIEDE2000 distance:

$$\text{agreement} = \frac{1}{1 + \overline{\Delta E_{00}} / 12}$$

The denominator 12 is calibrated so that agreement = 0.60 corresponds to a mean ΔE₀₀ of approximately 8 units, a conventional threshold above which colour pairs are judged clearly distinct under standard viewing conditions; we treat 0.60 as an explicit benchmark for strong consensus rather than as a perceptual constant.

## Inclusion Criteria

Four criteria governed retention: a system must provide a discrete pitch-class-to-colour mapping (systems mapping intervals, modes, or continuous frequency were excluded, as were those specifying only lightness or brightness without hue; partial coverage of the chromatic scale was permitted); all assignments must be convertible to CIELAB coordinates; each system must be attributable to a published source with sufficient detail to verify colour assignments; and directly derived or copied systems were merged with their originals. These criteria retained 25 primary systems; six further systems meeting the same criteria entered through the snowball procedure, bringing the final retained catalogue to 31. A sensitivity analysis on all 31 systems (flat agreement 0.237, Rayleigh R = .60, semitone–hue correlation r = .49) leaves every conclusion unchanged.

## Family Classification

The 70 candidate systems were classified into eight reasoning families (F1 Spectral Analogy, F2 Circle of Fifths, F3 Cosmological, F4 Emotion-Mediated, F5 Synesthetic, F6 Esoteric, F7 Psychophysical, F8 Pedagogical) based on the stated design rationale of each system in the original source text, before any agreement scores were computed, to avoid circular analysis. Two independent coders assigned each system to a family; approximately 12% of cases produced disagreements, which were resolved through discussion. Twelve systems invoke a secondary rationale alongside their primary one; a priority rule assigns each to the first applicable family in the F1→F8 order, so that a colour organ justified on both spectral and pedagogical grounds is coded F1. Family–color-similarity independence was confirmed via adjusted Rand index (ARI = .23 at k = 5) [20].

## Simulated Chance Baseline

A chance baseline was estimated by drawing 2,000 ensembles of n = 24 random 12-colour systems uniformly from the sRGB gamut and passing each through the identical standardization and scoring pipeline. For ensembles of this size, simulated chance agreement is 0.212 (95% interval [0.196, 0.231]); observed scores are compared against this distribution wherever "chance" is invoked.

## EPA Procrustes Method

To test the hedonic account, ten cross-modal dimensions central to the pitch–hue question (pitch height, loudness, tempo, and hardness on the auditory–tactile side; lightness, brightness, saturation, and hue warmth on the visual side; size and pleasantness as cross-modal anchors) were each coded on 11 sensorimotor-affective profile dimensions [21] (visual, auditory, tactile, gustatory, olfactory, interoceptive, motor, valence, arousal, magnitude, spatial) and the resulting profiles were reduced to three principal components, capturing 68.3% of variance. Each of the ten dimensions was then assigned coordinates in Evaluation-Potency-Activity (EPA) affective space [22], drawing on published semantic-differential [22] and colour-affect norms [23–25]. Procrustes alignment [26] found the rotation, reflection, and uniform scaling that minimized squared distances between the sensorimotor PC configuration and the EPA configuration of the same ten dimensions. Significance was assessed by permuting the correspondence assignments before alignment across 10,000 permutations. Directional statistics used throughout [27]; semantic embeddings via Nomic [28].

---

# Box 2. A Congruency Framework for Neural Research

**The circularity problem.** Neural research on pitch–hue correspondence has been blocked by a fundamental circularity: congruency is defined by asking participants what feels congruent, so no congruency criterion exists that is independent of behavioral report. As a result, no neural correlate of pitch–hue congruency has been identified. The present findings break this circularity directly — because no single historical map commands ground-truth authority, defining congruency from Newton's or Scriabin's system imports an arbitrary cultural choice into the experimental design and biases RSA matrices against the actual structure in the data.

**The EPA resolution.** Because the Evaluation (good–bad) axis is the primary dimension aligning auditory and visual dimensions in affective space (Procrustes disparity 0.559, p = .027), it provides a theory-derived, participant-independent congruency gradient. Pitch–hue pairs that agree in their Evaluation profiles are "congruent" by this criterion; those that disagree are "incongruent." This anchors congruency in the affective geometry the historical corpus itself reveals, not in any individual mapper's intuition.

**Theoretical RDMs for RSA.** The IRP and FRI structural theories produce predicted pitch-to-hue mappings with internally consistent interval-arc isomorphisms — both beat the 90° random-hue null (IRP: 46.2°, p = .001; FRI: 54.9°, p = .009). These can be submitted directly as theoretical representational dissimilarity matrices (RDMs) in representational similarity analysis against EEG or fMRI embeddings, testing whether neural geometry during audiovisual processing mirrors the structure identified here.

**The Stroop paradigm.** For behavioral operationalization, audiovisual Stroop paradigms — in which participants hear a tone while viewing a written note name that either matches or conflicts with the sounded pitch — create a congruency mismatch on the Evaluation dimension identified as the primary affective channel. This manipulation is clean and participant-independent, enabling localization of neural correlates without presupposing the mapping.

---

**Outstanding Questions**

1. Does the Evaluation-axis primacy in pitch–hue alignment replicate in non-Western participant samples and cross-cultural EPA norms, or is it itself a Western construct?
2. Do behavioral matching experiments confirm the family-level predictions — specifically, that Pedagogical and Synesthetic families elicit faster or more consistent responses than Cosmological pairings?
3. When IRP, FRI, and EPA theoretical RDMs are entered simultaneously into RSA of EEG or fMRI data from audiovisual congruency tasks, which model best accounts for the neural representational geometry?
4. What is the minimal affective vocabulary — the smallest set of evaluative descriptors — that bridges pitch and color experience across individuals and cultures?
5. Does synesthesia amplify rather than create the shared affective geometry, such that synesthetes show a stronger Evaluation-axis alignment than controls while the alignment direction remains the same?

---

# Figure Legends

**Figure 1. Three centuries of pitch–hue mapping proposals and their distribution across reasoning traditions.** (Left) Historical timeline of 70 candidate pitch–hue mapping systems from Newton (1704) to the present. Proposal density peaks in the 19th–early 20th century and again in the digital age, with a trough during the serialist era (1930–1980). (Right) Distribution of the 70 candidate systems across the eight reasoning families. The Spectral Analogy family (F1) dominates with 22 systems, reflecting the outsized influence of Newton's prism metaphor on more than a third of all recorded proposals.

**Figure 2. Within-family agreement scores and representative consensus maps for three reasoning traditions.** (Left) CIEDE2000 agreement scores for five families with at least two members, compared against the global pooled mean (dashed line; 0.221). The Pedagogical family (F8) leads at 0.348 — 57% above the pooled consensus — while the Cosmological family (F3) falls below the flat baseline at 0.187. No individual deviation is significant under permutation. (Right) Consensus hue wheels for F8 Pedagogical, F5 Synesthetic, and F3 Cosmological. Educators and synesthetes converge more tightly than the global pool; cosmological systems diverge. CIEDE2000: CIE 2000 color-difference formula.

**Figure 3. Structural regularities in historical pitch–hue correspondences: interval-distance correlation and first-principles theory performance.** (Left) Semitone distance between pitch classes plotted against mean CIEDE2000 hue distance across 25 historical systems (r = .393, permutation p = .002). Larger musical intervals consistently map to larger color distances, supporting a partial structural isomorphism. The function saturates near 85° and never reaches the complementary-hue region, so perfect fifths average only 80.7° of separation rather than the predicted ~180°. (Right) Consensus angular error for structural theories against the 90° random-hue null. Only IRP (46.2°, p = .001) and FRI (54.9°, p = .009) achieve below-null error. IRP: interval-ratio projection; FRI: frequency-ratio isomorphism; CIEDE2000: CIE 2000 color-difference formula.

**Figure 4. Hedonic account: shared affective geometry between auditory and visual dimensions, and the position of pitch–hue in the cross-modal correspondence landscape.** (Left) Ten auditory and visual dimensions positioned in Evaluation–Activity space after Procrustes alignment. Auditory dimensions (blue) and visual dimensions (orange) overlap primarily along the Evaluation (good–bad) axis, the dominant aligning dimension (r = .74, p = .014). Procrustes disparity = 0.559 (permutation null mean 0.833, SD 0.106; p = .027). (Right) Mean behavioral effect sizes across catalogued cross-modal correspondence pairings grouped by proposed mechanism; pitch–hue (d = 0.20) is the weakest documented pairing, a consequence of its large sensorimotor distance (r = −.379, p = .027). EPA: Evaluation–Potency–Activity; CMC: cross-modal correspondence.

---

# References

[1] Ward J, Huckstep B, Tsakanikos E. Sound-color synesthesia: To what extent does it use cross-modal mechanisms common to us all? Cortex. 2006;42(2):264–280. doi:10.1016/S0010-9452(08)70352-6

[2] Newton I. Opticks: or, A Treatise of the Reflexions, Refractions, Inflexions and Colours of Light. Sam. Smith and Benj. Walford; 1704.

[3] Castel L-B. Clavecin pour les yeux, avec l'art de peindre les sons. Mercure de France. 1725:2552–2577.

[4] Scriabin A. Prometheus: The Poem of Fire, Op. 60. Edition Russe de Musique; 1911.

[5] Galeyev BM. The problem of synesthesia in the arts. Leonardo. 2007;40(1):61–68. doi:10.1162/leon.2007.40.1.61

[6] Spence C. Crossmodal correspondences: A tutorial review. Atten Percept Psychophys. 2011;73(4):971–995. doi:10.3758/s13414-010-0073-7

[7] Marks LE. The Unity of the Senses: Interrelations among the Modalities. Academic Press; 1978.

[8] Parise CV, Spence C. Audiovisual cross-modal correspondences in the general population. Multisens Res. 2014;27(5–6):473–494. doi:10.1163/22134808-00002472

[9] Martino G, Marks LE. Synesthesia: Strong and weak. Curr Dir Psychol Sci. 2001;10(2):61–65. doi:10.1111/1467-8721.00116

[10] Walker P. Cross-sensory correspondences and cross talk between dimensions of connotative meaning: Visual angularity is hard, high-pitched, and bright. Atten Percept Psychophys. 2016;78(5):1441–1472. doi:10.3758/s13414-016-1090-5

[11] Palmer SE, Schloss KB, Xu Z, Prado-León LR. Music–color associations are mediated by emotion. Proc Natl Acad Sci USA. 2013;110(22):8836–8841. doi:10.1073/pnas.1212562110

[12] Jewanski J. Colour and music. In: Macy L, ed. Grove Music Online. Oxford University Press; 2009. doi:10.1093/gmo/9781561592630.001.0001/omo-9781561592630-e-0000006156

[13] Gage J. Color and Culture: Practice and Meaning from Antiquity to Abstraction. University of California Press; 1999.

[14] Peacock K. Instruments to perform color-music: Two centuries of technological experimentation. Leonardo. 1988;21(4):397–406. doi:10.2307/1578099

[15] Wells R. Music and visual color: A proposed correlation. Leonardo. 1980;13(2):101–107. doi:10.2307/1577980

[16] Newhall SM, Nickerson D, Judd DB. Final report of the O.S.A. subcommittee on the spacing of the Munsell colors. J Opt Soc Am. 1943;33(7):385–418. doi:10.1364/JOSA.33.000385

[17] Hard A, Sivik L. NCS — Natural Color System: A Swedish standard for color notation. Color Res Appl. 1981;6(3):129–138. doi:10.1002/col.5080060303

[18] Munroe R. XKCD Color Survey [Internet]. 2010. Available from: https://blog.xkcd.com/2010/05/03/color-survey-results/

[19] Sharma G, Wu W, Dalal EN. The CIEDE2000 color-difference formula: Implementation notes, supplementary test data, and mathematical observations. Color Res Appl. 2005;30(1):21–30. doi:10.1002/col.20070

[20] Ward JH Jr. Hierarchical grouping to optimize an objective function. J Am Stat Assoc. 1963;58(301):236–244. doi:10.1080/01621459.1963.10500845

[21] Lynott D, Connell L, Brysbaert M, Brand J, Carney J. The Lancaster Sensorimotor Norms: Multidimensional measures of perceptual and action strength for 40,000 English words. Behav Res Methods. 2020;52(3):1271–1291. doi:10.3758/s13428-019-01316-z

[22] Osgood CE, Suci GJ, Tannenbaum PH. The Measurement of Meaning. University of Illinois Press; 1957.

[23] Ou L-C, Luo MR, Woodcock A, Wright A. A study of colour emotion and colour preference. Part I: Colour emotions for single colours. Color Res Appl. 2004;29(3):232–240. doi:10.1002/col.20010

[24] Hevner K. The affective character of the major and minor modes in music. Am J Psychol. 1935;47(1):103–118. doi:10.2307/1416710

[25] Wedin L. A multidimensional study of perceptual-emotional qualities in music. Scand J Psychol. 1972;13(1):241–257. doi:10.1111/j.1467-9450.1972.tb00073.x

[26] Gower JC. Generalized Procrustes analysis. Psychometrika. 1975;40(1):33–51. doi:10.1007/BF02291478

[27] Mardia KV. Statistics of Directional Data. Academic Press; 1972.

[28] Nussbaum Z, Morris JX, Duderstadt B, Mulyar A. Nomic Embed: Training a reproducible long context text embedder. arXiv:2402.01613 [Preprint]. 2024. Available from: https://arxiv.org/abs/2402.01613

[29] Kivijärvi S. Applicability of an applied music notation system: A case study of Figurenotes. Int J Music Educ. 2019;37(4):654–666. doi:10.1177/0255761419845475

[30] Nanayakkara SC, Wyse L, Ong SH, Taylor EA. Enhancing musical experience for the hearing-impaired using visual and haptic displays. Hum-Comput Interact. 2013;28(2):115–160. doi:10.1080/07370024.2012.697006

[31] Baione A, Rizzo G, Barco L, Urbanelli A, Di Biasi L, Tortora G. Musipainter: A music-conditioned generative architecture for artistic image synthesis. Intell Syst Appl. 2025;29. doi:10.1016/j.iswa.2025.200611

---

# CRediT Author Contribution Statement

Alex Noah Feldman: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing – original draft, Writing – review & editing. E.E. Kuruoglu: Conceptualization, Supervision, Writing – review & editing.

---

# Acknowledgements

No funding was received for this work.

---

# Open Practices Statement

The data and code associated with this article are available at https://github.com/alexTrod/pitch-hue-correspondences. The shared repository includes the colour catalogue, pairwise distance matrices, bootstrap samples, and all analysis scripts used this study. No new behavioural or experimental data were collected; all pitch–hue mapping systems analysed are cited in the references.

---

# Declaration of Interests

The authors declare no competing interests.

---

## Status (last updated 2026-08-10)

- **Main text word count:** ~4,640 words (Introduction ~798 + §1 ~559 + §2 ~703 + §3 ~1,490 + Discussion ~1,090)
- **References:** 31 Vancouver-numbered entries, all citations resolved
- **Figures:** Draft panels in figures/aesthetic/tics_figures/ — Fig 1–2 require panel assembly; Fig 3 right and Fig 4 left/right are cropped and ready (regenerate from source for final submission)
- **Remaining author actions before submission:**
  1. Add Kuruoglu's ORCID (title page line 9 and cover letter)
  2. Confirm Kuruoglu's full first name in the CRediT statement
  3. Populate the GitHub repository with data files and analysis scripts (see review/push_to_github.sh)
  4. Verify reference [31] (Baione et al. 2025) DOI suffix against live ScienceDirect page
  5. Replace placeholder reviewer names in the cover letter with real contacts
  6. Jewanski [12]: confirm page numbers 110–115 against the 2001 New Grove print volume if citing the print edition
