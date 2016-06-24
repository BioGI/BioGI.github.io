---
Strain Rate Calculations for Use in Hierarchical Sherwood Correlations
author: Farhad Behafarid
date: 24 June 2016
---

## Strain rate tensor

Defined as half the sum of the velocity gradient tensor and its transpose.

Strain rate tensor= $\begin{bmatrix}
\frac{\partial u}{\partial x}  							& \frac{1}{2}(\frac{\partial u}{\partial y} +  \frac{\partial v}{\partial x})   & \frac{1}{2}(\frac{\partial u}{\partial z} +  \frac{\partial w}{\partial x}) \\
\frac{1}{2}(\frac{\partial v}{\partial x} +  \frac{\partial u}{\partial y})     & \frac{\partial v}{\partial y} 						& \frac{1}{2}(\frac{\partial v}{\partial z} +  \frac{\partial w}{\partial y}) \\
\frac{1}{2}(\frac{\partial w}{\partial x} +  \frac{\partial u}{\partial z})   	& \frac{1}{2}(\frac{\partial w}{\partial y} +  \frac{\partial v}{\partial z})   & \frac{\partial w}{\partial z} 
\end{bmatrix}$


## Second Invariant of a symmetrical tensor

~~~math
II_A =\frac{1}{2} (A_{ii} A_{jj} - A_{ij} A_{ij})
~~~

~~~math
II_A =\frac{1}{2} \Big( [A_{11} A_{22} + A_{11} A_{33} + A_{22} A_{33}]  - [A_{12} A_{12} + A_{13} A_{13} + A_{23} A_{23} ] \Big)
~~~

Computing S to be used in Sherwood number correlations:

~~~math
S = \sqrt{\frac{II_A}{2}}
~~~

Summerizing:
~~~math
S =\frac{1}{2} \Big( \sqrt{[A_{11} A_{22} + A_{11} A_{33} + A_{22} A_{33}]  - [A_{12} A_{12} + A_{13} A_{13} + A_{23} A_{23} ]} \Big)
~~~


