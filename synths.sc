s.boot;
s.scope(2);

(

SynthDef("grain", { |out, amp=0.1, freq=20, sustain=0.001, pan|
	var snd = LFSaw.ar(freq);
	var amp2 = amp * AmpComp.ir(freq.max(50)) * 0.1;
	var env = EnvGen.ar(Env.perc(sustain, 0.09), doneAction: 2);
	OffsetOut.ar(out, Pan2.ar(snd * env, pan));
}, \ir ! 5).add;



)

//Testing and exploring the synth

(
Pbindef(\grainplayer,
	\instrument, \grain, \sustain, 0.001, \freq, 20, \pan, 0.0, \dur, 0.25,
).play;
)

// change pattern
Pbindef(\grainplayer, \dur, Pn(Prand(#[0.1, 1.0, 4, 2, 0.5, 3], inf)));
Pbindef(\grainplayer, \dur, Pn(Prand(#[0.1, 0.4, 0.3, 2, 0.5, 0.3], inf)));


Pbindef(\grainplayer, \dur, 0.01);


// panning
Pbindef(\grainplayer, \pan, Pn(Pseq([-1.0, 1.0])));
Pbindef(\grainplayer, \pan, Pn(Pseq([-1.0, 1.0, 0.0, 0.5, -0.5])));