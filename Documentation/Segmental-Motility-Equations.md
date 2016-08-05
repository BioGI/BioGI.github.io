---
Segmental geometry adn velocity equations
author: Farhad Behafarid
date: 5 Aug 2016
---

## Boundary Position

In defining the equations to describe the time-varying boundary position (geometry evolution in time), it is essential to make sure that the volume (and mass) is conserved. 

Two z-dependent curves (zero summation) at initial time step:
~~~math
A_{1(z)} = A_{base} +A_{amp}  \bigg[ cos \big( 2\pi \frac{z}{L} + \pi \big) \bigg] \\

A_{2(z)} = A_{base} +A_{amp}  \bigg[ cos \big( 2\pi \frac{z}{L} +2\pi \big) \bigg] \\
~~~

Time dependent parameters:

~~~math
\alpha_{(t)} = \frac{time}{T_s} \\

\beta_{(t)} = cos^2 \big( \alpha_{(t)} \pi \big) \\
~~~

The area (function of time and z) can be computed as:
~~~math
A_{(z,t)} = \beta_{(t)} A_{1(z)} + \big[ 1-\beta_{(t)} \big] A_{2(z)} \\
~~~

And having the area, time varying local radius is:
~~~math
R_{(z,t)}    = \sqrt{\frac{A_{(z,t)}}{\pi} } \\

R_{(z,t)}    = \sqrt{\frac{ \beta_{(t)} A_{1(z)} + \big[ 1-\beta_{(t)} \big] A_{2(z)}      }{\pi} } \\

\boxed{R_{(z,t)}    = \sqrt{\frac{ \beta_{(t)} \big[ A_{1(z)} -  A_{2(z)} \big]  +  A_{2(z)}      }{\pi} }} \\
~~~


## Boundary Velocity

~~~math
\frac{d R_{(z,t)}}{dt} = \bigg( \frac{A_{1(z)}- A_{2(z)} }{\pi} \bigg)   \bigg( \frac{d\beta}{dt} \bigg)      \bigg[ \frac{ \beta_{(t)} A_{1(z)} + \big[ 1-\beta_{(t)} \big] A_{2(z)}      }{\pi}    \bigg]^{\frac{-1}{2}}                   
~~~

~~~math
\frac{d\alpha}{dt} =\frac{1}{T_s}
~~~


~~~math
\frac{d\beta}{dt} = -2 \pi \bigg( \frac{d\alpha}{dt} \bigg) sin(\alpha \pi) cos(\alpha \pi) \\

\frac{d\beta}{dt} = \frac{-2 \pi}{T_s} sin(\alpha \pi) cos(\alpha \pi)
~~~

Finally:

~~~math
\boxed{V_{(z,t)}= \frac{d R_{(z,t)}}{dt} = \frac{-2 \pi}{T_s} sin(\alpha \pi) cos(\alpha \pi) \bigg( \frac{A_{1(z)}- A_{2(z)} }{\pi} \bigg) \bigg[ \frac{ \beta_{(t)} A_{1(z)} + \big[ 1-\beta_{(t)} \big] A_{2(z)}      }{\pi}    \bigg]^{\frac{-1}{2}}    }               
~~~



