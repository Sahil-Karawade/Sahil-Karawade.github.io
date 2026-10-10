---
layout: post
title: "Can You Hear the Difference, or Did You Get Lucky?"
date: 2026-10-10
permalink: /articles/can-you-hear-the-difference/
category: Audio
author: false
reading_time: 6
description: "A blind audio comparison can produce a convincing score by chance. Here is how to read the result without overstating it."
---

*A blind audio comparison can produce a convincing score by chance. Here is how to read the result without overstating it.*

Suppose you compare two versions of the same recording. One is the original; the other has been compressed into a smaller audio file. You think you can hear a difference, so you try a blind test. You identify the version correctly ten times out of sixteen.

That is better than half. Is it enough to show that you heard something?

This is an illustrative result, not a listening session anyone has reported. Under a simple guessing model, a score of ten or more out of sixteen occurs about 23% of the time. A result that looks encouraging can still be fairly ordinary for someone choosing without an audible clue.

The score needs a reference point. That is where an ABX test and a little probability become useful.

## What A, B, and X mean

In an ABX comparison, A and B are two reference signals. X is one of those signals, selected at random and presented without revealing its identity. You can listen to the references and X, then decide whether X matches A or B. The process repeats with a newly assigned X. [ABX procedure](https://www.ohl.to/audio/docs/abx/abxman.pdf)

The question is specific: can you identify which reference you are hearing?

It is different from asking which version you prefer. You could reliably identify a difference without preferring either version. You could also have a strong preference when the identities are visible but fail to identify the versions when they are hidden. The test does not ask you to defend that preference. It asks you to perform a matching task.

Nor does a file comparison, by itself, compare two pairs of headphones. Both files ordinarily travel through the same playback equipment. The claim being tested should describe what actually changed.

## Sixteen guesses have many possible outcomes

For the calculation, assume sixteen trials chosen in advance. X is assigned independently on every trial, with equal chances of being A or B. Under the guessing model, each answer has a one-half chance of being correct, and the listener receives no information that predicts X.

There are 65,536 possible sequences of correct and incorrect answers: two possibilities multiplied together sixteen times. Under these assumptions, they are equally likely.

Only one sequence gets every answer right. Many sequences get ten right. To evaluate a score of ten, we count all sequences with ten, eleven, twelve, thirteen, fourteen, fifteen, or sixteen correct answers. That asks how often guessing would produce this score or a better one.

The calculation uses the binomial distribution, which describes counts of successes across independent trials with a fixed success probability. [Binomial model](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm)

| Illustrative score | Chance of this score or better under the guessing model |
|---|---:|
| 10 out of 16 | 22.72% |
| 12 out of 16 | 3.84% |
| 13 out of 16 | 1.06% |

These are calculated probabilities, not results from a study. The total number of qualifying sequences for thirteen or more correct is 697. Dividing 697 by 65,536 gives approximately 0.0106, or 1.06%.

That percentage is not the probability that you were guessing. It describes how unusual the result would be if the guessing model applied. It also does not certify that the test was fair. A revealing click or timing difference could help someone identify X without hearing the feature they intended to compare.

## A high score can answer the wrong question

Imagine that version B begins with a small delay. If A starts immediately and B does not, identifying the delay could produce an excellent score. It would not establish that the listener heard a compression artifact in the music.

This is another hypothetical example. It illustrates why a test needs controls as well as a hidden label. If the intended question concerns compression, the files should come from the same source recording and contain the same passage, with their beginnings aligned. Differences in editing, channel layout, or gain can create additional clues.

Formal audio-assessment guidance treats listening conditions, reference material, familiarisation, and level control as parts of the method. ITU-R BS.1116 uses a different assessment procedure from ABX, but it makes the broader point clearly: a listening result depends on how the comparison was constructed. [ITU assessment guidance](https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1116-3-201502-I%21%21PDF-E.pdf)

For a personal test, write down what A and B contain before beginning. Keep the output device, software processing, and volume unchanged. If you are investigating a particular artifact, identify the passage where you expect to hear it during practice rather than searching for a new explanation after each scored trial.

## Why matching levels needs an explanation

Want to see how your own score compares with the table? Prepare two aligned versions of the same short recording, then [try a sixteen-trial blind comparison on WaveLocus](https://wavelocus.com/abx-audio-test). Load the files as A and B, listen to the references, and decide which one matches X on each trial. Keep the completed score, including a result near chance, and use the table above to interpret it.

Before starting, check the level-matching option. RMS means root mean square. For audio samples, it is a measure related to their average squared amplitude. WaveLocus describes its matching as attenuating the file with the higher RMS value. That is a digital-level adjustment, not a guarantee that the two files sound equally loud. Its previews start at sample zero, but the files are not otherwise time-aligned. Remove any unequal leading silence during file preparation.

Those limits matter whichever tool you use. Check its method before treating the score as evidence. A desktop comparator is another option; foobar2000 provides an ABX component for comparing two tracks. [foobar2000 ABX component](https://www.foobar2000.org/components/view/foo_abx)

## Do not keep restarting until a good score appears

The probability table describes one planned session. It does not describe a collection of sessions from which only the best result is reported.

Suppose a hypothetical listener runs twenty independent sixteen-trial sessions while guessing. In each session, the chance of thirteen or more correct is approximately 1.06%. Across all twenty, the chance of getting at least one such score is about 19.3%.

We obtain that by calculating the chance that none of the twenty sessions reaches the score, then subtracting it from one. This assumes independent sessions under the same guessing model. It shows why the best-looking attempt can be misleading when the earlier attempts disappear.

Practising is reasonable. Keep practice separate from the scored session. Choose the number of trials beforehand, complete them, and retain the result. If you stop because you are uncomfortable or tired, record that the session was incomplete. Start at a comfortable, low volume; turning it up is not a substitute for a clearer test question.

## What to say after the test

A strong result from a well-controlled comparison supports a narrow statement: this listener distinguished these signals under these conditions. It does not establish that one version is better, that everyone can hear the difference, or that an upgrade is worth its price.

A result near chance also leaves questions open. The distinction might be too small for this passage, this setup, or this session. Failing to demonstrate it does not prove that the files are identical or say anything clinical about the listener’s hearing.

For an informative report, keep the score beside the file preparation, passage, equipment, level treatment, and planned trial count. Those details let someone judge what you actually tested. Sixteen answers are much more useful when the question they answered is clear.
