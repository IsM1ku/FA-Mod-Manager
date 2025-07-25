//
//  MENU
//

/////////////////////////////////////////////
// Level
pitaMenuSub Level
pitaMenuName ListGroups
pitaMenu "auto~tree.active.Groups*.treeView"

pitaMenuSub Level
pitaMenuName DoRadiosity
pitaMenu "auto~tree.active.DoRadiosity"

pitaMenuSub Level
pitaMenuName AddNewLevelStuff
pitaMenu "open rh_NewLevel"

pitaMenuSub Groups
pitaMenuName funcPacks
pitaMenu "auto~tree.active.Groups.Funcs.packs*.treeview"


/////////////////////////////////////////////
// Packs
pitaMenuSub Packs
pitaMenu InvertSelectedPacks

pitaMenuSub Packs
pitaMenuName "Hide Selected"
pitaMenu "auto~selected.ModHide=1"

pitaMenuSub Packs
pitaMenuName "Unhide Selected"
pitaMenu "auto~selected.ModHide=0"

pitaMenuSub Packs
pitaMenuName "Unhide All"
pitaMenu "auto~tree.active.ed_pack.ModHide=0"

pitaMenuSub Packs
pitaMenu DupeSelected

pitaMenuSub Packs
pitaMenuName SetupWatchAsRoad
pitaMenu "run MakeRoadSection"

pitaMenuSub Packs
pitaMenuName SetupWatchAsRoadSubPiece
pitaMenu "run MakeRoadSectionSubPiece"

pitaMenuSub Packs
pitaMenuName ListHullsOfSelected
pitaMenu "auto~selected.ed_cld_hull.listview"

pitaMenuSub Packs
pitaMenu MountSelectedToAllSelectedRoadPacks


/////////////////////////////////////////////
// AI
pitaMenuSub AI
pitaMenu "ShowAis"
pitaMenuSub AI
pitaMenu "toggleWatch 0"
pitaMenuSub AI
pitaMenu "DrawPathMap"
pitaMenuSub AI
pitaMenu "gaitInc"
pitaMenuSub AI
pitaMenu "toggleWatchVerbosity 0"
pitaMenuSub AI
pitaMenu "toggleWatchVerbosity -1"
pitaMenuSub AI
pitaMenuName "Insert Checkpoint to watch"
pitaMenu "auto~watch.AddFunc(ef_checkpoint,cp0,1)"

/////////////////////////////////////////////
// VSD
pitaMenuSub VSD
pitamenu PushSelectedExtents

pitaMenuSub VSD
pitaMenuName "VSD Room"
pitaMenu "run VSDroom"

pitaMenuSub VSD
pitaMenuName "VSD Room Box"
pitaMenu "run VSDroomBox"

pitaMenuSub VSD
pitaMenuName "VSD Room Selected"
pitaMenu "run VSDroomSelected"

pitaMenuSub VSD
pitaMenuName "VSD Door In X"
pitaMenu "run VSDdoorX"

pitaMenuSub VSD
pitaMenuName "VSD Door In Y"
pitaMenu "run VSDdoorY"

pitaMenuSub VSD
pitaMenuName "VSD Door In Z"
pitaMenu "run VSDdoorZ"


/////////////////////////////////////////////
// Mesh/Texture
pitaMenuSub Mesh
pitaMenuName "ShowSelTextures"
pitaMenu "auto~selected.Meshes*.Surfaces*.Textures*.treeView"

pitaMenuSub Mesh
pitaMenuName UnsmoothSelected
pitaMenu "auto~selected.Meshes*.Unsmooth()"

pitaMenuSub Mesh
pitaMenuName ApplyTempTextureToSel
pitaMenu "run ApplyTempTexture"

pitaMenuSub Mesh
pitaMenuName DelAllSurfacesFromSel
pitaMenu "auto~selected.Meshes*.Surfaces*.Remove"

pitaMenuSub Mesh
pitaMenuName SetSelectedEmissive
pitaMenu "auto~selected.Meshes*.Surfaces*.Textures*.ColorEmissive=0.25 0.25 0.25"

pitaMenuSub Mesh
pitaMenu CombineEqualTextures 

/////////////////////////////////////////////
// Misc
pitaMenuSub Miscellaneous
pitaMenuName AddComment
pitaMenu "run AddComment"

pitaMenuSub Miscellaneous
pitaMenuName MoveSpawnPoints
pitaMenu "auto~tree.all.dwSpawnPoint.GB.C.load()"

pitaMenuSub Miscellaneous
pitaMenuName AddSpawnPoint
pitaMenu "insert dwSpawnPoint"

pitaMenuSub Miscellaneous
pitaMenuName DrawCollisions24m
pitaMenu "kdop_draw_cull_dist 24"

pitaMenuSub Miscellaneous
pitaMenuName DrawCollisions1000m
pitaMenu "kdop_draw_cull_dist 1000"

pitaMenuSub Miscellaneous
pitaMenuName CutScenePaths
pitaMenu "run CutScenePaths"

pitaMenuSub Miscellaneous
pitaMenuName MakeElevator
pitaMenu "run make_elev"

pitaMenuSub Miscellaneous
pitaMenu "lodDistanceGain 0.1"

pitaMenuSub Miscellaneous
pitaMenuName InvalidateAllRTS
pitaMenu "invalidateallrts"

pitaMenuSub Miscellaneous
pitaMenuName DisownSelected
pitaMenu "auto~selected.Disown"

pitaMenuSub Miscellaneous
pitaMenuName CheckoutSelected
pitaMenu "auto~selected.Checkout"


/////////////////////////////////////////////
// Runtime
pitaMenuSub Runtime
pitaMenu "TeleportToTarget 0"
pitaMenuSub Runtime
pitaMenu "slow_down"
pitaMenuSub Runtime
pitaMenu "TeleportToCamera 0"
pitaMenuSub Runtime
pitaMenu "time_scale 1.0"

/////////////////////////////////////////////
// FullAuto

if isFA


	// DOCS
	pitaMenuSub FullAuto
	pitaMenuName FA_DocsFolder
	pitaMenu "GotoUrl~S:\__PIDS__\FullAuto\FA_VSS_MIRROR\"



endif // isFA

/////////////////////////////////////////////
// DebugPoints
pitaMenuSub DebugPoints
pitaMenuName NextDebugPoint
pitaMenu "GotoDebugPointMod +1"

pitaMenuSub DebugPoints
pitaMenuName PreviousDebugPoint
pitaMenu "GotoDebugPointMod -1"

pitaMenuSub DebugPoints
pitaMenuName ToggleDebugPoints
pitaMenu "GotoDebugPointMod 0"

pitaMenuSub DebugPoints
pitaMenu "GotoBug"

pitaMenuSub DebugPoints
pitaMenu "MakeTempDebugPoint"

pitaMenuSub DebugPoints
pitaMenu "GotoDebugPointNearestMod"

/////////////////////////////////////////////
// other

pitaMenuName TreeSelected
pitaMenu "auto~selected.TreeView()"

pitaMenuName MultiPSC
pitaMenu "MultiPSC"

/////////////////////////////////////////////
// Booleans

pitaBool "drawRacePaths"
AddHotKey~"drawRacePaths" 0 1 

pitaBool "drawDetourPaths"
AddHotKey~"drawDetourPaths" 0 1 

pitaBool "drawAIPaths"
AddHotKey~"drawAIPaths" 0 1 

pitaBool "drawCameraPaths"
AddHotKey~"drawCameraPaths" 0 1 

pitaBool "drawScriptingPaths"
AddHotKey~"drawScriptingPaths" 0 1 

pitaBool "drawCustomPaths"
AddHotKey~"drawCustomPaths" 0 1 

pitaBool "drawConstructionPaths"
AddHotKey~"drawConstructionPaths" 0 1 

pitaBool "treePacksByL1"
AddHotKey~"treePacksByL1" 0 1 

pitaBool "drawCldPortals"
AddHotKey~"drawCldPortals" 0 1 
 
pitaBool "drawCldRooms"
AddHotKey~"drawCldRooms" 0 1 

pitaBool "drawCldNormal"
AddHotKey~"drawCldNormal" 0 1 
 
pitaBool "ShowComments"

pitaBool "SelectWholeHull"
pitaBool "SelectOnlyVisibleHulls"

pitaBool "PlayerInvisible"

pitaBool "noDialog"

pitaBool "gfxReflections"

pitaBool "lazyTextureUpdate"

//////////////////////////////////
// Placement Tool Items


// Example filters
addObjectFilter       "*"
addObjectFilterName   "All Props"
addObjectFilter       "FA*"
addObjectFilterName   "All FA"
addObjectFilter       "FA*hwy*"
addObjectFilterName   "HWY's"
addObjectFilter       "??_FX_*"
addObjectFilterName   "Effects"
addObjectFilter       "fa_PRP*"
AddObjectFilterName   "Props"
AddObjectFilter       "fa_*genbldg*_??"
AddobjectFilterName   "Generic buildings"
AddObjectFilter       "dt_*"
AddobjectFilterName   "Old dt_ Props"

//////////////////////////////////
//////////////////////////////////
run localMenuOptions

LoadScript "wmountscript1.txt"
