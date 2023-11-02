# readme

stupid practice to draw some points on ellipse curve by myself

![Imgur](https://i.imgur.com/lM7SRRu.png)

## note

**Oh shoot, github markdown does not support latex syntax**

$(m,n)$ is the center point of ellipse
$a$ is longer, $b$ is shorter, $c$ is center to focus point

```math
\forall P(x, y)  \\
x = m + a \cdot cos(t) \\
y = n + b \cdot sin(t) \\
-\pi < t < \pi
```
-----

```math
\varepsilon = \sqrt{1 - \frac{b^2}{a^2}} \\
= \frac{c}{a}
```

```math
f_1 = m + c = m + a \varepsilon \\
f_2 = m - c = m - a \varepsilon
```

## super-ellipse

reference:
* http://mathworld.wolfram.com/Superellipse.html
* https://en.wikipedia.org/wiki/Superellipse

```math

0 \le t < 2\pi   \\

x(t) = | cos(t) |^{2/n} \cdot a \cdot \text{sgn}(cos(t)) \\

y(t) = | sin(t) |^{2/n} \cdot b \cdot \text{sgn}(sin(t)) \\

```
Because $cos(t)$ and $sin(t)$ could be negative, $sgn(w)$ would be -1 if $cos(t) < 0$. And $sng(w)$ is 1 if $sin(t) > 0$

Shape will differ if:
- $0 < n < 1$ concave, parabola if n=0.5
- $n=1$ parallelogram
- $1<n<2$ convect
- $n=2$ ellipse (if a=b, it is a circle)
- $n>2$ rectangle with rounded corners (squircle)

![img](https://i.imgur.com/fGnCB64.png)
