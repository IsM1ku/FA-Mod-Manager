//-----------------------------------------------------------------------------
// @notes:
// sc = screen coordinates. Positioned as if screen was 640x480.
// AspectCorrectHUDElementRight/Left correct for off-aspect views, e.g. 720p 
// left and right justified.
//-----------------------------------------------------------------------------

ClearHUDSetup
//-----------------------------------------------------------------------------
// Group 0 draws all elements, regardless of priority
SetCurrentHUDElementGroup 0  

CreateHUDElement BoostGauge
SetHUDElementValidScreenModes "WideScreen Normal SplitScreen Network"
//SetHUDElementData "sc = 79.3653, 73.3592"
SetHUDElementData "sc = 26.5431, 36.7795"
SetHUDElementData "scale = 0.0045"
SetHUDElementData "reverse = false"
SetHUDElementData "iconScale = .18"
SetHUDElementData "iconOffset = 105,0"
SetHUDElementValidStates "Event"
SetHUDElementData "H2H_sc = 95.0, 60.0"
SetHUDElementData "canDrawWhenUnwinding = true"
SetHUDElementData "canDrawWhenDead = true"
AspectCorrectHUDElementLeft

CreateHUDElement UnwreckGauge
SetHUDElementValidScreenModes "WideScreen Normal SplitScreen Network"
//SetHUDElementData "sc = 560.3171, 73.5791"
SetHUDElementData "sc = 613.0697, 37.0477"
SetHUDElementData "scale = 0.0045"
SetHUDElementData "reverse = true"
SetHUDElementData "iconScale = .18"
SetHUDElementData "iconOffset = -105,0"
SetHUDElementValidStates "Event"
AspectCorrectHUDElementRight

/*
CreateHUDElement RearViewMirror
SetHUDElementValidScreenModes "WideScreen Normal Network"
SetHUDElementData "sc = 321.1005, 67.3954"
//SetHUDElementData "sc = 321.3421, 29.5066"
SetHUDElementData "scale = 0.0045"
SetHUDElementData "scaleGains = 1.33333337, 1.33333337, 1.0"
SetHUDElementData "uvScale = 2.0"
*/

CreateHUDElement ArmorGauge
SetHUDElementValidHUDModes "Full"
//SetHUDElementData "sc = 545.4683, 364.1258"
SetHUDElementData "sc = 594.9613, 391.3729"
SetHUDElementData "scale = 0.0045"
SetHUDElementData "SpeedScale = .20"
SetHUDElementData "SpeedSC = 540.0f, 340.0"
AspectCorrectHUDElementRight

CreateHUDElement Reticule
SetHUDElementValidScreenModes "WideScreen Normal SplitScreen  Network"
SetHUDElementValidStates "Event"
//SetHUDElementData "sc = 320.0000, 243.3762"
SetHUDElementData "sc = 320.0000, 244.1174"
SetHUDElementData "scale = 0.0045"
SetHUDElementData "fontId = 1"

CreateHUDElement MapGauge
SetHUDElementValidHUDModes "Full"
SetHUDElementValidScreenModes "WideScreen Normal SplitScreen Network"
SetHUDElementValidStates "Event"
//SetHUDElementData "sc = 87.2521, 367.2905"
SetHUDElementData "sc = 36.1611, 395.2323"
SetHUDElementData "scale = 0.0045"
SetHUDElementData "mapCenterOffset = 13, 0"
SetHUDElementData "mapIconScale = 0.0625"
SetHUDElementData "maxIconDist = 62"
SetHUDElementData "canDrawWhenUnwinding = true"
AspectCorrectHUDElementLeft

CreateHUDElement DamageZoneIndicators
SetHUDElementValidStates "Event"
SetHUDElementData "canDrawWhenUnwinding = false"
SetHUDElementData "Alpha = 0.75"
SetHUDElementData "TBOffset = 60.0"
SetHUDElementData "TBScale  = 1.0, 1.0"
SetHUDElementData "LROffset = 30.0"
SetHUDElementData "LRScale  = 0.75, 1.0"

CreateHUDElement NetOvertimeCountdownDisplay
SetHUDElementValidScreenModes "WideScreen Normal SplitScreen Network"
SetHUDElementData "sc = 320.0, 160.0"
SetHUDElementData "scale = 0.3125"
SetHUDElementData "timeOffset = 0, 0"
SetHUDElementData "timeScale = 1.0"
SetHUDElementData "timeFontId = 2"
SetHUDElementData "canDrawWhenUnwinding = false"
SetHUDElementData "fontId = 1"
SetHUDElementData "canDrawWhenDead = true"
//AspectCorrectHUDElementLeft

CreateHUDElement VOIPTalkersDisplay
SetHUDElementValidScreenModes "WideScreen Normal Network"
SetHUDElementData "sc = 440, 140"
SetHUDElementData "scale = 0.5"
SetHUDElementData "fontId = 1"
SetHUDElementData "alpha = 0.5"
SetHUDElementData "canDrawWhenDead = true"

CreateHUDElement OpponentMarkerDisplay
SetHUDElementValidHUDModes "Full"
SetHUDElementData "leftCornerPivotX = 160"
SetHUDElementData "leftCornerPivotY = 360"
SetHUDElementData "rightCornerPivotX = 480"
SetHUDElementData "rightCornerPivotY = 360"

CreateHUDElement GoalIntroSequence
SetHUDElementValidStates "Intro"

CreateHUDElement RivalIntroSequence
SetHUDElementValidStates "Intro"
SetHUDElementData "totalString = WRECK POINTS"

CreateHUDElement PostRaceSequence
SetHUDElementValidStates "WrapUp"

CreateHUDElement PostRaceStatsSequence
SetHUDElementValidStates "WrapUp"

CreateHUDElement TakedownMessage
SetHUDElementValidStates "Event WrapUp"
SetHUDElementData "sc = 320.0, 155.0"
SetHUDElementData "scale = 1.0"
SetHUDElementData "priority = 4"
//SetHUDElementData "rivalTakedownString = RIVAL EXECUTED!"
//SetHUDElementData "defaultTakedownString = POUNDED!"
SetHUDElementData "duration = .75"
SetHUDElementData "fadeOutTime = .5"
SetHUDElementData "nameTextScale = .5"
SetHUDElementData "nameXOffset = 32"
SetHUDElementData "weaponIconSize = 32"
SetHUDElementData "trailSize = 5"
SetHUDElementData "jitterRate = 5.0"
SetHUDElementData "jitterScale = 10.0"
SetHUDElementData "scaleJitterRate = 10.0"
SetHUDElementData "scaleJitterScale = .15"
//SetHUDElementData "turtleString = TURTLED!"
//SetHUDElementData "crashString = SPLAT!"
//SetHUDElementData "suicideString = SUICIDE!"
//SetHUDElementData "knockoutString = KNOCKED OUT!"
//SetHUDElementData "outtaTimeString = OUT OF TIME!"
//SetHUDElementData "bountyString = BONUS"
SetHUDElementData "canDrawWhenEventComplete = true"
SetHUDElementData "barScale = .25"
SetHUDElementData "barOffset = 0, 5.0"
SetHUDElementData "barSlideTime = .25"
SetHUDElementData "barStartX = -1024.0"
SetHUDElementData "barHoldX = 0.0"
SetHUDElementData "barEndX = 1024.0"
SetHUDElementData "fontId = 10"
SetHUDElementData "rivalPopScale = 2.0"
SetHUDElementData "rivalPopTime = .25"
SetHUDElementData "canDrawWhenDead = true"

//-----------------------------------------------------------------------------
// Group 1 = Messages
SetCurrentHUDElementGroup 1 

CreateHUDElement GoMessage
SetHUDElementValidStates "Event"
SetHUDElementData "sc = 320, 187.5f"
SetHUDElementData "duration = 1.5"
SetHUDElementData "scale = 0.25"
SetHUDElementData "trailSize = 10"
SetHUDElementData "jitterRate = 10.0"
SetHUDElementData "jitterScale = 3.125"
SetHUDElementData "scaleJitterRate = 10.0"
SetHUDElementData "scaleJitterScale = .1"
SetHUDElementData "priority = 8"
SetHUDElementData "canDrawWhenDead = true"

CreateHUDElement CountdownMessage
SetHUDElementValidStates "PreEvent"
SetHUDElementValidGameModes "Race Knockout TimeTrial CatAndMouse Rampage DeathMatch"
SetHUDElementData "sc = 320, 187.5f"
SetHUDElementData "scale = 0.175"
SetHUDElementData "ScaleRange = 0.0, 0.25"
SetHUDElementData "CircleRadius = 50.0, 0.0"
SetHUDElementData "CircleRate = .33333, .33333"
SetHUDElementData "trailSize = 10"
SetHUDElementData "priority = 7"
SetHUDElementData "canDrawWhenDead = true"

CreateHUDElement StatusMessage
SetHUDElementValidStates "Event"
SetHUDElementData "sc = 320.0, 100.0"
SetHUDElementData "scale = 3.5"
SetHUDElementData "priority = 6"
SetHUDElementData "duration = 4.0"
SetHUDElementData "fadeOutTime = 1.0"
SetHUDElementData "trailSize = 10"
SetHUDElementData "entrySpeed = 10.0"
SetHUDElementData "scaleRange = 0, .3125"
SetHUDElementData "dY = 25.0"
SetHUDElementData "fontId = 0"
SetHUDElementData "canDrawWhenDead = true"

CreateHUDElement LapMessage
SetHUDElementValidStates "Event"
SetHUDElementData "sc = 320.0, 100.0"
SetHUDElementData "scale = 3.5"
SetHUDElementData "canDrawWhenEventComplete = true"
SetHUDElementData "canDrawWhenUnwinding = true"
SetHUDElementData "priority = 5"
SetHUDElementData "duration = 4.0"
SetHUDElementData "fadeOutTime = 1.0"
SetHUDElementData "trailSize = 10"
SetHUDElementData "entrySpeed = 10.0"
SetHUDElementData "scaleRange = 0, .3125"
SetHUDElementData "dY = 25.0"
SetHUDElementData "fontId = 0"
SetHUDElementData "canDrawWhenDead = true"

CreateHUDElement SplitTimeMessage
SetHUDElementValidStates "Event"
SetHUDElementValidGameModes "Race CatAndMouse Knockout TimeTrial"
SetHUDElementData "sc = 320.0, 100.0"
SetHUDElementData "scale = 2.5"
SetHUDElementData "priority = 1"
SetHUDElementData "duration = 4.0"
SetHUDElementData "fadeOutTime = 1.0"
SetHUDElementData "trailSize = 10"
SetHUDElementData "entrySpeed = 10.0"
SetHUDElementData "scaleRange = 0, .3125"
SetHUDElementData "dY = 25.0"
SetHUDElementData "fontId = 0"
SetHUDElementData "canDrawWhenDead = true"

CreateHUDElement Teletype
SetHUDElementValidScreenModes "WideScreen Normal Network"
SetHUDElementData "canDrawWhenUnwinding = false"
SetHUDElementData "sc = 4.0, 140"
SetHUDElementData "size = 640.0, 85.0"
SetHUDElementData "scale = 0.5"
SetHUDElementData "fontId = 1"
SetHUDElementData "DrawFrame = false"			//draw the box??
SetHUDElementData "alpha = 0.5"					//overall alpha 0.0 to 1.0
SetHUDElementData "BaseOffset = 1.0"			//Y offset for text inside box
SetHUDElementData "LineAdjust = 0.0"			//spacing between lines
SetHUDElementData "WeaponIconSize = 32.0"		//size of weapon icons
SetHUDElementData "InactiveTime = 5.0"			// ** not used (legacy) **
SetHUDElementData "RemoveTime = 7.0"			//remove items after this time
SetHUDElementData "FadeTime = 0.5"				//how long fade takes

//-----------------------------------------------------------------------------
// Group 2 = Wrong way Message
SetCurrentHUDElementGroup 2

CreateHUDElement WrongWayMessage
SetHUDElementValidStates "Event"
SetHUDElementData "sc = 320.0, 100.0"
SetHUDElementData "scale = .25"
SetHUDElementData "fontId = 1"
SetHUDElementData "priority = 0"
SetHUDElementData "scaleRange = 2,1"
SetHUDElementData "fadeInTime = 1"
SetHUDElementData "trailSize = 5"
SetHUDElementData "Alpha 0.75"

