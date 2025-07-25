
// This file (pitaLocal.psc) is run after all the configuration files have run

// When you exit the debug menu (TweakData) these files are created.  
//   Having them "run" here means those settings will take effect the next 
//   time you start the game.

run TweakData_camera
run TweakData_gfx
run TweakData_gfxRad
run TweakData_hud
run TweakData_light
run TweakData_vm
run TweakData_amix

wantX2Controller 1
//x2DisableProps 0
//x2DisableHud 0  	//set 1 if you want to take glam screencaps.

gfxBuildShaderCache 1
//disablePitaNote 1 	// set to 1 for release builds (i.e. builds shipped to pubs)


//g_useWMountPresets 1	// Xenon weapon select menu that uses preset combos
//gfxMipMapsDebug 1 	// set to 1 at launch to enable mip map debug rendering mode
//showscriptstatus 1 	//set 1 to show if any script for the current level has errors on xenon (redtext onscreen)

//--------------
//Tuning Toggles
//--------------

g_useproccam 1 		//setting 0 disables the takedown, jump and death cams
nukeais 0 		//setting 1 disables ais from appearing in the game. Warning! this is moderately unstable!
disableaiweapons 0 	//setting 1 prevents ais from using weapons -- for testing scrubbing/dueling
disableAmbientTraffic 0 //set to 1 to disable driving traffic in the game
//WeaponImpactForceFixSwapXZ 1 //set 0 to disable axis voodoo swapping on rear weapon hits.
//leaveaisactive 1 	//set 1 to allow the ais to use the car throughout. 
//debugShowStreakMultiplier 1 //set 1 to show a basic onscreen multiplier indicator



//---------------------
//QA debugging toggles.
//---------------------
//isDVDBuild 1		//Set this if you want it to behave properly for a DVD. 

isDeveloperBuild 1	//setting 1 enables a variety of tools only appropriate for Devs.
//pitaDebug 1 		//Set to zero for release builds. Shows fps and memory left stats. 
//carverbose 1 		//setting 1 displays various carstats and tire behaviours
//drawAIPositions 1	//setting 1 shows a chart of the relative positions of the ais to the player.
//DrawSafeZone 1	//setting 1 draws a rectangle in the screen that all pertinent info must be printed inside. 

//showInputDebug 1 	//setting 1 enables oncreen visualizer of trigger outputs. (For tuning controller throw responses)

//netverbose 1 		//Setting netverbose 1 shows network stats during gameplay. 
g_permitnathosting 1 	//enables hosting behind strict nat. 

//allowOutOfTimeDeath 0 //Setting zero prevents the demo from timing you out after 5 minutes.
//g_UseXUIPauseMenu 0  //requires isdeveloper to be set on. setting zero for this var uses the qa pause menu with bonus options.

//disableDemoTimeout 1 	//setting 1 disables auto reboot if idling for too long (OXMDemo)

ShowDebugControls 0		//This option will display the DebugControls help text

ShowDebugControls_scale 0.75	//This sets the size of the DebugControls help text (from 0.0 to 1.0)
ShowDebugControls_PosX 1.0	//Sets the x coordinate for the help text display
ShowDebugControls_PosY 1.0	//Sets the y coordinate for the help text display

ShowCamComments_Simple 1	//This option will only display the pack, level and two coordinates

ShowCamComments_Scale 0.75	//This will increase the text size (from 0.0 to 1.0)
ShowCamComments_Opacity 128	//This option allows you to change the transparency of the information's background (from 0-255)
ShowCamComments_PosX 70.0	//This will move the debug text horizontally (by pixel)
ShowCamComments_PosY 80.0	//this will move the debug text vertically (by pixel)

DebugUnwindInfo 1			//Effectively changes the debugUnwind mode into the standard bugging tool


//------------------------------------------
//Game optimization and camera debugging tools.
//------------------------------------------
//textureCacheDebug 1 	//Will indicate the current texture cache usage on screen.  If you see all red bars, then the cache is filling up.  If this happens more on certain levels and corresponds to declining performance at that time, it's worth noting.
//pathDebug 1 		//Will draw the camera paths in the game and prevent out-of-bounds deaths / teleports.  If you go out of bounds and get a camera detach/hiccup, a yellow line will draw from the car to the border of the closest camera path.  Useful for detecting zones where the camera will detach from the car.

//---------------------

// Debug Unbinds
/*
unbind joy0_l3+joy0_dpadup               // pitaDebug 1
unbind joy0_l3+joy0_dpaddown             // pitaDebug 0
unbind joy0_r3+joy0_l3+joy0_l1           // TweakData 1
unbind joy1_r3+joy1_l3+joy1_l1           // TweakData 1
unbind joy0_square+joy0_dpadleft         // gfxDisplayAlpha -1
unbind joy0_square+joy0_dpadright        // DoSingleStep
unbind joy0_square+joy0_dpaddown         // printActiveObjectStats
unbind joy0_dpadright+joy0_l3            // GotoDebugPoint +1
unbind joy0_dpadleft+joy0_l3             // GotoDebugPoint -1
unbind joy0_dpaddown+joy0_l3             // GotoDebugPointNearest    0   // l3+dpaddown
unbind joy0_dpadup+joy0_l3               // GotoDebugPointNearestCam 0   // l3+dpadup
unbind joy0_x+joy0_r3                    // ToggleDebugCam 1
unbind joy0_r1+joy0_r3                   // TeleportToTarget 0   // r3+black
unbind joy0_square+joy0_dpadup           // nukeme 0
unbind joy0_x+joy0_dpaddown              // toggleai 0
unbind joy0_square+joy0_circle+joy0_back // RebootToSystem
*/

//doIntroSequence 0
//g_isDemo 1
g_onlineUseLan 0

//gravityScale 2.1		//Number of Earth Gravities in the world of full auto

//launchmode 1			//dev fe



//	Enable ONLY ONE of these to play Gladiator or Base Assault
//g_deathmatch 1           // Turns on Gladiator
//baseAssaultMode 1        // Turns on Base Assault

//	Enable ALL these options when playing Gladiator or base assault
//tracksFromPix 1
//launchmode 3
//useSpawnPoints 1

//g_deathMatchKills 10     // Sets the number of kills needed to win
//g_healthPickupScale 10.0 // Scales the amount of life that is given back per unit of unwind time used
//g_healthPickupSpeed 3.0  // Scales the speed at which unwind is used up when restoring life

