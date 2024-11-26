This repository contains artifacts for the paper '[To adopt or not to adopt L4S-compatible congestion control? Understanding performance in a partial L4S deployment](https://doi.org/10.48550/arXiv.2411.10952),' accepted for presentation at the PAM 2025 conference.

# L4S

With few exceptions, the path to deployment for any Internet technology requires that there be some benefit to unilateral adoption of the new technology. In an Internet where the technology is not fully deployed, is an individual better off sticking to the status quo, or adopting the new technology? This question is especially relevant in the context of the Low Latency, Low Loss, Scalable Throughput (L4S) architecture, where the full benefit is realized only when compatible protocols (scalable congestion control, accurate ECN, and flow isolation at queues) are adopted at both endpoints of a connection and also at the bottleneck router. 

In this experiment, we consider the perspective of the sender of an L4S flow using scalable congestion control, without knowing whether the bottleneck router uses an L4S queue, or whether other flows sharing the bottleneck queue are also using scalable congestion control. Specifically, we conduct single or multiple flow coexistence experiments where L4S flows (TCP Prague and L4S-compatible BBRv2) share the same bottleneck with non-L4S flows (TCP CUBIC, BBRv1/v2/v3). These experiments are performed over various AQM types on the router, including FIFO, CoDel, PIE, FQ, FQ-CoDel, and DualPI2.

This repository includes:

 - FABRIC testbed notebooks and descriptions for generating experiment data.
 - Instructions for placing the data into the corresponding folder.
 - Google Colab notebooks for generating figures from the data.

To run this experiment on [FABRIC](https://fabric-testbed.net), you should have a FABRIC account with keys configured, and be part of a FABRIC project. You will need to have set up SSH keys and understand how to use the Jupyter interface in FABRIC.

