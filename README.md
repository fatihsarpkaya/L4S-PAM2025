This repository contains artifacts for the paper [To adopt or not to adopt L4S-compatible congestion control? Understanding performance in a partial L4S deployment](https://doi.org/10.48550/arXiv.2411.10952), accepted for presentation at the PAM 2025 conference.

# L4S

With few exceptions, the path to deployment for any Internet technology requires that there be some benefit to unilateral adoption of the new technology. In an Internet where the technology is not fully deployed, is an individual better off sticking to the status quo, or adopting the new technology? This question is especially relevant in the context of the Low Latency, Low Loss, Scalable Throughput (L4S) architecture, where the full benefit is realized only when compatible protocols (scalable congestion control, accurate ECN, and flow isolation at queues) are adopted at both endpoints of a connection and also at the bottleneck router. 

In this experiment, we consider the perspective of the sender of an L4S flow using scalable congestion control, without knowing whether the bottleneck router uses an L4S queue, or whether other flows sharing the bottleneck queue are also using scalable congestion control. Specifically, we conduct single or multiple flow coexistence experiments where L4S flows (TCP Prague and L4S-compatible BBRv2) share the same bottleneck with non-L4S flows (TCP CUBIC, BBRv1/v2/v3). These experiments are performed over various AQM types on the router, including FIFO, CoDel, PIE, FQ, FQ-CoDel, and DualPI2.

This repository includes:

 - FABRIC testbed notebooks and descriptions for generating experiment data.
 - Google Colab notebooks for generating figures from the data.

To run this experiment on [FABRIC](https://fabric-testbed.net), you should have a FABRIC account with keys configured, and be part of a FABRIC project. You will need to have set up SSH keys and understand how to use the Jupyter interface in FABRIC.

## Run my Experiment (Generating Experiment Data)

To reproduce our experiments on FABRIC, log in to the FABRIC testbed's JupyterHub environment. Open a new terminal from the launcher, and run:

> git clone https://github.com/fatihsarpkaya/L4S.git

In order to get the results for Prague throughput and Prague queueing delay heatmaps, run the `single_bottleneck.ipynb` notebook. 

In this notebook, the experiment parameters are chosen as following.
```
 exp_factors = {
    'n_bdp': [0.5, 1, 2, 4, 8],  # n x bandwidth delay product
    'btl_capacity': [100], #in Mbps 
    'base_rtt': [10], # in ms 
    'aqm': ['FIFO', 'single_queue_FQ', 'Codel', 'FQ', 'FQ_Codel', 'DualPI2'],
    'ecn_threshold': [5], # in ms 
    'ecn_fallback': [0],  #fallback algorithm, TCP Prague falls back to classic TCP when it detects single queue classic ECN bottleneck # 0: OFF, 1: ON  
    'rx_L4S_ecn': [3],  # 0: noecn, 1: ecn, 3: accecn 
    'rx_legacy_ecn': [0],  # 0: noecn, 1: ecn 
    'cc_tx_L4S': ["prague"],
    'cc_tx_legacy': ["cubic"],
    'trial': [1,2,3,4,5,6,7,8,9,10]
}
```

The original results were obtained from 10 trials per experiment, with each experiment lasting 60 seconds. To save time, you may consider reducing the experiment duration. While this shorter duration might not be sufficient for accurate measurements, it should provide a general idea about the throughput and queueing delay.

As mentioned before, the paramaters and the experiment duration could be changed as needed.

Upon completion of the notebook execution, the plots will be saved and displayed at the end of the notebook.
