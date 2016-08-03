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

<!---

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

--->

## Computing the strain rate for use in corelations:
~~~math
S =  \sqrt{2 \bigg[ E_{11}^2 + E_{22}^2 + E_{33}^2  + 2 \big( E_{12}^2 + E_{13}^2 + E_{23}^2 \big) \bigg] }
~~~


~~~math
S= \sqrt{2 \bigg[ \big(\frac{\partial u}{\partial x}\big)^2 
                + \big(\frac{\partial v}{\partial y}\big)^2
                + \big(\frac{\partial w}{\partial z}\big)^2   \bigg]
                + \big( \frac{\partial u}{\partial y}+ \frac{\partial v}{\partial x} \big)^2                 
                + \big( \frac{\partial u}{\partial z}+ \frac{\partial w}{\partial x} \big)^2 
                + \big( \frac{\partial w}{\partial y}+ \frac{\partial v}{\partial z} \big)^2 
                 }
~~~

Look at this: [Link](http://www.cfd-online.com/Forums/fluent-udf/90818-strain-rate-magnitude.html)

