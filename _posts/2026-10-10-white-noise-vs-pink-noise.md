---
layout: post
title: "Why Does White Noise Sound Sharper Than Pink Noise?"
date: 2026-10-10
permalink: /articles/white-noise-vs-pink-noise/
category: Audio
author: false
reading_time: 5
description: "Two ways of dividing the frequency range explain why “equal power” can produce very different sounds."
---

*Two ways of dividing the frequency range explain why “equal power” can produce very different sounds.*

White noise is described as having equal power across frequency. That sounds like a recipe for balance. So why can it sound like a bright hiss, while pink noise has less of that sharp edge?

The missing detail is the size of the frequency interval being compared. White noise distributes power equally across equal-width frequency bands. Pink noise distributes power equally across octaves. Those are different definitions of equal. [Noise definitions](https://www.mathworks.com/help/dsp/ref/dsp.colorednoise-system-object.html)

We can see the difference with two frequency ranges and a small calculation.

## Two octaves with different widths

Frequency measures how many cycles occur each second. Its unit is hertz, abbreviated Hz. An octave spans a doubling of frequency: 100 to 200 Hz is one octave, as is 1,000 to 2,000 Hz. [Octave analysis](https://www.mathworks.com/help/signal/ref/poctave.html)

Their widths, however, are different:

| Frequency range | Frequency ratio | Width |
|---|---|---|
| 100–200 Hz | 2:1 | 100 Hz |
| 1,000–2,000 Hz | 2:1 | 1,000 Hz |

The second band is ten times wider. Both are octaves because an octave describes a ratio, not a fixed number of hertz.

To calculate white-noise power in these bands, use an illustrative model. Assume an ideal signal with a constant power density throughout both ranges. Assign it one arbitrary unit of power per hertz. These are teaching units, not measurements from a recording or speaker.

The 100–200 Hz band then contains 100 power units. The 1,000–2,000 Hz band contains 1,000. The wider band receives ten times as much power simply because it contains ten times as much frequency width.

The chosen density changes the numbers, but not the ratio. At two units per hertz, the totals would be 200 and 2,000. At half a unit, they would be 50 and 500.

This gives white noise more power in higher octave bands. It does not tell us that the second band sounds ten times louder. The calculation describes signal power, not a listener’s loudness judgment.

## How pink noise changes the balance

Pink noise reduces power density as frequency increases. In the ideal model, its density is proportional to one divided by frequency. At twice the frequency, the density is half as large. Across an octave, that reduction compensates for the increasing band width. The result is equal power per octave. [Pink-noise spectrum](https://www.mathworks.com/help/dsp/ref/colorednoise.html)

For a simple illustration, suppose an ideal pink-noise signal contains 100 arbitrary power units between 100 and 200 Hz. It would also contain 100 between 200 and 400 Hz, and 100 between 1,000 and 2,000 Hz, provided all those bands lie within its operating range.

White noise would not maintain those equal octave totals. Starting at 100 units in the first band, its next octave would contain 200, because 200–400 Hz is twice as wide.

These examples explain the spectral difference behind the opening question. Relative to its lower octaves, white noise puts more power into higher octaves. Pink noise does not have that increasing octave-power pattern. That makes a brighter, more hiss-like character for white noise a reasonable expectation, rather than a contradiction of its definition. [White and pink octave spectra](https://www.mathworks.com/help/signal/ref/poctave.html)

The expectation is not a promise about what every listener will hear. The calculation alone cannot account for the playback equipment or establish perceived loudness.

## Why both can look “flat” on a graph

A spectrum needs a definition of what its vertical axis measures.

A power-density graph reports power per unit of frequency. White noise is flat in that representation. An octave-band graph adds the power within each octave. Pink noise is flat in that representation, while white noise rises toward higher octave bands. MathWorks demonstrates both views using generated noise. [Spectrum comparison](https://www.mathworks.com/help/signal/ref/poctave.html)

Changing the frequency axis to a logarithmic scale is not, by itself, the same operation as adding power within octave bands. To interpret a plot, check whether it shows power density or total band power.

The question “Which noise has a flat spectrum?” therefore needs a second question: flat according to which measurement?

## Try a short comparison

How does the difference sound through your headphones or speakers? [Compare white and pink noise on WaveLocus](https://wavelocus.com/noise-generator) using the short exercise below. Listen for a change in the hiss or tonal balance, then describe what you actually hear. A subtle difference, or no clear difference, is worth recording too.

1. Turn your device volume down before starting. Use the same headphones or speakers throughout.
2. Select white noise and play a short sample, such as three seconds, at a conservative digital level.
3. Stop playback and write down what you noticed. “More hiss,” “less bass,” or “no clear difference” are observations, not required answers.
4. Select pink noise, leaving duration, digital level, output route, and device volume unchanged. Keep the seed unchanged for repeatable trials within each noise type.
5. Repeat the comparison in the opposite order. Note whether your description remains consistent.

Keep playback quiet and stop if it is uncomfortable. Loudness and exposure duration both matter for hearing risk. [CDC guidance](https://www.cdc.gov/hearing-loss/prevention/)

This is an informal listening exercise. The same digital-level setting does not establish equal perceived loudness, and it is not a calibrated sound-pressure reading. Keeping a seed also does not make different noise colors identical signals. Record a possible level difference separately from a difference in tonal character.

## What the comparison can answer

The exercise can help you connect a spectral definition to an audible difference in your setup. It cannot establish that one noise type is universally more pleasant or that your equipment has an accurate frequency response.

For this question, the useful habit is to make “equal” precise. Equal-width bands and equal-ratio bands ask different things of a signal. Once that distinction is visible, the contrast between white and pink noise becomes something we can calculate and investigate, rather than a collection of color names to memorise.
