---
layout: post
title: "Your Mic Test Passed. That Doesn’t Mean Your Meeting App Can Hear You"
date: 2026-10-03
permalink: /articles/your-mic-test-passed/
category: Audio
author: false
reading_time: 3
medium_url: https://medium.com/p/a545337e5736
description: "A moving level bar on a test website shows that your browser received sound. It doesn’t show which microphone your meeting app will use."
---

*A moving level bar on a test website shows that your browser received sound. It doesn’t show which microphone your meeting app will use.*

A microphone test website may pick up your voice even when your meeting app doesn’t. Each can use a different microphone or have different microphone permissions. The test page asks your browser for microphone access and draws a wave or bar when sound arrives. Your meeting app maintains its own device selection and permissions. A passing test site, therefore, can’t confirm that the app is using the same microphone.

### Step 1: Test inside the app you’ll use

**Zoom desktop app.** Open Settings, then Audio. Click **Test speaker** to hear a tone. Click **Test microphone** to record your voice and hear it played back. An input-level bar moves when Zoom picks up sound. Zoom also offers a test meeting.

**Google Meet.** On the pre-join screen, the mic, speaker and camera each have a dropdown. Click the microphone and speak, and Google says a moving bar means the mic works. Click the speaker, then **Test speakers**, to hear a test sound.

Two practical points:

- A level bar shows that sound arrived, not how you sound. Say a full sentence at your normal distance and, where the app offers playback, listen to it.
- Google’s help page warns that mismatched microphone and external speaker devices can cause echo. Use one headset for both where you can.

### Step 2: If something fails, run an independent test

If your meeting app doesn’t pick up your voice, run a browser-based microphone test, such as [WaveLocus’s microphone test](https://wavelocus.com/microphone-test) or [OnlineMicTest](https://www.onlinemictest.com/). You only need one. Allow microphone access, then speak at your normal distance from the microphone. Look for a line or bar that changes as you speak. If the test lets you choose a microphone, select the same one you chose in your meeting app. A response shows that the browser is receiving sound; it doesn’t confirm that the meeting app is receiving it or that your voice sounds clear.

### Step 3: Read the result

- **The browser test responds to your voice, but the meeting app doesn’t.** Check which microphone the meeting app has selected and whether you’re muted. Also, check that the app has permission to use the microphone. If you’re using it in a browser, check permission for that website too.
- **Neither test responds to your voice.** Check the microphone’s physical mute switch and its cable or Bluetooth connection. Make sure each test is using the microphone you intended. Change one thing, then test again.
- **The meeting app picks up your voice, but you can’t hear its speaker test.** Check which speaker or headphones the app has selected, then check their volume and connection.

### What these checks can’t tell you

These microphone and speaker checks don’t show what another participant will hear during a real call. Your connection, the meeting app’s audio processing, and the other person’s speakers or headphones can affect the result. A short test call with another person gives you a better check of the full conversation, though it cannot guarantee every future call will sound the same.

**Sources:** [Zoom: Testing your audio settings](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0062765) · [Google Meet: Before a meeting](https://support.google.com/meet/answer/10409699) · [MDN: getUserMedia()](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) · [OnlineMicTest](https://www.onlinemictest.com/)
