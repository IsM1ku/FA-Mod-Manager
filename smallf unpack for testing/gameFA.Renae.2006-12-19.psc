// Load the material driving properties matrix
//  - this defines various traction AND drag properties by material
LoadMatDrivPropDesc matdrivpropscript.txt

pitaNet 0
isCel 1
//nukeAis 1
isXb2 1
isFa 1

//ADDED by johnh 9-26-2005!!!!!! Till we can decide if we want all Rivals gamestyle for demo
//doIntroSequence 0


updatedda 1


// display score multiplier debug text
debugShowStreakMultiplier 0
//---------------CAMERA-------------------------------------
camCarVGain 0
//-----END OF---CAMERA-------------------------------------

//--------------------CAT AND MOUSE------------------------
//How to set up: This is the time in seconds that the player will look at the score tile, before respawning.
//The Loosing Mouse respawn delay should not be "too short", but as short as possible.
//The Loosing Mouse should have a shorter respawn than the winning Mouse. 
//The Mice should have a shorter respawn than the cats.
//The Loosing Cat should have a longer respawn than the winning Mouse. 
//The Winning Cat respawn delay should not be "too long"
//Based on a Bug, we have determined that 7 seconds is "too long".

LosingMouseRespawnDelay 	1.75 //default 3
WinningMouseRespawnDelay 	4.5 //default 5
LosingCatRespawnDelay 		4.5 //default 6
WinningCatRespawnDelay 		5 //default 7

SplitMessageInterval 10 //default 10. Frequency of split time display (between cat and opponent mouse)
g_miceExplodeOnDeath 0
//--------END OF------CAT AND MOUSE------------------------

//-----------POWERSLIDE, DRIVING AND STEERING--------------- 
flipcorrectgain 1	//big air stabilizer.

carSlideKe 0.45 // default 0.5	powerslide boost!
downforceScale 1 // default 1 downforce multiplier
carFlightDragGain 0 		// airbrakes! zeroed for now. warning! the default value (if unset) is 5!!!

reverseTurnscale 	.5// default 0.50		Forward steercurve is multiplied by this when driving in reverse. 
reverseGear 		2// default 2 		Gear that reverse emulates for teh purposes of speed limiting.	

brakeStartGain  1 //default 1 When the brake button is first pressed, then the brakes start at this much % of their max power.
brakeEndGain 1.5 //default 1 When the brake button is held, this is the peak multiplier on the brake power that the car can achieve. (Handbrake is driven off the base brake value set in the car.) 
//zeroed for now.
brakeRiseRate 	0.25  //default 0.5 Brakes increase by this much every second. This is the ramp up time to full power. 
brakeFallRate 	4.0  //default 4. Brakes roll off this fast after the player releases the brake button. Basically make this number high. 

reverseTransitionSpeed 6 //the value is in meters per second

g_aiMinBoostUseTime 1 //AIs will wait untiil they have this much boost before using boost.
g_railAccelScale 0.65  //AIs that are railing will accelerate more believeably instead of having instant acceleration. 

g_introAISpeedClamp 50 //during 321, the cars will not go faster than this in mph.
ReSpawnSpeed 50 	   //respawn speed in mph (STU 10-05-06: Reduced from 70)

respawnDelay 2.5       // default 1 -- this is the respawn delay in game time for multiplayer. 
respawndelaySP 1.5     // default 2.5 -- this is the respawn delay in game time for single player. 
respawnDelayAI 2.5     // default 5 -- this is the base respawn delay for AI, and is amplified by the respawn delay gains in the difficulty file. 

secondaryExplodeDelay 1.2          //default 2.0 -- the delay before the player's secondary explosion (Added by STU 10-05-06)
secondaryExplodeDelayAI 1.0        //default 1.0 -- the delay before the AI's secondary explosion (Added by STU 10-05-06)

h2hRespawnDelay 4.0    // respawn delay for players in H2H. (STU 10-05-06: Reduced from 5)
showOnlineScoreOverlay 2.25     //default 3.0 -- (Added by STU 10-05-06)
showScoreOverlay  2.25          //default 3.0 -- (Added by STU 10-05-06)


//----END OF--POWERSLIDE, DRIVING AND STEERING--------------- 


//self damage scale! (1024 is mondo self death, 0 is none.)
selfDamageScale 0
teamDamageScale 1

aiToggleDelay 999999


//------Start of Car Gearing Responsiveness-------------
//These settings are really good -- change at your own risk!!

gearShiftDoIt 1                  //defaults to true         Turns antibogging gear shifting technology on and off
gearShiftPlayersOnly 0           //defaults to false        Turns on for players only
gearShiftLowestGear 2            //defaults to 3            Sets the gear at which the code will trigger (and all gears higher)
gearShiftBoggingTimeout 22       //defaults to 60           This is a delay to retry the bogging code after the game has downshifted. (60 = 1sec approx) This may not be needed now.
gearShiftRPMRatioReduction -0.05 //defaults to -0.05 500RPM Sets the number to reduce the ratio by (to avoid potential oscillation)
gearShiftBoggingDownshiftTimeout 100  //(defaults to 60)	    This is a slight delay after upshifting before starting to check for bogging. This is needed to prevent double upshifting.

//--------End of Car Gearing Responsiveness-------------


//--------Start of collision settings-------------------
//General game feel -- environment -- punishing vs believability

collisionDmgGainWorld 					40.0  //(default 10.f) 	Modulates damage applied by world objects (e.g. solid walls) to objects that run into them.
collisionDmgGainTraffic 				2.0   //(default 12.f) 	Modulates damage applied by traffic to objects that run into them.
g_ambientTrafficDensity					0.5   //(default 1) Reduce or increase the traffic game wide by some amount. (Short ceiling tuning syndrome) Choose the level with the most traffic and apply nerf to make it acceptable. 


//Ramming through destroyables and falling destroyables!
collisionDmgGainDestroyables 			0.1   //(default 8.f) 	Modulates damage applied by destroyables (e.g. lamp posts) to objects that run into them.
collisionDmgPropSpeedGain 				 12    //This multiplier is applied to the speed of a prop when computing damage dealt by that prop, only effective if the prop is moving towards its target
collisionDmgPropFallVGain 			     12    //This multiplier is applied to the DOWNWARD speed of a prop when computing damage dealt by that prop, only effective if the prop is moving downwards
collisionDmgPropSpeedThresh 		    512    //Threshold below which prop damage is capped.  The units vary as they are compared to a combination speeds effected by propSpeedGain and FallVGain

//Ways to prevent death by 1000 papercuts!
minorCollisionDmgThreshold 				0.65  //(default .8f) 	Controls the degree to which your armor can be destroyed by 'minor' damage
collisionDeathSpeedThreshold			110	  //(default 72)	This is the speed at which the player dies outright if he runs into a wall.
collisionDmgAutokillThresholdPVP        999   //(default 120)   When two hero cars collide above this speed, one will be autokilled.
collisionDmgMinorSpeedThreshold			50	  //(default 30) 	Speed at which hitting the world is no longer a fender bender -- it does Major class damage.

//Car vs car class damage rewards!
collisionGainCarVeryLow					1.79  //Streamline, Sceptre does this much extra damage to everything.
collisionGainCarLow						2.34  //Vulcan, Inferno does this much extra damage to everything.
collisionGainCarMed						2.85  //Honcho, Guardian does this much extra damage to everything.
collisionGainCarHigh					3.16  //Hookzilla does this much extra damage to everything.
//Please not that the cars also resist damage taken, I am currently trying to get this moved into pscs. 
//The reason the resistance is important is because the speed at which a winner is declared is modified by the values above,
// whereas the resistance tables are not factored into the speed calcs. 

//Winner/Looser car vs car damage rewards!
collisionDmgGainHeroVsHeroLoser			0.70  //(default 4.f) 	Modulates damage applied by competitor objects to other competitor objects they run into.                           
collisionDmgGainHeroVsHeroWinner		1.9   //(default 4.f) 	Modulates damage applied by competitor objects to other competitor objects they run into.                           
collisionDmgWinnerSpeedDelta			20	  //(default is 20) If the delta speed (in mph) is lower than this, there is no "winner".  

//One potential problem that I foresee here is that if the gains are high enough that falling debris will damage you, super very fast moving debris is likely to kill you in one hit.  We may want to clamp the max computed speed?

//The collision properties of individual packs can also be tuned using the 'collisionDamageGain' and 'damageFromPhysicalGain' variables available in collision reps.
//collisionDamageGain affects how much damage a pack inflicts on things it runs into.
//damageFromPhysicalGain affects how much damage a pack suffers after running into things.
//Note: There are eight settings available for each of these variables.  Four of the settings are designed specifically for use with player cars. 
//--------End of collision settings---------------------


//------Start of Rewind and Turbo settings--------------
//REWIND
//maximum time the player can unwind for
unwindMaxTime 8.0

//Starting energon 
startingUnwind 8.0

//Unwrecking Clock speed
unwindTimeScale 2.5

//When a destruction camera occurrs, then this amount of time is rewound after playing the glamour camera.
//Added end of project, so leaving commented out.
//g_DestructionRewindTime -3.4   //Default set by Rob, -3.4. Note, if this is commented, then the value is also -3.4 seconds via hardcoded setting.


//Unwrecking Clock replenish
UnwindDefault 8.0
scoreUnwindGain 0.0025
takedownUnwindGain 0

//Wreck Total multipliers
competitorScoreMultiplier 10
carScoreMultiplier 2.5
decorationScoreMultiplier 1
gagScoreMultiplier 1
worldScoreMultiplier 5
landmarkScoreMultiplier 5

//TURBO

//AI AND BOOST.
//frequency that AIs are offered boost which they use at their discretion.
//Lower numbers are less frequent use. 
boostAIGain 0.1
//at start of event AIs wont use boost for this many seconds.
boostMinGameTime 45

//LEGACY/BROKEN
boostMinSpeed -1024 	//legacy, disabled -- Minimum speed that must be maintained in order to remain boosting in mph
//boostResetOnDeath 0 	//(false), "reset boost to default on death" I dont think this works right now.

//MAIN BOOST TUNING - ACTIVATING AND USING BOOST
//Boost is now set up according to the "Boolean" mechanic. You have it, you use it and get a pop, then you don't have it anymore.
//Boost is reimagined! When the player is below 50 he gets a pop to 50, when the player is above 50 he gets only the engine doubler. The player has between 6 and 3 seconds of boost. The player can collect boost and use it partially at anytime. 

boostDefault 0.5  		//amount of boost player starts with in seconds          
boostBoltSpeed 25	   	//this is the speed boost the player can get if he uses boost while he is below the boost speed cap (50). 
boostBoltMaxSpeed 30	//max amount of speed you can boost bolt to in mph
boostBoltSpeed 15		//instant speed boost given on boost activation
boostMaxTime 6.0		//max amount of boost that can be accrued in seconds. This works with the boostbolt to calculate the boostbolt that smaller tanks get.
boostCooldownTime 1.00 	//"cooldown period, during which boost cannot be activated, in secoonds." 
boostMinTime 0  		//you must have this much boost in seconds to see boost or use it. 

//BOOST REPLENISH TABLES
//Note use a table of zeros to isolate rewards for tuning. eg:
//SetBoostGains "slide 		0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0"

disableBoostDeltaThrottle 0 //Awards boost in seconds(1) or percent(0) of tank. 

//Tuning notes: 
//Tuning for the largest size ganks the smaller tanks on gain rate.
//We tried 4x difference in size and this penalized the small tank cars too heavily. 

//Treat spin as a bonus for completing 360s.
//Spin awards disabled for now (over rich and we need to frame tank sizes).
SetBoostGains "slide 		0.75 	 0.75	 0.75 		0.75 	0.75 	0.75 	0.75		 0.75	  0.75		 0.75"
SetBoostGains "jump 		1 		1 1.5	1.5 2.0 	2.5 3 		3.5 4.00 	5"
SetBoostGains "twowheels 	0.00 0.00 0.00 00.0 00.00 00.00 00.00 00.00 00.00 00.00"
SetBoostGains "spin 		0.00 0.00 0.00 0.00 0.000 0.000 0.000 0.000 0.000 0.000"
SetBoostGains "roll 		0.00 0.00 00.0 00.0 00.00 00.00 00.00 00.00 00.00 00.00"
SetBoostGains "flip 		0.00 0.00 00.0 00.0 00.00 00.00 00.00 00.00 00.00 00.00"
//------End of Rewind and Turbo settings-------------

//------------AI Aiming-------------
//This was added end of project 10/10/2006 so we left it off due to safety. This should be turned on for future projects.
//g_aiAutoAim 0 //When set to 'g_aiAutoAim 1' the ai's secondary weapon autoaims like the player. This value defaults to off.
//----End of----AI Aiming-------------

//----Start of AI DDA settings------
//--DDA settings for AI difficulty--
//UPDATE: 2005-04-20: Ja sez: these are the new dda pscs and values.  
//sample defaults: 
//SAMPLE: DDAValueKeys ".5 1.0 2.0"
//SAMPLE: DDADistanceKeys "-128 0 128"
//2.0 is the maximum. If you want more response than that, then set the distance shorter.

//Ingame DDA

//g_DDAValueKeys "0.75 1.05 2.0" 
//g_DDADistanceKeys "-400 -8 16 128"


//No DDA
//DDAValueKeys "1.0 1.0 1.0" 
//DDADistanceKeys "-160 -32 16 256"
//easy
//g_DDAValueKeys "0.55 1.1 1.4" 
//g_DDADistanceKeys "-160 -32 10 256"
//ahead they suck a lot. behind they are not great at catching up. they will pass when neck and neck
//hard
//g_DDAValueKeys "1 1.25 2.0" 
//g_DDADistanceKeys "-128 -32 64 256"
//ahead they are good they can get away. behind they are good, and neck and neck they are great.

//ArcadeDDA defaults added 12-9-2005

arcadeDDAValueKeys0 	"0.955 1.010 1.05"
arcadeDDADistanceKeys0 	"-54 -10 32 48"
//															spacer for legibility
arcadeDDAValueKeys1 	"0.972 1.010 1.06" 
arcadeDDADistanceKeys1 	"-64 2 24 76"
//															spacer for legibility
arcadeDDAValueKeys2     "0.985 1.005 1.04" 
arcadeDDADistanceKeys2  "-24 -14 24 78"

//-----------CheatGain Handles---------------------------
//This section goes with the ddavaluekey settings from above.
//This section describes which parameters of the car become better, and by how much when the car gets buffed up by the cheatgain.
//Generally, this is used to set the scope of just how cheated the AIs will get when they are too good or suck too much.

//Usually some AI buffing is acceptable even at neck and neck, because after all, the AI is blind. 
//Max is when the AI needs help. 
//If you set MAXes too high the AI can't cope with superheroic abilities and crashes, falling behind even more.
//Min is when the AI is too good and needs to be slowed down. 
//Very low numbers here will make the AIs wipe out soon after passing the player. This can also make the game too easy. 

//UPDATE JH-2005-04-20: well i met with Jason to try to understand the interplay between the Valuekey multiplier 
//and its infleuence on the cheats below. 
//The most current information I have is that the (Valuekey)-1 X the GainMAX X the item affected = your cheat result. 
//using the active numbers here are some sample results:
//eg Vulcan that sucks is getting (3-1)X1.9X350hp = 1330 horsepower! when it sucks (512 meters behind). 
//By the same math when the car rocks it is getting (0.5-1)X0.4X350hp = -87.5 horsepower! when it rocks (128 meters ahead).
//This just seems wrong.
//Ja said, "It's gonna change soon, just massage the numbers and wait for the update."  


//Settings last modified by J.Harley 2005-2-20
//Modifies the PeakPower on the AI.
//This is one of the safer and better handles for tuning AI gain.
//DDAAiAccelGainMin 0.7
//DDAAiAccelGainNorm 1
//DDAAiAccelGainMax 8.5

//Modifies the Downforce on the AI 
//Note: the race speed amplifies this cheat geometrically as average speed goes higher. Be careful.
//If you are driving very fast and you see cars swerving back and forth unrealistically, and you are not able to knock them around,
// your DownforceGain is too high.
//Generally I would say you want to undergain the AIs so the player will have more infleuence as the cars go faster,
// but this strongly affects cornering ability at high speed, so your range is limited here.
//DDAAiDownforceGainMin 0.9
//DDAAiDownforceGainNorm 1.25
//DDAAiDownforceGainMax 4.0

//Modifies Tire Traction on the AI. 
//Note: As the cars go faster traction still helps but falls off in favor of downforce.
//A pretty decent handle, especially for cars that suck.
//DDAAiFrictionGainMin 0.9
//DDAAiFrictionGainNorm 1
//DDAAiFrictionGainMax 1.5



//Modifies the Drag on the AI car.
//Please note that for Drag Gain the Min/Max is named inversely (bug).
//This means that Min drag is when the AI is AHEAD and MAX drag is when they are behind. 
//Also note that when Drag gets too high it can artificially speed-limit the cars. 
//this is not really a good handle. 
//DDAAiDragGainMax 1.0
//DDAAiDragGainNorm 1.0 
//DDAAiDragGainMin 1.0
//Finally, there are more CG DDAA handles in MOD -- type wtff DDAA to get a full list. Those handles are for weapon abilities of the AIs. Since we don't use weapons they do not affect the AIs performance. 




//UPDATE!!! 2005-04-20: Ja sez: the dda stuff below here is no longer used. 
//Settings last modified by J.Harley 2005-2-20
//aboveCGStep 0.45
//sets how frequently AIs that are behind will try to pass. Default 0.15
//belowCGStep 1
//this sets how long it takes to catch up to the winner, as well as all others. Default: 2 
//middleDDA 1.01
//This sets overtake speed of passing cars, however too low and the cars cannot pass. Default: 1.01
//----End  of AI DDA settings------




//[dh] disabled setting strPil in here, because we need different pil for PS3 -- it's initialized properly in
//code anyways, so no point overriding it.
// REM Renae	Added again for the demo
strPil "fa_demopil"

shared "S:\DEV\FA"
//disableHud 0



femDamageThresh 8


bind p profileToggleDisplayMode
bind t TweakData 1
//profileIfPaused 1

//disableCameraLoops 1

// Keyboard stuff
bind 1 femDraw -1

	

musicVolume 1.0
soundfxvolume 0.5
reverbGain 0.625
XAudioGain 1.0

light_dir "0.5 0.30  -1"

fontGame "fontGameFullAuto"

execute_psc "controlsFA.psc"	 // runs script	that binds controls

///DEBUG/// run DebugPoints

execute_psc "FAHUDSetup.psc"
execute_psc "CarColors.psc"


if isRunTimeEXE

		wantX2Controller 1
		controllerDeadZone .25

		dxUsedManagedResources 0
		gfxPureDevice 1
		// VIDEO
	
		
		dontSkipUi 0

		//DEBUG
		fpuVerbose 0
		pitaDebug 0

		//Settings

		background_color 0
		specialIconScale 48
		specialIconSpacing 0
		pitchInvert 1
		doIntroSequence 1
	if targetPlatform EQU 3

	   dxFullScreen 1
		dxRefreshRate 60
	endif
else
	isDeveloperBuild 1
	run dev 
endif

num_laps 3
num_frags 10
run MorphingWeaponSetup

//reticulesize!! default is 0.15 (hard to see), 0.22 clips over the car in some cases
g_reticulescale .15

//camerafovsetting 0.41 // this should be set via VFXDefaults now.

DDAMercyDistance "-2048 2048"

run PitaText_mapping

LoadScript "VFXScript.txt"
LoadScript "DifficultyScript.txt"

//ADDED by milesh 13-06-2006!!!!!! We can now control scoring in Deathmatch type events here.
killScore 2
deathPenalty 1

//ADDED by milesh 10-05-2005!!!!!! We can now control how long it takes for the player car to respawn after death.  Default time was set to 4.5 sec
//respawnDelay 5.0  (STU: Commented out 10-05-2006.)

demoMatchDuration 321

//--------------------------------------------------------------------------
// these are the steering curve spline points.
// there must be eight points per curve
// they are set at 20mph each:  0,20,  40, 60,  80,    100,  120,  140
// car name spelling and the quotes are important!
graphmaxspeed 200 //make the graph show increments of 20 and go to a max of 200
//--------------------------------------------------------------------------
maxTurnScaleDelta 0.07  //(default = .125, max 1, min 0 disables the curve)

SetCarSteerCurve "Executioner	1 0.99 0.80 0.48 0.068  0.02  0.01  0.01"	/D
SetCarSteerCurve "Warlord 		1 0.9  0.80 0.38 0.12   0.08 0.05  0.05"

SetCarSteerCurve "Outlaw 		1 0.90 0.65 0.38 0.15   0.095 0.09  0.09"	/D
SetCarSteerCurve "HSK75			1 0.90 0.65 0.38 0.15   0.1   0.1   0.1" 	/D
SetCarSteerCurve "Sceptre 		1 0.95 0.80 0.32 0.10   0.1   0.1   0.1"   /DR

SetCarSteerCurve "Demon 		1 0.9  0.6 0.21 0.1   0.06 0.05 0.05" 	/D
SetCarSteerCurve "Wraith 		1 0.85 0.62 0.35 0.15   0.12  0.11  0.112" 	/D
SetCarSteerCurve "Streamline	1 0.9  0.59 0.18 0.05   0.05  0.03  0.03"	/D
SetCarSteerCurve "Kinetik 		1 0.95 0.75 0.45 0.11   0.04  0.025 0.028"  /D
SetCarSteerCurve "Inferno 		1 0.9  0.65 0.35 0.08   0.03  0.03  0.03" 	/D


SetCarSteerCurve "Phantom 		1 0.95 0.7  0.35 0.14   0.06  0.02  0.02"		/D
SetCarSteerCurve "Ardent 		1 0.9  0.80 0.22 0.035  0.010 0.007 0.007" 		/D
SetCarSteerCurve "Enforcer 		1 0.9  0.65 0.50 0.30   0.14  0.12  0.12" 		/DR
SetCarSteerCurve "Thunderhawk	1 0.95 0.75 0.38 0.07   0.04  0.03  0.03"    	/D
SetCarSteerCurve "Vulcan 		1 0.95 0.8  0.4  0.12   0.05  0.02  0.02"  		/D
SetCarSteerCurve "Tec	 		1 0.90 0.65  0.350 0.10  0.04 0.02 0.02" 		/D
SetCarSteerCurve "Opulent 		1 0.95 0.75 0.5  0.13   0.04  0.0065  0.0065"	/D
SetCarSteerCurve "Python 		1 0.93 0.68 0.38 0.10   0.025 0.015 0.015"		/D
SetCarSteerCurve "Hitman 		1 0.99 0.62 0.30 0.05   0.01  0.005 0.005"		/D
SetCarSteerCurve "Magnus 		1 0.9 0.75  0.45 0.08   0.02  0.008 0.008"		/D


SetCarSteerCurve "Jupiter 		1    0.9  0.8  0.55 0.15  0.095 0.07  0.07" 	/D
SetCarSteerCurve "Roughneck 	1    0.92 0.70 0.45 0.15  0.095 0.06  0.06" 	/D
SetCarSteerCurve "Guardian	 	1    0.95 0.8  0.45 0.10  0.065 0.05  0.042"	/D
SetCarSteerCurve "Honcho 		1    .95  0.9  0.35 0.03  0.02  0.02  0.02" 	/D
SetCarSteerCurve "Rampart	 	1 0.86 0.65 0.35 0.10  0.08 0.045 0.040"	/DR
SetCarSteerCurve "Kodiak 		1    0.9 0.65  0.25 0.01  0.003 0.002 0.0025"   /D
SetCarSteerCurve "Hookzilla 	1    0.9 0.60  0.22 0.04  0.013 0.011 0.011"	/D

// they are set at 20mph each:  0,20,  40, 60,  80,    100,  120,  140


// dsw: moved run CareerScript.psc to pita.psc and mod.psc, must be after the pitaLocal.psc 
// These settings added by DanielT on 09-28
// They are defaults which make the game run "retail" unless there is a pitaLocal.psc
// which says otherwise.

// Launch the game into the DEMO front end rather than DevUI
// g_LaunchMode 2 //[rwbm]: Don't set a default here.. demo builds need to be compiled as such.

// Disable this for improved performance -- think this is the default in code... (DanielT)
gfxFSAA 1

// Controller settings
controllerDeadZone 0.2
g_ps3InvertPitch 0

// Here just to be safe. It's false in code but we've always used true in pitaLocal
disableThreadedRendering 1

// piExec disabled for retail builds
enablePiExec 0

// Other debug stuff disabled by default
disablePitaNote 1
pitaDebug 0
isDeveloperBuild 0