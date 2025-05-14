# Scaling the Stars
## Optimizing MPI communication on GPUs in the PROMPI stellar dynamics code

This repository contains the code to generate the slides for the presentation
about PROMPI delivered by Miren Radia at the [HPC RSE SIG
meeting](https://socrse.github.io/hpc-rse-sig/) on Mon 19 May 2025. This
presentation is based on [one I previously
gave](https://github.com/mirenradia/20241212_PROMPI_DiRAC_Day_presentation) at
the [DiRAC Science Day 2024](https://dirac.ac.uk/dirac-science-day-2024/) on Thu
12 Dec 2024.

## Quarto

These slides are written in [Quarto](https://quarto.org/) markdown in the
[Reveal.js](https://quarto.org/docs/presentations/revealjs/) format.

### Build

To generate the slides, [install Quarto](https://quarto.org/docs/get-started/)
and then execute

```
quarto render slides.qmd
```

It should generate a `slides.html` file which you can open with a web browser.

### GitHub Pages

If you are looking at this repository on GitHub, the slides are deployed to
[this GitHub Pages
site](https://mirenradia.github.io/20250519_PROMPI_HPC_RSE_meeting_presentation).

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under [CC-BY-4.0][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
