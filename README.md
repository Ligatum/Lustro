### Repositories

The project is intentionally split into dedicated repositories:

* **Lustro** — this main repository with documentation, specifications, tests, and empirical results
* **Lustro_API** — API and implementation **[Lustro_API Repository](https://github.com/Ligatum/Lustro_API)**
* **Lustro_Audit** — Audit code and analysis **[Lustro_Audit Repository](https://github.com/Ligatum/Lustro_Audit)**

---

# Lustro V1

Lustro V1 is a 256-bit deterministic, single-pass diffusion engine where transformation parameters are derived dynamically from the evolving state itself. Lustro relies on two complementary mechanisms: ERD generates control parameters through a multi-stage, co-evolving internal state and applies them to the shared state, which then feeds into IDM's next round of the main transformation. Implemented in Rust, it provides a unified API with streaming, batching, live-state forking, and automatic parallel stream dispatch. The API provides Python and C/C++ extensions.

The engine is evaluated as a core mechanism for:

* **Hash**
* **PRNG**
* **XOF**

The scalar implementation (using the C/C++ interface) reaches over **13 GB/s** aggregate throughput with batch processing, tested on an Intel i5-11600K (12 logical threads @ 4.5 GHz).

All results presented here are empirical observations of the system's behavior. They do not constitute a formal proof of cryptographic security.

---

**<p align="center">Comparative overview of Lustro tree batching capabilities.</p>**

<img width="1814" height="1087" alt="lustro_comparison" src="https://github.com/user-attachments/assets/d523895d-e50e-4db7-9a9c-c2b32537770a" />

---

## Documentation

Detailed documentation for the project is available below:

1. **[Technical Concept](DOCS/TECHNICAL_CONCEPT.md)** – Core theoretical concept, description and observations. Test results with source files are provided under this **[link](TESTS)**.
2. **[Ecosystem Policy](DOCS/ECOSYSTEM-POLICY.md)** – Guidelines and policies concerning the ecosystem.
3. **[FAQ](DOCS/FAQ.md)** – Frequently asked questions.
4. **[API Architecture](https://github.com/Ligatum/Lustro_API/blob/main/ARCHITECTURE.md)** – Technical breakdown and bindings for Lustro V1 API. Ready to use C/C++ DLL files can be found under this **[link](API/LUSTRO_DLL_FILES)**.
5. **[Philosophy & Origins](DOCS/ORIGINS.md)** – Why Lustro...?

---

**<p align="center">Conceptual diagram of the Lustro mechanism.</p>**

<img width="1359" height="1061" alt="lustro_diagram" src="https://github.com/user-attachments/assets/a267cf39-e666-4cb4-985c-218afd4a5e1f" />
