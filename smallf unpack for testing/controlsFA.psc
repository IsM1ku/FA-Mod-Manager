//---------------------------------------
//  FA - Xbox controller controls
//---------------------------------------

// Trigger key:

// pX_turn = turn
// pX_pitch = pitch
// pX_strafe = camera?
// pX_rudder = camera?
// pX_crouch = look back
// pX_thrust = +/-  gas/brake
// pX_trigger_0 = primary
// pX_trigger_1 = secondary
// pX_trigger_2 = fire super weapon
// pX_trigger_3 = handbrake
// pX_trigger_4 = boost
// pX_trigger_6 = unwind
// pX_trigger_7 = 
// pX_trigger_8 = 
// pX_trigger_9 = custom camera adjustment


// This is a temporary 'reset' functionality
bind n DamageMe 0

// debug struff
bind q SimTogglePause
///DEBUG/// bind joy0_r3+joy0_dpaddown printActiveObjectStats
///DEBUG/// bind joy1_r3+joy1_dpaddown printActiveObjectStats


//---------------------------------------
//  {{ Joysticks
//---------------------------------------
bind_sig joy0_lx p0_turn  -1
bind_sig joy1_lx p1_turn  -1
bind_sig joy2_lx p2_turn  -1
bind_sig joy3_lx p3_turn  -1

bind_sig joy0_ly p0_pitch  -1
bind_sig joy1_ly p1_pitch  -1
bind_sig joy2_ly p2_pitch  -1
bind_sig joy3_ly p3_pitch  -1

bind_sig joy0_rx p0_strafe -1
bind_sig joy1_rx p1_strafe -1
bind_sig joy2_rx p2_strafe -1
bind_sig joy3_rx p3_strafe -1

bind_sig joy0_ry p0_rudder  1
bind_sig joy1_ry p1_rudder  1
bind_sig joy2_ry p2_rudder  1
bind_sig joy3_ry p3_rudder  1

//---------------------------------------
//  Joysticks }}
//---------------------------------------


//---------------------------------------
//   L2 (left trigger)
//---------------------------------------
// brake
bind_sig joy0_l2 p0_reverse 1
bind_sig joy1_l2 p1_reverse 1
bind_sig joy2_l2 p2_reverse 1
bind_sig joy3_l2 p3_reverse 1

//---------------------------------------
//   L1 (white)
//---------------------------------------
// boost
bind_sig joy0_l1 p0_trigger_4 1
bind_sig joy1_l1 p1_trigger_4 1
bind_sig joy2_l1 p2_trigger_4 1
bind_sig joy3_l1 p3_trigger_4 1

//---------------------------------------
//   R2 (right trigger)
//---------------------------------------
// gas
bind_sig joy0_r2 p0_thrust 1
bind_sig joy1_r2 p1_thrust 1
bind_sig joy2_r2 p2_thrust 1
bind_sig joy3_r2 p3_thrust 1

//---------------------------------------
//   R1 (black)
//---------------------------------------
// unwreck
bind_sig joy0_r1 p0_trigger_6 1 
bind_sig joy1_r1 p1_trigger_6 1
bind_sig joy2_r1 p2_trigger_6 1
bind_sig joy3_r1 p3_trigger_6 1

//---------------------------------------
//   X (A) - 
//---------------------------------------
// primary dumbfire
bind_sig joy0_x p0_trigger_0 1
bind_sig joy1_x p1_trigger_0 1
bind_sig joy2_x p2_trigger_0 1
bind_sig joy3_x p3_trigger_0 1


//---------------------------------------
//  () (CIRCLE) (B)
//---------------------------------------
// fire secondary
bind_sig joy0_circle p0_trigger_1 0
bind_sig joy1_circle p1_trigger_1 0
bind_sig joy2_circle p2_trigger_1 0
bind_sig joy3_circle p3_trigger_1 0

//---------------------------------------
//  [] (SQUARE) (XX)
//---------------------------------------
// handbrake
bind_sig joy0_square p0_trigger_3 1
bind_sig joy1_square p1_trigger_3 1
bind_sig joy2_square p2_trigger_3 1
bind_sig joy3_square p3_trigger_3 1

//---------------------------------------
//  /\ (TRIANGLE) (Y)
//---------------------------------------
// look back
bind_sig joy0_triangle p0_crouch 1
bind_sig joy1_triangle p1_crouch 1
bind_sig joy2_triangle p2_crouch 1
bind_sig joy3_triangle p3_crouch 1

//---------------------------------------
//  R3
//---------------------------------------
// fire primary
bind_sig joy0_r3 p0_trigger_0 1
bind_sig joy1_r3 p1_trigger_0 1
bind_sig joy2_r3 p2_trigger_0 1
bind_sig joy3_r3 p3_trigger_0 1

//---------------------------------------
//  START button
//---------------------------------------
// pause + menu
bind joy0_start Do_FA_StartMenu 0
bind joy1_start Do_FA_StartMenu 1
bind joy2_start Do_FA_StartMenu 2
bind joy3_start Do_FA_StartMenu 3

//---------------------------------------
//  SELECT (back)
//---------------------------------------
// restart
bind joy0_back DamageMe 0
bind joy1_back DamageMe 1
bind joy2_back DamageMe 2
bind joy3_back DamageMe 3


//  - time shift for debugging, DoViewControls for shipping
//bind joy0_back slow_down
//bind joy1_back slow_down
//bind joy2_back slow_down
//bind joy3_back slow_down
//bind joy0_back DoViewControls 0
//bind joy1_back DoViewControls 1
//bind joy2_back DoViewControls 2
//bind joy3_back DoViewControls 3
//bind joy0_back drawRadar0 -1
//bind joy1_back drawRadar1 -1
//bind joy2_back drawRadar2 -1
//bind joy3_back drawRadar3 -1


//---------------------------------------
//  {{ D-PAD
//---------------------------------------
// change view mode
bind joy0_dpadup IncrementViewMode 0
bind joy1_dpadup IncrementViewMode 1
bind joy2_dpadup IncrementViewMode 2
bind joy3_dpadup IncrementViewMode 3
//bind joy0_dpaddown DecrementViewMode 0
//bind joy1_dpaddown DecrementViewMode 1
//bind joy2_dpaddown DecrementViewMode 2
//bind joy3_dpaddown DecrementViewMode 3

//---------------------------------------
//  D-PAD }}
//---------------------------------------

// debug
bind_sig r p0_trigger_8 1


//---------------------------------------
// ...and now, the new stuff.
//---------------------------------------

//Sensitivity 0
g_SensitivityLow_A 0.12
g_SensitivityLow_B -0.25
//Sensitivity 1
g_SensitivityMedium_A 0.12
g_SensitivityMedium_B -0.25
//Sensitivity 2
g_SensitivityHigh_A 0.12
g_SensitivityHigh_B -0.25


// Setup config0 ... (A) This is the Default FA1 controller scheme
btn_mapping  0 // start a new button mapping template
btn_sig   lx		turn		-1	0.12 0.25 sensitivity 1.0 deadzone 0.17 max 1.0
btn_sig   ly		pitch		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   rx		strafe		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   ry		rudder		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
// ...buttons...
btn_sig   l2       reverse		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	// L2 == Left trigger
btn_sig   l1       trigger_4	1													// L1 == White button, trigger_4 == boost
btn_sig   r2       thrust		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	// R2 == Right trigger
btn_sig   r1       trigger_6	1													// R1 == Black button, trigger_6 == unwreck 
btn_sig   x        trigger_0	1
//btn_sig_x x        trigger_2	1													// special case override for tertiary weapons.												// x  == A, trigger_0 == fire primary
btn_sig   circle   trigger_1	1													// Circle == B, trigger_1 == fire secondary
btn_sig   square   trigger_3	1													// Square == XX?, trigger_3 == handbrake
btn_sig   triangle crouch		1													// Triangle == Y, crouch == look back
btn_sig   r3       trigger_0	1
//btn_sig_x r3       trigger_2	1													// special case override for tertiary weapons.
btn_sig   l3       trigger_2	1
btn_func  start    Do_FA_StartMenu	CtrlID											// Do_FA_StartMenu == pause + menu
btn_func  back     DamageMe		CtrlID												// ? restart
btn_func  dpadup   IncrementViewMode CtrlID

// Setup config1 ... (B) This is the E3 PlayStation Controller scheme
btn_mapping  1 // start a new button mapping template
// ...analog sticks...
btn_sig   lx		turn		-1	0.12 0.25 sensitivity 1.0 deadzone 0.17 max 1.0
btn_sig   ly		pitch		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   rx		strafe		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   ry		rudder		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
// ...buttons...
btn_sig   square   reverse		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	
btn_sig   circle   trigger_4	1													
btn_sig   x        thrust		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	
btn_sig   Triangle trigger_6	1													
btn_sig   R1       trigger_0	1													
btn_sig   L1       trigger_1	1													
btn_sig   L2       trigger_3	1													
btn_sig   R2	   crouch		1													
btn_sig   L3       trigger_2	1
btn_func  start    Do_FA_StartMenu	CtrlID											
btn_func  back     DamageMe		CtrlID												
btn_func  dpadup   IncrementViewMode CtrlID

// Setup config2 ... (C) This is the Sony classic PS3 PlayStation Controller scheme (R2/L2 triggers = fire primary/secondary)
btn_mapping  2 // start a new button mapping template
// ...analog sticks...
btn_sig   lx		turn		-1	0.12 0.25 sensitivity 1.0 deadzone 0.17 max 1.0
btn_sig   ly		pitch		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   rx		strafe		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   ry		rudder		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
// ...buttons...
btn_sig   square   reverse		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	
btn_sig   circle   trigger_4	1													
btn_sig   x        thrust		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	
btn_sig   Triangle trigger_6	1													
btn_sig   R2       trigger_0	1													
btn_sig   L2       trigger_1	1													
btn_sig   L1       trigger_3	1													
btn_sig   R1	   crouch		1													
btn_sig   L3       trigger_2	1
btn_func  start    Do_FA_StartMenu	CtrlID											
btn_func  back     DamageMe		CtrlID												
btn_func  dpadup   IncrementViewMode CtrlID

// Setup config3 ... (D)
btn_mapping  3 // start a new button mapping template (see Isaque!)
// ...analog sticks...
btn_sig   lx		turn		-1	0.12 0.25 sensitivity 1.0 deadzone 0.17 max 1.0
btn_sig   ly		pitch		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   rx		strafe		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   ry		rudder		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
// ...buttons...
btn_sig   L2       reverse		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	// L2 == Left trigger
btn_sig   x        trigger_4	1													
btn_sig   R2       thrust		1	0.25 0.75 sensitivity 1.0 deadzone 0.00 max 1.0	// R2 == Right trigger
btn_sig   circle   trigger_6	1													
btn_sig   R1       trigger_0	1													
btn_sig   L1       trigger_1	1													
btn_sig   square   trigger_3	1													
btn_sig   Triangle crouch		1													
btn_sig   L3       trigger_2	1
btn_func  start    Do_FA_StartMenu	CtrlID											
btn_func  back     DamageMe		CtrlID												
btn_func  dpadup   IncrementViewMode CtrlID

// Setup config4 ... (E) This is the FA1 setup, but Primary and Secondary weapon firing are swapped.
btn_mapping  4 // start a new button mapping template
// ...analog sticks...
btn_sig   lx		turn		-1	0.12 0.25 sensitivity 1.0 deadzone 0.17 max 1.0
btn_sig   ly		pitch		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   rx		strafe		-1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
btn_sig   ry		rudder		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0
// ...buttons...
btn_sig   l2       reverse		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0	// L2 == Left trigger
btn_sig   l1       trigger_6	1													// L1 == White button, trigger_4 == boost
//btn_sig_x l1     trigger_2	1													// special case override for tertiary weapons.
btn_sig   r2       thrust		1	0.25 0.75 sensitivity 1.0 deadzone 0.11 max 1.0	// R2 == Right trigger
btn_sig   r1       trigger_4	1													// R1 == Black button, trigger_6 == unwreck 
btn_sig   circle   trigger_0	1													// x  == A, trigger_0 == fire primary
btn_sig   x		   trigger_1	1													// Circle == B, trigger_1 == fire secondary
btn_sig   square   trigger_3	1													// Square == XX?, trigger_3 == handbrake
btn_sig   triangle crouch		1													// Triangle == Y, crouch == look back
btn_sig   r3       trigger_0	1
btn_sig   l3       trigger_2	1
btn_func  start    Do_FA_StartMenu	CtrlID											// Do_FA_StartMenu == pause + menu
btn_func  back     DamageMe		CtrlID												// ? restart
btn_func  dpadup   IncrementViewMode CtrlID

btn_apply_default_mappings
