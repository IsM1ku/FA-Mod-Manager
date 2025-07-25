if isDeveloperBuild

	bind joy0_r3+joy0_dpaddown printActiveObjectStats
	bind joy1_r3+joy1_dpaddown printActiveObjectStats
	bind joy0_l3+joy0_dpadup pitaDebug 1
	bind joy0_l3+joy0_dpaddown pitaDebug 0
	bind joy0_r3+joy0_l3+joy0_l1 TweakData 1
	bind joy1_r3+joy1_l3+joy1_l1 TweakData 1
	bind joy0_square+joy0_dpadleft gfxDisplayAlpha -1
	bind joy0_triangle+joy0_dpadleft g_UseXUIPauseMenu -1
	bind joy0_circle+joy0_dpadleft g_DrawRaceData -1
	bind joy0_circle+joy0_dpadright toggleWatchHeros 0
	bind joy0_square+joy0_dpadright DoSingleStep
	bind joy0_square+joy0_dpaddown printActiveObjectStats
	bind joy0_dpadright+joy0_l3 GotoDebugPoint +1
	bind joy0_dpadleft+joy0_l3  GotoDebugPoint -1
	bind joy0_dpaddown+joy0_l3  GotoDebugPointNearest    0   // l3+dpaddown
	bind joy0_dpadup+joy0_l3    GotoDebugPointNearestCam 0   // l3+dpadup
	bind joy0_x+joy0_r3 ToggleDebugCam 1
	bind joy0_square+joy0_r3 TeleportToTarget 0   // r3+black
	bind joy0_square+joy0_dpadup nukeme 0
	bind joy0_x+joy0_dpaddown toggleai 0
	bind joy0_triangle+joy0_dpadright toggleai 0
	bind joy0_square+joy0_circle+joy0_back RebootToSystem
	bind joy0_r3+joy0_l3 ShowDebugControls -1

	run DebugPoints.psc
else

	// these shouldn't be on, but just in case.
	pitadebug 0
	disablePitaNote 1
	gfxBuildShaderCache 0
endif
