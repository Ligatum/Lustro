## **Lustro V1 Project Description**

Lustro V1 is a single pass, deterministic diffusion engine built around the idea that transformation parameters can emerge from the evolving state itself rather than from predefined schedules or static control structures. Observations suggest an even, approximately isotropic information propagation process.

The project currently evaluates this architecture as a core mechanism for primitives such as hash functions, pseudo-random number generators (PRNG), and extendable-output functions (XOF). Scalar version speed can reach over **13 GB/s** with aggregate batching (i5-11600K @ 4.5 GHz).

The API, technical documentation, test implementations, empirical evaluation, and design philosophy are provided across the Lustro repositories.

All observations presented in this repository are empirical and describe the behaviour of the system. These observations are not intended as a formal proof of cryptographic security.

**<p align="center">Comparative overview of Lustro tree batching capabilities.</p>**

<img width="1884" height="1125" alt="lustro_comparison" src="https://github.com/user-attachments/assets/2e7c3134-75e9-4d76-ac2f-7f7dc279c6a5" />

## Links

The Audit code is available **[HERE](https://github.com/Ligatum/Lustro_Audit)**.<br>

The API code is available **[HERE](https://github.com/Ligatum/Lustro_API)**.<br>

## Documentation

Detailed documentation for the project is available below:

1. **[Technical Concept](DOCS/TECHNICAL_CONCEPT.md)** – Core theoretical concept, description and observations. Test results with source files are provided **[here](TESTS)**.
2. **[Ecosystem Policy](DOCS/ECOSYSTEM-POLICY.md)** – Guidelines and policies concerning the ecosystem.
3. **[FAQ](DOCS/FAQ.md)** – Frequently asked questions.
4. **[API Architecture](DOCS/ARCHITECTURE.md)** – Technical breakdown and bindings for Lustro V1 API.  RTU C/C++ DLL files can be found **[here](API/LUSTRO_DLL_FILES)**.
5. **[Philosophy & Origins](DOCS/ORIGINS.md)** – Why Lustro...?

##

**<p align="center">Conceptual diagram of the Lustro mechanism.</p>**

<img width="1359" height="1061" alt="lustro_diagram" src="https://github.com/user-attachments/assets/a267cf39-e666-4cb4-985c-218afd4a5e1f" />
