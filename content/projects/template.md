---
title: "Axon Growth Simulation"
# description and summary are unused?
description: "Sample article showcasing basic Markdown syntax and formatting for HTML elements."
summary: "ffffffff"
# toc: true
# authors: ["unused?"]  
links:
- icon: "envelope"
  iconPack: "fas"
  url: "mailto:admin@knc.ai"
  text: "admin@knc.ai"

- icon: "github"
  iconPack: "fab"
  url: "https://github.com/knc-neural-calculus/mltests"
  text: "mltests"

- icon: "globe"
  iconPack: "fas"
  url: "https://knc.ai/projects/template"
  text: "knc.ai"

# you can get icons here:
# https://fontawesome.com/icons?d=gallery&p=2&m=free

authorLinks:
  - name: Michael Ivanitskiy
    url: ../../members/miv
  - name: John Balis
    url: ../../members/balis
  - name: Diogenes the Cynic
    url: "mailto:standoutofmysunlight@ancientgreece.edu"


# tags, categories, themes, series, and dates can be commented out without issue
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
date:  "2019-03-11"
lastmod: "2019-03-11"
draft: true # set this to 'false' when you want the project to appear on the list
---

<!-- PUT DESCRIPTION TEXT HERE above the more -->
This text goes in the project list, as well as the top of the project page.


<!--more-->

In this work, we attempted to model the generation of neural connectomes. Our model consisted of 3 interdependent layers: the diffusion of neurite growth factors across a 2-D space, the growth of axons dependent on the gradients of various neurite growth factors, and a simplified model of neuron activity. Each of these three layers influenced the other layers. For example, the model of neuron activity took into account the incoming connections to a neuron, and the level of activity combined with the neuron type determined the output of various neurite growth factors. Our model is very versatile, and is capable of simulating an essentially unlimited number of types of neurons and growth factors, and their affinities can be fine tuned based on data from physical experiments. We hope to extend this model to incorporate a more detailed model of neuron activity, as well as a more detailed model of synaptogenesis.