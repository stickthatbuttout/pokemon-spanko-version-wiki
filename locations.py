import re
from collections import defaultdict

# Input text (replace this with reading from a file if necessary)
text = """
# See the documentation on the wiki to learn how to edit this file.
#-------------------------------
[002] # New Bark Town
Water,21
    35,MAGIKARP,2,3
    25,AZURILL,2,3
    25,WOOPER,2,3
    15,TYNAMO,2,3
#-------------------------------
[005] # Route 31
Land,21
    20,ROOKIDEE,3,4
    15,BOUNSWEET,3,4
    15,FLABEBE,3,4
    15,LILLIPUP,3,4
    15,LOTAD,3,4
    10,SEEDOT,3,4
    10,SMOLIV,3,4
LandNight,21
    20,GRUBBIN,3,4
    20,ZIGZAGOON,3,4
    15,ROOKIDEE,3,4
    15,SEEDOT,3,4
    10,FLABEBE,3,4
    10,HOOTHOOT,3,4
    10,LOTAD,3,4
Water,21
    35,MAGIKARP,3,4
    25,AZURILL,3,4
    25,WINGULL,3,4
    15,BARBOACH,3,4
#-------------------------------
[006] # Dark Cave
Cave,21
    20,GEODUDE,5,7
    20,NACLI,5,7
    20,ROLYCOLY,5,7
    20,ZUBAT,5,7
    10,DWEBBLE,5,7
    10,GLIMMET,5,7
Water,21
    25,AZURILL,5,7
    25,BARBOACH,5,7
    25,MAGIKARP,5,7
    25,WOOPER,5,7
#-------------------------------
[007] # Route 27
Water,21
    14,GASTRODON,32,34
    14,OCTILLERY,32,34
    13,QWILFISH,32,34
    13,SEADRA,32,34
    13,TENTACRUEL,32,34
    13,WAILMER,32,34
    13,WHISCASH,32,34
    7,SHARPEDO,32,34
#-------------------------------
[008] # Cherrygrove City
Water,21
    35,MAGIKARP,3,4
    25,AZURILL,3,4
    25,WOOPER,3,4
    15,CHEWTLE,3,4
#-------------------------------
[010] # Dragon's Den
Land,21
    17,NOIBAT,28,30
    17,RIOLU,28,30
    17,SWABLU,28,30
    17,TRAPINCH,28,30
    14,FLAAFFY,28,29
    8,CYCLIZAR,28,29
    5,AMPHAROS,30
    5,AXEW,28,30
Water,21
    20,DRATINI,24,27
    20,MAGIKARP,28,30
    10,CLAUNCHER,28,30
    10,DREDNAW,28,30
    10,GASTRODON,30
    10,GYARADOS,28,30
    10,PELIPPER,28,30
    10,STARYU,28,30
#-------------------------------
[020] # Ruins of Alph
Land,21
    20,HOPPIP,6,8
    20,KRICKETOT,8,10
    20,POOCHYENA,6,8
    20,SKITTY,8,10
    10,BALTOY,5,6
    10,PICHU,5,6
LandNight,21
    20,NINCADA,6,8
    20,POOCHYENA,6,8
    20,SKITTY,8,10
    20,SPINARAK,8,10
    10,BALTOY,5,6
    10,CLEFFA,5,6
Water,21
    20,CHEWTLE,8,10
    20,DEWPIDER,8,10
    20,INKAY,8,10
    20,TYNAMO,8,10
    20,WOOPER,8,10
RockSmash,100
    50,GEODUDE,8,10
    25,NACLI,8,10
    25,ROLYCOLY,8,10
#-------------------------------
[021] # Route 30
Land,21
	15,BLIPBUG,3,4
    15,FLABEBE,3,4
    15,LILLIPUP,3,4
    15,FLETCHLING,3,4
    15,ROOKIDEE,3,4
    15,LOTAD,3,4
	10,BOUNSWEET,3,4
LandNight,21
	15,LILLIPUP,3,4
    15,ZIGZAGOON,3,4
    15,BLIPBUG,3,4
    15,FLABEBE,3,4
	15,ROOKIDEE,3,4
    15,SEEDOT,3,4
	10,GRUBBIN,3,4
Water,21
    20,MAGIKARP,3,4
    20,AZURILL,3,4
    20,WINGULL,3,4
    20,BARBOACH,3,4
    20,LOTAD,3,4
HeadbuttHigh
	20,BOUNSWEET,3,4
	20,SEEDOT,3,4
	20,GRUBBIN,3,4
	20,SMOLIV,3,4
	20,HOOTHOOT,3,4
HeadbuttLow
	20,BOUNSWEET,3,4
	20,SEEDOT,3,4
	20,GRUBBIN,3,4
	20,SMOLIV,3,4
	20,HOOTHOOT,3,4
#-------------------------------
[022] # Ruins of Alph 1
Cave,21
    100,UNOWN,5
#-------------------------------
[023] # Ruins of Alph 2
Cave,21
    100,UNOWN,5
#-------------------------------
[024] # Ruins of Alph 3
Cave,21
    100,UNOWN,5
#-------------------------------
[025] # Ruins of Alph 4
Cave,21
    100,UNOWN,5
#-------------------------------
[027] # Route 32
Land,21
    12,BOUNSWEET,8,10
    12,COTTONEE,8,10
    12,GOSSIFLEUR,8,10
    12,MAREEP,8,10
    12,MEOWTH,8,10
	12,NIDORANmA,8,10
    12,WATTREL,8,10
    8,CUTIEFLY,8,10
    8,PAWMI,8,10
LandNight,21
    12,ODDISH,8,10
	12,SHINX,8,10
    12,COTTONEE,8,10
    12,GOSSIFLEUR,8,10
    12,MEOWTH,8,10
    12,NIDORANmA,8,10
    12,TEDDIURSA,8,10
    8,CUTIEFLY,8,10
    8,WYNAUT,8,10
Water,21
    25,CARVANHA,8,10
    25,CHINCHOU,8,10
    25,QWILFISH,8,10
    25,REMORAID,8,10
HeadbuttHigh
	20,CUTIEFLY,8,10
	20,NATU,8,10
	20,GOSSIFLEUR,8,10
	20,TEDDIURSA,8,10
	20,BOUNSWEET,8,10
HeadbuttLow
	20,CUTIEFLY,8,10
	20,NATU,8,10
	20,GOSSIFLEUR,8,10
	20,TEDDIURSA,8,10
	20,BOUNSWEET,8,10
#-------------------------------
[028] # Union Cave
Cave,21
    14,DWEBBLE,9,11
    14,MANKEY,9,11
    12,ARON,9,11
    12,CUBONE,9,11
    12,DRILBUR,9,11
    12,MACHOP,9,11
    12,SLUGMA,9,11
    12,TRAPINCH,9,11
Water,21
    20,BARBOACH,9,11
    20,CHINCHOU,9,11
    20,CLAUNCHER,9,11
    20,SHELLOS,9,11
    20,STARYU,9,11
#-------------------------------
[030] # Route 33
Land,21
    21,BUDEW,9,11
    24,MEOWTH,9,11
    21,PETILIL,9,11
    22,RELLOR,9,11
    12,CUFANT,9,11
LandNight,21
    19,HATENNA,9,11
    19,HOUNDOUR,9,11
    24,MEOWTH,9,11
    18,RELLOR,9,11
    10,CUFANT,9,11
    10,PANCHAM,9,11
RockSmash,100
    40,GEODUDE,9,11
    25,NACLI,9,11
    25,ROLYCOLY,9,11
    10,ONIX,9,11
#-------------------------------
[031] # Deep Well
Cave,21
    40,AZURILL,12,14
    20,MEDITITE,12,14
    20,VANILLITE,12,14
    10,SHUPPET,12,14
    10,WYNAUT,12,14
Water,21
    40,AZURILL,12,14
    20,GRIMER,12,14
    20,MAREANIE,12,14
    20,MARILL,12,14
#-------------------------------
[036] # Ilex Forest
Cave,21
    15,LITWICK,10,14
	15,PHANTUMP,10,14
    15,MEDITITE,10,14
    15,GASTLY,10,14
    15,IMPIDIMP,10,14
    5,ABRA,10,14
    5,BONSLY,10,14
    5,MINCCINO,10,14
    6,PIKACHU,10,14
    3,HAPPINY,10,14
    1,TOGEPI,10,14
HeadbuttLow
	19,HOOTHOOT,10,14
	19,COMBEE,10,14
	19,EXEGGCUTE,10,14
	19,PINECO,10,14
	19,FERROSEED,10,14
	3,HERACROSS,10,14
	1,TOGEPI,10,14
HeadbuttHigh
	19,HOOTHOOT,10,14
	19,COMBEE,10,14
	19,EXEGGCUTE,10,14
	19,PINECO,10,14
	19,FERROSEED,10,14
	3,HERACROSS,10,14
	1,TOGEPI,10,14
#-------------------------------
[037] # Route 34
Land,21
    18,CAPSAKID,12,14
    18,COMBEE,12,14
    18,GROWLITHE,12,14
    18,MAKUHITA,12,14
    18,MILCERY,12,14
    10,PETILIL,12,14
LandNight,21
    18,MAKUHITA,12,14
    18,MILCERY,12,14
    18,ROCKRUFF,12,14
    18,VENONAT,12,14
    18,VULPIX,12,14
    10,PETILIL,12,14
#-------------------------------
[041] # Route 3
Land,21
    16,DONPHAN,37,39
    16,HELIOPTILE,37,39
    12,EXCADRILL,37,39
    12,MAGNETON,37,39
    12,MIENFOO,37,39
    12,ORTHWORM,37,39
    12,STANTLER,37,39
    4,COALOSSAL,37,39
LandNight,21
    16,CLAYDOL,37,39
    16,DONPHAN,37,39
    12,EXCADRILL,37,39
    12,MAGNETON,37,39
    12,MIENFOO,37,39
    12,ORTHWORM,37,39
    12,STANTLER,37,39
    4,COALOSSAL,37,39
RockSmash,100
    30,CARKOL,37,39
    30,GRAVELER,37,39
    30,NACLSTACK,37,39
    5,COALOSSAL,37,39
    5,PORYGON,37,39
#-------------------------------
[042] # Viridian Forest
Land,21
    15,FOONGUS,37,38
    14,GIRAFARIG,37,39
    14,LOUDRED,37,39
    14,SKARMORY,37,39
    14,ORBEETLE,37,39
    14,VIVILLON,37,39
    14,NIDORINO,37,39
    1,LEAFEON,37,39
LandNight,21
    15,FOONGUS,37,38
    14,GIRAFARIG,37,39
    14,LOUDRED,37,39
    14,NIDORINO,37,39
    14,ORBEETLE,37,39
    14,SIGILYPH,37,39
    14,SKARMORY,37,39
    1,LEAFEON,37,39
HeadbuttHigh
	24,SKARMORY,37,39
	24,SKORUPI,37,39
	24,VIVILLON,37,39
	24,ORBEETLE,37,39
	4,HERACROSS,37,39
HeadbuttLow
	24,SKARMORY,37,39
	24,SKORUPI,37,39
	24,VIVILLON,37,39
	24,ORBEETLE,37,39
	4,HERACROSS,37,39
#-------------------------------
[043] # Violet City
Water,21
    35,MAGIKARP,3,4
    25,AZURILL,3,4
    25,WINGULL,3,4
    15,BARBOACH,3,4
#-------------------------------
[046] # Route 35
Land,21
    18,CAPSAKID,12,14
    18,COMBEE,12,14
    18,DARUMAKA,12,14
    18,GROWLITHE,12,14
    18,TOEDSCOOL,12,14
    10,HOUNDOUR,12,14
LandNight,21
    20,HOUNDOUR,12,14
    16,DRIFLOON,12,14
    16,TOEDSCOOL,12,14
    16,VENONAT,12,14
    16,VULPIX,12,14
    16,ZUBAT,12,14
Water,21
	25,TYNAMO,12,14
	25,BASCULIN,12,14
	25,CHEWTLE,12,14
	25,REMORAID,12,14
HeadbuttHigh
	25,DRIFLOON,12,14
	25,COMBEE,12,14
	25,VENONAT,12,14
	25,CAPSAKID,12,14
HeadbuttLow
	25,DRIFLOON,12,14
	25,COMBEE,12,14
	25,VENONAT,12,14
	25,CAPSAKID,12,14
#-------------------------------
[047] # National Park
Land,21
    14,COMBEE,10,14
    14,CUTIEFLY,10,14
    14,GRUBBIN,10,14
    14,KARRABLAST,10,14
    14,SEWADDLE,10,14
    14,SHELMET,10,14
    14,SPEWPA,10,14
    2,YANMA,10,14
LandNight,21
    14,CUTIEFLY,10,14
    14,KARRABLAST,10,14
    14,SEWADDLE,10,14
    14,SHELMET,10,14
    14,SPEWPA,10,14
    14,SPINARAK,10,14
    14,VENONAT,10,14
    2,YANMA,10,14
BugContest,21
    10,COMBEE,10,14
    10,JOLTIK,10,14
    10,VENONAT,10,14
    9,NINCADA,10,14
    9,PINECO,10,14
    9,SPEWPA,10,14
    9,SPINARAK,10,14
    7,BLIPBUG,10,14
    7,SIZZLIPEDE,10,14
    5,VIVILLON,10,14
    4,SHUCKLE,10,14
    3,HERACROSS,10,14
    3,LARVESTA,10,14
    3,SCYTHER,10,14
    2,YANMA,10,14
#-------------------------------
[052] # Route 38
Land,21
    18,MAWILE,15,18
    18,MUDBRAY,15,18
    16,MUNCHLAX,15,18
    16,PONYTA,15,18
    16,WOOLOO,15,18
	16,SNEASEL,15,18
LandNight,21
	18,SABLEYE,15,18
    18,ABSOL,15,18
    16,MUNCHLAX,15,18
    16,WOOLOO,15,18
	16,PONYTA,15,18
	16,SNEASEL,15,18
HeadbuttHigh
	25,KOMALA,15,18
	25,GLIGAR,15,18
	25,MURKROW,15,18
	25,SWABLU,15,18
HeadbuttLow
	25,KOMALA,15,18
	25,GLIGAR,15,18
	25,MURKROW,15,18
	25,SWABLU,15,18
#-------------------------------
[053] # Route 39
Land,21
    18,MAWILE,15,18
    18,MUDBRAY,15,18
    16,MUNCHLAX,15,18
    16,PONYTA,15,18
    16,WOOLOO,15,18
	16,SNEASEL,15,18
LandNight,21
	18,SABLEYE,15,18
    18,ABSOL,15,18
    16,MUNCHLAX,15,18
    16,WOOLOO,15,18
	16,PONYTA,15,18
	16,SNEASEL,15,18
HeadbuttHigh
	25,KOMALA,15,18
	25,GLIGAR,15,18
	25,MURKROW,15,18
	25,SWABLU,15,18
HeadbuttLow
	25,KOMALA,15,18
	25,GLIGAR,15,18
	25,MURKROW,15,18
	25,SWABLU,15,18
#-------------------------------
[055] # Route 40
Water,21
    10,BASCULIN,20,22
    10,HORSEA,20,22
    10,MANTYKE,20,22
    10,SHELLDER,20,22
    10,TENTACOOL,20,22
    10,WAILMER,20,22
    8,BINACLE,20,22
    8,CHINCHOU,20,22
    8,EISCUE,20,22
    8,QWILFISH,20,22
    8,SPHEAL,20,22
#-------------------------------
[056] # Cianwood City
Water,21
    10,BASCULIN,20,22
    10,HORSEA,20,22
    10,MANTYKE,20,22
    10,SHELLDER,20,22
    10,TENTACOOL,20,22
    10,WAILMER,20,22
    8,BINACLE,20,22
    8,CHINCHOU,20,22
    8,EISCUE,20,22
    8,QWILFISH,20,22
    8,SPHEAL,20,22
RockSmash,100
    30,GEODUDE,20,22
    20,CARKOL,20,22
    20,NACLI,20,22
    20,PYUKUMUKU,20,22
    6,GRAVELER,25
    4,NACLSTACK,24
#-------------------------------
[060] # Route 42
Land,21
    14,CUFANT,20,23
    14,RUFFLET,20,23
    14,SANDILE,20,23
    14,SPRITZEE,20,23
    14,STEENEE,20,23
    14,WHISMUR,20,23
    8,SHROODLE,20,23
    4,HAWLUCHA,20,23
    4,KIRLIA,20,23
LandNight,21
    14,GOLETT,20,23
    14,MIGHTYENA,20,23
    14,MIMIKYU,20,23
    14,MISDREAVUS,20,23
    10,HONEDGE,20,23
    10,ZORUA,20,23
    8,SANDILE,20,23
    8,SHROODLE,20,23
    4,GIMMIGHOUL,20,23
    4,HAWLUCHA,20,23
Water,21
    20,BASCULIN,20,23
    20,DREDNAW,22,23
    20,REMORAID,20,23
    20,SHELLOS,20,23
    10,CLODSIRE,20,23
    10,QUAGSIRE,20,23
RockSmash,100
    42,GEODUDE,20,23
    25,CARKOL,20,23
    21,NACLI,20,23
    6,GRAVELER,25
    6,NACLSTACK,24
#-------------------------------
[065] # Route 44
Land,21
    18,SOLOSIS,24,26
    18,SALANDIT,24,26
    18,TOEDSCOOL,24,26
    18,FOONGUS,24,26
	12,FALINKS,24,26
    4,CYCLIZAR,24,26
    4,ABSOL,24,26
    4,DITTO,24,26
    4,KANGASKHAN,24,26
Water,21
    20,AZUMARILL,24,26
    20,BERGMITE,24,26
    20,MAREANIE,24,26
    20,STARYU,24,26
    15,REMORAID,24,26
    5,OCTILLERY,25,26
HeadbuttHigh
    30,STARAVIA,24,26
	30,CORVISQUIRE,24,26
	30,KOMALA,24,26
	10,FARFETCHD,24,26
HeadbuttLow
    30,STARAVIA,24,26
	30,CORVISQUIRE,24,26
	30,KOMALA,24,26
	10,FARFETCHD,24,26
#-------------------------------
[066] # Route 29
Land,21
    16,LILLIPUP,2,3
    16,SCATTERBUG,2,3
    16,FLABEBE,2,3
    16,WOOLOO,2,3
    16,PAWMI,2,3
	16,SMOLIV,2,3
    4,RALTS,2,3
LandNight,21
    16,LILLIPUP,2,3
	16,TEDDIURSA,2,3
    16,SCATTERBUG,2,3
    16,ZIGZAGOON,2,3
    16,SHROODLE,2,3
    16,PAWMI,2,3
    4,RALTS,2,3
HeadbuttHigh
	16,BOUNSWEET,2,3
	17,PIKIPEK,2,3
	17,STARLY,2,3
	17,ROOKIDEE,2,3
	16,SKWOVET,2,3
	16,HOOTHOOT,2,3
	1,TOGEPI,2,3
HeadbuttLow
	16,BOUNSWEET,2,3
	17,PIKIPEK,2,3
	17,STARLY,2,3
	17,ROOKIDEE,2,3
	16,SKWOVET,2,3
	16,HOOTHOOT,2,3
	1,TOGEPI,2,3
#-------------------------------
[067] # Ice Path
Cave,21
    12,SWINUB,25,28
    11,SANDSHREW,25,28
    11,VULPIX,25,28
    10,CRYOGONAL,25,28
    10,DARUMAKA,25,28
    10,SNOM,25,28
    10,SNORUNT,25,28
    10,VANILLITE,25,28
    9,SNOVER,25,28
    5,CETODDLE,25,28
    2,BELDUM,20
#-------------------------------
[068] # Route 43
Land,21
    10,DOLLIV,24,26
    10,GIRAFARIG,24,26
    10,KILOWATTREL,25
    10,MIENFOO,24,26
    10,PONYTA,24,26
    10,TOEDSCOOL,24,26
    10,VIVILLON,24,26
    9,NIDORINO,24,26
    8,SKIPLOOM,24,26
    8,TANGELA,24,26
    5,ROTOM,24,26
LandNight,21
    10,GIRAFARIG,24,26
    10,GOLBAT,25
    10,MIENFOO,24,26
    10,PANCHAM,24,26
    10,PONYTA,24,26
    10,TOEDSCOOL,24,26
    10,VIVILLON,24,26
    9,NIDORINO,24,26
    8,SKIPLOOM,24,26
    8,TANGELA,24,26
    5,ROTOM,24,26
#-------------------------------
[069] # Lake of Rage
Land,21
    15,KILOWATTREL,25
    15,MIENFOO,24,26
    16,PONYTA,24,26
    14,TOEDSCOOL,24,26
    15,VIVILLON,24,26
    10,SKIPLOOM,24,26
    10,TANGELA,24,26
    5,ROTOM,24,26
LandNight,21
    15,GOLBAT,25
    15,MIENFOO,24,26
    16,PONYTA,24,26
    14,TOEDSCOOL,24,26
    15,VIVILLON,24,26
    10,SKIPLOOM,24,26
    10,TANGELA,24,26
    5,ROTOM,24,26
Water,21
    90,MAGIKARP,16,19
    7,GYARADOS,20
    3,DRATINI,20,23
#-------------------------------
[072] # Mt. Mortar
Cave,21
    10,RHYHORN,20,24
    9,CHARJABUG,20,24
    9,KLINK,20,24
    9,NUMEL,22,24
    9,SKORUPI,20,24
    9,TORKOAL,20,24
    8,ORTHWORM,22,24
    8,SANDILE,20,24
    8,SNEASEL,20,24
    7,MACHOP,20,24
    5,GLIMMET,22,24
    5,MINIOR,22,24
    4,LARVITAR,20,24
Water,21
    20,BASCULIN,20,23
    20,DREDNAW,22,23
    20,REMORAID,20,23
    20,SHELLOS,20,23
    9,CLODSIRE,20,23
    9,QUAGSIRE,20,23
    2,FEEBAS,15,18
#-------------------------------
[073] # Hidden Village
Land,21
    16,CENTISKORCH,48,52
    16,CHARJABUG,48,52
    16,LUDICOLO,48,52
    16,RABSCA,48,52
    16,SCYTHER,48,52
    15,PINSIR,48,52
    5,HATTERENE,48,52
LandNight,21
    16,CHARJABUG,48,52
    16,FROSMOTH,48,52
    16,RABSCA,48,52
    16,SCYTHER,48,52
    16,SHIFTRY,48,52
    15,PINSIR,48,52
    5,GRIMMSNARL,48,52
#-------------------------------
[074] # Mt Moon 1F
Cave,21
    9,CLAYDOL,36,41
    9,COPPERAJAH,36,41
    9,CRUSTLE,36,41
    9,DURALUDON,36,41
    9,EXCADRILL,36,41
    9,FALINKS,36,41
    9,GOLBAT,36,41
    9,LAIRON,36,41
    9,ORTHWORM,36,41
    9,RHYHORN,36,41
    7,GLIMMORA,36,41
    2,CLEFAIRY,36,41
    1,GLACEON,36,41
#-------------------------------
[075] # Mt Moon B1F
Cave,21
    9,CLAYDOL,36,41
    9,COPPERAJAH,36,41
    9,CRUSTLE,36,41
    9,DURALUDON,36,41
    9,EXCADRILL,36,41
    9,FALINKS,36,41
    9,GOLBAT,36,41
    9,LAIRON,36,41
    9,ORTHWORM,36,41
    9,RHYHORN,36,41
    7,GLIMMORA,36,41
    2,CLEFAIRY,36,41
    1,GLACEON,36,41
#-------------------------------
[076] # Route 4
Land,21
    20,VESPIQUEN,36,41
    19,SALANDIT,36,41
	18,FLOETTE,36,41
    18,PIKACHU,36,41
    18,WOBBUFFET,36,41
    6,SALAZZLE,36,41
    1,EEVEE,36,41
LandNight,21
    20,PAWNIARD,36,41
	19,SALANDIT,36,41
	18,FLOETTE,36,41
    18,PIKACHU,36,41
    18,WOBBUFFET,36,41
    6,SALAZZLE,36,41
    1,EEVEE,36,41
Water,21
    20,BARBOACH,38,41
    20,BASCULIN,38,41
    20,DREDNAW,38,41
    20,QWILFISH,38,41
    16,CLAWITZER,38,41
    4,FEEBAS,38,41
HeadbuttHigh
	25,FLOETTE,36,41
	25,RIBOMBEE,36,41
	25,VIBRAVA,36,41
	25,EXEGGCUTE,36,41
HeadbuttLow
	25,FLOETTE,36,41
	25,RIBOMBEE,36,41
	25,VIBRAVA,36,41
	25,EXEGGCUTE,36,41
#-------------------------------
[078] # Route 5
Land,21
    20,FLOETTE,42,45
    20,PIKACHU,42,45
    20,RIBOMBEE,42,45
    16,WOBBUFFET,42,45
    12,EXEGGCUTE,42,45
    11,VIBRAVA,42,44
    1,ESPEON,42,45
LandNight,21
    20,PAWNIARD,42,45
    20,PIKACHU,42,45
    20,RIBOMBEE,42,45
    16,WOBBUFFET,42,45
    12,EXEGGCUTE,42,45
    11,VIBRAVA,42,44
    1,UMBREON,42,45
#-------------------------------
[081] # Route 6
Land,21
    20,PAWMO,42,45
    20,BRELOOM,42,45
    20,HARIYAMA,42,45
    20,HELIOPTILE,42,45
	19,AMPHAROS,42,45
    1,JOLTEON,42,45
Water,21
    20,ARAQUANID,42,45
    20,EELEKTRIK,42,45
    20,LANTURN,42,45
    20,QWILFISH,42,45
    16,TOXAPEX,42,45
    4,BARBARACLE,42,45
HeadbuttHigh
	40,ELECTRODE,42,45
	30,KILOWATTREL,42,45
	30,GALVANTULA,42,45
HeadbuttLow
	40,ELECTRODE,42,45
	30,KILOWATTREL,42,45
	30,GALVANTULA,42,45
#-------------------------------
[082] # Vermilion City
Water,21
    20,ARAQUANID,42,45
    20,EELEKTRIK,42,45
    20,LANTURN,42,45
    20,QWILFISH,42,45
    16,TOXAPEX,42,45
    4,BARBARACLE,42,45
#-------------------------------
[085] # Route 17
Land,21
    14,ARBOLIVA,48,52
    14,GLIGAR,48,52
    14,KILOWATTREL,48,52
    14,STANTLER,48,52
    13,STOUTLAND,48,52
    13,SUDOWOODO,48,52
    8,CYCLIZAR,48,52
    7,GREEDENT,48,52
    3,DUBWOOL,48,52
LandNight,21
    14,GLIGAR,48,52
    14,GRAFAIAI,48,52
    14,KILOWATTREL,48,52
    14,STANTLER,48,52
    13,OBSTAGOON,48,52
    13,SUDOWOODO,48,52
    8,CYCLIZAR,48,52
    7,DUBWOOL,48,52
    3,GREEDENT,48,52
Water,21
    30,CLAWITZER,48,52
    30,PELIPPER,48,52
    30,SHARPEDO,48,52
    6,TOXAPEX,48,52
    2,OVERQWIL,48,52
    2,WALREIN,48,52
#-------------------------------
[093] # Route 8
Land,21
    20,ALTARIA,46,50
	20,AMOONGUSS,46,50
    20,MUK,46,50
    19,ROSELIA,46,50
    19,TSAREENA,46,50
    1,CHANSEY,46,50
    1,SYLVEON,46,50
LandNight,21
	20,ARIADOS,46,50
    20,AMOONGUSS,46,50
    20,MUK,46,50
    19,ROSELIA,46,50
    19,TSAREENA,46,50
    1,CHANSEY,46,50
    1,SYLVEON,46,50
HeadbuttHigh
    20,CORVIKNIGHT,46,50
    20,JUMPLUFF,46,50
    20,STARAPTOR,46,50
    20,TOUCANNON,46,50
	20,VENOMOTH,46,50
HeadbuttLow
    20,CORVIKNIGHT,46,50
    20,JUMPLUFF,46,50
    20,STARAPTOR,46,50
    20,TOUCANNON,46,50
	20,VENOMOTH,46,50
#-------------------------------
[094] # Route 7
Land,21
	19,GLALIE,46,50
    16,GLOOM,46,50
    16,ABOMASNOW,46,50
    16,AMOONGUSS,46,50
    16,FORRETRESS,46,50
    16,TSAREENA,46,50
    1,EEVEE,46,50
LandNight,21
    19,FROSLASS,46,50
    16,GLOOM,46,50
    16,ABOMASNOW,46,50
    16,AMOONGUSS,46,50
    16,FERROTHORN,46,50
	16,TSAREENA,46,50
    1,EEVEE,46,50
HeadbuttHigh
	40,DRIFBLIM,46,50
	30,NINJASK,46,50
	30,SHEDINJA,46,50
HeadbuttLow
	40,DRIFBLIM,46,50
	30,NINJASK,46,50
	30,SHEDINJA,46,50
#-------------------------------
[099] # Route 20
Water,21
    12,QWILFISH,50,54
    12,SEADRA,50,54
    12,SHARPEDO,50,54
    12,STARYU,50,54
    11,GASTRODON,50,54
    11,MANTINE,50,54
    11,OCTILLERY,50,54
    11,SHELLDER,50,54
    4,WAILORD,50,54
    4,WALREIN,50,54
#-------------------------------
[158] # Seafoam Islands 1F
Cave,21
	14,SNEASEL,50,54
	14,PILOSWINE,50,54
	6,GLALIE,50,54
	6,FROSLASS,50,54
	12,CETODDLE,50,54
	12,CRYOGONAL,50,54
	12,VANILLUXE,50,54
	12,DARMANITAN,50,54
	12,ABOMASNOW,50,54
#-------------------------------
[159] # Seafoam Islands B1F
Cave,21
	14,SNEASEL,50,54
	14,PILOSWINE,50,54
	6,GLALIE,50,54
	6,FROSLASS,50,54
	12,CETODDLE,50,54
	12,CRYOGONAL,50,54
	12,VANILLUXE,50,54
	12,DARMANITAN,50,54
	12,ABOMASNOW,50,54
#-------------------------------
[160] # Seafoam Islands B2F
Cave,21
	14,SNEASEL,50,54
	14,PILOSWINE,50,54
	6,GLALIE,50,54
	6,FROSLASS,50,54
	12,CETODDLE,50,54
	12,CRYOGONAL,50,54
	12,VANILLUXE,50,54
	12,DARMANITAN,50,54
	12,ABOMASNOW,50,54
#-------------------------------
[161] # Seafoam Islands B3F
Cave,21
	14,SNEASEL,50,54
	14,PILOSWINE,50,54
	6,GLALIE,50,54
	6,FROSLASS,50,54
	12,CETODDLE,50,54
	12,CRYOGONAL,50,54
	12,VANILLUXE,50,54
	12,DARMANITAN,50,54
	12,ABOMASNOW,50,54
Water,21
	24,WALREIN,50,54
	24,AVALUGG,50,54
	24,SHELLDER,50,54
	24,EISCUE,50,54
	4,LAPRAS,50,54
#-------------------------------
[164] # Seafoam Islands B4F
Cave,21
	14,SNEASEL,50,54
	14,PILOSWINE,50,54
	6,GLALIE,50,54
	6,FROSLASS,50,54
	12,CETODDLE,50,54
	12,CRYOGONAL,50,54
	12,VANILLUXE,50,54
	12,DARMANITAN,50,54
	12,ABOMASNOW,50,54
#-------------------------------
[100] # Cinnabar Island
Water,21
    12,QWILFISH,50,54
    12,SEADRA,50,54
    12,SHARPEDO,50,54
    12,STARYU,50,54
    11,GASTRODON,50,54
    11,MANTINE,50,54
    11,OCTILLERY,50,54
    11,SHELLDER,50,54
    4,WAILORD,50,54
    4,WALREIN,50,54
#-------------------------------
[101] # Route 21
Land,21
    20,EXPLOUD,52,55
    20,GIRAFARIG,52,55
    20,MACHOKE,52,55
    20,PRIMEAPE,52,55
	10,TANGROWTH,50,54
    5,ZOROARK,52,55
	5,DITTO,52,55
Water,21
    12,QWILFISH,50,54
    12,SEADRA,50,54
    12,SHARPEDO,50,54
    12,STARYU,50,54
    11,GASTRODON,50,54
    11,MANTINE,50,54
    11,OCTILLERY,50,54
    11,SHELLDER,50,54
    4,WAILORD,50,54
    4,WALREIN,50,54
HeadbuttHigh
	40,SNEASEL,52,55
	20,TANGROWTH,52,55
	20,STARAPTOR,52,55
	20,FARFETCHD,52,55
HeadbuttLow
	40,SNEASEL,52,55
	20,TANGROWTH,52,55
	20,STARAPTOR,52,55
	20,FARFETCHD,52,55
#-------------------------------
[103] # Route 1
Land,21
    14,BRELOOM,53,56
    14,MEDICHAM,53,56
    14,PAWMO,53,57
    14,PIKACHU,53,56
    14,MIENSHAO,53,56
    14,JUMPLUFF,53,56
    14,TSAREENA,53,56
    1,EEVEE,53,56
LandNight,21
    14,MEDICHAM,53,56
    14,OBSTAGOON,53,56
    14,PAWMO,53,56
    14,PIKACHU,53,56
    14,MIENSHAO,53,56
    14,PANCHAM,53,56
    14,TSAREENA,53,56
    1,EEVEE,53,56
HeadbuttHigh
	20,TALONFLAME,53,56
	20,TOUCANNON,53,56
	20,SKARMORY,53,56
	20,CORVIKNIGHT,53,56
	20,STARAPTOR,53,56
HeadbuttLow
	20,TALONFLAME,53,56
	20,TOUCANNON,53,56
	20,SKARMORY,53,56
	20,CORVIKNIGHT,53,56
	20,STARAPTOR,53,56
#-------------------------------
[105] # Route 22
Land,21
	16,MAWILE,55,57
    14,SNEASEL,55,57
    14,AMOONGUSS,55,57
    14,MAGNETON,55,57
    14,ORBEETLE,55,57
    14,PERSIAN,55,57
    14,ROSELIA,55,57
LandNight,21
	16,SABLEYE,55,57
    14,SNEASEL,55,57
    14,AMOONGUSS,55,57
    14,GLOOM,55,57
    14,MAGNETON,55,57
    14,ORBEETLE,55,57
    14,PERSIAN,55,57
Water,21
    20,DREDNAW,55,57
    20,EELEKTRIK,55,57
    20,MAGIKARP,55,57
    20,PYUKUMUKU,55,57
    20,SHELLDER,55,57
#-------------------------------
[107] # Route 28
Land,21
    14,AGGRON,64,68
    14,COPPERAJAH,64,68
    14,RAPIDASH,64,68
    14,STOUTLAND,64,68
    14,CORVIKNIGHT,64,68
    14,FLYGON,64,68
    16,ARCANINE,64,68
LandNight,21
    14,AGGRON,64,68
    14,BISHARP,64,68
    14,COPPERAJAH,64,68
    14,OBSTAGOON,64,68
    14,CORVIKNIGHT,64,68
    14,FLYGON,64,68
    16,NINETALES,64,68
Water,21
    20,CLAWITZER,64,68
    20,CLODSIRE,64,68
    20,QUAGSIRE,64,68
    20,WALREIN,64,68
    10,OVERQWIL,64,68
    5,LAPRAS,64,68
    5,MILOTIC,64,68
HeadbuttHigh
	60,BRAVIARY,64,68
	20,NOIVERN,64,68
    10,STARAPTOR,64,68
	10,KILOWATTREL,64,68
HeadbuttLow
	60,BRAVIARY,64,68
	20,NOIVERN,64,68
    10,STARAPTOR,64,68
	10,KILOWATTREL,64,68
#-------------------------------
[115] # Space-Time Distortion
Land,21
    10,AERODACTYL,60,65
    10,BASTIODON,60,65
    10,GREATTUSK,60,65
    10,IRONMOTH,60,65
    10,IRONTREADS,60,65
    10,RAMPARDOS,60,65
    10,SLITHERWING,60,65
    5,GHOLDENGO,60,65
    5,GUZZLORD,60,65
    5,IRONVALIANT,60,65
    5,POIPOLE,60,65
    5,PORYGONZ,60,65
    5,ROARINGMOON,60,65
Water,21
    20,GYARADOS,60,65
    20,LAPRAS,60,65
    20,MALAMAR,60,65
    20,MILOTIC,60,65
    16,EELEKTROSS,60,65
    4,DRAGONITE,60,65
#-------------------------------
[117] # Route 11
Land,21
    14,DARMANITAN,46,50
    12,GROWLITHE,46,50
    13,TALONFLAME,46,50
    12,ARBOLIVA,46,50
    12,CENTISKORCH,46,50
    12,ELDEGOSS,46,50
    12,GOGOAT,46,50
    12,TOEDSCRUEL,46,50
    1,FLAREON,46,50
LandNight,21
    12,ARBOLIVA,46,50
    12,CENTISKORCH,46,50
    12,DARMANITAN,46,50
    12,ELDEGOSS,46,50
    12,GOGOAT,46,50
    12,GROWLITHE,46,50
    12,TALONFLAME,46,50
    12,TOEDSCRUEL,46,50
    3,DOUBLADE,46,50
    1,FLAREON,46,50
#-------------------------------
[119] # Victory Road
Cave,21
    12,BISHARP,57,60
    12,KLINKLANG,57,60
    12,TANGROWTH,57,60
    10,GOLBAT,57,60
    10,GRIMMSNARL,57,60
    10,HARIYAMA,57,60
    10,LUXRAY,57,60
    10,MINIOR,57,60
    10,URSARING,57,60
    4,PERRSERKER,57,60
#-------------------------------
[143] # Route 12
Water,21
    20,GASTRODON,46,50
    20,PELIPPER,46,50
    20,SEADRA,46,50
    20,SHARPEDO,46,50
    16,BASCULIN,46,50
    3,WAILORD,46,50
    1,VAPOREON,46,50
#-------------------------------
[144] # Lavender Tower 2F
Cave,21
    15,BANETTE,46,50
    15,DRIFBLIM,46,50
    15,DUSCLOPS,46,50
    15,HAUNTER,46,50
    15,LAMPENT,46,50
    15,MISDREAVUS,46,50
    5,GIMMIGHOUL,46,50
    5,MIMIKYU,46,50
#-------------------------------
[153] # Kanto Safari Zone
Land,21
    13,CYCLIZAR,24,30
    13,GIRAFARIG,24,30
    13,MILTANK,24,30
    13,PAWMO,24,30
    13,SNORLAX,24,30
    13,TAUROS,24,30
    6,GIBLE,10,13
    6,SCORBUNNY,10,13
    6,TREECKO,10,13
    3,EEVEE,24,30
    1,BLISSEY,24,30
Water,21
    23,AZUMARILL,24,30
    23,EISCUE,24,30
    23,MANTINE,24,30
    23,PYUKUMUKU,24,30
    6,TOTODILE,10,13
    2,LAPRAS,24,30
#-------------------------------
[176] # Union Cave B1F
Cave,21
    15,MAGNEMITE,10,13
    15,NUMEL,10,13
    14,DUSKULL,10,13
    14,GOLETT,10,13
    14,NOIBAT,10,13
    14,ONIX,10,13
    14,SWINUB,10,13
Water,21
    24,BARBOACH,10,13
    24,CLAUNCHER,10,13
    24,HORSEA,10,13
    24,SHELLOS,10,13
	4,DITTO,10,13
#-------------------------------
[182] # Mt. Silver Room 1
Cave,21
    10,KINGAMBIT,64,68
    10,GENGAR,64,68
    10,GOLEM,64,68
    10,RHYPERIOR,64,68
    9,HAXORUS,64,68
    9,MAGNEZONE,64,68
    8,ALAKAZAM,64,68
    8,CLEFABLE,64,68
    8,MACHAMP,64,68
    8,STEELIX,64,68
    5,GALLADE,64,68
    5,GARDEVOIR,64,68
#-------------------------------
[183] # Mt. Silver Room 2
Cave,21
	10,KINGAMBIT,64,68
    10,GENGAR,64,68
    10,GOLEM,64,68
    10,RHYPERIOR,64,68
    9,HAXORUS,64,68
    9,MAGNEZONE,64,68
    8,ALAKAZAM,64,68
    8,CLEFABLE,64,68
    8,MACHAMP,64,68
    8,STEELIX,64,68
    5,GALLADE,64,68
    5,GARDEVOIR,64,68
Water,21
    23,CLOYSTER,64,68
    23,STARMIE,64,68
    23,TOXAPEX,64,68
    23,WAILORD,64,68
    4,DRAGONAIR,64,68
    4,KINGDRA,64,68
#-------------------------------
[184] # Silver Pass
Land,21
    17,ARCHALUDON,64,68
    17,KLEAVOR,64,68
    17,SCIZOR,64,68
    17,SCYTHER,64,68
    17,VIKAVOLT,64,68
    17,VOLCARONA,64,68
    5,GIMMIGHOUL,64,68
#-------------------------------
[185] # Lavender Town Mart
Cave,21
    20,DRIFBLIM,46,50
    20,HAUNTER,46,50
    20,LAMPENT,46,50
    20,ROTOM,46,50
    6,DOUBLADE,46,50
    6,GIMMIGHOUL,46,50
    6,MIMIKYU,46,50
    2,GENGAR,46,50
#-------------------------------
[186] # Whirl Islands Cave B1F
Cave,21
    10,MAWILE,20,24
    9,CLEFAIRY,20,24
    9,GASTLY,20,24
    9,MACHOP,20,24
    9,MANKEY,20,24
    10,SABLEYE,20,24
    8,SNEASEL,20,24
    9,SOLOSIS,20,24
    9,TOEDSCOOL,20,24
    9,TORKOAL,20,24
    9,TRAPINCH,20,24
#-------------------------------
[190] # Route 24
Land,21
    15,DUBWOOL,38,41
    15,GRAFAIAI,38,41
    15,GREEDENT,38,41
	15,STOUTLAND,38,41
    14,RUFFLET,38,41
    10,SHELMET,38,41
	16,PERSIAN,38,41
LandNight,21
    15,DUBWOOL,38,41
    15,GRAFAIAI,38,41
    15,GREEDENT,38,41
    15,NOCTOWL,38,41
    14,URSARING,38,41
    10,KARRABLAST,38,41
	16,PERSIAN,38,41
Water,21
    20,BARBOACH,38,41
    20,BASCULIN,38,41
    20,DREDNAW,38,41
    20,QWILFISH,38,41
    16,CLAWITZER,38,41
    4,FEEBAS,38,41
#-------------------------------
[194] # Cerulean Cave 1F
Cave,21
    10,ARCHALUDON,65,70
    10,CINDERACE,65,70
    10,DRAGONITE,65,70
    10,FERALIGATR,65,70
    10,GARCHOMP,65,70
    10,HAXORUS,65,70
    10,KINGAMBIT,65,70
    10,NOIVERN,65,70
    10,SCEPTILE,65,70
    10,VOLCARONA,65,70
#-------------------------------
[195] # Cerulean Cave B1F
Cave,21
    10,AEGISLASH,65,70
    10,CROBAT,65,70
    10,GOGOAT,65,70
    10,INFERNAPE,65,70
    10,LUCARIO,65,70
    10,MAMOSWINE,65,70
    10,METAGROSS,65,70
    10,TYRANITAR,65,70
    10,VANILLUXE,65,70
    10,VENUSAUR,65,70
Water,21
    15,BASCULEGION,65,70
    15,GYARADOS,65,70
    15,KINGDRA,65,70
    15,LAPRAS,65,70
    15,MILOTIC,65,70
    15,WALREIN,65,70
    10,SWAMPERT,65,70
#-------------------------------
[198] # Whirl Islands Cave SE
Cave,21
    10,MAWILE,20,24
    9,CLEFAIRY,20,24
    9,GASTLY,20,24
    9,MACHOP,20,24
    9,MANKEY,20,24
    10,SABLEYE,20,24
    8,SNEASEL,20,24
    9,SOLOSIS,20,24
    9,TOEDSCOOL,20,24
    9,TORKOAL,20,24
    9,TRAPINCH,20,24
#-------------------------------
[220] # Route 18
Land,21
    14,ARBOLIVA,48,52
    14,GLIGAR,48,52
    14,KILOWATTREL,48,52
    14,STANTLER,48,52
    13,STOUTLAND,48,52
    13,SUDOWOODO,48,52
    8,CYCLIZAR,48,52
    7,GREEDENT,48,52
    3,DUBWOOL,48,52
LandNight,21
    14,GLIGAR,48,52
    14,GRAFAIAI,48,52
    14,KILOWATTREL,48,52
    14,STANTLER,48,52
    13,OBSTAGOON,48,52
    13,SUDOWOODO,48,52
    8,CYCLIZAR,48,52
    7,DUBWOOL,48,52
    3,GREEDENT,48,52
Water,21
    30,CLAWITZER,48,52
    30,PELIPPER,48,52
    30,SHARPEDO,48,52
    6,TOXAPEX,48,52
    2,OVERQWIL,48,52
    2,WALREIN,48,52
#-------------------------------
[221] # Route 16
Land,21
    14,ARBOLIVA,48,52
    14,GLIGAR,48,52
    14,KILOWATTREL,48,52
    14,STANTLER,48,52
    13,STOUTLAND,48,52
    13,SUDOWOODO,48,52
    8,CYCLIZAR,48,52
    7,GREEDENT,48,52
    3,DUBWOOL,48,52
LandNight,21
    14,GLIGAR,48,52
    14,GRAFAIAI,48,52
    14,KILOWATTREL,48,52
    14,STANTLER,48,52
    13,OBSTAGOON,48,52
    13,SUDOWOODO,48,52
    8,CYCLIZAR,48,52
    7,DUBWOOL,48,52
    3,GREEDENT,48,52
Water,21
    30,CLAWITZER,48,52
    30,PELIPPER,48,52
    30,SHARPEDO,48,52
    6,TOXAPEX,48,52
    2,OVERQWIL,48,52
    2,WALREIN,48,52
#-------------------------------
[222] # Route 37
Land,21
    14,ESPURR,15,17
    14,RIOLU,15,17
    14,SANDSHREW,15,17
    14,SKIDDO,15,17
    14,STANTLER,15,17
	14,PHANPY,15,17
    8,ZORUA,15,17
    8,SHROOMISH,15,17
HeadbuttHigh
	26,TANGELA,15,17
	25,TEDDIURSA,15,17
	25,SKWOVET,15,17
	24,VOLTORB,15,17
HeadbuttLow
	26,TANGELA,15,17
	25,TEDDIURSA,15,17
	25,SKWOVET,15,17
	24,VOLTORB,15,17
#-------------------------------
[223] # Route 41
Water,21
    10,BASCULIN,20,22
    10,HORSEA,20,22
    10,MANTYKE,20,22
    10,SHELLDER,20,22
    10,TENTACOOL,20,22
    10,WAILMER,20,22
    8,BINACLE,20,22
    8,CHINCHOU,20,22
    8,EISCUE,20,22
    8,QWILFISH,20,22
    8,SPHEAL,20,22
#-------------------------------
[224] # Route 25
Land,21
    15,DUBWOOL,38,41
    15,GRAFAIAI,38,41
    15,GREEDENT,38,41
	15,STOUTLAND,38,41
    14,RUFFLET,38,41
    10,SHELMET,38,41
	16,PERSIAN,38,41
LandNight,21
    15,DUBWOOL,38,41
    15,GRAFAIAI,38,41
    15,GREEDENT,38,41
    15,NOCTOWL,38,41
    14,URSARING,38,41
    10,KARRABLAST,38,41
	16,PERSIAN,38,41
Water,21
    20,BARBOACH,38,41
    20,BASCULIN,38,41
    20,DREDNAW,38,41
    20,QWILFISH,38,41
    16,CLAWITZER,38,41
    4,FEEBAS,38,41
#-------------------------------
[225] # Route 19
Water,21
    12,QWILFISH,50,54
    12,SEADRA,50,54
    12,SHARPEDO,50,54
    12,STARYU,50,54
    11,GASTRODON,50,54
    11,MANTINE,50,54
    11,OCTILLERY,50,54
    11,SHELLDER,50,54
    4,WAILORD,50,54
    4,WALREIN,50,54
#-------------------------------
[243] # Route 46
Land,21
    16,LILLIPUP,2,3
	16,NIDORANmA,2,3
    18,SCATTERBUG,2,3
    16,STARLY,2,3
    15,PIKIPEK,2,3
    15,ROOKIDEE,2,3
    4,RALTS,2,3
LandNight,21
    16,LILLIPUP,2,3
	16,NIDORANmA,2,3
    18,SCATTERBUG,2,3
    20,ZIGZAGOON,2,3
    16,HOOTHOOT,2,3
    10,PIKIPEK,2,3
    4,RALTS,2,3
#-------------------------------
[244] # Route 45
Land,21
    22,CARKOL,32,33
    22,GRAVELER,32,34
    22,NACLSTACK,32,34
    15,LYCANROC,32,34
    14,GLIGAR,32,34
    5,COALOSSAL,35
LandNight,21
    24,GRAVELER,32,34
    20,CARKOL,32,33
    20,NACLSTACK,32,34
    16,LYCANROC,32,34
    10,GLIMMET,32,34
    5,COALOSSAL,35
    5,GLIMMORA,35
#-------------------------------
[245] # Route 26
Land,21
    15,DUOSION,32,34
	15,MUDSDALE,32,34
    14,MAGNETON,32,34
    14,TOEDSCRUEL,32,34
    14,STANTLER,32,34
    14,SANDILE,32,34
    14,HATTREM,32,34
LandNight,21
	15,PAWNIARD,32,34
    15,DUSKULL,32,34
    14,MAGNETON,32,34
    14,TOEDSCRUEL,32,34
    14,MORGREM,32,34
    14,SANDILE,32,34
    14,STANTLER,32,34
Water,21
    14,GASTRODON,32,34
    14,OCTILLERY,32,34
    13,QWILFISH,32,34
    13,SEADRA,32,34
    13,TENTACRUEL,32,34
    13,WAILMER,32,34
    13,WHISCASH,32,34
    7,SHARPEDO,32,34
HeadbuttHigh
	24,NOCTOWL,32,34
	24,CAPSAKID,32,34
	24,SKORUPI,32,34
	24,XATU,32,34
	4,SCYTHER,32,34
HeadbuttLow
	24,NOCTOWL,32,34
	24,CAPSAKID,32,34
	24,SKORUPI,32,34
	24,XATU,32,34
	4,SCYTHER,32,34
#-------------------------------
[246] # Tohjo Falls
Cave,21
    20,EXCADRILL,32,34
    20,LAIRON,32,34
    20,MAROWAK,32,34
    20,NOIBAT,32,34
    20,SLUGMA,32,34
Water,21
    20,BASCULIN,32,34
    20,CLAUNCHER,32,34
    20,LANTURN,32,34
    20,STARYU,32,34
    10,SEADRA,32,34
    10,SHELLDER,32,34
#-------------------------------
[258] # Johto Safari Zone
Land,21
    8,BULBASAUR,10
    8,CHIMCHAR,10
    8,CUBONE,22,25
    8,EXEGGCUTE,22,25
    8,GIMMIGHOUL,22,25
    8,MILTANK,22,25
    8,PETILIL,22,25
    8,PIKACHU,22,25
    8,RUFFLET,22,25
    8,SCYTHER,22,25
    8,SNORLAX,22,25
    8,TAUROS,22,25
    2,BELDUM,15
    2,LARVITAR,20
Water,21
    20,BERGMITE,22,25
    20,CLODSIRE,22,25
    20,INKAY,20
    20,QUAGSIRE,22,25
    10,GRIMER,22,25
    8,MUDKIP,10
    2,DRATINI,22,25
#-------------------------------
[265] # Whirl Islands Cave SW
Cave,21
    10,MAWILE,20,24
    9,CLEFAIRY,20,24
    9,GASTLY,20,24
    9,MACHOP,20,24
    9,MANKEY,20,24
    10,SABLEYE,20,24
    8,SNEASEL,20,24
    9,SOLOSIS,20,24
    9,TOEDSCOOL,20,24
    9,TORKOAL,20,24
    9,TRAPINCH,20,24
Water,21
    10,GULPIN,20,24
    10,BASCULIN,20,24
    10,CHINCHOU,20,24
    10,HORSEA,20,24
    10,MANTYKE,20,24
    10,QWILFISH,20,24
    10,SHELLDER,20,24
    10,SPHEAL,20,24
    10,TENTACOOL,20,24
    10,WAILMER,20,24
#-------------------------------
[019] # Route 2
Land,21
	15,PIKACHU,42,45
	15,SKARMORY,42,45
	15,RELLOR,42,45
	15,HOUNDOOM,42,45
	15,AMPHAROS,42,45
	15,NIDORINO,42,45
	5,GOLURK,43,45
	5,HATTERENE,42,45
LandNight,21
	15,PIKACHU,42,45
	15,SKARMORY,42,45
	15,RELLOR,42,45
	15,HOUNDOOM,42,45
	15,LUXRAY,42,45
	15,NIDORINO,42,45
	5,GOLURK,43,45
	5,GRIMMSNARL,42,45
HeadbuttHigh
	25,SKARMORY,42,45
	25,JUMPLUFF,42,45
	25,FERROTHORN,42,45
	25,FORRETRESS,42,45
HeadbuttLow
	25,SKARMORY,42,45
	25,JUMPLUFF,42,45
	25,FERROTHORN,42,45
	25,FORRETRESS,42,45
#-------------------------------
[080] # Vermilion Cave
Cave,21
	20,EXCADRILL,42,45
	20,DONPHAN,42,45
	20,SANDSLASH,42,45
	20,RHYDON,42,45
	16,ONIX,42,45
	4,STEELIX,42,45
"""

# Dictionary to store Pokémon data
pokemon_locations = defaultdict(list)

# Regular expressions for parsing
location_pattern = re.compile(r'\[(\d+)\] # (.+)')
encounter_pattern = re.compile(r'(\w+),\d+')
pokemon_pattern = re.compile(r'(\d+),([A-Z]+),\d+,\d+')

# Variables to keep track of current location and encounter type
current_location = None
current_encounter = None

# Parsing the text line by line
for line in text.splitlines():
    line = line.strip()
    if location_match := location_pattern.match(line):
        current_location = location_match.group(2)  # e.g., "Route 33"
    elif encounter_match := encounter_pattern.match(line):
        current_encounter = encounter_match.group(1)  # e.g., "Land"
    elif pokemon_match := pokemon_pattern.match(line):
        encounter_rate = pokemon_match.group(1)
        pokemon_name = pokemon_match.group(2).capitalize()  # Capitalize first letter only
        pokemon_locations[pokemon_name].append((current_location, current_encounter, encounter_rate))

# Function to generate HTML for a specific Pokémon
def generate_html(pokemon_name, locations):
    html = f"<!-- {pokemon_name} -->\n<h2 id=\"locations\">Locations</h2>\n<table>\n"
    html += "  <thead>\n    <tr>\n      <th>Route</th>\n      <th>Encounter Type</th>\n      <th>Encounter Rate</th>\n    </tr>\n  </thead>\n"
    html += "  <tbody>\n"
    for location, encounter_type, encounter_rate in locations:
        html += f"    <tr>\n      <td>{location}</td>\n      <td>{encounter_type}</td>\n      <td>{encounter_rate}%</td>\n    </tr>\n"
    html += "  </tbody>\n</table>\n"
    return html

# Generate HTML for all Pokémon
all_html_output = ""
for pokemon_name, locations in pokemon_locations.items():
    all_html_output += generate_html(pokemon_name, locations) + "\n"
    
# Write the HTML output to a file
output_file = 'pokemon_locations.html'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(all_html_output)

# Print the full HTML output
print(all_html_output)
