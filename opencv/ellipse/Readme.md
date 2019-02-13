# readme

stupid practice to draw some points on ellipse curve by myself

![Imgur](https://i.imgur.com/lM7SRRu.png)

## note

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
