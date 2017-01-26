s.boot;
s.scope(2);

(

SynthDef("grain", { |out, amp=0.1, freq=20, sustain=0.001, pan|
	var snd = LFSaw.ar(freq)*amp;
	var env = EnvGen.ar(Env.perc(sustain, 0.0000001), doneAction: 2);
	OffsetOut.ar(out, Pan2.ar(snd * env, pan));
}, \ir ! 5).add;


SynthDef("grain2", { |out, amp=0.8, freq=440, sustain=0.01, pan|
	var snd = FSinOsc.ar(freq);
	var amp2 = amp * AmpComp.ir(freq.max(50)) * 0.5;
	var env = EnvGen.ar(Env.sine(sustain, amp2), doneAction: 2);
	OffsetOut.ar(out, Pan2.ar(snd * env, pan));
}, \ir ! 5).add;

SynthDef("noiseburst", { |out, amp=0.1, sustain=0.01, pan|
	var snd = PinkNoise.ar(1.0);
	var amp2 = amp * AmpComp.ir(1.max(50)) * 0.5;
	var env = EnvGen.ar(Env.sine(sustain, amp2), doneAction: 2);
	OffsetOut.ar(out, Pan2.ar(snd * env, pan));
}, \ir ! 5).add;


)

//Testing and exploring the synth

(
Pbindef(\grainplayer,
	\instrument, \noiseburst, \amp, 0.3, \sustain, 0.02, \pan, 0.0, \dur, 0.08,
).play;
)

(
Pbindef(\grainplayer,
	\instrument, \grain, \freq, 5000, \amp, 0.3, \sustain, 0.02, \pan, 0.0, \dur, 0.08,
).play;
)

// change pattern
Pbindef(\grainplayer, \dur, Pn(Prand(#[0.1, 1.0, 4, 2, 0.5, 3], inf)));
Pbindef(\grainplayer, \dur, Pn(Prand(#[0.1, 0.4, 0.3, 2, 0.5, 0.3], inf)));


Pbindef(\grainplayer, \dur, 0.01);


// panning
Pbindef(\grainplayer, \pan, Pn(Pseq([-1.0, 1.0])));
Pbindef(\grainplayer, \pan, Pn(Pseq([-1.0, 1.0, 0.0, 0.5, -0.5])));

Pbindef(\grainplayer, \pan, Pn(Prand(#[-1.0, 1.0, 0.0, 0.24, 0.5, -0.5], inf)));




