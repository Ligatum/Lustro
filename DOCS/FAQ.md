# Lustro V1 FAQ

*This FAQ is a plain-language summary for convenience only. **Version 1.0 – Last Updated 09.09.2026**.*  
*It does not modify, extend, or override the Lustro Technology License (LTL) 1.0 or the Lustro Ecosystem Policy.*

---

> **Most developers never need a Commercial License.**  
> You are generally free to use Lustro in your own software, including commercial products and SaaS. A Commercial License is only required if you want to distribute Lustro itself as a reusable development technology, commercially exploit hardware implementations, or obtain a specific licensing exception.

---

### Can I use Lustro in my commercial product?
**Yes.** Commercial use is explicitly permitted, including SaaS applications. You may embed Lustro Core inside your own applications, databases, storage engines, operating systems, enterprise platforms, security software, embedded firmware, and similar products.

### Can I use Lustro inside my company's internal systems?
**Yes.** Internal commercial use is fully permitted. As long as Lustro remains an internal implementation component of your software or infrastructure, no Commercial License is required.

### Do I have to open-source my product?
**No.** You may keep your own application source code proprietary. The License does not require you to disclose your application's code.

### Can I modify the source code?
**Yes.** You may modify the Licensed Work and create derivative works, including as part of your own commercial products and services, subject to the terms in the License. Ligatum maintains its canonical reference implementation as the ecosystem's Single Source of Truth (SSoT).

### Can I put Lustro inside my own SDK or framework that I sell to other companies?
**Yes**, provided that your SDK does not expose Lustro Core itself as a primary reusable technology or development platform to your customers. If your SDK's main purpose is to provide third parties with access to Lustro Core as a Reusable Technology Offering, a Commercial License is required.

---

### When do I actually need a Commercial License?
A Commercial License is required when Lustro Core itself is offered as a **Reusable Technology Offering**, or when **Commercial Hardware Exploitation** is involved.

Typical examples requiring a license:
- Hosted cloud services primarily providing raw Lustro Core execution or API access.
- Public APIs or SDKs whose primary purpose is to expose Lustro Core to third-party developers.
- Commercial FPGA, ASIC, or hardware implementations.

*Building standard applications that use Lustro merely as an internal component does not require a Commercial License. If you are unsure whether your project requires a license, please reach out to us.*

---

### Does it matter if my project is non-commercial, non-profit, or an academic project?
The definition of a Reusable Technology Offering applies regardless of non-profit status. However, Ligatum may grant Commercial Licenses or waivers for non-commercial, academic, or exceptional open-source cases at no cost. Simply ask us.

### Can I implement Lustro Core in an FPGA or ASIC?
**Yes, for non-commercial research and testing.** Any commercial deployment of a hardware implementation – including manufacturing, selling, or running it internally in a commercial production environment – requires a Commercial License.

### What happens on the Change Date (03-09-2031)?
On the Change Date, commercial software distribution restrictions on the Licensed Work expire, transitioning the copyright license into a permanent, open license for everyone. *(Note: Hardware implementation restrictions remain governed under their respective terms).*

### Can I write a language binding (e.g., Go, Node.js, Python, C#)?
**Yes, this is highly encouraged.** If your binding interfaces with an unmodified Lustro Core without redistributing a modified engine as a competing platform, it is not restricted by this License. The code you write for the binding belongs entirely to you.

### Can I fork the project?
**Yes.** Forking and modification are permitted under the License. However, you cannot distribute or offer your fork as a Reusable Technology Offering, nor represent it as an official or authorized implementation of Lustro Core. Our guiding principle is *Reference before fragmentation*.

### Can I perform independent research, benchmarking, statistical tests, or cryptanalysis?
**Yes, absolutely.** Independent analysis, third-party cryptanalysis, statistical evaluation, and academic research are core pillars of the project philosophy and are explicitly welcomed.

### Can I write my own implementation of the Lustro architecture from scratch?
The Ligatum Technology License covers the *Licensed Work* (the source code, documentation, and materials distributed by Ligatum). An independent software implementation written strictly from scratch without using our codebase is not governed by this copyright license.  
*However, please note that the underlying state-evolution architecture and mechanisms are subject to pending patent applications.*

---

### Contact & Licensing Inquiries
For commercial licensing, exceptions, or clarification regarding your architecture, contact us at:  
📧 **licensing@ligatum.com**

---
*Lustro Technology License (LTL) 1.0 · Lustro Ecosystem Policy 1.0 · Copyright © 2026 Ligatum*
