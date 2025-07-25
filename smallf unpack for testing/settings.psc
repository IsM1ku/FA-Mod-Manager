texPresetWantDiffuse 1
texPresetWantDiffuseAlpha 0
texPresetWriteAlpha 1
texPresetWriteAlpha1 0
texPresetAlphaV 2
texPresetBrightnessV 1.0
texPresetWriteSpecularAlpha 0
texPresetUseTexAlpha 1
PushPreset "GaryPreset1"

texPresetWantDiffuse 1
texPresetWantDiffuseAlpha 0
texPresetWriteAlpha 1
texPresetWriteAlpha1 0
texPresetAlphaV 2
texPresetBrightnessV 1.0
texPresetWriteSpecularAlpha 0
texPresetUseTexAlpha 1
PushPreset "GaryDuplicate"


texPresetWantDiffuse 1
texPresetWantDiffuseAlpha 0
texPresetWriteAlpha 1
texPresetWriteAlpha1 0
texPresetAlphaV 2
texPresetBrightnessV 1.0
texPresetWriteSpecularAlpha 0
texPresetUseTexAlpha 1
PushPreset "GaryDuplicate"



texPresetWantDiffuse 1
texPresetWantDiffuseAlpha 0
texPresetWriteAlpha 1
texPresetWriteAlpha1 0
texPresetAlphaV 2
texPresetBrightnessV 1.0
texPresetWriteSpecularAlpha 0
texPresetUseTexAlpha 1
PushPreset "GaryDuplicate"



// HUD TEXTURE

// HUD - Misc
texPresetAlphaV 2		// source art alpha in [0..255] crunched to [0..127] in texture
texPresetBrightnessV 1.0
texPresetWantDiffuse 1
texPresetWantDiffuseAlpha 0
texPresetWriteAlpha 0

// HUD - Options
texPresetFilterMip 1
texPresetCompression 1		// 4 bit pal
texPresetAutoShrink 1		// shrink if > 256 height or width
texPresetMipLevels 0		// No
texPresetFilterTex 0		// no emboss

// HUD - Debug (** don't touch; use defaults)
texPresetPaddForFilter 0
texPresetHasAlpha 0
texPresetUseTexAlpha 1
texPresetAlphaX2 1		//  texture [0..127] expanded to [0..255]
texPresetWriteAlpha1 0
texPresetWriteSpecularAlpha 1

PushPreset "HUD Image"

// Specialized Renderers
texPresetPaddForFilter 0
texPresetHasAlpha 0
texPresetUseTexAlpha 1
texPresetAlphaX2 1		//  texture [0..127] expanded to [0..255]
texPresetWriteAlpha1 0
texPresetWriteSpecularAlpha 1
PushSpecializedPreset "PaintedMetal"

// Specialized Renderers
texPresetPaddForFilter 0
texPresetHasAlpha 0
texPresetUseTexAlpha 1
texPresetAlphaX2 1		//  texture [0..127] expanded to [0..255]
texPresetWriteAlpha1 0
texPresetWriteSpecularAlpha 1
PushSpecializedPreset "Glass"

// Specialized Renderers
texPresetPaddForFilter 0
texPresetHasAlpha 0
texPresetUseTexAlpha 1
texPresetAlphaX2 1		//  texture [0..127] expanded to [0..255]
texPresetWriteAlpha1 0
texPresetWriteSpecularAlpha 1
PushSpecializedPreset "Light"
