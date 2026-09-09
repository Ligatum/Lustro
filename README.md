## **Lustro V1 Project Description**

Lustro V1 is a deterministic, single-pass diffusion engine where transformation parameters are derived dynamically from the evolving state itself. Implemented in Rust, the engine provides a unified API with streaming capabilities, built-in batching, and automatic parallel stream dispatch.

The architecture is currently evaluated as a core mechanism for primitives, including hash functions, pseudo-random number generators (PRNG), and extendable-output functions (XOF). Multi-threaded aggregate throughput for the scalar implementation reaches over 13 GB/s using batch processing (tested on Intel i5-11600K, 12t @ 4.5 GHz).

The API, technical documentation, test implementations, empirical evaluation, and design philosophy are provided across the Lustro repositories.

All observations presented in this repository are empirical and describe the system's observed behavior. They are not intended as a formal proof of cryptographic security.

## Links

* **API Layer & Bindings:** [Lustro_API Repository](https://github.com/Ligatum/Lustro_API)
* **Standalone Reference Core:** [Lustro_Audit Repository](https://github.com/Ligatum/Lustro_Audit)

---

**<p align="center">Comparative overview of Lustro tree batching capabilities.</p>**

<img width="1814" height="1087" alt="lustro_comparison" src="https://github.com/user-attachments/assets/d523895d-e50e-4db7-9a9c-c2b32537770a" />

---

## Documentation

Detailed documentation for the project is available below:

1. **[Technical Concept](DOCS/TECHNICAL_CONCEPT.md)** – Core theoretical concept, description and observations. Test results with source files are provided under this **[link](TESTS)**.
2. **[Ecosystem Policy](DOCS/ECOSYSTEM-POLICY.md)** – Guidelines and policies concerning the ecosystem.
3. **[FAQ](DOCS/FAQ.md)** – Frequently asked questions.
4. **[API Architecture](DOCS/ARCHITECTURE.md)** – Technical breakdown and bindings for Lustro V1 API. RTU C/C++ DLL files can be found under this **[link](API/LUSTRO_DLL_FILES)**.
5. **[Philosophy & Origins](DOCS/ORIGINS.md)** – Why Lustro...?

---

**<p align="center">Conceptual diagram of the Lustro mechanism.</p>**

<img width="1359" height="1061" alt="lustro_diagram" src="https://github.com/user-attachments/assets/a267cf39-e666-4cb4-985c-218afd4a5e1f" />
