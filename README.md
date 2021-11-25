# matematica

* É possível criar expressões matemáticas numa página HTML renderizada em Django, utilizando LateX.
* deve-se importar MathJax, no script:
```HTML
<script type="text/javascript" id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3.0.0/es5/tex-mml-chtml.js">
  </script>
```
* As expressões em Latex devem estar entre etiquetas `$$`
* Veja o exemplo em <img src="https://github.com/CR-21-22/matematica/blob/main/matematica/templates/calculadora/index.html" width="100px"> que renderizado fica como em baixo.
* Veja mais informação sobre [Latex/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics) assim como [simbolos em Latex](https://www.caam.rice.edu/~heinken/latex/symbols.pdf).

![index](index.png)
