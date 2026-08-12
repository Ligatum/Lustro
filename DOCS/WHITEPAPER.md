**A chemist by education. A systems observer and explorer by obsession.**

**Lustro — Observed system behaviour. By Ligatum.**

***

What is Lustro V1?

***

# **1. Executive Summary**

\* Lustro V1 is a deterministic, dynamic diffusion engine designed for rapid state-wide information propagation. It replaces layered transformation pipelines with an autonomous state-evolution mechanism. The engine was developed as an experimental architecture intended to explore whether dynamic, state-dependent permutation geometry can produce distinct emergent characteristics compared to traditional fixed-stage designs. Currently, it is evaluated as a core mechanism for primitives such as hash functions, pseudo-random number generators (PRNG), and extendable-output functions (XOF). The API implementation and benchmark test suites are provided within the accompanying project repository. Community feedback is highly appreciated.

\* Aggregate throughput speed characteristics for scalar version:\
6 physical cores - Hash/PRNG/XOF up to ~ 10 GB/s\
12 logical cores - Hash/PRNG/XOF up to ~ 13 GB/s\
Tests were performed on an Intel Core i5-11600K @ 4.5 GHz (constant frequency). Thread scaling exceeds 90% for large batches. Native AVX2 support is being finalized for the premium edition.

\* Limitations of interpretation: All of the findings in this document are empirical and describe observed system properties. These findings do not constitute a formal mathematical proof of cryptographic security, perfect randomness or ergodicity. Questions regarding short and long-term state evolution and alternative interpretations remain open.

# **2. The Mechanism, IDM and ERD**

\* Lustro V1 engine is built around an intentional separation of responsibilities between two complementary mechanisms: Initial Diffusion Module (IDM) and Evolving Representation Dynamics (ERD).

\* State Architecture: During the initial mixing phase (IDM), the state is mapped into four parallel 64-bit lanes to exploit Instruction-Level Parallelism (ILP) on modern architectures. Within ERD the state is processed as two 128-bit words.

\* Initial Diffusion Module (IDM): A state-wide mixing layer combining addition, rotation, XOR, and multiplicative diffusion. It utilizes short dependency chain and high ILP for optimal execution time.

\* Evolving Representation Dynamics (ERD): It is a state-driven evolutionary control mechanism that compresses its own state representation into two interacting feedback channels. These channels generate dynamic rotation keys. Within Lustro V1 the resulting closed feedback loop produces state-dependent rotation values that drive the two final 128-bit state permutations.

\* Architectural Rationale: While the ERD is capable of acting as a standalone state-evolution mechanism, the IDM catalyses an efficient initial diffusion stage. Separating these responsibilities improves overall efficiency.

\* The rotation-based output described here reflects Lustro V1 implementation. The underlying ERD control mechanism is not inherently limited to rotation values and may be adapted to derive other classes of control parameters in future iterations.

# **3. Empirical Observations**

\* Mechanism Behaviour: Lustro does not seem to behave like a traditional layered transformation pipeline. Observations suggest that it can be interpreted as a dynamic 'state-flow' controlled system. During its development the engine underwent industry standard tests (BigCrush, PractRand, Smhasher3, NIST SP 800-22) alongside a battery of custom-made tests. Primary aim was to evaluate raw dynamics of Lustro Core, without relying on any additional transformation layer. The complete test suites are available within the repository.

\* Dynamic Rotation Behaviour: Rotations within Lustro V1 do not act as fixed parameters. Instead, rotation values emerge directly from the evolving state, continuously altering the permutation geometry and reducing the persistence of observable structural patterns.

\* Homogeneous Diffusion and Structural Cohesion: Information propagation across the whole 256-bit state remains highly uniform. Empirical data showed no evidence of isolated mixing domains or independent lanes. The engine exhibited statistically uniform behaviour across all tested categories. Extended space and trajectory analyses showed no evidence of progressive state-space concentration, orbit convergence, or abnormal recurrence behaviour. Additionally, repeating analyses under various observation parameters produced consistent results. Aggregate statistical testing on raw engine state occasionally reveals weak deviations. No evidence currently links these effects to a localized bias or a structural weakness. They may instead reflect underlying engine dynamics or test-specific conditions.

\* Local, Linear, Rotational and Differential Tests: Across a series of varied experiments no input was able to establish a persistent pattern. Lustro's state-dependent rotation network continuously morphs the permutation space and was observed to prevent the emergence of stable trajectories.

\* Spectral and Algebraic Uniformity: Affine, quadratic, and frequency-domain evaluations show an absence of invariant subspaces or dominant propagation modes. The system exhibited no dominant geometric orientation and no tested representation exposed a clearly visible underlying structure.

# **4. Open Questions and future evaluation**

\* Short and long-term state evolution in alternative representations remains an open question.

\* External evaluation of resistance to advanced cryptanalytic methods is openly welcome.

------------------------------------------------------------------------

Summary: Based on current empirical observations - Lustro operates as a highly coupled 256-bit architecture governed by non-linear state-evolution mechanics. The combination of rapid state-wide diffusion, state-dependent permutations and the absence of observable privileged structures is driven by the ERD mechanism, with IDM performing efficient initial diffusion. In this architecture, the ERD mechanism effectively functions as a dynamic state orchestrator.
