# Renderizar expressões matemáticas com MathJax

* É possível criar expressões matemáticas numa página HTML renderizada em Django, utilizando LateX.
* deve-se importar MathJax, no script:
```HTML
	<script type="text/x-mathjax-config">
      MathJax.Hub.Config({
          showProcessingMessages: false, //Close js loading process information
          messageStyle: "none", //Do not display information
          extensions: ["tex2jax.js"],
          jax: ["input/TeX", "output/HTML-CSS"],
          tex2jax: {
              inlineMath:  [ ["$", "$"] ], //In-line formula selection$
              displayMath: [ ["$$","$$"] ], //The formula selection in the paragraph$$
              skipTags: ['script', 'noscript', 'style', 'textarea', 'pre','code','a'], //Avoid certain tags
              ignoreClass:"comment-content", //Avoid tags containing the Class
              processClass: "mathjax-latex",
          },
          "HTML-CSS": {
              availableFonts: ["STIX","TeX"], //Optional font
              showMathMenu: false //Close the right-click menu display
          }
      });
      MathJax.Hub.Queue(["Typeset",MathJax.Hub])
	</script>
	<script src="https://cdn.bootcss.com/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

```

Veja em baixo como fica renderizado o exemplo deste repositório.

<img src="https://github.com/CR-21-22/matematica/blob/main/index.png" width="400" >


### Expressões no meio do texto
* As expressões em Latex que queremos que apareçam in-line (no meio do texto) devem estar entre etiquetas `$`. 
* Por exemplo  $R_{[bps]}$ está em formato matemático em linha

### Expressões isoladas num parágrafo
* As expressões em Latex que queremos que apareçam isoladas numa linha devem estar entre etiquetas `$$`. 
* Por exemplo a expressão seguinte vai ficar numa linha isolada: $$ P_{[\text{dBW}]} = P_{[\text{dBm}]} + 30 $$

## Mais informação
* consulte o exemplo no [codesandbox](https://codesandbox.io/s/mathjax-jw4py?file=/index.html:241-1313)
* Veja mais informação sobre [Latex/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics) assim como [simbolos em Latex](https://www.caam.rice.edu/~heinken/latex/symbols.pdf).
