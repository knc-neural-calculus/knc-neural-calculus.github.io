---
title: "Axon Growth Simulation"
# description and summary are unused?
# description: "Sample article showcasing basic Markdown syntax and formatting for HTML elements."
# summary: "ffffffff"
# toc: true
# authors: ["unused?"]  
links:

- icon: "github"
  iconPack: "fab"
  url: "https://github.com/knc-neural-calculus/axon-growth-sim"
  text: "axon-growth-sim"

# you can get icons here:
# https://fontawesome.com/icons?d=gallery&p=2&m=free

authorLinks:
  - name: Michael Ivanitskiy
    url: ../../members/miv
  - name: Connor Puritz
    url: mailto:cpuritz@umich.edu

# tags, categories, themes, series, and dates can be commented out without issue
# tags: ["markdown", "css", "html", "themes"]
# categories: ["themes", "syntax"]
# series: ["Themes Guide"]
# date:  "2019-03-11"
# lastmod: "2019-03-11"
draft: false # set this to 'false' when you want the project to appear on the list
---


<!-- PUT DESCRIPTION TEXT HERE above the more -->
## Modelling biological generation of connectomes

<!--more-->

In this work, we attempted to model the generation of neural connectomes. Our model consisted of 3 interdependent layers: the diffusion of neurite growth factors across a 2-D space, the growth of axons dependent on the gradients of various neurite growth factors, and a simplified model of neuron activity. Each of these three layers influenced the other layers. For example, the model of neuron activity took into account the incoming connections to a neuron, and the level of activity combined with the neuron type determined the output of various neurite growth factors. Our model is very versatile, and is capable of simulating an essentially unlimited number of types of neurons and growth factors, and their affinities can be fine tuned based on data from physical experiments. We hope to extend this model to incorporate a more detailed model of neuron activity, as well as a more detailed model of synaptogenesis.


![growth](../../static/img/axon-growth.png)

<img src="/assets/axon-growth-sim/axon-growth.png" style="width: 25vw;">
<img src="axon-growth-sim/img/axons_t6.png" style="width: 25vw;">
<img src="axon-growth-sim/img/axons_t7.gif" style="width: 25vw;">
<img src="axon-growth-sim/img/diffusion_example.png" style="width: 25vw;">
<img src="axon-growth-sim/img/example_img.png" style="width: 25vw;">
<img src="axon-growth-sim/img/fiber.png" style="width: 25vw;">
<img src="axon-growth-sim/img/two_clusters_1.png" style="width: 25vw;">


