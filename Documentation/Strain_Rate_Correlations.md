---
Strain Rate Calculations for Use in Hierarchical Sherwood Correlations
author: Farhad Behafarid
date: 24 June 2016
---

## Strain rate tensor

Defined as half the sum of the velocity gradient tensor and its transpose:

E = $\begin{bmatrix}
\frac{\partial u}{\partial x}  							& \frac{1}{2}(\frac{\partial u}{\partial y} +  \frac{\partial v}{\partial x})   & \frac{1}{2}(\frac{\partial u}{\partial z} +  \frac{\partial w}{\partial x}) \\
\frac{1}{2}(\frac{\partial v}{\partial x} +  \frac{\partial u}{\partial y})     & \frac{\partial v}{\partial y} 						& \frac{1}{2}(\frac{\partial v}{\partial z} +  \frac{\partial w}{\partial y}) \\
\frac{1}{2}(\frac{\partial w}{\partial x} +  \frac{\partial u}{\partial z})   	& \frac{1}{2}(\frac{\partial w}{\partial y} +  \frac{\partial v}{\partial z})   & \frac{\partial w}{\partial z} 
\end{bmatrix}$


## Second Invariant of the Symmetrical Strain Rate Tensor; E:

~~~math
II_E =\frac{1}{2} (E_{ii} E_{jj} - E_{ij} E_{ij})
~~~

~~~math
II_E =\frac{1}{2} \Big( \big[E_{11} E_{22} + E_{11} E_{33} + E_{22} E_{33} \big]  - \big[ E_{12} E_{12} + E_{13} E_{13} + E_{23} E_{23} \big] \Big)
~~~

Computing S to be used in Sherwood number correlations:

~~~math
S = \sqrt{\frac{II_E}{2}}
~~~

Summerizing:
~~~math
S =\frac{1}{2}  \sqrt{\big[E_{11} E_{22} + E_{11} E_{33} + E_{22} E_{33}\big]  - \big[E_{12} E_{12} + E_{13} E_{13} + E_{23} E_{23} \big]} 
~~~


