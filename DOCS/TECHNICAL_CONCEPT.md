
**A chemist by education. A systems observer and explorer by obsession.**

**Lustro — Observed system behaviour. By Ligatum.**

---

## 1. Executive Summary

- Lustro V1 is a deterministic, dynamic diffusion engine designed for rapid information propagation across the full 256-bit state. It departs from conventional layered transformation pipelines by using a state-dependent evolution mechanism. The engine was developed as an experimental architecture to evaluate whether dynamic, state-dependent permutation geometry produces observable properties distinct from fixed-stage constructions. The current implementation is intended for evaluation as a core mechanism for primitives such as hash functions, pseudo-random number generators (PRNGs), and extendable-output functions (XOF). The API implementation and benchmark test suites are provided within the accompanying project repository. Community feedback is highly appreciated.

- Aggregate throughput for the scalar implementation:

  | Cores | Throughput (Hash/PRNG/XOF) |
  |---|---|
  | 6 physical cores | up to ~10 GB/s |
  | 12 logical cores | up to ~13 GB/s |

  Tests were performed on an Intel Core i5-11600K @ 4.5 GHz (constant frequency). Parallel scaling exceeds 90% for large batches.

- **Limitations of interpretation:** All of the findings in this document are empirical and describe observed system properties. These findings do not constitute a formal mathematical proof of cryptographic security. Questions regarding short and long-term state evolution and alternative interpretations remain open.

---

## 2. The Mechanism, IDM and ERD

- Lustro V1 engine is built around an intentional separation of responsibilities between two complementary mechanisms: **Initial Diffusion Module (IDM)** and **Evolving Representation Dynamics (ERD)**.

- **State Architecture:** During the initial mixing phase (IDM), the state is mapped into four parallel 64-bit lanes to exploit instruction-level parallelism (ILP) on modern architectures. Within ERD the state is processed as two 128-bit words.

- **Initial Diffusion Module (IDM):** A state-wide mixing layer combining addition, rotation, XOR, and multiplicative diffusion. It utilizes short dependency chains and high ILP to reduce execution latency.

- **Evolving Representation Dynamics (ERD):** It is a state-driven evolutionary control mechanism that compresses its own state representation into two interacting feedback channels. These channels generate state-dependent rotation values. In Lustro V1, the resulting closed feedback loop drives the two final 128-bit state permutations.

- **Architectural Rationale:** While the ERD is capable of acting as a standalone state-evolution mechanism, the IDM provides an efficient initial diffusion stage. Separating these responsibilities improves overall efficiency.

- The rotation-based output described here reflects Lustro V1 implementation. The underlying ERD control mechanism is not inherently limited to rotation values and may be adapted to derive other classes of control parameters in future iterations.

---

## 3. Empirical Observations

- **Mechanism Behaviour:** Lustro does not seem to behave like a traditional layered transformation pipeline. Observations suggest that it can be interpreted as a dynamic 'state-flow' controlled system. During its development the engine underwent industry-standard tests (BigCrush, PractRand, Smhasher3, NIST SP 800-22) alongside a series of custom-made tests. The primary aim was to evaluate Lustro Core dynamics without relying on an additional transformation layer. The test suites and results are available within the repository.

- **Dynamic Rotation Behaviour:** Rotations within Lustro V1 do not act as fixed parameters. Instead, rotation values emerge directly from the evolving state, continuously altering the permutation geometry and reducing the persistence of observable structural patterns.

- **Diffusion and Structural Behaviour:** Measured diffusion was broadly uniform across the 256-bit state. Empirical data showed no evidence of isolated mixing domains or independent lanes. No statistically significant deviations were detected in the evaluated categories. Extended state-space and trajectory analyses showed no measurable evidence of progressive state-space concentration, orbit convergence, or persistent recurrence patterns. Additionally, repeating analyses under various observation parameters produced consistent results. Aggregate statistical testing of the raw engine state occasionally reveals weak deviations. No evidence currently links these deviations to a localized bias or structural weakness. They may instead reflect underlying engine dynamics or test-specific conditions.

- **Local, Rotational and Differential Tests:** Across a series of varied experiments no tested input difference produced a persistent observable pattern. Lustro's state-dependent rotation mechanism changes the effective permutation structure as the state evolves. No stable trajectories were observed under the tested conditions.

- **Spectral and Algebraic Structure:** Affine, quadratic, and frequency-domain evaluations did not reveal invariant subspaces under tested projections. The tested representations exhibited no dominant geometric orientation and none of the representations revealed a persistent structural feature.

---

## 4. Open Questions and Future Evaluation

- Short and long-term state evolution in alternative representations remains an open question.

- External evaluation of resistance to advanced cryptanalytic methods is openly welcome.

---
