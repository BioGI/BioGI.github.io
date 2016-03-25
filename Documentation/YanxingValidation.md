---
title: Validation of new particle dissolution model using Yanxing data
author: Farhad Behafarid, Ganesh Vijayakumar
date: 25 Mar 2016
bibliography: ../References/references.bib
---



# Chosen case from Yanxing's data files
One of the Yanxing's simulations was chosen as defined by the parameters below (re01s-b/sca-f-01.dat and re01s-b/sca-c-01.dat):

~~~math
U_o = 0.1 m/s \\
\nu= 0.125 m^2/s \\
S^* = 1 \\
Re_s= 0.1 \\
~~~

<!---
The output plots are presented in Figures below

#### Figure: {#Chhosen-Case-Scalar}
![Sc=10](./yanxingSphereData/re01s-b/scalar_Both_Re01_Sc10.png){width=50%}
Caption: Total scalar released form Yanxing data 

#### Figure: {#Chhosen-Case-Flux}
![Sc=10](./yanxingSphereData/re01s-b/Scalar_Release_At_each_Timestep_SC10_REs01_25_Mar_16_Farhad.png){width=50%}
Caption: $q^"A$  from Yanxing data

#### Figure: {#Chhosen-Case-Cb}
![Sc=10](./yanxingSphereData/re01s-b/Cb_over_Cs_Re01_Sc10.png){width=50%}
Caption: $C_b/C_s$ based on Yanxing data 
--->




#Parameters

Using below equations we can get the dimensional parameters needed for our simulations:

~~~math
\left.\begin{aligned}
S    = \frac{U_o}{H} \\
Re_s = \frac{S \; R^2}{ \nu} \\
S^*  = Re_s \; Sc \\
H/R = 20\\
L/R = 50 \\
W/R = 20 \\
\end{aligned}
\right\}
\qquad \text{Non-dimensional parameters}
~~~


~~~math
\left.\begin{aligned}
R   = \frac{20 \; Re_s \; \nu }{U_o} =2.5 m\\
H = W = 20 R = 50 m  \\
L = 50 R = 125 m \\
Sc  = \frac{S*}{Re_s} = 10\\
D_m = \frac{\nu}{Sc} = 0.0125 m^2/s\\
C_s =1 mol/m^3\\
\end{aligned}
\right\}
\qquad \text{Parameters needed}
~~~





# Sherwood number 

We got $N^"_s A_P$ from the last time step of the data file (sca-f-01.dat, last column, last row):


~~~math
N^"_s A_P =  4.058773 \frac{mol} {s} \\
A_P= 4 \pi R^2= 4 \pi (2.5)^2 =78.54 m^2 \\
N^"_s= \frac{4.058733} {78.54} = 0.051677 \frac{mol} {m^2.s} 
~~~

Computing the bulk concentration corresponding to the last time step in the data file, we have:

$C_b= 0.000092$

Therefore:

~~~math
Sh= \frac{N^"_s} {D_m  (\frac{C_s-C_b}{R}) } = \frac{0.051677} {0.0125 (\frac{1-0.000092}{2.5})} = 10.336   \\
~~~

The computed Sherwood number of 10.336 is not what we  expected (Sh= 1.3 from Sherwood plots and correlations)





