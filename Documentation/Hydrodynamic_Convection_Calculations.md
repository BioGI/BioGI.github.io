---
Hydrodynamic Convection Calculations for Use in Hierarchical Sherwood Correlations
author: Farhad Behafarid
date: 10 March 2017
---

## Velocity Gradients

All 36 velocity gradinet components are computed using velocity values at all nodes 

## Material Derivatives of the Velocity

~~~math

[\frac{D\vec{U}}{Dt}]_x = u \frac{\partial u}{\partial x}+ v  \frac{\partial u}{\partial y}+ (w+w_{frame}) \frac{\partial u}{\partial z} \\
[\frac{D\vec{U}}{Dt}]_y = u \frac{\partial v}{\partial x}+ v  \frac{\partial v}{\partial y}+ (w+w_{frame}) \frac{\partial v}{\partial z} \\
[\frac{D\vec{U}}{Dt}]_z = u \frac{\partial w}{\partial x}+ v  \frac{\partial w}{\partial y}+ (w+w_{frame}) \frac{\partial w}{\partial z} \\

~~~



## Laplacian

~~~math

[\nabla^2(\vec{U})]_x = \frac{\partial^2 u}{\partial x^2}+ \frac{\partial^2 u}{\partial y^2}+\frac{\partial^2 u}{\partial z^2} = A_1\\

[\nabla^2(\vec{U})]_y = \frac{\partial^2 v}{\partial x^2}+ \frac{\partial^2 v}{\partial y^2}+\frac{\partial^2 v}{\partial z^2} = A_2\\ 

[\nabla^2(\vec{U})]_z = \frac{\partial^2 w}{\partial x^2}+ \frac{\partial^2 w}{\partial y^2}+\frac{\partial^2 w}{\partial z^2} = A_3 
~~~


## Material Derivatives of the Laplacian

~~~math

\big[\frac{D}{Dt} (\nabla^2 \vec{U})\big]_x = u \frac{\partial A_1}{\partial x}+ v  \frac{\partial A_1}{\partial y}+ (w+w_{frame}) \frac{\partial A_1}{\partial z} \\
\big[\frac{D}{Dt} (\nabla^2 \vec{U})\big]_y = u \frac{\partial A_2}{\partial x}+ v  \frac{\partial A_2}{\partial y}+ (w+w_{frame}) \frac{\partial A_2}{\partial z} \\
\big[\frac{D}{Dt} (\nabla^2 \vec{U})\big]_z = u \frac{\partial A_3}{\partial x}+ v  \frac{\partial A_3}{\partial y}+ (w+w_{frame}) \frac{\partial A_3}{\partial z} \\

~~~


Look at this: [Link](http://www.cfd-online.com/Forums/fluent-udf/90818-strain-rate-magnitude.html)

