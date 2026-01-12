# Hebbian Learning

*This small project was originally part of a homework assignment that I worked on during my master's degree.*
  
## The Model
Here, we construct a Hopfield network of $N=64$ neurons in continuous time, whose dynamics are gouverned by:  

$$\dot{\mathbf{x}} = -\mathbf{x} + f(W\mathbf{x}) + \sigma \eta(t),$$  

where $\mathbf{x}$ is the vector of firing rates, $W$ a $N \times N$ weight matrix, $\eta(t)$ a white noise term with amplitude $\sigma=0.1$ and $f(x)=\text{sign}(x)$ the activation function. 

### Storing one pattern
We start by storing a single pattern $\mathbf{p}$ in the Hopfield network. Here, the weight matrix is given by:  

$$W = \frac{1}{N}\mathbf{p}\mathbf{p}^T,$$  

where $\mathbf{p} = (p_1, \ldots, p_{64})$ is assumed to be a column vector. In what follows, we will map the $64-\text{dimensional}$ vector $\mathbf{p}$ into a $8 \times 8$ matrix.  
  
The pattern $\mathbf{p}$ we wish to store is the following:  
<p align="center" width="100%">
    <img width="30%" src="Figs/pattern_1.png">
</p>
  
Each pixel represents a neuron: dark purple corresponds to the stored value $-1$ and bright yellow to $1$. As we simulate the network, we will see that the neurons update to values between $-1$ and $1$, represented by a colour gradient.  


One method to simulate the network is by using the Euler scheme with a stepwidth of $dt=0.1$. The update is given by the following equation:  

$$\mathbf{x}(t+dt) = \mathbf{x}(t) + \dot{\mathbf{x}}(t)dt = \mathbf{x}(t) - \mathbf{x}(t)dt + f(W\mathbf{x}(t))dt + 0.1\eta(t)\sqrt{dt}.$$

The initial conditions are generated randomly. After repeatedly simulating the network over time, we observe that the network inevitably converges towards one of two distinct, stable, states: either $\mathbf{p}$ or $-\mathbf{p}$.

<p align="center" width="100%">
    <img width="75%" src="figure_1.png">
</p>

<p align="center" width="100%">
    <img width="75%" src="figure_2.png">
</p>  
  

One can try explaining these behaviours - ignoring the stochastic term (as it is quite small), let us prove that $p$ and $-p$ are equilibrium points of the dynamics. First, note that:  

$$\dot{\mathbf{p}} = -\mathbf{p} + \text{sign}(W\mathbf{p}) \Leftrightarrow \dot{p}_i = -p_i + \text{sign}((W\mathbf{p})_i) \ \forall i \in \{1, \ldots, 64\},$$

and therefore:  

$$\begin{aligned} -p_i + \text{sign}((W\mathbf{p})_i) =& -p_i + \text{sign}\left( \sum_{j=1}^{64} W_{ij}p_j \right) = -p_i + \text{sign}\left( \sum_{j=1}^{64}\frac{1}{64} p_ip_jp_j \right) \\
&= -p_i + \text{sign}\left( \frac{p_i}{64} \sum_{j=1}^{64} p_jp_j \right) = -p_i + \text{sign}\left( \frac{p_i}{64} \sum_{j=1}^{64} 1 \right) \\
&= p_i + \text{sign}\left( \frac{p_i}{64} \cdot 64 \right) = -p_i + \text{sign}(p_i) = 0.
\end{aligned}$$
  
The same reasoning can be applied to $-\mathbf{p}.$ Therefore, $\mathbf{p}$ and $-\mathbf{p}$ are both equilibrium points. Furthermore, these two equilibria are stable (i.e. attractors); this property can be shown via the Lyapunov function.  
  
### Storing two patterns
We now introduce a second pattern $\mathbf{q}$ to be stored in the network: 
<p align="center" width="100%">
    <img width="30%" src="Figs/pattern_2.png">
</p>

The weight matrix is now given by:  

$$W = \frac{1}{N} \left( \mathbf{p}\mathbf{p}^T + \mathbf{q}\mathbf{q}^T \right).$$
  
As previosuly, we will simulate the network over time: we observe that the network converges towards one of the stored patterns or its opposite, depending on initial conditions. 

<p align="center" width="100%">
    <img width="75%" src="figure_3.png">
    <img width="75%" src="figure_4.png">
    <img width="75%" src="figure_5.png">
    <img width="75%" src="figure_6.png">
</p>
  

### Maximum storage capacity
When storing $M$ patterns, the weight vector becomes:
$$W = \frac{1}{N} \sum_{i=1}^M \mathbf{p}_i\mathbf{p}_i^T.$$
  
We would like to know more about the maximum number of patterns that can be stored. In theory, if one were to store approximately $0.18N$ patterns [[1]](#1) in our network and start at a given pattern, there is a small chance that part of the pattern will be distorted after the first iteration, potentially leading to an avalanche effect.  
  
Actually, one can expect to see an avalanche effect as early as trying to store above $0.138N$ patterns [[1]](#1); the network will converge towards spurious states (i.e. stable states that are not any of the patterns). Below this proportion, one will likely observe near-convergence (a small fraction of bits may be flipped) towards one of the patterns.  
  
In our case, we have $\lfloor 0.138 \cdot 64 \rfloor = 8$. Therefore, we will consider a total of $9$ distinct patterns and investigate what happens when progressively trying to increas the number of stored patterns.
<p align="center" width="100%">
    <img width="10%" src="Figs/pattern_1.png">
    <img width="10%" src="Figs/pattern_2.png">
    <img width="10%" src="Figs/pattern_3.png">
    <img width="10%" src="Figs/pattern_4.png">
    <img width="10%" src="Figs/pattern_5.png">
    <img width="10%" src="Figs/pattern_6.png">
    <img width="10%" src="Figs/pattern_7.png">
    <img width="10%" src="Figs/pattern_8.png">
    <img width="10%" src="Figs/pattern_9.png">
</p>

#### Storing three patterns
The network always converges towards one of the three patterns.
<p align="center" width="100%">
    <img width="75%" src="figure_7.png">
</p>
  
#### Storing four patterns
Again, the network always converges towards one of the four patterns.
<p align="center" width="100%">
    <img width="75%" src="figure_8.png">
</p>

#### Storing three patterns
Yet again, the network always converges towards one of the five patterns.
<p align="center" width="100%">
    <img width="75%" src="figure_9.png">
</p>

#### Storing six patterns
Here, we can already see that for the last pattern, one of the bits is missing.
<p align="center" width="100%">
    <img width="75%" src="figure_10.png">
</p>
  
In fact, setting the sixth pattern $\mathbf{p}_6$ as the initial condition, we observe that over time, the network converges towards a stable state that resembles pattern $\mathbf{p}_6$, to the exception of one missing bit.
<p align="center" width="100%">
    <img width="75%" src="figure_11.png">
</p>

#### Storing seven patterns 
By adding another pattern $\mathbf{p}_7$, we observe that two of the patterns are not memorized by the network anymore.
<p align="center" width="100%">
    <img width="75%" src="figure_12.png">
</p>

Setting initial conditions to these two patterns (i.e. $\mathbf{p}_6$ and $\mathbf{p}_2$), one can observe that some of the bits in the patterns flip, consequently causing others to flip too.
<p align="center" width="100%">
    <img width="75%" src="figure_13.png">
</p>

#### Storing eight patterns
One can observe an avalanche effect in at least one of the patterns. Most of the patterns seem to remain stable, or converge towards a pattern with a difference of a few flipped bits.
<p align="center" width="100%">
    <img width="75%" src="figure_14.png">
</p>

#### Storing nine patterns: breaking point
From now on, all initial conditions are a pattern. Doing so will allow to better evaluate which ones remain stable, and if not, towards which new configurations the network converges. As shown below, one can see that for almost all starting patterns, the final state is very different.
<p align="center" width="100%">
    <img width="75%" src="figure_15.png">
</p>

Most of the patterns seem to converge towards one of two different states that resemble, but are none of the patterns. An avalanche effect is indeed observed for at least three patterns.

## References
<a id="1">[1]</a> 
David J. C. MacKay (2003). 
Information theory, inference, and
learning algorithms.
chapter 42.
