from bcsv import *

enum_009fa2d460ce_286d6aa2ee6b = (
	('EC', '東進入禁止'),
	('WC', '西進入禁止'),
	('3B', '東西進入可'),
)

enum_01016811d685_37fe72043e75 = (
	('KeepSwimming'  , '回遊：通常'),
	('Float'         , '待機'),
	('RoundsSwimming', '回遊：見回り'),
	('ChasePlayer'   , 'プレイヤーサーチ'),
	('Legion'        , '大群'),
	('Predator'      , '捕食者'),
	('AntiStream'    , '抗水流'),
	('SwimAndWait'   , '回遊＆待機'),
)

enum_017c76af34f4_35ed35a1a2a5 = (
	('Light'     , '軽い'),
	('Normal'    , '通常'),
	('Heavy'     , '重い'),
	('VeryHeavy' , 'すごく重い'),
	('LightWheel', 'キャスター：軽い'),
	('HeavyWheel', 'キャスター：重い'),
	('Floated'   , '浮遊'),
)

enum_046a2d7d535d_d28a72f9a4ec = (
	('Free'   , '性別なし'),
	('Manly'  , '男性向け'),
	('Womanly', '女性向け'),
)

enum_04c6f73235ef_eb1f48d30352 = (
	('Normal' , 'イーブン'),
	('Shuffle', 'シャッフル'),
	('Random' , 'ランダム'),
)

enum_05496a929e72_1987c9f2e67f = (
	('Shop'  , 'お店'),
	('Label1', 'タヌポート'),
)

enum_0571932eb060_3c22bd5c3fdd = (
	('None'    , 'なし'),
	('Simple'  , 'シンプル'),
	('Gorgeous', 'ゴージャス'),
	('Cool'    , 'クール'),
	('Cute'    , 'キュート'),
	('Active'  , 'アクティブ'),
	('Elegant' , 'エレガント'),
)

enum_06495113f123_3d33eb822663 = (
	('None' , 'なし'),
	('Right', '直角'),
	('Slant', '斜め'),
)

enum_064edb92c317_a4705285e5f1 = (
	('Sale'      , '販売品'),
	('NotForSale', '非売品'),
	('NotSee'    , '掲載不可'),
)

enum_07500acb2a20_c4ab2d74d5ad = (
	('AllRegion'   , '全リージョン'),
	('ExceptEurope', '欧州以外'),
)

enum_07d126e46327_fafea373c976 = (
	('None'  , '未設定'),
	('High'  , '高'),
	('Normal', '中'),
	('Low'   , '低'),
)

enum_09c40b1f72c1_d8cf6e1a81aa = (
	('DNE_NNW', '昼：北東、夜：北西'),
	('DNW_NNE', '昼：北西、夜：北東'),
)

enum_0a0cce2b4f07_e7b3e2de0566 = (
	('Normal'                      , '通常'),
	('OnlyWallNoGravity'           , '壁のみ/重力無'),
	('OnlyWall'                    , '壁のみ/重力有'),
	('OnlyFloor'                   , '床のみ/重力有'),
	('OnlyOriginalFloor'           , '書き換え前の床のみ/重力有'),
	('NoBgCheckNoGravity'          , 'BGチェック無/重力無'),
	('NoBgCheckUseGravity'         , 'BGチェック無/重力有'),
	('OnlyWallNoGravity_SitSpecial', '立ちのとき壁のみ、座り時BGチェック無/重力無'),
)

enum_0caaf5f51cb7_b79133e4ebb1 = (
	('None'    , 'なし'),
	('Synchro' , '同期'),
	('Random'  , 'ランダム'),
	('LightOff', '消灯'),
)

enum_0e2adceecdfa_0e2adceecdfa = (
	('1x1', '1x1'),
	('3x3', '3x3'),
)

enum_0ed369abe447_b58ba6b527fb = (
	('None'         , 'なし'),
	('Chair'        , 'イス'),
	('ChestOrCloset', 'タンス・クロゼット'),
	('Table'        , 'テーブル'),
	('Bed'          , 'ベッド'),
)

enum_106465ec3a51_1268c2c082da = (
	('Normal', '通常の家'),
	('Tent'  , 'テント'),
	('None'  , 'なし'),
)

enum_10a6294998ff_537c16dab4e8 = (
	('None'  , '追従なし'),
	('Auto'  , '自動追従'),
	('Manual', '手動追従'),
)

enum_10c129883403_814d6adbca21 = (
	('SpNpcOnly'        , '特殊NPCの会話中のみ(自動通信あり)'),
	('ReadOnly'         , '参照のみ可能'),
	('ManualSend'       , '自動通信しない(送信を自前で対応する)'),
	('BitSend'          , 'ビット管理（無断使用不可）'),
	('NoCheck'          , '警告なし（無断使用不可）'),
	('HetHostOnly'      , '自分の村のみ書き換え可(自動通信あり)'),
	('ReadMyVillageOnly', '自分の村のみ参照のみ可能(AOC用)'),
)

enum_10d294d5ba3c_9f0b7bd1cc21 = (
	('None'  , 'なし'),
	('All'   , '通年'),
	('Spring', '春'),
	('Summer', '夏'),
	('Autum' , '秋'),
	('Winter', '冬'),
)

enum_156e850c7e27_b09d6477c3b6 = (
	('FtrLoopAuto'                 , 'FtrLoopAuto'),
	('FtrLoopFade'                 , 'FtrLoopFade'),
	('FtrLoopSwitch'               , 'FtrLoopSwitch'),
	('FtrTriggerOnOff'             , 'FtrTriggerOnOff'),
	('FtrTriggerOnce'              , 'FtrTriggerOnce'),
	('FtrTriggerToLoopOnOff'       , 'FtrTriggerToLoopOnOff'),
	('FtrTriggerToLoopWaitEndOnOff', 'FtrTriggerToLoopWaitEndOnOff'),
	('FtrChest'                    , 'FtrChest'),
	('FtrMailBox'                  , 'FtrMailBox'),
	('FtrTV'                       , 'FtrTV'),
	('FtrLoopTrigger'              , 'FtrLoopTrigger'),
	('FtrLoopTriggerWaitEndOnKeep' , 'FtrLoopTriggerWaitEndOnKeep'),
	('FtrInsectSing'               , 'FtrInsectSing'),
	('FtrActionMusicJacket'        , 'FtrMusicJacket'),
)

enum_17a769bfe354_791918aecc14 = (
	('Invalid'  , '未使用'),
	('Red'      , '赤'),
	('Pink'     , 'ピンク'),
	('Yellow'   , '黄'),
	('Purple'   , '紫'),
	('Green'    , '緑'),
	('Blue'     , '青'),
	('LightBlue', '水色'),
	('Black'    , '黒'),
)

enum_19d95e13020f_5e46daa0967c = (
	('None'        , 'なし'),
	('FluorLamp'   , '電球'),
	('Candle'      , 'ろうそく'),
	('EmissionOnly', 'エミッションのみ'),
	('SpotLight'   , 'スポットライト'),
	('Monitor'     , 'モニター'),
)

enum_1be25fe2a516_ddd20c924fed = (
	('Orange', '白熱灯'),
	('White' , '蛍光灯'),
)

enum_1dbcb57b21ff_7eb8e52a5bb1 = (
	('Chair'             , 'イス・スツール'),
	('Sofa'              , 'ソファ・ベンチ'),
	('Desk'              , '机'),
	('Table'             , 'テーブル'),
	('Bed'               , 'ベッド'),
	('Chest'             , 'タンス・クローゼット'),
	('Shelf'             , '棚'),
	('Dresser'           , 'ドレッサー'),
	('Screen'            , 'スクリーン'),
	('Arch'              , 'アーチ'),
	('WorkBench'         , '作業台'),
	('SewingTable'       , '裁縫台'),
	('Kitchen'           , 'キッチン'),
	('KitchenThings'     , '雑貨：キッチン'),
	('Dining'            , '雑貨：食卓'),
	('Lamp'              , '照明'),
	('TV'                , 'テレビ'),
	('GameConsole'       , 'ゲーム機'),
	('Audio'             , 'オーディオ機器'),
	('MusicalInstrument' , '楽器'),
	('Clock'             , '時計'),
	('HouseDoorDeco'     , 'ドア飾り'),
	('HomeAppliances'    , '生活家電'),
	('Fan'               , '扇風機系'),
	('AirConditioning'   , 'エアコン'),
	('Heating'           , '暖房'),
	('Fireplace'         , '暖炉'),
	('Toilet'            , '便器'),
	('Bathtub'           , '浴槽'),
	('BathroomThings'    , '雑貨：バス・トイレ'),
	('Beauty'            , '雑貨：美容系'),
	('Plants'            , '植物'),
	('Study'             , '雑貨：書斎'),
	('Supplies'          , '雑貨：家庭'),
	('School'            , '雑貨：学校'),
	('Office'            , '雑貨：オフィス'),
	('Hospital'          , '雑貨：病院'),
	('Museum'            , '雑貨：博物館系'),
	('Shop'              , '雑貨：お店'),
	('SuppliesFacility'  , '雑貨：施設'),
	('Seaside'           , '雑貨：海辺'),
	('Space'             , '雑貨：宇宙'),
	('Star'              , '雑貨：星'),
	('Vehicle'           , '雑貨：交通'),
	('Animal'            , '雑貨：動物'),
	('Fish'              , '雑貨：魚'),
	('FishSP'            , '雑貨：魚SP'),
	('Insect'            , '雑貨：昆虫'),
	('InsectSP'          , '雑貨：昆虫SP'),
	('Toy'               , '雑貨：玩具'),
	('Sports'            , '雑貨：スポーツ'),
	('Playground'        , '雑貨：公園'),
	('SuppliesOutdoors'  , '雑貨：アウトドア'),
	('Ranch'             , '雑貨：畑・牧場'),
	('Garden'            , '雑貨：庭'),
	('JapaneseStyle'     , '雑貨：和風'),
	('SuppliesFolkCraft' , '雑貨：民芸品'),
	('Easter'            , '雑貨：イースター'),
	('SuppliesSeason'    , '雑貨：季節イベント'),
	('Compass'           , 'ポケ森コラボ'),
	('Picture'           , '絵画'),
	('Sculpture'         , '彫刻'),
	('Bromide'           , 'ブロマイド'),
	('Posters'           , 'ポスター'),
	('None'              , '未設定'),
	('Unnecessary'       , '設定不要'),
	('Wood'              , '◆◆木'),
	('Herringbone'       , '◆ヘリンボーン'),
	('Country'           , '◆パーケットフローリング'),
	('DecoWood'          , '◆デコレーションフローリング'),
	('ColorfulWood'      , '◆カラフルフローリング'),
	('PaintWood'         , '◆ペイントフローリング'),
	('ParquetIron'       , '◆アイアンパーケット'),
	('Parquet'           , '◆スクエアな寄せ木'),
	('SimpleParquet'     , '◆シンプルな寄せ木'),
	('Tatami'            , '◆畳'),
	('TatamiPanel'       , '◆淵無し畳'),
	('Japanese'          , '◆和風'),
	('Stone'             , '◆◆石'),
	('Iron'              , '◆鉄'),
	('Brick'             , '◆レンガ'),
	('ArchBrick'         , '◆アーチレンガ'),
	('Tile'              , '◆◆タイル'),
	('Argyle'            , '◆アーガイル'),
	('Chocolate'         , '◆アソート'),
	('Honeycomb'         , '◆ハニカムタイル'),
	('FloorKitchen'      , '◆レトロなクロス'),
	('Morocco'           , '◆モロッカンタイル'),
	('FloorTile'         , '◆モザイクタイル'),
	('TileChecker'       , '◆ピータイル'),
	('Cloth'             , '◆◆布'),
	('Dot'               , '◆ドットカーペット'),
	('Panel'             , '◆パネルカーペット'),
	('PuzzleMat'         , '◆パズル'),
	('Rubber'            , '◆ラバー'),
	('SimpleCarpet'      , '◆シンプルカーペット'),
	('Camouflage'        , '◆迷彩'),
	('AnimalFloor'       , '◆動物柄'),
	('Neta'              , '◆◆ネタ：ハチミツ'),
	('Luxury'            , '◆ネタ：高級'),
	('Decadence'         , '◆ネタ：退廃'),
	('FloorMachine'      , '◆ネタ：機械'),
	('Sidewalk'          , '◆歩道'),
	('FloorSports'       , '◆ネタ：スポーツ'),
	('Grassland'         , '◆草'),
	('NatureGreen'       , '◆自然：緑'),
	('NatureFallenLeaves', '◆自然：落ち葉系'),
	('Nature'            , '◆◆自然'),
	('NatureBrown'       , '◆自然：茶'),
	('NatureWhite'       , '◆自然：白'),
	('SpNature'          , '◆◆特殊（自然）'),
	('SpInorganic'       , '◆◆特殊（無機質）'),
	('Sanrio'            , '◆◆サンリオ'),
	('WallWood'          , '■■木'),
	('WallHerringbone'   , '■ヘリンボーン'),
	('WallHall'          , '■ホール'),
	('WallMixPlankWood'  , '■寄せ木'),
	('WallPegbpard'      , '■パンチングボード'),
	('WallPaintWood'     , '■ペイントウッド'),
	('WallPanelMold'     , '■パネルモールド'),
	('WallStone'         , '■■石'),
	('WallBrick'         , '■レンガ'),
	('WallStucco'        , '■ペイントウォール'),
	('WallIron'          , '■■鉄'),
	('WallTin'           , '■トタン'),
	('WallTile'          , '■■タイル'),
	('WallTilee'         , '■タイル'),
	('WallTwoToneTile'   , '■ツートンタイル'),
	('WallMetro'         , '■メトロタイル'),
	('WallWoodTile'      , '■パターンタイル'),
	('WallMorocco'       , '■モロッカンタイル'),
	('WallHoneycomb'     , '■ハニカムタイル'),
	('WallChocolate'     , '■チョコ'),
	('WallCrown'         , '■クラウン'),
	('WallCloth'         , '■■布'),
	('WallSimple'        , '■シンプルクロス'),
	('WallDot'           , '■ドット'),
	('WallHeart'         , '■ハート'),
	('WallCute'          , '■キュート'),
	('WallStripe'        , '■ストライプ'),
	('WallFruit'         , '■フルーツ'),
	('WallFlower'        , '■花柄'),
	('WallManor'         , '■小花柄'),
	('WallCountry'       , '■草花模様'),
	('WallRose'          , '■バラ'),
	('WallFlowerPop'     , '■テキスタイルフラワー'),
	('WallArtDeco'       , '■アールデコ'),
	('WallCamouflage'    , '■迷彩'),
	('WallPuzzle'        , '■パズル'),
	('WallDollhouse'     , '■キルト'),
	('WallToy'           , '■おもちゃ'),
	('WallDiner'         , '■ダイナー'),
	('WallJapanese'      , '■和風'),
	('WallTeaRoom'       , '■茶室'),
	('Asia'              , '■グローバル系'),
	('WallLibrary'       , '■本棚'),
	('WallNeta'          , '■■ネタ'),
	('WallNature'        , '■■自然'),
	('WallSpNatureCool'  , '■■特殊（自然寒色）'),
	('WallSpNatureWarm'  , '■■特殊（自然暖色）'),
	('WallSpIndoor'      , '■■特殊（室内）'),
	('WallSpInorganic'   , '■■特殊（無機質）'),
	('WallSanrio'        , '■■サンリオ'),
	('RugSimple'         , '●●シンプル'),
	('RugPattern'        , '●●柄物：正方形'),
	('RugPatternSlender' , '●●柄物：細長'),
	('RugKitchen'        , '●●キッチンマット'),
	('RugSlender'        , '●●細長マット'),
	('RugWood'           , '●●木'),
	('RugRoundShaggymat' , '●まるいマット'),
	('RugRoundShaggy'    , '●まるいラグ'),
	('RugFruits'         , '●●果物'),
	('RugRose'           , '●●バラ'),
	('RugHeart'          , '●●ハート'),
	('RugStar'           , '●●星'),
	('RugMessageMat'     , '●●メッセージマット'),
	('RugIcon'           , '●●アイコン'),
	('RugPark'           , '●●どうぶつの森'),
	('RugSanrio'         , '●●サンリオ'),
)

enum_1e2429734a5c_ee729020db58 = (
	('None'        , 'なし'),
	('Dot'         , 'ドット'),
	('Stripe'      , 'ストライプ'),
	('CheckA'      , 'チェックA'),
	('CheckB'      , 'チェックB'),
	('TraditionalA', 'トラディショナルA'),
	('TraditionalB', 'トラディショナルB'),
	('Retro'       , 'レトロ'),
	('Natural'     , 'ナチュラル'),
	('Toy'         , 'トイ'),
	('Cool'        , 'クール'),
)

enum_23f7dd8d5dc1_9e5af7814467 = (
	('Always' , '常時'),
	('Daytime', '昼'),
	('Night'  , '夜'),
)

enum_282b3f1c6bd6_e34f70824d5a = (
	('All'            , '全部'),
	('TreeOak'        , '植物：木：広葉樹'),
	('TreeOakStump'   , '植物：木：広葉樹：切り株'),
	('TreeCedar'      , '植物：木：針葉樹'),
	('TreeCedarStump' , '植物：木：針葉樹：切り株'),
	('TreePalm'       , '植物：木：ヤシの木'),
	('TreePalmStump'  , '植物：木：ヤシの木：切り株'),
	('TreeBamboo'     , '植物：木：竹'),
	('TreeBambooStump', '植物：木：竹：切り株'),
	('TreeFruit'      , '植物：木：果物'),
	('TreeEasterEgg'  , '植物：木：イースターのタマゴ'),
	('WeedSpr'        , '植物：雑草：春'),
	('WeedSmr'        , '植物：雑草：夏'),
	('WeedAut0'       , '植物：雑草：秋０'),
	('WeedAut1'       , '植物：雑草：秋１'),
	('WeedAut2'       , '植物：雑草：秋２'),
	('WeedWin0'       , '植物：雑草：冬０'),
	('WeedWin1'       , '植物：雑草：冬１'),
	('TreeMoney'      , '植物：木：金のなる木'),
	('FlwCosmos'      , '植物：花：コスモス'),
	('FlwTulip'       , '植物：花：チューリップ'),
	('FlwPansy'       , '植物：花：パンジー'),
	('FlwRose'        , '植物：花：バラ'),
	('FlwLily'        , '植物：花：ユリ'),
	('FlwAnemones'    , '植物：花：アネモネ'),
	('FlwMum'         , '植物：花：キク'),
	('FlwHyacinth'    , '植物：花：ヒヤシンス'),
	('FlwSuzuran'     , '植物：花：スズラン'),
	('Hole'           , '穴'),
	('Fence'          , '柵'),
	('Stone'          , '岩'),
)

enum_2a04dcc2be18_4ae6d2210ecb = (
	('Level0', 'なし'),
	('Level1', '1段'),
)

enum_2c1ecb54c4b5_fa9288c80a2d = (
	('None'          , 'なし'),
	('Cap'           , '帽子'),
	('AccessoryEye'  , 'アクセサリ：目'),
	('Tops'          , 'トップス'),
	('Bottoms'       , 'ボトムス'),
	('Socks'         , '靴下'),
	('Shoes'         , '靴'),
	('Scoop'         , 'スコップ'),
	('Axe'           , 'オノ'),
	('FishingRod'    , 'つりざお'),
	('Net'           , 'アミ'),
	('Umbrella'      , 'カサ'),
	('GroundMaker'   , '道造成キット'),
	('Watering'      , 'ジョウロ'),
	('Bag'           , 'カバン'),
	('CliffMaker'    , '崖造成キット'),
	('Ladder'        , 'はしご'),
	('ChangeStick'   , '変身ステッキ'),
	('Cracker'       , 'クラッカー'),
	('Slingshot'     , 'パチンコ'),
	('PinataStick'   , 'ピニャータ割り棒'),
	('FenceMaker'    , '柵造成キット'),
	('Book'          , '本'),
	('AccessoryMouth', 'アクセサリ：口'),
	('RiverMaker'    , '川造成キット'),
	('TkkGuitar'     , 'とたけけギター'),
	('PaperFan'      , 'うちわ'),
	('SmartPhone'    , 'スマホ'),
	('Firework'      , '花火'),
	('StickLight'    , 'スティックライト'),
	('SoapBubble'    , 'シャボン玉'),
	('BlowStick'     , 'ふきもどし'),
	('Ocarina'       , 'オカリナ'),
	('Panpipe'       , 'パンフルート'),
	('Tambourine'    , 'タンバリン'),
	('Broom'         , 'ほうき'),
	('Coffee'        , 'コーヒー'),
	('Ice'           , 'アイス'),
	('BagHand'       , '手提げカバン'),
	('JumpStick'     , 'ジャンプ棒'),
	('Dumbbell'      , 'ダンベル'),
	('Windmill'      , 'かざぐるま'),
	('RcmTourFlag'   , 'つぶまめツアー旗'),
	('Firewood'      , '薪'),
	('Spanner'       , 'スパナとかなづち'),
	('HandLens'      , '虫眼鏡'),
	('FruitBasket'   , '果物カゴ'),
	('Duster'        , 'はたき'),
	('CuteBagHand'   , '手提げかばん(キュート)'),
	('CoolBagHand'   , '手提げかばん(クール)'),
	('LowBagHand'    , '手提げかばん(生活度低)'),
	('HighBagHand'   , '手提げかばん(生活度高)'),
	('SmallBook'     , '本(小)'),
	('LightDumbbell' , 'ダンベル(軽い)'),
	('Candy'         , 'キャンディ'),
	('Canister'      , '缶'),
	('Sandwich'      , 'サンドウィッチ'),
	('Doughnut'      , 'ドーナッツ'),
	('Branch'        , 'えだ'),
	('Sketchbook'    , 'スケッチブック'),
	('Balloon'       , 'ふうせん'),
	('Sprayer'       , 'きりふき'),
	('Cop'           , 'コップ'),
	('Smoothie'      , 'スムージー'),
	('Hammer'        , 'かなづち'),
	('Brush'         , 'はけ'),
)

enum_2c27ffe999d6_e4da0c79dac6 = (
	('Communication', 'F0：どうぶつ交流系'),
	('Money'        , 'F1：お金系'),
	('Insect'       , 'F2：ムシ系'),
	('DIY'          , 'F3：ＤＩＹ系'),
	('Event'        , 'F4：イベント系'),
	('Fish'         , 'F5：サカナ系'),
	('HHA'          , 'F6：道具系'),
	('LandMaking'   , 'F7：造成系'),
	('MyDesign'     , 'F8：マイデザイン系'),
	('Negative'     , 'F9：ネガティブ系'),
	('Plant'        , 'F10：植物系'),
	('Smartphone'   , 'F11：スマホ系'),
)

enum_2d78bfb5905f_6f798aada062 = (
	('None'                                    , '-'),
	('TopsTexTopCoatL'                         , 'トレンチコート'),
	('TopsTexTopTshirtsHKungfu'                , 'カンフーなふく'),
	('TopsTexOnepieceAlineNCheer'              , 'チアのコスチューム'),
	('TopsTexTopOuterLStajanBlue'              , 'スタジャン'),
	('TopsTexTopTshirtsHNumberball3'           , '３ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball2'           , '２ばんだまのふく'),
	('TopsTexOnepieceBalloonNSatin'            , 'サテンのワンピース'),
	('TopsTexTopTshirtsNCamisole'              , 'シンプルフリルキャミソール'),
	('TopsTexTopYshirtsLChina'                 , 'チャイナふく'),
	('TopsTexTopTshirtsLRaglan'                , 'ラグランＴシャツ'),
	('TopsTexOnepieceAlineLTweed'              , 'ツイードワンピース'),
	('TopsTexOnepieceAlineHPolkadotSpring'     , 'はるのみずたまワンピース'),
	('TopsTexOnepieceAlineNMuumuu'             , 'パインがらムームー'),
	('TopsTexOnepieceBoxLYosoiki'              , 'よそいきなふく'),
	('TopsTexOnepieceBoxNRetroGreen'           , 'レトロボックスワンピース'),
	('TopsTexTopTshirtsNBasketballshirtsPurple', 'バスケシャツ'),
	('TopsTexTopOuterNKnit'                    , 'ノースリーブのニット'),
	('TopsTexTopOuterLDownjacketBlue'          , 'ダウンジャケット'),
	('TopsTexOnepieceAlineHYumeiro'            , 'ゆめいろこうしワンピース'),
	('TopsTexOnepieceBoxLEnsembleBlue'         , 'せいそなアンサンブル'),
	('TopsTexTopYshirtsLWhite'                 , 'ワイシャツ'),
	('TopsTexOnepieceBalloonHPolkadotBlue'     , 'ベルトつきみずたまワンピース'),
	('TopsTexTopTshirtsHSailor'                , 'はんそでセーラーふく'),
	('TopsTexTopOuterLParkaGray'               , 'シンプルなパーカー'),
	('TopsTexTopTshirtsLSmockTulip'            , 'スモック'),
	('TopsTexOnepieceAlineHFlowerPink'         , 'はながらワンピース'),
	('TopsTexOnepieceBalloonLLolita'           , 'ロリータなワンピース'),
	('SocksTexTights'                          , 'ストッキング'),
	('SocksTexAmitights'                       , 'あみタイツ'),
	('TopsTexOnepieceBoxLChidori'              , 'ちどりごうしワンピース'),
	('TopsTexOnepieceBoxHParty'                , 'パーティーワンピ'),
	('TopsTexOnepieceBoxLBubbly'               , 'バブリーなセットアップ'),
	('TopsTexOnepieceBalloonNXmasRed'          , 'クリスマスなドレス'),
	('TopsTexOnepieceBalloonHHoodRed'          , 'メルヘンなドレス'),
	('TopsTexOnepieceBalloonHMaid'             , 'メイドのふく'),
	('TopsTexTopCoatLAcademicdress'            , 'がくしのふく'),
	('TopsTexOnepieceBalloonHWaitress'         , 'ダイナーのユニフォーム'),
	('TopsTexTopYshirtsHWhite'                 , 'はんそでワイシャツ'),
	('TopsTexTopYshirtsNWhite'                 , 'ノースリーブえりつきシャツ'),
	('TopsTexOnepieceAlineLRabbit'             , 'ウサギなふく'),
	('TopsTexOnepieceAlineLHeroine'            , 'ヒロインスーツ'),
	('TopsTexTopCoatLHanten'                   , 'はんてん'),
	('TopsTexOnepieceBoxLBathrobes'            , 'バスローブ'),
	('TopsTexOnepieceBalloonNBallet'           , 'バレエのいしょう'),
	('TopsTexOnepieceAlineLCat'                , 'ネコなふく'),
	('TopsTexOnepieceBalloonHTyrolean'         , 'チロリアンなドレス'),
	('TopsTexOnepieceAlineNXmastreeNormal'     , 'もみのきワンピース'),
	('TopsTexTopCoatLRain'                     , 'レインコート'),
	('TopsTexTopCoatLNoble'                    , 'きぞくのコート'),
	('TopsTexTopYshirtsHPolo'                  , 'ポロシャツ'),
	('TopsTexTopCoatLWhitecoat'                , 'はくい'),
	('TopsTexTopCoatHCock'                     , 'コックさんのふく'),
	('TopsTexTopCoatLCafe'                     , 'カフェのせいふく'),
	('TopsTexTopTshirtsHGym'                   , 'たいそうふく'),
	('TopsTexTopTshirtsNTanktop'               , 'タンクトップ'),
	('TopsTexTopYshirtsLComedian'              , 'コメディアンなふく'),
	('TopsTexTopYshirtsLRiders'                , 'ライダースジャケット'),
	('TopsTexTopTshirtsNCamisoleprint'         , 'はながらのプリントキャミ'),
	('TopsTexTopYshirtsLDenim'                 , 'デニムジャケット'),
	('TopsTexTopCoatHRubberapron'              , 'ゴムエプロン'),
	('TopsTexTopTshirtsHFishing'               , 'つりジャケット'),
	('TopsTexTopCoatLMouton'                   , 'ムートンコート'),
	('TopsTexTopYshirtsLFlannel'               , 'ネルシャツ'),
	('TopsTexTopYshirtsNDenim'                 , 'そでなしＧジャン'),
	('TopsTexTopCoatHApron'                    , 'エプロン'),
	('TopsTexTopCoatLInfantry'                 , 'へいたいのふく'),
	('TopsTexOnepieceBoxNPrimitive'            , 'げんしじんなふく'),
	('TopsTexTopCoatLGunknight'                , 'じゅうきしのふく'),
	('TopsTexTopYshirtsHAloha'                 , 'パインがらアロハシャツ'),
	('TopsTexTopTshirtsNCamisolelace'          , 'レースのキャミソール'),
	('TopsTexTopOuterLJersey'                  , 'ジャージ'),
	('TopsTexTopYshirtsLWestern'               , 'ウェスタンなふく'),
	('TopsTexTopTshirtsNEkiden'                , 'えきでんなふく'),
	('TopsTexTopYshirtsHChina'                 , 'はんそでチャイナふく'),
	('TopsTexTopTshirtsHSoccer'                , 'サッカーのユニフォーム'),
	('TopsTexTopOuterLSukajantiger'            , 'トラのスカジャン'),
	('TopsTexTopYshirtsHHappi'                 , 'はっぴ'),
	('TopsTexTopOuterLSukajandragon'           , 'ドラゴンのスカジャン'),
	('TopsTexTopTshirtsHCamouflage'            , 'めいさいなふく'),
	('TopsTexTopTshirtsHCycle'                 , 'サイクルジャージ'),
	('TopsTexTopTshirtsHChick'                 , 'ひよこがらＴシャツ'),
	('TopsTexOnepieceDressLPrincess'           , 'プリンセスなふく'),
	('TopsTexOnepieceRibNKnit'                 , 'そでなしニットワンピ'),
	('TopsTexTopYshirtsLArgyle'                , 'アーガイルベスト'),
	('TopsTexTopYshirtsHExplorer'              , 'たんけんふく'),
	('TopsTexTopYshirtsLJacketgaudy'           , 'ハデなジャケット'),
	('TopsTexTopYshirtsLNecktie'               , 'ネクタイつきワイシャツ'),
	('TopsTexTopCoatHItamae'                   , 'いたまえのふく'),
	('TopsTexTopYshirtsLBlazer'                , 'ブレザー'),
	('TopsTexTopCoatLKing'                     , 'おうさまのふく'),
	('TopsTexOnepieceAlineNStrawberry'         , 'イチゴのふく'),
	('TopsTexOnepieceAlineNWatermelon'         , 'スイカのふく'),
	('TopsTexOnepieceAlineNOrange'             , 'オレンジのふく'),
	('TopsTexOnepieceAlineNKiwi'               , 'キウイのふく'),
	('TopsTexOnepieceAlineNGrape'              , 'ぶどうのふく'),
	('TopsTexOnepieceAlineNPineapple'          , 'パイナップルのふく'),
	('BottomsTexPantsNormalSweat'              , 'スウェットパンツ'),
	('BottomsTexSkirtAlineTweed'               , 'ツイードスカート'),
	('BottomsTexPantsNormalLeather'            , 'レザーパンツ'),
	('BottomsTexPantsNormalSlacks'             , 'スラックス'),
	('BottomsTexPantsNormalJersey'             , 'ジャージズボン'),
	('BottomsTexPantsNormalBoder'              , 'ボーダーパンツ'),
	('BottomsTexPantsNormalDenimholes'         , 'あなあきデニム'),
	('TopsTexTopYshirtsLTwotone'               , 'ツートンのエリつきシャツ'),
	('TopsTexTopTshirtsHNumberball1'           , '１ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball4'           , '４ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball5'           , '５ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball6'           , '６ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball7'           , '７ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball8'           , '８ばんだまのふく'),
	('TopsTexTopTshirtsHNumberball9'           , '９ばんだまのふく'),
	('TopsTexTopYshirtsLTiedsweater'           , 'トレンディーなふく'),
	('TopsTexTopYshirtsLSportsjersey'          , 'スポーツジャージ'),
	('BottomsTexPantsNormalSportsjersey'       , 'スポーツジャージのズボン'),
	('BottomsTexSkirtAlineKilt'                , 'キルト'),
	('TopsTexTopYshirtsLGilet'                 , 'ベストつきワイシャツ'),
	('BottomsTexSkirtAlineSailorNavy'          , 'セーラーふくのスカート'),
	('BottomsTexPantsNormalCamouflage'         , 'めいさいパンツ'),
	('TopsTexOnepieceBoxHNurse'                , 'かんごしのワンピース'),
	('TopsTexTopYshirtsHNurse'                 , 'かんごしのジャケット'),
	('BottomsTexPantsWideCargo'                , 'カーゴパンツ'),
	('BottomsTexPantsWideSusomise'             , 'すそみせズボン'),
	('TopsTexOnepieceOverallLPajama'           , 'パジャマ'),
	('TopsTexTopTshirtsNBorder'                , 'ボーダーのタンクトップ'),
	('BottomsTexSkirtAlineLace'                , 'レーススカート'),
	('TopsTexOnepieceBalloonLCorsetPurple'     , 'コルセットドレス'),
	('TopsTexOnepieceBoxLShirt'                , 'シャツワンピ'),
	('TopsTexOnepieceAlineNShirt'              , 'そでなしシャツワンピ'),
	('TopsTexTopYshirtsLTuxedo'                , 'タキシード'),
	('TopsTexTopCoatLMorningcoat'              , 'モーニングコート'),
	('BottomsTexPantsWideSchool'               , 'せいふくのズボン'),
	('BottomsTexPantsNormalSlacksgaudy'        , 'ハデなスラックス'),
	('TopsTexOnepieceOverallLJockey'           , 'ジョッキーのふく'),
	('TopsTexOnepieceOverallLBear'             , 'クマなふく'),
	('TopsTexOnepieceOverallLFirefighter'      , 'しょうぼうしのふく'),
	('TopsTexOnepieceOverallLFrog'             , 'カエルなふく'),
	('TopsTexOnepieceOverallLKappa'            , 'カッパスーツ'),
	('TopsTexOnepieceDressLClassic'            , 'アントワネットなドレス'),
	('TopsTexOnepieceAlongNNile'               , 'ナイルなふく'),
	('TopsTexOnepieceOverallLWorkwear'         , 'さぎょうぎ'),
	('TopsTexOnepieceOverallLClown'            , 'ピエロのふく'),
	('TopsTexOnepieceOverallLHero'             , 'ヒーロースーツ'),
	('TopsTexOnepieceOverallHJinbei'           , 'じんべい'),
	('TopsTexOnepieceOverallLNinja'            , 'しのびのふく'),
	('TopsTexOnepieceOverallLDragon'           , 'ドラゴンスーツ'),
	('BottomsTexPantsWideCowboy'               , 'カウボーイパンツ'),
	('TopsTexOnepieceOverallLHotel'            , 'ホテルマンなふく'),
	('TopsTexTopYshirtsLTailored'              , 'テーラードジャケット'),
	('TopsTexOnepieceBoxLAttendant'            , 'フライトアテンダントのふく'),
	('TopsTexTopYshirtsLVest'                  , 'チョッキつきワイシャツ'),
	('TopsTexOnepieceAlongLWitch'              , 'まほうつかいのローブ'),
	('TopsTexOnepieceBlongLAodai'              , 'アオザイ'),
	('TopsTexOnepieceBlongLKappogi'            , 'かっぽうぎ'),
	('TopsTexOnepieceAlongLChimachogori'       , 'チマチョゴリ'),
	('AccessoryMouthBeakYellow'                , 'くちばし'),
	('AccessoryMouthBeard'                     , 'カイゼルひげ'),
	('TopsTexOnepieceOverallLPolice'           , 'けいかんのふく'),
	('TopsTexOnepieceBlongHToga'               , 'ローマなふく'),
	('TopsTexOnepieceKimonoLUme'               , 'ウメがらのきもの'),
	('TopsTexOnepieceAlongLGothic'             , 'ゴシックなふく'),
	('TopsTexOnepieceBoxNGreece'               , 'ギリシャなふく'),
	('TopsTexTopTshirtsHKanji'                 , 'かんじＴシャツ'),
	('TopsTexOnepieceAlineLMold'               , 'かびたワンピース'),
	('TopsTexOnepieceBlongHEgypt'              , 'エジプトのふく'),
	('TopsTexTopYshirtsLCardiganyshirt'        , 'カーディガン&シャツ'),
	('TopsTexTopOuterLArgyle'                  , 'アーガイルのセーター'),
	('TopsTexTopOuterLFlowerknit'              , 'はながらのニット'),
	('TopsTexTopOuterLTennis'                  , 'テニスセーター'),
	('TopsTexOnepieceOverallNArabia'           , 'アラビアなふく'),
	('TopsTexOnepieceOverallLMummy'            , 'ほうたいのふく'),
	('TopsTexOnepieceOverallLBone'             , 'ボーンなふく'),
	('TopsTexOnepieceOverallNWrestling'        , 'プロレススーツ'),
	('TopsTexOnepieceOverallLBaseball'         , 'やきゅうのふく'),
	('TopsTexOnepieceOverallLPilot'            , 'きちょうのふく'),
	('TopsTexOnepieceOverallLBull'             , 'マタドールなふく'),
	('TopsTexOnepieceDressHHolland'            , 'オランダなドレス'),
	('TopsTexTopOuterLNordic'                  , 'ノルディックなセーター'),
	('TopsTexTopOuterLSnow'                    , 'スノーセーター'),
	('TopsTexTopOuterLNordiccardigan'          , 'ノルディックなカーディガン'),
	('TopsTexTopOuterLAran'                    , 'アランセーター'),
	('TopsTexTopOuterLYumekawa'                , 'ゆめかわなセーター'),
	('TopsTexOnepieceOverallLSpace'            , 'うちゅうふく'),
	('TopsTexTopOuterLArancardigan'            , 'アランカーディガン'),
	('TopsTexOnepieceOverallLRacer'            , 'レーサーなふく'),
	('TopsTexOnepieceAlineHSuspendersskirt'    , 'つりスカート'),
	('TopsTexOnepieceBoxLJumperskirtuniform'   , 'ジャンパースカートのせいふく'),
	('TopsTexTopCoatLNocollar'                 , 'ノーカラーコート'),
	('TopsTexTopYshirtsLRugby'                 , 'ラガーシャツ'),
	('TopsTexOnepieceOverallLSaropetto'        , 'デニムのサロペット'),
	('TopsTexTopOuterLSweat'                   , 'シンプルなトレーナー'),
	('TopsTexOnepieceBalloonHMarine'           , 'マリンルックワンピース'),
	('TopsTexTopTshirtsLHenley'                , 'ヘンリーネックＴシャツ'),
	('TopsTexTopTshirtsHGillet'                , 'ジレコーデＴシャツ'),
	('TopsTexTopCoatHStripeshirts'             , 'オーバーストライプシャツ'),
	('TopsTexTopCoatLCoverall'                 , 'カバーオール'),
	('TopsTexOnepieceBlongHSally'              , 'サリー'),
	('TopsTexOnepieceBalloonHStrange'          , 'ふしぎなワンピース'),
	('TopsTexTopYshirtsHCuba'                  , 'キューバシャツ'),
	('TopsTexTopCoatLPcoat'                    , 'ピーコート'),
	('TopsTexTopYshirtsLNocollar'              , 'ノーカラーシャツ'),
	('TopsTexTopYshirtsLWork'                  , 'ワークシャツ'),
	('TopsTexOnepieceAlongLBustier'            , 'ビスチェワンピース'),
	('TopsTexTopYshirtsHBowling'               , 'ボウリングシャツ'),
	('TopsTexTopTshirtsLVnecksweater'          , 'Ｖネックセーター'),
	('TopsTexOnepieceBalloonNFairy'            , 'ようせいのふく'),
	('ShoesSandalGetaBlack'                    , 'げた'),
	('TopsTexTopYshirtsLFleece'                , 'ボアフリース'),
	('TopsTexTopYshirtsLTweed'                 , 'ツイードジャケット'),
	('TopsTexOnepieceOverallLSuspenders'       , 'サスペンダーなふく'),
	('BottomsTexPantsWideTweed'                , 'ツイードパンツ'),
	('TopsTexTopTshirtsLLayeredtshirts'        , 'かさねぎＴシャツ'),
	('TopsTexTopTshirtsHLace'                  , 'レースのシャツ'),
	('TopsTexTopCoatLChester'                  , 'チェスターコート'),
	('TopsTexTopCoatLChestercheck'             , 'チェックのチェスターコート'),
	('BottomsTexPantsHalfCargo'                , 'ハーフカーゴパンツ'),
	('TopsTexTopTshirtsHBigstole'              , 'おおばんストールＴシャツ'),
	('TopsTexOnepieceOverallHDwarf'            , 'こびとのふく'),
	('BottomsTexPantsHotRunning'               , 'ランニングパンツ'),
	('TopsTexTopYshirtsLPrince'                , 'おうじさまシャツ'),
	('TopsTexTopTshirtsNFitness'               , 'フィットネスタンクトップ'),
	('TopsTexTopOuterLFlight'                  , 'フライトジャケット'),
	('TopsTexTopTshirtsHTiedye'                , 'タイダイＴシャツ'),
	('TopsTexTopYshirtsLBoavest'               , 'ボアベスト'),
	('TopsTexTopCoatLQuilting'                 , 'キルティングダウン'),
	('BottomsTexSkirtLongPleats'               , 'ロングプリーツスカート'),
	('BottomsTexSkirtAlineTennis'              , 'テニススカート'),
	('AccessoryGlass'                          , 'まるめがね'),
	('AccessoryGlassSquare'                    , 'スクエアめがね'),
	('AccessoryGlassHeart'                     , 'ハートのサングラス'),
	('AccessoryGlassThurmont'                  , 'サーモントめがね'),
	('AccessoryGlassOctagon'                   , 'オクタゴンめがね'),
	('AccessoryGlassStar'                      , 'ほしのサングラス'),
	('AccessoryGlassBoston'                    , 'ボストンめがね'),
	('AccessoryGlassTriangle'                  , 'さんかくサングラス'),
	('BottomsTexSkirtBoxDenim'                 , 'デニムスカート'),
	('TopsTexTopTshirtsLPeasant'               , 'ペザントブラウス'),
	('TopsTexOnepieceAlongHNegligee'           , 'ネグリジェ'),
	('TopsTexOnepieceOverallLJudo'             , 'じゅうどうぎ'),
	('BottomsTexPantsHotDenimholes'            , 'あなあきショートデニム'),
	('BottomsTexSkirtLongDot'                  , 'みずたまロングスカート'),
	('TopsTexTopTshirtsNTubetop'               , 'チューブトップ'),
	('BottomsTexPantsWideHickory'              , 'ヒッコリーのペインターパンツ'),
	('BottomsTexPantsNormalChain'              , 'チェーンつきパンツ'),
	('BottomsTexPantsNormalDown'               , 'ダウンパンツ'),
	('BottomsTexSkirtLongChino'                , 'ロングチノスカート'),
	('TopsTexOnepieceAlineLBorder'             , 'ボーダーワンピース'),
	('AccessoryGlassDoublebridge'              , 'ダブルブリッジめがね'),
	('TopsTexOnepieceAlineHLinen'              , 'リネンワンピース'),
	('BottomsTexSkirtBoxDown'                  , 'ダウンスカート'),
	('TopsTexTopTshirtsNMuscle'                , 'マッスルタンクトップ'),
	('TopsTexOnepieceKimonoLWizard'            , 'まじゅつしのローブ'),
	('BottomsTexPantsHotDenim'                 , 'デニムショートパンツ'),
	('TopsTexTopTshirtsHBorder'                , 'はんそでボーダーＴシャツ'),
	('TopsTexTopOuterLDownvest'                , 'ダウンベスト'),
	('AccessoryGlassBottle'                    , 'ビンぞこめがね'),
	('BottomsTexSkirtBoxSweat'                 , 'スウェットスカート'),
	('TopsTexTopYshirtsLCoach'                 , 'コーチジャケット'),
	('TopsTexTopCoatLGowncoat'                 , 'ガウンコート'),
	('TopsTexTopTshirtsLChidori'               , 'ちどりのカーディガン'),
	('TopsTexOnepieceAlineNHalterneckstripe'   , 'ホルターネックのワンピース'),
	('TopsTexTopTshirtsHPocketshirts'          , 'ポケットつきＴシャツ'),
	('TopsTexOnepieceKimonoLMiko'              , 'みこしょうぞく'),
	('BottomsTexSkirtBoxCorduroy'              , 'コーデュロイスカート'),
	('BottomsTexPantsWideGaucho'               , 'ガウチョパンツ'),
	('TopsTexOnepieceBoxNModern'               , 'モガなワンピース'),
	('TopsTexTopYshirtsLSlimknit'              , 'スリムニット'),
	('BottomsTexSkirtBoxLeather'               , 'レザースカート'),
	('TopsTexTopOuterLCollegecardigan'         , 'カレッジカーディガン'),
	('BottomsTexSkirtBoxFringe'                , 'フリンジスカート'),
	('TopsTexOnepieceKimonoLHakama'            , 'はかま'),
	('TopsTexTopTshirtsHKnot'                  , 'まえむすびＴシャツ'),
	('TopsTexOnepieceOverallLTights'           , 'ぜんしんタイツ'),
	('BottomsTexPantsWideDenim'                , 'デニムのペインターパンツ'),
	('TopsTexTopTshirtsHGoldprint'             , 'ゴールドプリントＴシャツ'),
	('TopsTexOnepieceOverallLWaders'           , 'ウェーダー'),
	('BottomsTexPantsNormalChinashort'         , 'チャイナなクロップドパンツ'),
	('BottomsTexPantsNormalChina'              , 'チャイナなズボン'),
	('BottomsTexPantsWideKungfu'               , 'カンフーなズボン'),
	('TopsTexOnepieceBalloonHMagical'          , 'マジカルなドレス'),
	('BottomsTexSkirtBoxGrass'                 , 'こしみの'),
	('TopsTexOnepieceAlineLBolerocoat'         , 'ボレロコート'),
	('TopsTexOnepieceBoxLOffice'               , 'オフィスなふく'),
	('AccessoryGlassCrack'                     , 'ヒビわれめがね'),
	('TopsTexTopTshirtsLAlphabet'              , 'えいじＴシャツ'),
	('TopsTexOnepieceAlongNPearl'              , 'パールつきロングドレス'),
	('TopsTexOnepieceKimonoLKinagashi'         , 'きながし'),
	('TopsTexTopOuterLSukajanhawk'             , 'タカのスカジャン'),
	('TopsTexOnepieceBalloonHSimple'           , 'しっそなドレス'),
	('TopsTexOnepieceOverallLSimple'           , 'しっそなふく'),
	('TopsTexOnepieceBalloonNBunny'            , 'タキシードドレス'),
	('TopsTexOnepieceOverallLFleecepajama'     , 'フリースパジャマ'),
	('TopsTexOnepieceAlongLLeathercoat'        , 'レザーコート'),
	('TopsTexOnepieceBoxNBathtowel'            , 'バスタオル'),
	('TopsTexTopYshirtsLSuitsmen'              , 'スーツ'),
	('BottomsTexPantsWideBellbottoms'          , 'ベルボトムパンツ'),
	('TopsTexTopYshirtsLGakuran'               , 'がくせいふく'),
	('TopsTexTopYshirtsLGakuranopen'           , 'ヤンチャながくせいふく'),
	('TopsTexTopCoatLPoncho'                   , 'ポンチョコート'),
	('BottomsTexPantsWideFrilled'              , 'フリルつきパンツ'),
	('BottomsTexPantsHotYacht'                 , 'ヨットのショートパンツ'),
	('BottomsTexPantsHalfMulticolor'           , 'マルチカラーのハーフパンツ'),
	('BottomsTexPantsHalfFormal'               , 'きれいめハーフパンツ'),
	('BottomsTexSkirtBoxLeopard'               , 'ヒョウがらミニスカート'),
	('BottomsTexSkirtLongCheck'                , 'チェックのロングスカート'),
	('TopsTexTopCoatLVampire'                  , 'ヴァンパイアのふく'),
	('TopsTexOnepieceBoxLAutumncheck'          , 'あきいろチェックワンピース'),
	('BottomsTexPantsNormalNoble'              , 'きぞくのズボン'),
	('TopsTexOnepieceBalloonNBlockcheck'       , 'ブロックチェックワンピ'),
	('TopsTexTopOuterLMaone'                   , 'ＭＡ‐１'),
	('TopsTexTopOuterLCamo'                    , 'めいさいのＭＡ‐１'),
	('TopsTexOnepieceAlongLFrilled'            , 'フリフリワンピース'),
	('BottomsTexPantsHalfAloha'                , 'パインがらアロハパンツ'),
	('TopsTexOnepieceBalloonNIdleeightys'      , 'アイドルなふく'),
	('TopsTexTopYshirtsLHanten'                , 'うみのはんてん'),
	('BottomsTexPantsNormalCropped'            , 'クロップドパンツ'),
	('TopsTexOnepieceBoxLBohemian'             , 'ボヘミアンワンピ'),
	('BottomsTexSkirtAlineFrilled'             , 'フリルスカート'),
	('TopsTexTopOuterLMohair'                  , 'モヘアふうニット'),
	('TopsTexTopOuterLSpaceparker'             , 'スペースパーカー'),
	('TopsTexTopTshirtsHBaseball'              , 'ベースボールシャツ'),
	('TopsTexTopCoatLInparker'                 , 'パーカーオンコート'),
	('TopsTexTopTshirtsNTraining'              , 'ワークアウトトップス'),
	('TopsTexTopCoatLMod'                      , 'モッズコート'),
	('TopsTexTopOuterLParkertshirt'            , 'パーカーオンＴシャツ'),
	('TopsTexOnepieceRibLSwitchsweat'          , 'きりかえビッグスウェット'),
	('AccessoryGlassMask'                      , 'アイマスク'),
	('BottomsTexSkirtAlineTweedfrill'          , 'ツイードフリルスカート'),
	('TopsTexTopCoatLHeartapron'               , 'ハートのエプロン'),
	('BottomsTexPantsWideEasy'                 , 'ワイドイージーパンツ'),
	('TopsTexOnepieceRibNSheep'                , 'ひつじなふく'),
	('TopsTexOnepieceBalloonNSunflower'        , 'ひまわりのワンピース'),
	('TopsTexTopCoatLPrince'                   , 'プリンスなふく'),
	('BottomsTexSkirtBoxCamo'                  , 'めいさいスカート'),
	('TopsTexTopYshirtsHTraffic'               , 'こうつうゆうどうのふく'),
	('TopsTexTopCoatLTailcoat'                 , 'えんびふく'),
	('TopsTexOnepieceOverallHTyrolean'         , 'チロリアンなオーバーオール'),
	('BottomsTexPantsHotCulotte'               , 'キュロット'),
	('TopsTexTopOuterLNative'                  , 'ネイティブニット'),
	('TopsTexTopTshirtsHAmericanfootball'      , 'アメフトシャツ'),
	('TopsTexTopYshirtsLSki'                   , 'スキーウェア'),
	('TopsTexOnepieceOverallLStarsinger'       , 'スタアのふく'),
	('BottomsTexPantsWideSki'                  , 'スキーウェアのズボン'),
	('AccessoryMouthMask'                      , 'マスク'),
	('AccessoryGlassEyepatch'                  , 'がんたい'),
	('AccessoryGlassGogglesski'                , 'スキーゴーグル'),
	('AccessoryGlassGoggles'                   , 'すいえいゴーグル'),
	('AccessoryGlassRetro'                     , 'レトロなサングラス'),
	('AccessoryGlassPatch'                     , 'アイパッチ'),
	('AccessoryGlassSports'                    , 'スポーツサングラス'),
	('AccessoryGlassPilot'                     , 'パイロットサングラス'),
	('AccessoryGlassTortoiseshell'             , 'べっこうめがね'),
	('AccessoryGlassMini'                      , 'ちいさいサングラス'),
	('AccessoryGlassMonocle'                   , 'モノクル'),
	('AccessoryGlassThreed'                    , '3Dめがね'),
	('AccessoryGlassBlind'                     , 'ブラインドサングラス'),
	('TopsTexTopCoatLAnimal'                   , 'フェイクアニマルコート'),
	('TopsTexOnepieceBoxNLayered'              , 'レイヤーノースリーブワンピ'),
	('TopsTexOnepieceBoxHTiger'                , 'トラのＴシャツワンピ'),
	('TopsTexOnepieceRibLParkershirt'          , 'パーカーインシャツワンピ'),
	('TopsTexTopCoatLRetro'                    , 'レトロなコート'),
	('TopsTexOnepieceOverallLRompers'          , 'ロンパース'),
	('TopsTexOnepieceOverallLBondage'          , 'ボンテージ'),
	('BottomsTexPantsHalfOutdoor'              , 'アウトドアパンツ'),
	('TopsTexOnepieceOverallLSuper'            , 'スーパーヒーロースーツ'),
	('AccessoryMouthCat'                       , 'ネコのつけばな'),
	('TopsTexOnepieceDressHChinapoblana'       , 'チナポブラーナ'),
	('BottomsTexPantsNormalBondage'            , 'ボンテージパンツ'),
	('TopsTexTopTshirtsNHula'                  , 'フラダンスなトップス'),
	('BottomsTexPantsHalfEthnic'               , 'エスニックパンツ'),
	('TopsTexTopCoatLHippie'                   , 'ヒッピーなふく'),
	('TopsTexOnepieceRibLShawl'                , 'ショールコーデワンピ'),
	('BottomsTexPantsWideKnee'                 , 'ひざあてズボン'),
	('AccessoryMouthCucumber'                  , 'きゅうりパック'),
	('AccessoryGlassmouthNose'                 , 'つけばな'),
	('AccessoryGlassmouthBeard'                , 'ヒゲメガネ'),
	('BottomsTexSkirtLongTiered'               , 'ティアードスカート'),
	('TopsTexTopYshirtsLCareer'                , 'キャリアなジャケット'),
	('BottomsTexSkirtBoxCareer'                , 'キャリアなスカート'),
	('BottomsTexSkirtLongDrape'                , 'ドレープスカート'),
	('TopsTexOnepieceBalloonHDolly'            , 'ドーリーワンピース'),
	('TopsTexTopYshirtsLChimayo'               , 'チマヨベスト'),
	('AccessoryGlassBirthday'                  , 'バースデーサングラス'),
	('AccessoryGlassmouthPack'                 , 'パック'),
	('AccessoryGlassEyes'                      , 'をかしなめがね'),
	('BottomsTexPantsNormalCycle'              , 'サイクルボトム'),
	('BottomsTexPantsHalfSurf'                 , 'サーフパンツ'),
	('BottomsTexPantsHotLace'                  , 'レースショートパンツ'),
	('BottomsTexPantsHalfJersey'               , 'ジャージショートパンツ'),
	('TopsTexTopCoatLKuruta'                   , 'クルタ'),
	('TopsTexOnepieceBlongLShirt'              , 'ロングシャツワンピ'),
	('TopsTexTopOuterLPullover'                , 'プルオーバーアウター'),
	('BottomsTexPantsHotThai'                  , 'ムエタイパンツ'),
	('BottomsTexPantsHotDotgold'               , 'ゴールドドットパンツ'),
	('TopsTexTopYshirtsLTweedvest'             , 'ツイードベスト'),
	('BottomsTexSkirtLongWrap'                 , 'ベルトのまきスカート'),
	('BottomsTexSkirtLongEmbroidery'           , 'ししゅうのはながらスカート'),
	('BottomsTexSkirtLongGeometric'            , 'きかがくししゅうのスカート'),
	('AccessoryGlassCyber'                     , 'サイバーサングラス'),
	('TopsTexTopOuterLMuffler'                 , 'チェックマフラーつきセーター'),
	('TopsTexTopCoatLMuffler'                  , 'ロングデニムカーディガン'),
	('TopsTexOnepieceBoxNStandard'             , 'おおばんがらワンピ'),
	('TopsTexOnepieceAlineLRetro'              , 'レトロＡラインワンピース'),
	('TopsTexTopCoatHWaistshirt'               , 'こしまきシャツ'),
	('TopsTexOnepieceBoxHTshirts'              , 'Ｔシャツワンピ'),
	('TopsTexTopCoatNSequins'                  , 'ラメししゅうノースリーブ'),
	('TopsTexOnepieceOverallLVisual'           , 'ヴィジュアルけいコスチューム'),
	('TopsTexTopCoatLLeathertrench'            , 'レザートレンチ'),
	('TopsTexTopOuterLReindeer'                , 'トナカイセーター'),
	('TopsTexTopYshirtsHKnot'                  , 'まえむすびＹシャツ'),
	('TopsTexOnepieceBalloonHLace'             , 'はながらレースのワンピース'),
	('TopsTexTopCoatLSoutiencollar'            , 'ステンカラーコート'),
	('TopsTexTopOuterLHighsence'               , 'ハイセンスなセーター'),
	('TopsTexTopYshirtsLCowboy'                , 'カウボーイシャツ'),
	('TopsTexOnepieceRibNCaterpillar'          , 'あおむしのふく'),
	('TopsTexTopYshirtsLBustier'               , 'ビスチェキャミ'),
	('TopsTexOnepieceBoxLHouse'                , 'ハウスなプリントワンピ'),
	('TopsTexOnepieceBoxLForest'               , 'フォレストなワンピース'),
	('TopsTexOnepieceOverallHRugby'            , 'ラグビーのユニフォーム'),
	('TopsTexOnepieceOverallLPlatearmorIron'   , 'アイアンアーマー'),
	('TopsTexOnepieceAlongLDowncoat'           , 'ロングダウンコート'),
	('TopsTexOnepieceOverallLPlatearmorGold'   , 'ゴールデンアーマー'),
	('BottomsTexPantsWideSatin'                , 'サテンのパンツ'),
	('TopsTexOnepieceAlineLPcoat'              , 'スカートつきピーコート'),
	('TopsTexTopOuterLRainbow'                 , 'レインボーなニット'),
	('TopsTexOnepieceAlongHCachecoeur'         , 'カシュクールワンピース'),
	('AccessoryGlassLoose'                     , 'アンダーリムめがね'),
	('TopsTexTopOuterLBlouson'                 , 'ボアブルゾン'),
	('TopsTexTopCoatNShirt'                    , 'チュニックシャツ'),
	('AccessoryMouthRabbit'                    , 'ウサギのつけばな'),
	('TopsTexTopCoatLCoadigan'                 , 'コーディガン'),
	('BottomsTexPantsWideCorduroy'             , 'コーデュロイボトム'),
	('TopsTexOnepieceOverallLVolendam'         , 'オランダなコスチューム'),
	('TopsTexOnepieceRibLBore'                 , 'ボアパーカー'),
	('TopsTexTopCoatLPatchwork'                , 'パッチワークコート'),
	('TopsTexOnepieceBlongLBalmakarn'          , 'バルマカーンコート'),
	('AccessoryGlassRound'                     , 'ラウンドサングラス'),
	('AccessoryGlassButterfly'                 , 'バタフライサングラス'),
	('AccessoryGlassOval'                      , 'オーバルめがね'),
	('TopsTexTopTshirtsLEarphone'              , 'イヤフォンコーデ'),
	('TopsTexOnepieceOverallHArabia'           , 'アラビアひめなふく'),
	('BottomsTexSkirtBoxLace'                  , 'はながらレースのスカート'),
	('TopsTexTopTshirtsLMulti'                 , 'マルチボーダーニット'),
	('BottomsTexSkirtAlineFlare'               , 'フレアスカート'),
	('TopsTexTopYshirtsHMadras'                , 'マドラスチェックシャツ'),
	('TopsTexOnepieceAlongNEthnic'             , 'エスニックワンピ'),
	('TopsTexOnepieceOverallNCombinaison'      , 'ショートコンビネゾン'),
	('AccessoryGlassDot'                       , 'ドットサングラス'),
	('AccessoryMouthPig'                       , 'ブタのつけばな'),
	('TopsTexOnepieceKimonoLIcequeen'          , 'こおりのじょおうなドレス'),
	('AccessoryGlassmouthGasmask'              , 'ガスマスク'),
	('TopsTexOnepieceDressLNordic'             , 'さむいくにのドレス'),
	('AccessoryMouthRice'                      , 'ごはんつぶ'),
	('TopsTexOnepieceOverallLMariachi'         , 'マリアッチのいしょう'),
	('TopsTexOnepieceBoxLMarble'               , 'マーブルワンピース'),
	('TopsTexOnepieceAlongNMermaid'            , 'かいがらのドレス'),
	('TopsTexOnepieceBlongLHippie'             , 'ポンチョふうニット'),
	('AccessoryGlassVenetian'                  , 'ベネチアンマスク'),
	('TopsTexTopCoatNTanktunic'                , 'タンクトップチュニック'),
	('AccessoryGlassWood'                      , 'ウッドフレームめがね'),
	('AccessoryMouthCrow'                      , 'カラスマスク'),
	('AccessoryMouthRollingmustache'           , 'まきヒゲ'),
	('TopsTexOnepieceRibLCardigan'             , 'モールロングカーディガン'),
	('TopsTexTopYshirtsNRibnoncami'            , 'リボンショルダーキャミ'),
	('AccessoryMouthBeardChin'                 , 'アゴひげ'),
	('AccessoryMouthBandage'                   , 'ばんそうこう'),
	('AccessoryGlassmouthPierrot'              , 'ピエロのかめん'),
	('AccessoryMouthBeardRound'                , 'ラウンドひげ'),
	('TopsTexTopOuterLFleece'                  , 'がらものフリース'),
	('TopsTexTopCoatLDetective'                , 'めいたんていのふく'),
	('AccessoryMouthLeaf'                      , 'はっぱ'),
	('AccessoryGlassRhinestone'                , 'ラインストーンめがね'),
	('AccessoryGlassHeromask'                  , 'ヒーローマスク'),
	('AccessoryGlassSteampunk'                 , 'スチームパンクなゴーグル'),
	('TopsTexOnepieceBalloonHAngel'            , 'エンジェルなワンピース'),
	('TopsTexTopTshirtsLLoose'                 , 'ヨレヨレなシャツ'),
	('TopsTexOnepieceOverallLDevil'            , 'デビルなふく'),
	('ShoesSandalShower'                       , 'シャワーサンダル'),
	('TopsTexTopYshirtsLOpencollar'            , 'かいきんシャツ'),
	('ShoesLowcutLeathersneker'                , 'レザーのスニーカー'),
	('TopsTexTopTshirtsHMeme'                  , 'ミームなふく'),
	('SocksTexRibbon'                          , 'リボンソックス'),
	('ShoesHighcutMouton'                      , 'ムートンブーツ'),
	('ShoesLowcutEnamelpumps'                  , 'エナメルのパンプス'),
	('ShoesLowcutLoafers'                      , 'ローファー'),
	('ShoesSandalCrossbelt'                    , 'クロスベルトサンダル'),
	('TopsTexTopYshirtsLQuilting'              , 'キルティングジャケット'),
	('TopsTexOnepieceAlongNStripe'             , 'ストライプのマキシワンピ'),
	('ShoesLowcutBusiness'                     , 'ビジネスシューズ'),
	('TopsTexOnepieceAlineLJumperskirt'        , 'チェックのジャンパースカート'),
	('ShoesKneeVelour'                         , 'ベロアブーツ'),
	('ShoesKneeRainboots'                      , 'レインブーツ'),
	('ShoesSandalZori'                         , 'ぞうり'),
	('TopsTexTopOuterLSkidown'                 , 'スキーダウンジャケット'),
	('TopsTexOnepieceAlineNLace'               , 'レースのワンピース'),
	('CapHatSchool'                            , 'つうがくぼう'),
	('TopsTexOnepieceBalloonNClover'           , 'クローバーなワンピース'),
	('SocksTexSneakerin'                       , 'スニーカーインソックス'),
	('SocksTexAlan'                            , 'アランニットのソックス'),
	('SocksTexSequins'                         , 'スパンコールレギンス'),
	('SocksTexLeggings'                        , 'ストレッチレギンス'),
	('SocksTexDenimleggings'                   , 'デニムレギンス'),
	('SocksTexLine'                            , 'ラインソックス'),
	('SocksTexGarter'                          , 'ガーターつきストッキング'),
	('SocksTexNordic'                          , 'ノルディックなソックス'),
	('SocksTexTabi'                            , 'たび'),
	('TopsTexTopYshirtsLFactory'               , 'さぎょうふく'),
	('TopsTexTopOuterLBobble'                  , 'ポンポンセーター'),
	('TopsTexOnepieceDressLLady'               , 'しゅくじょなワンピース'),
	('TopsTexTopTshirtsLQuiet'                 , 'つつましいニット'),
	('TopsTexTopCoatLAnorak'                   , 'アノラック'),
	('TopsTexTopYshirtsLMultivest'             , 'たきのうベスト'),
	('CapHatNewyear'                           , 'ニューイヤーハット'),
	('CapHatBirthday'                          , 'バースデーハット'),
	('CapOrnamentTHyacinth1'                   , 'ヒヤシンスのかんむり'),
	('CapOrnamentTHyacinth2'                   , 'ヒヤシンスのかんむり・クール'),
	('CapOrnamentTHyacinth3'                   , 'ヒヤシンスのかんむり・パープル'),
	('CapOrnamentAnemones1'                    , 'アネモネのかんむり'),
	('CapOrnamentAnemones2'                    , 'アネモネのかんむり・クール'),
	('CapOrnamentAnemones3'                    , 'アネモネのかんむり・パープル'),
	('CapOrnamentTulip1'                       , 'チューリップのかんむり'),
	('CapOrnamentTulip2'                       , 'チューリップのかんむり・シック'),
	('CapOrnamentTulip3'                       , 'チューリップのかんむり・ダーク'),
	('CapOrnamentPansy1'                       , 'パンジーのかんむり'),
	('CapOrnamentPansy2'                       , 'パンジーのかんむり・クール'),
	('CapOrnamentPansy3'                       , 'パンジーのかんむり・パープル'),
	('CapOrnamentCosmos1'                      , 'コスモスのかんむり'),
	('CapOrnamentCosmos2'                      , 'コスモスのかんむり・ラブリー'),
	('CapOrnamentCosmos3'                      , 'コスモスのかんむり・ダーク'),
	('CapOrnamentRose1'                        , 'バラのかんむり'),
	('CapOrnamentRose2'                        , 'バラのかんむり・キュート'),
	('CapOrnamentRose3'                        , 'バラのかんむり・シック'),
	('CapOrnamentLily1'                        , 'ユリのかんむり'),
	('CapOrnamentLily2'                        , 'ユリのかんむり・キュート'),
	('CapOrnamentLily3'                        , 'ユリのかんむり・ダーク'),
	('CapOrnamentChrysanthemum1'               , 'キクのかんむり'),
	('CapOrnamentChrysanthemum2'               , 'キクのかんむり・シック'),
	('CapOrnamentChrysanthemum3'               , 'キクのかんむり・シンプル'),
	('TopsTexTopOuterLSnowcrystal'             , 'けっしょうのセーター'),
	('TopsTexTopTshirtsLDamage'                , 'ダメージニット'),
	('TopsTexOnepieceOverallNWrestler'         , 'レスリングのユニフォーム'),
	('CapHatSilkhat'                           , 'メッシュキャップ'),
	('CapHatMeshcap'                           , 'シルクハット'),
	('TopsTexTopCoatLSamurai'                  , 'かっちゅう'),
	('TopsTexOnepieceBlongLChina'              , 'チャイナドレス'),
	('TopsTexTopCoatLHandcover'                , 'うでカバーつきエプロン'),
	('TopsTexTopCoatLThiefBlack'               , 'かいとうのふく'),
	('TopsTexOnepieceAlineNSpace'              , 'スペースワンピース'),
	('CapHatExpedition'                        , 'たんけんぼう'),
	('CapHatBachelor'                          , 'がくしのぼうし'),
	('CapHatSombrero'                          , 'ソンブレロ'),
	('CapHatSafetyhat'                         , 'あんぜんヘルメット'),
	('CapHatCock'                              , 'コックさんのぼうし'),
	('CapHatPolice'                            , 'けいかんのぼうし'),
	('CapHatAjiro'                             , 'かさぼうし'),
	('CapHatUshanka'                           , 'フェイクファーハット'),
	('CapHatTriangle'                          , 'さんかくきん'),
	('CapHatKnitcap'                           , 'ニットキャップ'),
	('CapHatHunting'                           , 'ハンチング'),
	('CapHatWorkcap'                           , 'ワークキャップ'),
	('SocksTexFootcover'                       , 'フットカバー'),
	('SocksTexMixtweed'                        , 'ミックスツイードソックス'),
	('SocksTexLegwarmer'                       , 'レッグウォーマー'),
	('SocksTexCompression'                     , 'コンプレッションタイツ'),
	('SocksTexFolded'                          , 'みつおりソックス'),
	('SocksTexFrilledknee'                     , 'フリルつきニーハイソックス'),
	('SocksTexLace'                            , 'レースのソックス'),
	('SocksTexFrilled'                         , 'フリルソックス'),
	('SocksTexHoletights'                      , 'あなあきタイツ'),
	('SocksTexFootball'                        , 'サッカーソックス'),
	('SocksTexHole'                            , 'あなあきソックス'),
	('SocksTexBobble'                          , 'ポンポンソックス'),
	('SocksTexMultiblock'                      , 'マルチブロックソックス'),
	('SocksTexFluffy'                          , 'もこもこソックス'),
	('AccessoryGlassHmd'                       , 'HMD'),
	('AccessoryGlassNightvision'               , 'ナイトビジョン'),
	('TopsTexTopYshirtsLKids'                  , 'すこやかなセーター'),
	('CapHatSailor'                            , 'ふなのりのぼうし'),
	('CapHatViking'                            , 'バイキングのかぶと'),
	('SockstTexOverlapping'                    , 'かさねばきソックス'),
	('SocksTexHandknit'                        , 'てあみのソックス'),
	('SocksTexAerobics'                        , 'エアロビレギンス'),
	('SocksTexPucker'                          , 'くしゅくしゅソックス'),
	('SocksTexBorder'                          , 'ボーダーソックス'),
	('SocksTexOnepoint'                        , 'ワンポイントソックス'),
	('SocksTexKids'                            , 'キッズソックス'),
	('SocksTexCrocheting'                      , 'かぎばりあみソックス'),
	('SocksTexSpider'                          , 'スパイダーなタイツ'),
	('SocksTexEmbroidery'                      , 'はながらししゅうのタイツ'),
	('SocksTexRun'                             , 'ランニングタイツ'),
	('AccessoryMouthDog'                       , 'イヌのつけばな'),
	('CapHatWitch'                             , 'まじょのぼうし'),
	('CapHatDenim'                             , 'デニムキャップ'),
	('CapHatCycle'                             , 'サイクルキャップ'),
	('CapHatOutdoor'                           , 'アウトドアハット'),
	('CapHatKankanbo'                          , 'カンカンぼう'),
	('CapHatBeret'                             , 'ベレーぼう'),
	('CapHatOrange'                            , 'オレンジのぼうし'),
	('CapHatKiwi'                              , 'キウイのぼうし'),
	('CapHatStrawberry'                        , 'いちごのぼうし'),
	('CapHatGrape'                             , 'ぶどうのぼうし'),
	('CapHatPineapple'                         , 'パイナップルのぼうし'),
	('CapHatWatermelon'                        , 'スイカのぼうし'),
	('CapHatItamae'                            , 'わぼうし'),
	('CapHatCyclemet'                          , 'サイクルヘルメット'),
	('CapHatSwim'                              , 'すいえいキャップ'),
	('CapHatChina'                             , 'チャイナハット'),
	('BottomsTexPantsWideChino'                , 'ワイドチノ'),
	('BottomsTexPantsNormalChemical'           , 'ケミカルウォッシュデニム'),
	('TopsTexOnepieceOverallNHotdog'           , 'ホットドッグなふく'),
	('TopsTexOnepieceOverallLFarmer'           , 'うでカバーつきつなぎ'),
	('TopsTexTopOuterLChemical'                , 'ケミカルデニムジャケット'),
	('TopsTexTopTshirtsLLive'                  , 'ミュージックフェスなふく'),
	('TopsTexTopCoatLStraw'                    , 'みの'),
	('TopsTexTopOuterLRepresent'               , 'レペゼンなふく'),
	('CapHatTulip'                             , 'チューリップハット'),
	('CapHatBandana'                           , 'ペイズリーのバンダナ'),
	('CapHatTyrolean'                          , 'チロリアンハット'),
	('CapHatBowler'                            , 'リボンボーラーハット'),
	('CapHatStraw'                             , 'つばひろストローハット'),
	('CapHatShowercap'                         , 'みずたまシャワーキャップ'),
	('CapHatFelt'                              , 'なかおれハット'),
	('CapHatSimple'                            , 'しっそなぼうし'),
	('CapHatSports'                            , 'うんどうぼう'),
	('CapHatNightcap'                          , 'もこもこナイトキャップ'),
	('CapHatCrown'                             , 'おうかん'),
	('CapHatTowel'                             , 'タオル'),
	('CapHatAcorn'                             , 'どんぐりニット'),
	('CapHatCombat'                            , 'コンバットヘルメット'),
	('TopsTexTopYshirtsLCool'                  , 'ダンスジャージ'),
	('CapHatHokkamuri'                         , 'ほっかむり'),
	('CapHatCowl'                              , 'メルヘンなずきん'),
	('CapHatMummy'                             , 'ミイラのかぶりもの'),
	('CapHatRabbit'                            , 'ウサギのかぶりもの'),
	('CapHatCat'                               , 'ネコのかぶりもの'),
	('CapHatFaceknit'                          , 'めだしぼう'),
	('CapHatSkull'                             , 'ガイコツのかぶりもの'),
	('CapHatShallow'                           , 'あさいニットぼう'),
	('CapHatBear'                              , 'クマのかぶりもの'),
	('CapHatKappa'                             , 'カッパのおさら'),
	('CapHatCaptain'                           , 'キャプテンのぼうし'),
	('CapHatCasquette'                         , 'キャスケット'),
	('CapFullfaceKnightIron'                   , 'アイアンアーマーヘルメット'),
	('CapCostumeFrog'                          , 'カエルのかぶりもの'),
	('CapHatWizard'                            , 'とんがりぼうし'),
	('CapHatBalloon'                           , 'バルーンハット'),
	('BottomsTexPantsWideCool'                 , 'ダンスジャージズボン'),
	('CapFullfaceKnightGold'                   , 'ゴールデンアーマーヘルメット'),
	('TopsTexTopPuffHFrill'                    , 'フリルパフブラウス'),
	('TopsTexOnepieceSalopetteLAllinone'       , 'オールインワン'),
	('CapHatElegant'                           , 'エレガントなぼうし'),
	('CapCostumeFootball'                      , 'アメフトヘルメット'),
	('CapBangsFirefighter'                     , 'しょうぼうしのぼうし'),
	('CapMaskWelder'                           , 'ようせつマスク'),
	('TopsTexTopOuterLChristmas'               , 'クリスマスセーター'),
	('CapHatClown'                             , 'ピエロのぼうし'),
	('CapCostumeSamurai'                       , 'かぶと'),
	('TopsTexOnepieceOverallLMuscle'           , 'マッスルスーツ'),
	('CapHatVolendam'                          , 'オランダのぼうし'),
	('ShoesLowcutTrekking'                     , 'トレッキングシューズ'),
	('CapHelmetPilot'                          , 'ひこうぼう'),
	('CapBangsBonnet'                          , 'あかちゃんのぼうし'),
	('CapCostumeNinja'                         , 'にんじゃずきん'),
	('CapHelmetBaseballBlack'                  , 'やきゅうのヘルメット'),
	('CapCostumeJockey'                        , 'ジョッキーヘルメット'),
	('CapCostumeWrestling'                     , 'プロレスのマスク'),
	('CapBangsSausage'                         , 'ホットドッグマスク'),
	('CapBangsEarknit'                         , 'みみあてつきニット'),
	('CapHatDetective'                         , 'めいたんていのぼうし'),
	('TopsTexOnepieceOverallLCyber'            , 'サイバースーツ'),
	('TopsTexOnepieceFigure'                   , 'フィギュアのドレス'),
	('CapCostumeAstronaut'                     , 'アストロヘルメット'),
	('CapMaskPaint'                            , 'ペイントボールマスク'),
	('CapHatStrawhat'                          , 'むぎわらぼうし'),
	('CapHatTengallon'                         , 'テンガロンハット'),
	('TopsTexOnepieceOverallLFigure'           , 'フィギュアないしょう'),
	('SocksTexCharacter'                       , 'キャラクターソックス'),
	('CapHatSnowknit'                          , 'スノーニットぼう'),
	('CapHatColorful'                          , 'カラフルボーダーニットぼう'),
	('BottomsTexPantsHalfComic'                , 'アメコミがらハーフパンツ'),
	('BottomsTexPantsNormalMonpe'              , 'もんぺ'),
	('BottomsTexPantsWideRain'                 , 'レインパンツ'),
	('BottomsTexSkirtBoxAran'                  , 'ニットスカート'),
	('BottomsTexSkirtAlineFur'                 , 'ファースカート'),
	('BottomsTexPantsNormalSwewtfrill'         , 'スウェットフリルズボン'),
	('BottomsTexSkirtLongSweat'                , 'スウェットロングスカート'),
	('BottomsTexSkirtBoxBoa'                   , 'ボアスカート'),
	('BottomsTexPantsHalfBoa'                  , 'ボアハーフパンツ'),
	('BottomsTexSkirtAlineLeather'             , 'レザーのフレアスカート'),
	('BottomsTexSkirtLongLace'                 , 'まえボタンレースのスカート'),
	('BottomsTexSkirtAlineTutu'                , 'チュチュスカート'),
	('CapHelmetHero'                           , 'ヒーローヘルメット'),
	('TopsTexOnepieceOverallLPowered'          , 'パワードスーツ'),
	('TopsTexOnepieceAlongLRenaissance'        , 'ルネッサンスなドレス'),
	('CapHelmetTurban'                         , 'ターバン'),
	('CapCostumeGogglehelmet'                  , 'ゴーグルつきヘルメット'),
	('TopsTexTopYshirtsLGlass'                 , 'そうがんきょうつきベスト'),
	('TopsTexTopYshirtsLCamera'                , 'カメラつきワイシャツ'),
	('TopsTexTopTshirtsNEmbroidery'            , 'ししゅうのキャミソール'),
	('TopsTexOnepieceOverallLNordic'           , 'さむいくにのふく'),
	('CapCostumeRacing'                        , 'フルフェイスメット'),
	('SocksTexChimayo'                         , 'チマヨがらソックス'),
	('CapHatCow'                               , 'うしのほね'),
	('BottomsTexSkirtBoxChidori'               , 'ちどりのスカート'),
	('BottomsTexSkirtAlineShabby'              , 'シャビーなスカート'),
	('BottomsTexPantsWidePrintdenim'           , 'プリントデニム'),
	('BottomsTexPantsWideSuteteko'             , 'ステテコ'),
	('TopsTexOnepieceKimonoLHaregi'            , 'はれぎ'),
	('CapCostumeDevil'                         , 'デビルなかぶりもの'),
	('CapBangsSheep'                           , 'ひつじのかぶりもの'),
	('ShoesLowcutAnimal'                       , 'アニマルスリッパ'),
	('ShoesSandalBeachborder'                  , 'ビーチサンダル'),
	('ShoesLowcutStrap'                        , 'ストラップシューズ'),
	('ShoesKneeKnightIron'                     , 'アイアンアーマーシューズ'),
	('ShoesLowcutSchool'                       , 'うわばき'),
	('ShoesHighcutShortboots'                  , 'レザーのショートブーツ'),
	('ShoesSandalFlower'                       , 'フラワーなサンダル'),
	('ShoesHighcutFurboots'                    , 'ファーブーツ'),
	('ShoesLowcutLeopard'                      , 'アニマルパンプス'),
	('ShoesSandalBeads'                        , 'ビーズししゅうのサンダル'),
	('ShoesKneeRubberboots'                    , 'ながぐつ'),
	('TopsTexOnepieceKimonoLKanpukumen'        , 'ぐんしのふく'),
	('TopsTexOnepieceKimonoLKanpukuwomen'      , 'かんぷく'),
	('ShoesKneeAntique'                        , 'アンティークなブーツ'),
	('ShoesKneeKnightGold'                     , 'ゴールデンアーマーシューズ'),
	('ShoesLowcutSlipper'                      , 'スリッパ'),
	('ShoesHighcutWorkboots'                   , 'ワークブーツ'),
	('ShoesHighcutMoccasin'                    , 'モカシンブーツ'),
	('BottomsTexSkirtLongPatch'                , 'パッチワークスカート'),
	('ShoesHighcutBobbles'                     , 'ポンポンつきブーツ'),
	('ShoesKneeLegguard'                       , 'かっちゅうのすねあて'),
	('ShoesLowcutGlitter'                      , 'ストラップつきパンプス'),
	('ShoesSandalRoomborder'                   , 'ルームシューズ'),
	('ShoesSandalResin'                        , 'スリッポンサンダル'),
	('ShoesHighcutSlipon'                      , 'スリッポン'),
	('TopsTexOnepieceBoxLSchoolsmock'          , 'スクールスモック'),
	('ShoesLowcutLolita'                       , 'ロリータシューズ'),
	('ShoesLowcutBallet'                       , 'バレエシューズ'),
	('ShoesKneeVisual'                         , 'ヴィジュアルけいブーツ'),
	('TopsTexOnepieceSalopetteLRumba'          , 'ルンバないしょう'),
	('ShoesHighcutRubbertoe'                   , 'ラバートゥハイカットスニーカー'),
	('ShoesLowcutClog'                         , 'きぐつ'),
	('ShoesSandalComfort'                      , 'コンフォートサンダル'),
	('ShoesSandalGladiator'                    , 'グラディエーターサンダル'),
	('ShoesKneeHero'                           , 'ヒーローブーツ'),
	('ShoesHighcutBasket'                      , 'バスケットシューズ'),
	('ShoesKneeClown'                          , 'ピエロのくつ'),
	('ShoesSandalOutdoor'                      , 'アウトドアサンダル'),
	('CapHatEgg'                               , 'たまごのから'),
	('ShoesKneeWestern'                        , 'ウェスタンブーツ'),
	('TopsTexOnepieceRibNChick'                , 'ひよこなふく'),
	('TopsTexOnepieceAlongHRumba'              , 'ルンバなドレス'),
	('TopsTexTopTshirtsLSailor'                , 'セーラーシャツ'),
	('ShoesLowcutGgotshin'                     , 'コッシン'),
	('ShoesSandalAqua'                         , 'アクアサンダル'),
	('TopsTexOnepieceOverallLHighcollar'       , 'つめえりスーツ'),
	('ShoesLowcutSpike'                        , 'スパイク'),
	('ShoesLowcutPointedtoe'                   , 'トンがったクツ'),
	('TopsTexTopYshirtsLFischerhemd'           , 'フィッシャーヘムト'),
	('ShoesHighcutHightech'                    , 'ハイテクシューズ'),
	('ShoesKneeSki'                            , 'スキーブーツ'),
	('CapHatCavalier'                          , 'じゅうきしのぼうし'),
	('BottomsTexPantsHotShaggycheck'           , 'シャギーチェックのホットパンツ'),
	('BottomsTexSkirtLongEnaguas'              , 'エナグワス'),
	('AccessoryGlassmouthCatrina'              , 'スカルキャンディマスク'),
	('ShoesKneeLaceup'                         , 'あみあげブーツ'),
	('ShoesKneeRing'                           , 'リングシューズ'),
	('CapCostumeBangs'                         , 'のうぎょうぼう'),
	('TopsTexTopOuterLPsychedelic'             , 'ハデなカーディガン'),
	('CapCostumeHeadgear'                      , 'ヘッドギア'),
	('CapWigMohican'                           , 'モヒカン'),
	('CapWigRegent'                            , 'リーゼント'),
	('CapWigSamurai'                           , 'ちょんまげ'),
	('CapWigOnionhair'                         , 'たまねぎヘアー'),
	('CapWigDoublebun'                         , 'おだんごあたま'),
	('CapBangsHeadphone'                       , 'ヘッドホン'),
	('CapHelmetHeaddress'                      , 'ヘッドドレス'),
	('CapFullfaceVeil'                         , 'ベール'),
	('CapWigGeisya'                            , 'ゲイシャさん'),
	('CapHelmetMusic'                          , 'おんがくかのかつら'),
	('CapFullfacePowered'                      , 'パワードメット'),
	('ShoesKneePowered'                        , 'パワードブーツ'),
	('BottomsTexPantsWideTeared'               , 'やぶれたズボン'),
	('BottomsTexPantsNormalCroppedsweat'       , 'フィットネススウェットパンツ'),
	('BottomsTexSkirtBoxBoxpleats'             , 'ボックスプリーツスカート'),
	('BottomsTexSkirtBoxMouton'                , 'ムートンスカート'),
	('BottomsTexPantsHotMultistripe'           , 'マルチストライプのホットパンツ'),
	('BottomsTexPantsNormalKnit'               , 'ニットパンツ'),
	('BottomsTexSkirtLongDenim'                , 'ロングデニムスカート'),
	('BottomsTexSkirtBoxApron'                 , 'エプロンつきスカート'),
	('BottomsTexPantsHotFluffy'                , 'もこもこホットパンツ'),
	('BottomsTexPantsHalfBasketball'           , 'バスケットパンツ'),
	('BottomsTexPantsNormalTraining'           , 'ワークアウトパンツ'),
	('BottomsTexSkirtLongMaone'                , 'ＭＡ‐１スカート'),
	('BottomsTexPantsHotSequins'               , 'スパンコールのホットパンツ'),
	('BottomsTexPantsWideMultistripe'          , 'マルチストライプワイドパンツ'),
	('BottomsTexPantsNormalComedian'           , 'コメディアンのパンツ'),
	('BottomsTexSkirtAlinePearl'               , 'パールつきスカート'),
	('AccessoryMouthBubblegum'                 , 'ふうせんガム'),
	('AccessoryGlassFlower'                    , 'フラワーサングラス'),
	('BottomsTexPantsHotLeather'               , 'レザーのショートパンツ'),
	('BottomsTexPantsHalfGobelins'             , 'ゴブランハーフパンツ'),
	('BottomsTexPantsWideThail'                , 'タイパンツ'),
	('ShoesKneeSpace'                          , 'スペースブーツ'),
	('ShoesHighcutSports'                      , 'キッズなスニーカー'),
	('AccessoryGlassmouthStraw'                , 'ストローメガネ'),
	('TopsTexTopOuterNNosleeve'                , 'ノースリーブパーカー'),
	('ShoesLowcutHealth'                       , 'ウォーキングシューズ'),
	('BottomsTexSkirtLongCorte'                , 'コルテ'),
	('BottomsTexPantsNormalChimayo'            , 'チマヨがらフリースパンツ'),
	('TopsTexOnepieceBalloonHYumekawa'         , 'ゆめかわなドレス'),
	('TopsTexOnepieceKimonoLGaudy'             , 'ゴージャスなきもの'),
	('TopsTexOnepieceDressLNoble'              , 'きぞくのドレス'),
	('TopsTexOnepieceSalopetteLPsychedelic'    , 'サイケなつなぎ'),
	('ShoesLowcutToilet'                       , 'トイレスリッパ'),
	('TopsTexOnepieceKimonoLShitamachi'        , 'まちむすめのきもの'),
	('ShoesHighcutCute'                        , 'キュートなスニーカー'),
	('SocksTexFlowerdot'                       , 'フラワードットタイツ'),
	('SocksTexArgyle'                          , 'アーガイルソックス'),
	('ShoesLowcutMoccasin'                     , 'モカシン'),
	('ShoesLowcutMarine'                       , 'マリンシューズ'),
	('ShoesLowcutWing'                         , 'ウイングチップのシューズ'),
	('BottomsTexSkirtLongCutleather'           , 'カットレザースカート'),
	('BottomsTexSkirtAlinePatch'               , 'レザーパッチスカート'),
	('SocksTexSeethrough'                      , 'シースルーソックス'),
	('SocksTexWave'                            , 'せいがいはソックス'),
	('ShoesSandalRibbon'                       , 'リボンサンダル'),
	('TopsTexOnepieceBoxNTango'                , 'タンゴなドレス'),
	('BottomsTexSkirtLongWrapbicolor'          , 'ボタンのまきスカート'),
	('TopsTexOnepieceBoxNFlapper'              , 'フラッパードレス'),
	('TopsTexOnepieceKimonoLKorea'             , 'パジチョゴリ'),
	('TopsTexOnepieceKimonoLAsagao'            , 'あさがおのゆかた'),
	('ShoesSandalSports'                       , 'スポーツサンダル'),
	('TopsTexOnepieceOverallLSteampunk'        , 'スチームパンクなふく'),
	('BottomsTexSkirtLongTiedye'               , 'タイダイスカート'),
	('TopsTexOnepieceOverallLFarm'             , 'ファームなオーバーオール'),
	('TopsTexOnepieceSalopetteLHockey'         , 'アイスホッケーのユニフォーム'),
	('AccessoryMouthJokeDrip'                  , 'はなみず'),
	('CapFullfacePaperbag'                     , 'かみぶくろ'),
	('TopsTexTopTshirtsHStaff'                 , 'スタッフのふく'),
	('BottomsTexPantsHalfBotanical'            , 'ボタニカルハーフパンツ'),
	('TopsTexTopCoatLOilskin'                  , 'オイルスキンのジャケット'),
	('AccessoryMouthPasta'                     , 'たべこぼし'),
	('BottomsTexPantsWideGakuran'              , 'がくせいふくのズボン'),
	('BottomsTexSkirtLongLemon'                , 'レモンのスカート'),
	('BottomsTexPantsWideYumekawa'             , 'ゆめかわなズボン'),
	('BottomsTexSkirtLongFlower'               , 'はながらスカート'),
	('TopsTexTopYshirtsLGuide'                 , 'あんないがかりのふく'),
	('CapHatNewyearsilk'                       , 'ニューイヤーシルクハット'),
	('TopsTexTopOuterLBulldog'                 , 'ブルドッグジャージ'),
	('BottomsTexSkirtLongSailor'               , 'ロングセーラースカート'),
	('TopsTexOnepieceKimonoLHomongi'           , 'むじのほうもんぎ'),
	('TopsTexOnepieceKimonoLButterfly'         , 'ちょうがらのほうもんぎ'),
	('TopsTexOnepieceKimonoLYukatamen'         , 'かぶきなゆかた'),
	('TopsTexTopYshirtsLDoublet'               , 'ダブレット'),
	('CapMaskFox'                              , 'キツネのおめん'),
	('CapMaskOkina'                            , 'おきなののうめん'),
	('CapMaskNomen'                            , 'のうめん'),
	('AccessoryGlassMirror'                    , 'はんしゃきょう'),
	('AccessoryMouthLeather'                   , 'レザーマスク'),
	('AccessoryGlassmouthHockeyWhite'          , 'ホッケーのマスク'),
	('ShoesLowcutBrogues'                      , 'ギリー・ブローグズ'),
	('ShoesSandalBaboush'                      , 'バブーシュ'),
	('SocksTexCountry'                         , 'カントリーソックス'),
	('SocksTexStripe'                          , 'ストライプソックス'),
	('SocksTexStripedot'                       , 'デザインストッキング'),
	('CapHatKanbo'                             , 'かんぼう'),
	('CapHatGreenery'                          , 'グレンガリーぼう'),
	('CapFullfaceCatcher'                      , 'キャッチャーマスク'),
	('CapHelmetKandula'                        , 'アラビアのぼうし'),
	('CapFullfaceKuroko'                       , 'くろこ'),
	('CapHatKnitcasquette'                     , 'ボンボンつきキャスケット'),
	('CapHatScotlandRed'                       , 'スコットランドぼうし'),
	('ShoesHighcutSneaker_'                    , 'ハイカットスニーカー'),
	('TopsTexTopYshirtsLGingham'               , 'ギンガムチェックのシャツ'),
	('ShoesKneeEngineerboots_'                 , 'エンジニアブーツ'),
	('CapOrnamentRRibbonRed_'                  , 'リボン'),
	('TopsTexOnepieceRibNEgg'                  , 'たまごずし'),
	('TopsTexOnepieceRibNTuna'                 , 'まぐろずし'),
	('TopsTexOnepieceRibNKohada'               , 'こはだずし'),
	('ShoesLowcutRubbertoe'                    , 'ラバートゥスニーカー'),
	('ShoesKnee'                               , 'とんがりブーツ'),
	('TopsTexTopTshirtsN'                      , 'ビブス'),
	('CapOrnamentCAngel0'                      , 'てんしのわ'),
	('CapOrnamentTNurse'                       , 'ナースキャップ'),
	('CapHatIcecream'                          , 'ソフトクリームなぼうし'),
	('CapOrnamentCBunny'                       , 'バニーのみみ'),
	('CapHatSandogasa'                         , 'さんどがさ'),
	('CapOrnamentLMinistrawhat'                , 'ちいさめなぼうし'),
	('CapOrnamentLMinisilkhat'                 , 'ちいさめシルクハット'),
	('CapMaskLeaf'                             , 'はっぱのおめん'),
	('BagBackpackTown1'                        , 'タウンリュック'),
	('BagShoulderTravel'                       , 'トラベルポーチ'),
	('CapOrnamentRose4'                        , 'バラのかんむり・ブルー'),
	('CapOrnamentRose5'                        , 'バラのかんむり・ゴールド'),
	('CapOrnamentCTiara'                       , 'ティアラ'),
	('BagShoulderMessenger'                    , 'メッセンジャーバッグ'),
	('BagBackpackDry'                          , 'ドライサック'),
	('BagShoulderLeather'                      , 'レザーショルダー'),
	('BagShoulderFish'                         , 'おさかなポシェット'),
	('BagShoulderFishing'                      , 'フィッシングバッグ'),
	('BagShoulderCage'                         , 'ムシかご'),
	('BagShoulderFakefur'                      , 'フェイクファーバッグ'),
	('BagShoulderFringe'                       , 'フリンジレザーバッグ'),
	('BagShoulderRace'                         , 'てあみポーチ'),
	('BagShoulderBody'                         , 'ボディバッグ'),
	('BagShoulderBodybag'                      , 'レザーボディバッグ'),
	('BagShoulderDrum'                         , 'ななめかけボストン'),
	('BagShoulderPattern'                      , 'はるのみずたまショルダー'),
	('BagShoulderCanvas'                       , 'はんぷショルダー'),
	('BagShoulderRattan'                       , 'ラタンポシェット'),
	('BagShoulderStar'                         , 'スターなポシェット'),
	('BagShoulderCherryblossoms'               , 'さくらのポシェット'),
	('BagShoulderMaple'                        , 'もみじのポシェット'),
	('BagShoulderAcorn'                        , 'どんぐりポシェット'),
	('BagShoulderSnow'                         , 'スノーフレークポシェット'),
	('BagShoulderShell'                        , 'かいがらポシェット'),
	('BagShoulderTool'                         , 'ツールバッグ'),
	('BagShoulderSports'                       , 'スポーツバッグ'),
	('BagShoulderSacosh'                       , 'サコッシュ'),
	('BagShoulderParty'                        , 'パーティーバッグ'),
	('BagBackpackWood'                         , 'せおいばしご'),
	('BagBackpackJourney'                      , 'たびびとのリュック'),
	('BagBackpackSquare'                       , 'しかくいリュック'),
	('BagBackpackOutdoor'                      , 'アウトドアリュック'),
	('BagBackpackButterfly'                    , 'ちょうちょのバッグ'),
	('BagBackpackStuds'                        , 'スタッズリュック'),
	('BagBackpackSmall'                        , 'ミニレザーバッグ'),
	('BagBackpackMountain'                     , 'おおきめザック'),
	('BagBackpackBasket'                       , 'しょいこ'),
	('BagBackpackLid'                          , 'ふたつきリュック'),
	('BagBackpackKnapsack'                     , 'ナップサック'),
	('BagBackpackTote'                         , 'はんぷリュック'),
	('BagBackpackQuilt'                        , 'ははのナップサック'),
	('BagBackpackGrass'                        , 'くさあみリュック'),
	('BagBackpackHardshell'                    , 'ハードシェルリュック'),
	('SocksTexStandard'                        , 'ビビッドなソックス'),
	('ShoesLowcutSuede'                        , 'スエードスニーカー'),
	('TopsTexOnepieceAlineHOneflower'          , 'フラワーなワンピース'),
	('TopsTexTopTshirtsHMvp'                   , 'ＭＶＰなＴシャツ'),
	('TopsTexTopTshirtsHOne'                   , 'No.1のふく'),
	('CapWigPrincess'                          , 'おひめさま'),
	('CapWigTurban'                            , 'ヘアターバン'),
	('CapHelmetCoin'                           , 'コインヘッドピース'),
	('CapWigPigtail'                           , 'べんぱつ'),
	('CapWigVisual'                            , 'ヴィジュアルけいウィッグ'),
	('CapOrnamentCQueen0'                      , 'クイーンのかんむり'),
	('TopsTexOnepieceAlineNMarbledot'          , 'マーブルドットのワンピース'),
	('TopsTexOnepieceAlineNSimpledot'          , 'シンプルドットワンピース'),
	('TopsTexOnepieceAlineNHibiscus'           , 'ハイビスカスのムームー'),
	('TopsTexOnepieceAlineNPolynesia'          , 'ポリネシアンなムームー'),
	('TopsTexTopTshirtsNDanger'                , 'デンジャラスなタンクトップ'),
	('TopsTexTopOuterLHeart'                   , 'ハートのセーター'),
	('TopsTexTopOuterLTree'                    , 'きのセーター'),
	('TopsTexTopTshirtsHFrog'                  , 'かえるのＴシャツ'),
	('TopsTexTopTshirtsHBear'                  , 'くまのＴシャツ'),
	('TopsTexTopTshirtsHRabbit'                , 'うさぎのＴシャツ'),
	('TopsTexTopTshirtsHStripe'                , 'しましまＴシャツ'),
	('TopsTexTopTshirtsHLeopard'               , 'ヒョウがらＴシャツ'),
	('TopsTexTopTshirtsHMeat'                  , 'ボーンなＴシャツ'),
	('TopsTexTopTshirtsHHaze'                  , 'かすみのふく'),
	('TopsTexTopTshirtsHMarbledot'             , 'マーブルドットのＴシャツ'),
	('TopsTexTopTshirtsHSimpledot'             , 'シンプルドットのＴシャツ'),
	('TopsTexTopTshirtsLJagged'                , 'ギザギザのＴシャツ'),
	('TopsTexTopTshirtsHFlower'                , 'はながらのＴシャツ'),
	('TopsTexTopYshirtsHPolynesia'             , 'ポリネシアンなアロハ'),
	('TopsTexTopTshirtsHSpider'                , 'スパイダーなＴシャツ'),
	('TopsTexTopTshirtsHSkull'                 , 'ドクロＴシャツ'),
	('TopsTexTopTshirtsHAce'                   , 'エースのＴシャツ'),
	('TopsTexOnepieceAlineNPlaid'              , 'シンプルチェックのワンピ'),
	('CapCostumeSnowball0'                     , 'ゆきだるまのぼうし'),
	('CapOrnamentLTsumamizaiku'                , 'わかざり'),
	('CapOrnamentLGaudy'                       , 'はでなかみかざり'),
	('CapHatCaptainsky'                        , 'きちょうのぼうし'),
	('CapHatStudent'                           , 'がくせいぼう'),
	('CapOrnamentLHibiscus'                    , 'ハイビスカスのかみかざり'),
	('TopsTexTopTshirtsNStar'                  , 'ほしがらタンクトップ'),
	('TopsTexTopTshirtsHFire'                  , 'ファイアーなＴシャツ'),
	('TopsTexOnepieceAlineHPlaid'              , 'げんきなチェックのワンピ'),
	('SocksTexNuancetights'                    , 'ニュアンスタイツ'),
	('SocksTexDailytights'                     , 'デイリータイツ'),
	('SocksTexVividtights'                     , 'ビビッドなタイツ'),
	('SocksTexNeontights'                      , 'ネオンタイツ'),
	('SocksTexVividleggings'                   , 'ビビッドなレギンス'),
	('SocksTexNeonleggings'                    , 'ネオンレギンス'),
	('AcceMouthTest1_'                         , 'おしゃぶり'),
	('TopsTexTopOuterLMother'                  , 'ははのてあみセーター'),
	('TopsTexTopCoatLMother'                   , 'ははのてづくりエプロン'),
	('TopsTexTopOuterLKnit'                    , 'シンプルなニット'),
	('SocksTexDailysocks'                      , 'デイリーソックス'),
	('SocksTexNuancesocks'                     , 'ニュアンスソックス'),
	('CapHatBaseball'                          , 'ベースボールキャップ'),
	('TopsTexTopCoatLViking'                   , 'バイキングのふく'),
	('TopsTexTopCoatLRaindot'                  , 'みずたまレインコート'),
	('TopsTexOnepieceBlongLCandula'            , 'カンデューラ'),
	('CapHatTweed'                             , 'ツイードキャップ'),
	('TopsTexTopCoatHDiner'                    , 'ダイナーのエプロン'),
	('TopsTexTopTshirtsLLayeredlogoa'          , 'かさねぎプリントＴシャツ'),
	('TopsTexTopTshirtsLLogoa'                 , 'アームプリントＴシャツ'),
	('TopsTexTopPuffHPlaid'                    , 'ブロックチェックのパフスリーブ'),
	('TopsTexTopPuffHDolly'                    , 'ドーリーシャツ'),
	('TopsTexTopCoatHWorkapron'                , 'ワークエプロン'),
	('TopsTexTopTshirtsHBotanical'             , 'ボタニカルＴシャツ'),
	('TopsTexTopYshirtsLPsychedelic'           , 'サイケデリックシャツ'),
	('TopsTexOnepieceKimonoLTwelve'            , 'じゅうにひとえ'),
	('TopsTexOnepieceDressLMexico'             , 'セニョリータなドレス'),
	('TopsTexOnepieceKimonoLCrested'           , 'もんつきはかま'),
	('TopsTexOnepieceAlineNApple'              , 'リンゴのふく'),
	('TopsTexOnepieceAlineNPear'               , 'ナシのふく'),
	('TopsTexOnepieceAlineNCherry'             , 'さくらんぼのふく'),
	('TopsTexOnepieceAlineNPeach'              , 'モモのふく'),
	('BottomsTexPantsHalfSoccer'               , 'サッカーのズボン'),
	('BottomsTexPantsHalfExplorer'             , 'たんけんふくのズボン'),
	('BottomsTexSkirtBoxLStripe'               , 'アニマルがらスカート'),
	('BottomsTexPantsNormalAmericanfootball'   , 'アメフトズボン'),
	('ShoesLowcutKungfu'                       , 'カンフーシューズ'),
	('ShoesLowcutEmbroidery'                   , 'ししゅうのくつ'),
	('CapOrnamentLFlowerhairpin'               , 'おはなのヘアピン'),
	('CapOrnamentLHearthairpin'                , 'ハートのかみかざり'),
	('CapOrnamentLStarhairpin'                 , 'ほしのかみかざり'),
	('CapOrnamentTBarrette'                    , 'バレッタ'),
	('CapOrnamentTRibbon'                      , 'おおきなリボン'),
	('CapCostumeStar'                          , 'おほしさまのあたま'),
	('CapHatSkate'                             , 'スケボーヘルメット'),
	('CapHatAlan'                              , 'アランニットぼう'),
	('CapHatLogocap'                           , 'もじキャップ'),
	('CapHatGarlystrawhat'                     , 'リボンつきむぎわらぼうし'),
	('CapHatTulippatch'                        , 'パッチワークのチューリップぼう'),
	('CapHatApple'                             , 'リンゴのぼうし'),
	('CapHatPear'                              , 'ナシのぼうし'),
	('CapHatCherry'                            , 'さくらんぼのぼうし'),
	('CapHatPeach'                             , 'モモのぼうし'),
	('TopsTexTopTshirtsHKate'                  , 'ケイトのカットソー'),
	('TopsTexTopCoatLKate'                     , 'ケイトのコート'),
	('TopsTexOnepieceAlineNKate'               , 'ケイトのワンピース'),
	('BottomsTexPantsHalfKate'                 , 'ケイトのハーフパンツ'),
	('BottomsTexSkirtLongKate'                 , 'ケイトのスカート'),
	('CapHatKatecap'                           , 'ケイトのキャップ'),
	('CapHatKatehat'                           , 'ケイトのぼうし'),
	('SocksTexKatetights'                      , 'ケイトのタイツ'),
	('SocksTexKatesocks'                       , 'ケイトのソックス'),
	('ShoesHighcutKateboots'                   , 'ケイトのパンプス'),
	('ShoesHighcutKatesneaker'                 , 'ケイトのスニーカー'),
	('AccessoryGlassKate'                      , 'ケイトのサングラス'),
	('TopsTexTopOuterLRco'                     , 'たぬきかいはつブルゾン'),
	('TopsTexTopTshirtsHRco'                   , 'たぬきかいはつアロハ'),
	('CapHatMeshcapRco'                        , 'たぬきかいはつキャップ'),
	('CapHatBandanaRco'                        , 'たぬきかいはつバンダナ'),
	('SocksTexBorderRco'                       , 'たぬきかいはつソックス'),
	('ShoesSandalRco'                          , 'たぬきかいはつスリッパ'),
	('TopsTexTopTshirtsHStar'                  , 'いちばんぼしのふく'),
	('CapHatRain'                              , 'レインハット'),
	('AccessoryGlassNook0'                     , 'たぬきかいはつアイマスク'),
	('TopsTexTopTshirtsHNook0'                 , 'たぬきかいはつＴシャツ'),
	('BagBackpackNook0'                        , 'たぬきかいはつナップサック'),
	('TopsTexTopYshirtsHInsect'                , 'インセクトアロハ'),
	('TopsTexTopTshirtsHFish'                  , 'さかなＴシャツ'),
	('CapHatOutdoorpine'                       , 'パインがらアウトドアハット'),
	('TopsTexTopCoatLPajamas'                  , 'もこもこナイトガウン'),
	('TopsTexOnepieceBoxLPajamas'              , 'パジャマワンピ'),
	('TopsTexOnepieceBalloonHVisual'           , 'ヴィジュアルけいドレス'),
	('TopsTexOnepieceAlongLUzbek'              , 'ウズベクなふく'),
	('TopsTexOnepieceBlongLAttoushi'           , 'アットゥシ'),
	('TopsTexOnepieceKimonoLBingata'           , 'びんがたいしょう'),
	('TopsTexTopCoatLDoll'                     , 'ぬいぐるみマフラーつきコート'),
	('TopsTexOnepieceOverallLPaint'            , 'ペイントつなぎ'),
	('CapHatUzbek'                             , 'ウズベクなぼうし'),
	('CapHatMatampushi'                        , 'マタンプシ'),
	('TopsTexTopTshirtsHTwo0'                  , 'No.2のふく'),
	('TopsTexTopTshirtsHThree0'                , 'No.3のふく'),
	('TopsTexTopTshirtsHFour0'                 , 'No.4のふく'),
	('TopsTexTopTshirtsHHellojp0'              , 'こんにちはＴシャツ'),
	('TopsTexTopTshirtsHHellofr0'              , 'ボンジュールＴシャツ'),
	('TopsTexTopTshirtsHHelloen0'              , 'ハローＴシャツ'),
	('TopsTexTopTshirtsHHellokr0'              , 'アンニョンＴシャツ'),
	('TopsTexTopTshirtsHHelloch0'              , 'ニーハオＴシャツ'),
	('TopsTexTopTshirtsHHelloge0'              , 'ハーローＴシャツ'),
	('TopsTexTopTshirtsHHelloit0'              , 'チャオＴシャツ'),
	('TopsTexTopTshirtsHHellosp0'              , 'オラＴシャツ'),
	('TopsTexTopTshirtsHHellors0'              , 'プリヴェＴシャツ'),
	('TopsTexTopTshirtsHHellotw0'              , 'ハイＴシャツ'),
	('TopsTexTopTshirtsHHelloNr0'              , 'ホーイＴシャツ'),
	('TopsTexTopTshirtsHDal0'                  , 'ＤＡＬのＴシャツ'),
	('TopsTexTopCoatHDal0'                     , 'ＤＡＬエプロン'),
	('TopsTexTopOuterLDal0'                    , 'ＤＡＬのＭＡ‐１'),
	('AccessoryGlassDalmask0'                  , 'ＤＡＬアイマスク'),
	('AccessoryGlassDalglass0'                 , 'ＤＡＬサングラス'),
	('AccessoryGlassSlippers0'                 , 'ＤＡＬスリッパ'),
	('BagBackpackDal0'                         , 'ＤＡＬのバッグ'),
	('CapHatDal0'                              , 'ＤＡＬキャップ'),
	('BottomsTexSkirtAlineDot'                 , 'ドットミニスカート'),
	('SocksTexDotknee'                         , 'ドットのニーハイソックス'),
	('SocksTexSimpleknee'                      , 'シンプルなニーハイソックス'),
	('BottomsTexSkirtBoxGrass1'                , 'みどりのこしみの'),
	('ShoesKneeRecyclingboots0'                , 'リサイクルながぐつ'),
	('CapHatOkmotors'                          , 'OKモータースのキャップ'),
	('TopsTexTopYshirtsHOkmotors'              , 'OKモータースジャケット'),
	('TopsTexTopTshirtsHOkmotors'              , 'キャンパーのTシャツ'),
	('CapHatEggground'                         , 'じめんのたまごのから'),
	('CapHatEggrock'                           , 'いわのたまごのから'),
	('CapHatEggleaf'                           , 'はっぱのたまごのから'),
	('CapHatEggforest'                         , 'ウッディなたまごのから'),
	('CapHatEggsky'                            , 'そらとぶたまごのから'),
	('CapHatEggfish'                           , 'サカナのたまごのから'),
	('CapOrnamentEgg'                          , 'イースターなかんむり'),
	('CapHatEggparty'                          , 'たまごのパーティーハット'),
	('BagBackpackEgg'                          , 'イースターなバッグ'),
	('TopsTexOnepieceBalloonLEgg'              , 'たまごのパーティーワンピ'),
	('TopsTexOnepieceRibNEggground'            , 'じめんのたまごのふく'),
	('TopsTexOnepieceRibNEggrock'              , 'いわのたまごのふく'),
	('TopsTexOnepieceRibNEggleaf'              , 'はっぱのたまごのふく'),
	('TopsTexOnepieceRibNEggforest'            , 'ウッディなたまごのふく'),
	('TopsTexOnepieceRibNEggsky'               , 'そらとぶたまごのふく'),
	('TopsTexOnepieceRibNEggfish'              , 'サカナのたまごのふく'),
	('ShoesLowcutEggground'                    , 'じめんのたまごのくつ'),
	('ShoesLowcutEggrock'                      , 'いわのたまごのくつ'),
	('ShoesLowcutEggleaf'                      , 'はっぱのたまごのくつ'),
	('ShoesLowcutEggforest'                    , 'ウッディなたまごのくつ'),
	('ShoesLowcutEggsky'                       , 'そらとぶたまごのくつ'),
	('ShoesLowcutEggfish'                      , 'サカナのたまごのくつ'),
	('TopsTexTopTshirtsLBorder'                , 'ボーダーＴシャツ'),
	('TopsTexTopYshirtsLMountain'              , 'マウンテンパーカー'),
	('TopsTexTopCoatLDuffle'                   , 'ダッフルコート'),
	('TopsTexOnepieceRibLKnit'                 , 'ニットワンピース'),
	('TopsTexOnepieceRibLParka'                , 'パーカーワンピ'),
	('TopsTexOnepieceBoxHJumperskirt'          , 'ジャンパースカート'),
	('TopsTexOnepieceBoxHLayercamisole'        , 'レイヤーキャミワンピ'),
	('BottomsTexPantsNormalChino'              , 'チノパン'),
	('BottomsTexPantsNormalTwotone'            , 'ツートンなズボン'),
	('BottomsTexSkirtAlineGingham'             , 'ギンガムチェックのスカート'),
	('BottomsTexPantsNormalDenimNonwa'         , 'デニムパンツ'),
)

enum_30e2684ee89a_599636c94afd = (
	('Room0', '部屋0'),
	('Room1', '部屋1'),
	('Room2', '部屋2'),
	('Room3', '部屋3'),
	('Room4', '部屋4'),
	('Room5', '部屋5'),
)

enum_322263f6b5a3_7a83210f041c = (
	('Before', '前日'),
	('Skip'  , '中止'),
	('Same'  , '同時開催'),
)

enum_34f1ef8cdbcc_52861a019f72 = (
	('None'      , '未設定'),
	('Bed'       , 'ベッド'),
	('TV'        , 'テレビ'),
	('Audio'     , 'オーディオ機器'),
	('Clock'     , '時計'),
	('Plant'     , '植物'),
	('Bathtub'   , '浴槽'),
	('Desk'      , '机'),
	('Chair'     , '椅子'),
	('Instrument', '楽器'),
	('Kitchen'   , 'キッチン'),
	('Exercise'  , '運動'),
	('Outdoor'   , 'アウトドア'),
)

enum_3b7b05ca4a0a_52b2ca6f0581 = (
	('None'       , '未設定'),
	('Floor'      , 'かぐ'),
	('Upper'      , 'こもの'),
	('Wall'       , 'かべかけ'),
	('Ceiling_Rug', 'ラグ'),
	('Plant'      , 'しょくぶつ'),
	('Creature'   , 'いきもの'),
	('Food'       , 'たべもの'),
	('Material'   , 'そざい'),
	('Others'     , 'ほか'),
	('Tool'       , 'どうぐ'),
	('RoomFloor'  , 'ゆかいた'),
	('RoomWall'   , 'かべがみ'),
	('Unnecessary', '設定不要'),
	('Clothes'    , 'ファッション'),
)

enum_3bcfd82ce180_8ccc4bd385f8 = (
	('North', '北半球'),
	('South', '南半球'),
)

enum_3db89b93b3c4_1360cab183ed = (
	('Boy_normal'  , 'ぼんやり男'),
	('Boy_active'  , 'ハキハキ男'),
	('Boy_pride'   , 'コワイ男'),
	('Boy_snobby'  , 'キザ男'),
	('Girl_normal' , '普通女'),
	('Girl_active' , '元気女'),
	('Girl_pride'  , 'オトナ女'),
	('Girl_big_sis', 'アネキ女'),
)

enum_3f8ad7b8db09_a7b5a46a35b6 = (
	('None'     , '-'),
	('Enable'   , '可'),
	('Condition', '条'),
)

enum_3f984d1a17ec_8f1bbc952a3f = (
	('House'   , '家'),
	('Facility', '施設'),
	('Bridge'  , '橋'),
	('Slope'   , '坂'),
)

enum_3fa655858099_cae6208225e0 = (
	('None'            , 'なし'),
	('Trex'            , 'Tレックス'),
	('Archelon'        , 'アーケロン'),
	('FootPrint'       , 'あしあとのかせき'),
	('Ankiro'          , 'アンキロ'),
	('Ammonite'        , 'アンモナイト'),
	('Ophthalmosaurus' , 'オフタルモサウルス'),
	('Iguanodon'       , 'イグアノドン'),
	('Droop'           , 'ウンコのかせき'),
	('Amber'           , 'コハク'),
	('Trilobite'       , 'さんようちゅう'),
	('Archeopteryx'    , 'しそちょう'),
	('Stego'           , 'ステゴ'),
	('Spino'           , 'スピノ'),
	('Diplodocus'      , 'ディプロドクス'),
	('Dimetro'         , 'ディメトロドン'),
	('Tricera'         , 'トリケラトプス'),
	('Pachy'           , 'パキケファロサウルス'),
	('Parasauro'       , 'パラサウロロフス'),
	('Futaba'          , 'フタバサウルス'),
	('Pterano'         , 'プテラノドン'),
	('Brontotherium'   , 'メガセロプス'),
	('Australopithecus', 'アウストラロピテクス'),
	('Mammoth'         , 'マンモス'),
	('Deinonychus'     , 'ディノニクス'),
	('Smilodon'        , 'スミロドン'),
	('Anomalocaris'    , 'アノマロカリス'),
	('Megaloceros'     , 'メガロケロス'),
	('Dunkleosteus'    , 'ダンクルオステウス'),
	('FirstFish'       , 'ミクロンミンギア'),
	('FirstAmphibian'  , 'ユーステノプテロン'),
	('FirstFourLegs'   , 'アカントステガ'),
	('FirstMammal'     , 'ジュラマイア'),
	('Brachiosaurus'   , 'ブラキオサウルス'),
	('Quetzalcoatlus'  , 'ケツァルコアトルス'),
	('Shark'           , 'サメのはのかせき'),
)

enum_41a82db5b173_65380129188a = (
	('None'    , 'なし'),
	('Stone'   , 'いし'),
	('Office'  , 'オフィス'),
	('Learning', 'がくしゅう'),
	('Collage' , 'こうぎしつ'),
	('Study'   , 'しょさい'),
	('Birthday', 'バースデー'),
	('Apple'   , 'リンゴ'),
	('Peach'   , 'モモ'),
	('Cherry'  , 'さくらんぼ'),
	('Orange'  , 'オレンジ'),
	('Pear'    , 'ナシ'),
	('School'  , 'がっこう'),
	('Chinese' , 'ちゅうか'),
	('Panda'   , 'パンダ'),
	('Bear'    , 'クマ'),
	('Standee' , 'ハリボテ'),
	('Natural' , 'ナチュラル'),
	('Pet'     , 'ペット'),
	('Ring'    , 'リング'),
)

enum_41b98234401e_b5f5ba492fa2 = (
	('None'     , 'なし'),
	('Warm'     , '暖色'),
	('White'    , 'ホワイト'),
	('Yellow'   , 'イエロー'),
	('Orange'   , 'オレンジ'),
	('Red'      , 'レッド'),
	('Pink'     , 'ピンク'),
	('Purple'   , 'パープル'),
	('Blue'     , 'ブルー'),
	('LightBlue', 'みずいろ'),
	('Green'    , 'グリーン'),
)

enum_4270b8b74b46_c144e90289f3 = (
	('None'  , 'なし'),
	('ToFall', '縦横滝'),
)

enum_42f04d307ef8_30984578ef41 = (
	('Invalid', 'なし'),
	('Room0'  , 'エントランス'),
	('Room1'  , '奥部屋'),
	('Room2'  , '左部屋'),
	('Room3'  , '右部屋'),
	('Room4'  , '2F'),
	('Room5'  , '地下室'),
)

enum_44bd12ada204_11a50a2b435c = (
	('None'          , 'なし'),
	('SimpleTalk'    , 'SimpleTalk'),
	('StreetLamp'    , 'StreetLamp'),
	('InsectTent'    , 'InsectTent'),
	('FishTent'      , 'FishTent'),
	('CountdownBoard', 'CountdownBoard'),
	('CountdownStall', 'CountdownStall'),
	('BulletinBoard' , 'BulletinBoard'),
	('Campfire'      , 'Campfire'),
)

enum_4547a8a48a03_a84b967e0ad7 = (
	('S', '南'),
	('E', '東'),
	('N', '北'),
	('W', '西'),
)

enum_4608a26bdcad_ba6d01a90298 = (
	('Stop', 'ストップ'),
	('Tie' , 'タイ'),
)

enum_478bafec288f_571514e8ca3c = (
	('Floor'            , '床置き'),
	('Floor_Downer'     , '台になる'),
	('Floor_DownerLeft' , '台になる：左半分'),
	('Floor_DownerRight', '台になる：右半分'),
	('Floor_DownerFront', '台になる：手前半分'),
	('Floor_DownerUpper', '台になる：上物可'),
	('Floor_Upper'      , '上物可'),
	('Floor_Gate'       , '床置き：門：3x1'),
	('Floor_Corner'     , '床置き：コーナー：3x3'),
	('Wall_NoCol'       , '壁掛け：0'),
	('Wall_HalfUnit'    , '壁掛け：0.5'),
	('Wall_1Unit'       , '壁掛け：1'),
	('Rug'              , 'ラグ'),
)

enum_47e581a0f3c1_94306367028d = (
	('None'                      , '無し'),
	('NpcRelatedTops'            , 'NPC関連服'),
	('NpcRelatedAccessory'       , 'NPC関連アクセサリ'),
	('CapOrHelmet'               , '帽子・被り物'),
	('Accessory'                 , 'アクセサリ'),
	('Bottoms'                   , 'ボトムス'),
	('Shoes'                     , '靴'),
	('MyDesignTopsByPlayer'      , 'P自作マイデザイン服'),
	('MyDesignTopsByOtherPlayer' , '他人作マイデザイン服'),
	('MyDesignTopsByOtherVillage', '他村製マイデザイン服'),
	('SprintTopsInSpring'        , '春に春服を着用'),
	('SummerTopsInSummer'        , '夏に夏服を着用'),
	('AutumnTopsInAutumn'        , '秋に秋服を着用'),
	('WinterTopsInWinter'        , '冬に冬服を着用'),
	('WinterTopsInSummer'        , '夏に冬服を着用'),
	('SummerTopsInWinter'        , '冬に夏服を着用'),
	('WearCuteTops'              , 'キュートな服を着用'),
	('WearCoolTops'              , 'クールな服を着用'),
	('WearSimpleTops'            , 'シンプルな服を着用'),
	('WearGorgeousTops'          , 'ゴージャスな服を着用'),
	('WearActiveTops'            , 'アクティブな服を着用'),
	('WearElegantTops'           , 'エレガントな服を着用'),
)

enum_48fbbb9e63e7_c771014390e5 = (
	('AlwaysAppear'                   , '天気によらず発生'),
	('AppearInRain'                   , '雨天時のみ発生'),
	('AppearInSnowGroundTerm'         , '積雪期間のみ発生'),
	('NotAppearInRain'                , '雨天時は発生しない'),
	('NotAppearInRainAndSnow'         , '雨天時、降雪時は発生しない'),
	('AppearInCherryBlossomOpenUpTerm', '桜が咲いている期間のみ発生'),
	('AppearInAutumnLeavesTerm'       , '紅葉の期間のみ発生'),
)

enum_4a1ca0237618_2589c82f75a6 = (
	('Invalid'   , '検討中'),
	('Knob'      , 'ノブ（回転なし）'),
	('KnobRotate', 'ノブ（回転あり）'),
	('PlayerTent', 'プレイヤテント'),
	('NpcTent'   , 'NPCテント'),
)

enum_4bb482986734_fd8d6be18496 = (
	('Square', '四角い'),
	('Round' , '丸い'),
)

enum_4cb47c29b213_bcb1c15d0dcc = (
	('Normal', '通常'),
	('Heavy' , '動かない'),
	('None'  , 'なし'),
)

enum_4db76367118c_3ca2ed9ace4f = (
	('None'          , 'なし'),
	('Fan'           , 'せんぷうき'),
	('Airconditioner', 'エアコン'),
	('FanWall'       , 'かべかけせんぷうき'),
)

enum_5174da149586_78f560476764 = (
	('EventObj', 'イベントオブジェ'),
	('Ftr'     , '家具'),
	('NPC'     , 'NPC'),
)

enum_52e1af9ea232_bc050e1554c9 = (
	('1_0x1_0'     , '1x1'),
	('2_0x1_0'     , '2x1'),
	('2_0x2_0'     , '2x2'),
	('3_0x1_0'     , '3x1'),
	('3_0x2_0'     , '3x2'),
	('3_0x3_0'     , '3x3'),
	('1_0x0_5'     , '1x0.5'),
	('2_0x0_5'     , '2x0.5'),
	('1_5x1_5'     , '1.5x1.5'),
	('1_0x0_5_Wall', '1x0.5(壁)'),
	('0_5x1_0_Wall', '0.5x1(壁)'),
	('1_0x1_0_Wall', '1x1(壁)'),
	('1_0x1_5_Wall', '1x1.5 (壁)'),
	('1_0x2_0_Wall', '1x2\u3000 (壁)'),
	('2_0x1_0_Wall', '2x1(壁)'),
	('2_0x1_5_Wall', '2x1.5 (壁)'),
	('2_0x2_0_Wall', '2x2(壁)'),
	('1_0x1_0_Rug' , '1x1(ラグ)'),
	('2_0x1_0_Rug' , '2x1(ラグ)'),
	('2_0x2_0_Rug' , '2x2(ラグ)'),
	('3_0x2_0_Rug' , '3x2(ラグ）'),
	('3_0x3_0_Rug' , '3x3(ラグ）'),
	('4_0x3_0_Rug' , '4x3(ラグ)'),
	('4_0x4_0_Rug' , '4x4(ラグ)'),
	('5_0x4_0_Rug' , '5x4(ラグ)'),
	('5_0x5_0_Rug' , '5x5(ラグ)'),
)

enum_53801c2056ab_77e4c99ac56b = (
	('None'          , 'なし'),
	('NotEquippedN'  , 'NPC装備不可'),
	('Pants'         , 'ズボン'),
	('Skirt'         , 'スカート'),
	('Tops'          , 'トップス'),
	('Onepiece'      , 'ワンピース'),
	('Kimono'        , 'きもの'),
	('Cap'           , 'ぼうし'),
	('HeadHairAcce'  , 'ヘアアクセサリ'),
	('EyeAcce'       , 'メガネ'),
	('EyeAcceSP'     , '特殊メガネ'),
	('EyeAcceBlind'  , 'ブラインド'),
	('Mask'          , 'おめん'),
	('DecorateFtr'   , '装飾系'),
	('HornedBeetle'  , 'カブトムシ'),
	('Stag'          , 'クワガタ'),
	('Cicada'        , 'セミ'),
	('Grasshopper'   , 'バッタ'),
	('Butterfly'     , 'チョウ'),
	('Dragonfly'     , 'トンボ'),
	('Sealouse'      , 'フナムシ'),
	('Beetle'        , '甲虫'),
	('FlowerInsect'  , '花の虫'),
	('Stump'         , '切り株'),
	('RiverFish'     , '川サカナ'),
	('SeaFish'       , '海サカナ'),
	('RiverMouthFish', '汽水池サカナ'),
	('OutofQuest'    , 'クエスト対象外'),
)

enum_555bb220c90f_a5afdf39ebc3 = (
	('Plane', '平地'),
	('River', '川'),
	('Road' , '道'),
	('Cliff', '崖'),
	('Fall' , '滝'),
)

enum_56ee1b9c32d0_341e9128ff85 = (
	('None'          , 'なし'),
	('OnCapture'     , 'あり'),
	('OnCaptureUIcon', 'あり(Uアイコン)'),
)

enum_5ba0e3fef915_f4a390fc627b = (
	('AllYear', '通年'),
	('Spring' , '春'),
	('Summer' , '夏'),
	('Autumn' , '秋'),
	('Winter' , '冬'),
)

enum_5bb07f38004e_feaae8200c31 = (
	('RightToSlant', '直角 -> 斜め'),
	('SlantToRight', '斜め -> 直角'),
)

enum_5c6b871e086e_81d76143976e = (
	('None'             , '-'),
	('BabyFtr'          , 'ベビーキッズ家具'),
	('ToyFtr'           , 'TOY家具'),
	('CostumeClothes'   , 'コスチューム'),
	('BorderClothes'    , 'ボーダー服'),
	('FitnessFtr'       , 'フィットネス家具'),
	('SportsFtr'        , 'スポーツ家具'),
	('SchoolFtr'        , '学校家具'),
	('SportClothes'     , 'スポーツウェア'),
	('OutdoorFtr'       , 'アウトドア家具'),
	('LongsleeveClothes', '長袖の服'),
	('CoolHats'         , 'おしゃれ帽子'),
	('CoolShoes'        , 'おしゃれ靴'),
	('CoolUmbrella'     , 'おしゃれカサ'),
	('CoolClothes'      , 'おしゃれ服'),
	('TeatimeFtr'       , 'ティータイム家具'),
	('StationeryFtr'    , '文具系家具'),
	('TidyClothes'      , '清楚系服'),
	('KitchenFtr'       , 'キッチン家具'),
	('AdultGlasses'     , 'オトナメガネ'),
	('LightFtr'         , '照明'),
	('BathGoods'        , 'バスグッズ'),
	('CardiganClothes'  , 'カーディガン'),
	('PlantsFtr'        , '植物'),
	('FlowerSeeds'      , '花の種'),
	('CuteUmbrella'     , 'カサ'),
	('CuteClothes'      , 'かわいい服'),
	('TeddyFtr'         , 'クマ家具'),
	('CuteFtr'          , 'キュート'),
	('DailyFtr'         , '生活用品'),
	('BadClothes'       , 'ヤンキー服'),
	('MusicFtr'         , '音楽プレイヤー'),
	('RockFtr'          , 'ロック家具'),
	('HHA1'             , 'HHA_1_汎用'),
	('HHA2'             , 'HHA_2_家電'),
	('HHA3'             , 'HHA_3_勉強部屋'),
	('HHA4'             , 'HHA_4_キッチン'),
	('HHA5_1'           , 'HHA_5_趣味_ライブ'),
	('HHA5_2'           , 'HHA_5_趣味_フィットネス'),
	('HHA5_3'           , 'HHA_5_趣味_音楽'),
	('HHA6'             , 'HHA_6_バス'),
	('HHA7'             , 'HHA_7_植物'),
	('HHA3_NPC'         , 'HHA_3_NPC_勉強部屋'),
	('HHA4_NPC'         , 'HHA_4_NPC_キッチン'),
	('HHA5_1_NPC'       , 'HHA_5_NPC_趣味_ライブ'),
	('HHA5_2_NPC'       , 'HHA_5_NPC_趣味_フィットネス'),
	('HHA5_3_NPC'       , 'HHA_5_NPC_趣味_音楽'),
	('HHA6_NPC'         , 'HHA_6_NPC_バス'),
	('HHA_FixesPoints1' , 'HHA_規定の点数1'),
	('HHA_FixesPoints2' , 'HHA_規定の点数2'),
	('HHA_FixesPoints3' , 'HHA_規定の点数3'),
	('HHA_FixesPoints4' , 'HHA_規定の点数4'),
	('HHA_FixesPoints5' , 'HHA_規定の点数5'),
	('HHA_FixesPoints6' , 'HHA_規定の点数6'),
	('HHA_FixesPoints7' , 'HHA_規定の点数7'),
	('CoolFurniture'    , 'おしゃれ家具'),
	('Clock'            , '時計'),
	('LittleFtr'        , '小さめの家具'),
	('RoughShoes'       , 'しぶい靴'),
	('UiniqueFtr'       , '珍家具'),
)

enum_5db8059c5629_f2952caee23e = (
	('Leaf'                , '葉っぱ'),
	('LeafDesign'          , '葉っぱ（マイデザイン）'),
	('Wall'                , '壁紙'),
	('Floor'               , '床板'),
	('Carpet'              , 'ラグ'),
	('Tops'                , '装備品：トップス'),
	('Bottoms'             , '装備品：ボトムス'),
	('Onepiece'            , '装備品：ワンピース'),
	('Socks'               , '装備品：靴下'),
	('Shoes'               , '装備品：靴'),
	('Cap'                 , '装備品：帽子'),
	('Wig'                 , '装備品：かぶりもの'),
	('Glasses'             , '装備品：メガネ'),
	('Bag'                 , '装備品：バッグ'),
	('Umbrella'            , '装備品：かさ'),
	('Fishingrod'          , 'つりざお'),
	('GFishingrod'         , 'つりざお：金'),
	('Net'                 , 'あみ'),
	('GNet'                , 'あみ：金'),
	('Scoop'               , 'スコップ'),
	('Gscoop'              , 'スコップ：金'),
	('Axe'                 , 'オノ'),
	('GAxe'                , 'オノ：金'),
	('AxeDull'             , 'オノ（切れない）'),
	('Watering'            , 'じょうろ'),
	('GWatering'           , 'じょうろ：金'),
	('Pachinko'            , 'パチンコ'),
	('GPachinko'           , 'パチンコ：金'),
	('ToolChangeStick'     , '変身ステッキ'),
	('ToolRiverJump'       , '川越えツール'),
	('ToolLadder'          , 'ハシゴ'),
	('Bridge'              , '橋'),
	('Slope'               , '坂'),
	('ToolGroundMaker'     , '道造成キット'),
	('ToolRiverMaker'      , '川造成キット'),
	('ToolCliffMaker'      , '崖造成キット'),
	('Helmet'              , 'たぬき開発ヘルメット'),
	('Fence'               , '柵'),
	('Post'                , 'ポスト'),
	('Tent'                , 'ハウジングキット：黄'),
	('TentWhite'           , 'ハウジングキット：白'),
	('Cracker'             , 'クラッカー'),
	('Ocarina'             , 'オカリナ'),
	('Panflute'            , 'パンフルート'),
	('Tambourine'          , 'タンバリン'),
	('GlowStick'           , 'スティックライト'),
	('Uchiwa'              , 'うちわ'),
	('Music'               , 'ミュージック'),
	('Fossil'              , '化石'),
	('FossilJ'             , '鑑定済化石'),
	('SeedPitfall'         , 'おとしあなのタネ'),
	('RemakeKit'           , 'リメイクキット'),
	('SmartphoneCase'      , 'スマホケース'),
	('Medicine'            , 'おくすり'),
	('Timer'               , 'タイマー'),
	('Honeycomb'           , 'ハチの巣'),
	('FishBait'            , 'サカナの撒き餌'),
	('Cardboard'           , 'ダンボール'),
	('Present'             , 'プレゼントBOX'),
	('Present2'            , 'プレゼントBOX：クエスト用'),
	('WrappingPaper'       , 'ラッピング済みアイテム'),
	('WPaperYellow'        , 'ラッピングペーパー：イエロー'),
	('WPaperPink'          , 'ラッピングペーパー：ピンク'),
	('WPaperOrange'        , 'ラッピングペーパー：オレンジ'),
	('WPaperLightGreen'    , 'ラッピングペーパー：キミドリ'),
	('WPaperGreen'         , 'ラッピングペーパー：ミドリ'),
	('WPaperMint'          , 'ラッピングペーパー：ミント'),
	('WPaperLightBlue'     , 'ラッピングペーパー：ライトブルー'),
	('WPaperPurple'        , 'ラッピングペーパー：パープル'),
	('WPaperNavy'          , 'ラッピングペーパー：ネイビー'),
	('WPaperBlue'          , 'ラッピングペーパー：ブルー'),
	('WPaperWhite'         , 'ラッピングペーパー：ホワイト'),
	('WPaperRed'           , 'ラッピングペーパー：レッド'),
	('WPaperGold'          , 'ラッピングペーパー：ゴールド'),
	('WPaperBrown'         , 'ラッピングペーパー：ブラウン'),
	('WPaperGray'          , 'ラッピングペーパー：グレー'),
	('WPaperBlack'         , 'ラッピングペーパー：ブラック'),
	('WBagYellow'          , 'ラッピング袋：イエロー'),
	('WBagPink'            , 'ラッピング袋：ピンク'),
	('WBagOrange'          , 'ラッピング袋：オレンジ'),
	('WBagLightGreen'      , 'ラッピング袋：キミドリ'),
	('WBagGreen'           , 'ラッピング袋：ミドリ'),
	('WBagMint'            , 'ラッピング袋：ミント'),
	('WBagLightBlue'       , 'ラッピング袋：ライトブルー'),
	('WBagPurple'          , 'ラッピング袋：パープル'),
	('WBagNavy'            , 'ラッピング袋：ネイビー'),
	('WBagBlue'            , 'ラッピング袋：ブルー'),
	('WBagWhite'           , 'ラッピング袋：ホワイト'),
	('WBagRed'             , 'ラッピング袋：レッド'),
	('WBagGold'            , 'ラッピング袋：ゴールド'),
	('WBagBrown'           , 'ラッピング袋：ブラウン'),
	('WBagGary'            , 'ラッピング袋：グレー'),
	('WBagBlack'           , 'ラッピング袋：ブラック'),
	('YellowPaperBag'      , '汎用紙袋'),
	('Coin'                , 'ベル：コイン'),
	('MoneyBag010'         , 'ベル：金袋小'),
	('MoneyBag039'         , 'ベル：金袋中'),
	('MoneyBag069'         , 'ベル：金袋大'),
	('Book'                , '落とし物：本'),
	('LostQuestPorch'      , '落とし物：巾着'),
	('LostQuestMemo'       , '落とし物：本（かきもの）'),
	('Porch'               , '落とし物：ポーチ'),
	('OddGlove'            , '落とし物：片方の手袋'),
	('AutumnLeaf'          , 'もみじのはっぱ'),
	('SnowCrystal'         , '雪の結晶'),
	('SnowCrystalLarge'    , '雪の大結晶'),
	('Sakurapetal'         , 'さくらのはなびら'),
	('StarPiece'           , 'ほしのかけら'),
	('StarPieceRare'       , 'ほしのかけら：レア'),
	('StarPieceSeason'     , 'xほしのかけら：季節'),
	('ChristmasOrnamentA'  , 'クリスマスオーナメント赤'),
	('StarpieceCapricornus', 'やぎざのかけら'),
	('ChristmasOrnamentB'  , 'クリスマスオーナメント青'),
	('StarpieceAquarius'   , 'みずがめざのかけら'),
	('ChristmasOrnamentC'  , 'クリスマスオーナメント金'),
	('StarpiecePisces'     , 'うおざのかけら'),
	('StarpieceAries'      , 'おひつじざのかけら'),
	('JohnyParts'          , 'つうしんそうちのパーツ'),
	('StarpieceTaurus'     , 'おうしざのかけら'),
	('JohnnyQuestDust1'    , 'さびたパーツ'),
	('StarpieceGemini'     , 'ふたござのかけら'),
	('StarpieceCancer'     , 'かにざのかけら'),
	('StarpieceLeo'        , 'ししざのかけら'),
	('StarpieceVirgo'      , 'おとめざのかけら'),
	('StarpieceLibra'      , 'てんびんざのかけら'),
	('StarpieceScorpio'    , 'さそりざのかけら'),
	('StarpieceSagittarius', 'いてざのかけら'),
	('YutaroWisp'          , 'ゆうたろうのたましい'),
	('BdayCupcake'         , 'バースデーカップケーキ'),
	('BottleRecipe'        , 'メッセージボトル'),
	('PaperRecipe'         , 'レシピ'),
	('DIYRecipeFence'      , 'レシピ：柵'),
	('DIYRecipeFtr'        , 'レシピ：家具'),
	('BookRecipe'          , 'レシピ本'),
	('HowtoBookHair'       , 'ハウツー本：髪'),
	('HowtoBookExpansion'  , 'ハウツー本：機能拡張'),
	('MyDesignPro'         , 'マイデザインPRO'),
	('PlaneTicket'         , 'こうくうけん'),
	('TailorTicket'        , 'したてやひきかえけん'),
	('BellExchangeTicket'  , 'ベルひきかえけん'),
	('RollanTicket'        , 'ローランひきかえけん'),
	('OreStone'            , '鉱石：いし'),
	('OreClay'             , '鉱石：ねんど'),
	('OreIron'             , '鉱石：鉄鉱石'),
	('OreGold'             , '鉱石：金鉱石'),
	('Shell0'              , 'アコヤガイのかいがら'),
	('Oyster'              , 'カキのかいがら'),
	('Shell1'              , 'ホラガイ'),
	('Shell2'              , 'シャコガイ'),
	('Shell3'              , 'サンゴ'),
	('Shell4'              , 'ホネガイ'),
	('Shell5'              , 'ホタテガイ'),
	('Shell6'              , 'エビスガイ'),
	('Shell7'              , 'タカラガイ'),
	('Shell8'              , 'サンドダラー'),
	('ShellSummer'         , 'なつのかいがら'),
	('ShellFIshAsari'      , 'アサリ'),
	('InsAmenbo'           , 'アメンボ'),
	('InsAri'              , 'アリ'),
	('InsOkera'            , 'オケラ'),
	('InsKa'               , 'カ'),
	('InsGa'               , 'ガ'),
	('InsNishikiohtsu'     , 'ニシキオオツバメガ'),
	('InsKumo'             , 'クモ'),
	('InsMinomushi'        , 'ミノムシ'),
	('InsGengorou'         , 'ゲンゴロウ'),
	('InsKonohamushi'      , 'コノハムシ'),
	('InsSasori'           , 'サソリ'),
	('InsTaranchura'       , 'タランチュラ'),
	('InsHachi'            , 'ハチ'),
	('InsAburazemi'        , 'アブラゼミ'),
	('InsKumazemi'         , 'クマゼミ'),
	('InsTsukutsuku'       , 'ツクツクホウシ'),
	('InsHigurashi'        , 'ヒグラシ'),
	('InsMinminzemi'       , 'ミンミンゼミ'),
	('InsSeminonukegara'   , 'セミのぬけがら'),
	('InsDangomushi'       , 'ダンゴムシ'),
	('InsMukade'           , 'ムカデ'),
	('InsAosuji'           , 'アオスジアゲハ'),
	('InsAkaeri'           , 'アカエリアゲハ'),
	('InsAgehacho'         , 'アゲハチョウ'),
	('InsArekisandora'     , 'アレクサンドラアゲハ'),
	('InsOhkabamadara'     , 'オオカバマダラ'),
	('InsOhgomamadara'     , 'オオゴマダラ'),
	('InsOhmurasaki'       , 'オオムラサキ'),
	('InsKarasuageha'      , 'カラスアゲハ'),
	('InsMiirotateha'      , 'ミイロタテハ'),
	('InsMorufuocho'       , 'モルフォチョウ'),
	('InsMonkicho'         , 'モンキチョウ'),
	('InsMonshirocho'      , 'モンシロチョウ'),
	('InsAkiakane'         , 'アキアカネ'),
	('InsOniyanma'         , 'オニヤンマ'),
	('InsGinyanma'         , 'ギンヤンマ'),
	('Itotonbo'            , 'イトトンボ'),
	('InsNomi'             , 'ノミ'),
	('InsHae'              , 'ハエ'),
	('InsInago'            , 'イナゴ'),
	('InsKirigirisu'       , 'キリギリス'),
	('InsKohrogi'          , 'コオロギ'),
	('InsShoryobatta'      , 'ショウリョウバッタ'),
	('InsSuzumushi'        , 'スズムシ'),
	('InsTonosamabatta'    , 'トノサマバッタ'),
	('InsHanmyou'          , 'ハンミョウ'),
	('InsFunamushi'        , 'フナムシ'),
	('InsFunkorogashi'     , 'フンコロガシ'),
	('InsHotaru'           , 'ホタル'),
	('InsMitsubachi'       , 'ミツバチ'),
	('InsYadokari'         , 'ヤドカリ'),
	('InsGomadarakamikiri' , 'カミキリムシ'),
	('InsBaiorinmushi'     , 'バイオリンムシ'),
	('InsRuriboshikamikiri', 'ルリボシカミキリ'),
	('InsOugononikuwa'     , 'オウゴンオニクワガタ'),
	('InsOhkuwagata'       , 'オオクワガタ'),
	('InsOhsenchikogane'   , 'コガネムシ'),
	('InsKanabun'          , 'カナブン'),
	('InsKabutomushi'      , 'カブトムシ'),
	('InsKamemushi'        , 'カメムシ'),
	('InsGirafanokogiri'   , 'ギラファノコギリクワ'),
	('InsKohkasasu'        , 'コーカサスオオカブト'),
	('InsGoraiasu'         , 'ゴライアスハナムグリ'),
	('InsJinmenkamemushi'  , 'ジンメンカメムシ'),
	('InsZoukabuto'        , 'ゾウカブト'),
	('InsTamamushi'        , 'タマムシ'),
	('InsNanafushi'        , 'ナナフシ'),
	('InsNijiirokuwagata'  , 'ニジイロクワガタ'),
	('InsNokogirikuwagata' , 'ノコギリクワガタ'),
	('InsPurachinakogane'  , 'プラチナコガネ'),
	('InsHerakuresu'       , 'ヘラクレスオオカブト'),
	('InsHousekizoumushi'  , 'ホウセキゾウムシ'),
	('InsHosoakakuwagata'  , 'ホソアカクワガタ'),
	('InsMiyamakuwagata'   , 'ミヤマクワガタ'),
	('InsYonagunisan'      , 'ヨナグニサン'),
	('InsKatatsumuri'      , 'カタツムリ'),
	('InsKamakiri'         , 'カマキリ'),
	('FtrInsectTagame'     , 'タガメ'),
	('InsTentoumushi'      , 'テントウムシ'),
	('InsHanakamakiri'     , 'ハナカマキリ'),
	('FishAyu'             , 'アユ'),
	('FishArowana'         , 'アロワナ'),
	('FishYellowparch'     , 'イエローパーチ'),
	('FishUgui'            , 'ウグイ'),
	('FtrFishRanchu'       , 'ランチュウ'),
	('FishAngelfish'       , 'エンゼルフィッシュ'),
	('FishEndorikerii'     , 'エンドリケリー'),
	('FishOikawa'          , 'オイカワ'),
	('FishKamitsukigame'   , 'カミツキガメ'),
	('FishGuppi'           , 'グッピー'),
	('FishSyanhaigani'     , 'シャンハイガニ'),
	('FishSuppon'          , 'スッポン'),
	('FishTanago'          , 'タナゴ'),
	('FishThirapia'        , 'ティラピア'),
	('FishDemekin'         , 'デメキン'),
	('FishDokutaafish'     , 'ドクターフィッシュ'),
	('FishDojou'           , 'ドジョウ'),
	('FishDolado'          , 'ドラド'),
	('FishDonko'           , 'ドンコ'),
	('FishNeontetora'      , 'ネオンテトラ'),
	('FishPaiku'           , 'パイク'),
	('FishPirania'         , 'ピラニア'),
	('FishPiraruku'        , 'ピラルク'),
	('FishFuna'            , 'フナ'),
	('FishBlackbass'       , 'ブラックバス'),
	('FishBlueguill'       , 'ブルーギル'),
	('FishBeta'            , 'ベタ'),
	('FishRainbowfish'     , 'レインボーフィッシュ'),
	('FishWakasagi'        , 'ワカサギ'),
	('FishItou'            , 'イトウ'),
	('FishOoiwana'         , 'オオイワナ'),
	('FishGoldenTorauto'   , 'ゴールデントラウト'),
	('FishYamame'          , 'ヤマメ'),
	('FishOtamajakusi'     , 'オタマジャクシ'),
	('FishGa'              , 'ガー'),
	('FishKaeru'           , 'カエル'),
	('FishKingyo'          , 'キンギョ'),
	('FishKoi'             , 'コイ'),
	('FishZarigani'        , 'ザリガニ'),
	('FishNamazu'          , 'ナマズ'),
	('FishNishikigoi'      , 'ニシキゴイ'),
	('FishMedaka'          , 'メダカ'),
	('FishRaigyo'          , 'ライギョ'),
	('FishKingsalmon'      , 'キングサーモン'),
	('FishSake'            , 'サケ'),
	('FishTyouzame'        , 'チョウザメ'),
	('FishAji'             , 'アジ'),
	('FishAntyobi'         , 'アンチョビ'),
	('FishIka'             , 'イカ'),
	('FishIshidai'         , 'イシダイ'),
	('FishUtsubo'          , 'ウツボ'),
	('FishEi'              , 'エイ'),
	('FishKajiki'          , 'カジキ'),
	('FishKarei'           , 'カレイ'),
	('FishKumanomi'        , 'クマノミ'),
	('FishKurione'         , 'クリオネ'),
	('FishKobanzame'       , 'コバンザメ'),
	('FishSame'            , 'サメ'),
	('FishShiira'          , 'シイラ'),
	('FishSirakansu'       , 'シーラカンス'),
	('FishShumokuzame'     , 'シュモクザメ'),
	('FishJinbeezame'      , 'ジンベエザメ'),
	('FishSuzuki'          , 'スズキ'),
	('FishTai'             , 'タイ'),
	('FishTatsunootoshigo' , 'タツノオトシゴ'),
	('FishChouchouuo'      , 'チョウチョウウオ'),
	('FishChouchinankou'   , 'チョウチンアンコウ'),
	('FishDemenigisu'      , 'デメニギス'),
	('FishNaporeonfish'    , 'ナポレオンフィッシュ'),
	('FishNanyouhagi'      , 'ナンヨウハギ'),
	('FishNokogirizame'    , 'ノコギリザメ'),
	('FishHanahigeutubo'   , 'ハナヒゲウツボ'),
	('FishHarisenbon'      , 'ハリセンボン'),
	('FishHirame'          , 'ヒラメ'),
	('FishFugu'            , 'フグ'),
	('FishMaguro'          , 'マグロ'),
	('FishManbou'          , 'マンボウ'),
	('FishMinokasago'      , 'ミノカサゴ'),
	('FishRyuuguunotukai'  , 'リュウグウノツカイ'),
	('FishRouninaji'       , 'ロウニンアジ'),
	('Can'                 , 'あきカン'),
	('Boots'               , 'ながぐつ'),
	('Tire'                , 'タイヤ'),
	('Apple'               , 'リンゴ'),
	('Orange'              , 'オレンジ'),
	('Pear'                , 'ナシ'),
	('Peach'               , 'モモ'),
	('Cherry'              , 'さくらんぼ'),
	('Coconut'             , 'ヤシの実'),
	('BanbooShoot'         , 'たけのこ'),
	('Kabu'                , 'カブ'),
	('BadKabu'             , 'くさったカブ'),
	('SquashOrange'        , 'オレンジのカボチャ'),
	('SquashYellow'        , 'きいろいカボチャ'),
	('SquashGreen'         , 'みどりのカボチャ'),
	('SquashWhite'         , 'しろいカボチャ'),
	('Mush0'               , 'りっぱなキノコ'),
	('Mush1'               , 'まるいキノコ'),
	('Mush2'               , 'ほそいキノコ'),
	('Mush3'               , 'ひらたいキノコ'),
	('Mush4'               , 'めずらしいキノコ'),
	('DIYBranch'           , 'きのえだ'),
	('DIYPinecone'         , 'まつぼっくり'),
	('DIYAcorn'            , 'どんぐり'),
	('DIYWoodNormal'       , 'もくざい'),
	('DIYWoodSoft'         , 'やわらかいもくざい'),
	('DIYWoodHard'         , 'かたいもくざい'),
	('DIYBamboo'           , '竹材'),
	('DIYBambooSpring'     , 'はるのわかたけ'),
	('SeedPaperbag0'       , 'あかい種袋'),
	('SeedPaperbag1'       , 'しろい種袋'),
	('SeedPaperbag2'       , 'きいろい種袋'),
	('SeedPaperbag3'       , 'オレンジの種袋'),
	('Rose0'               , 'あかいバラ'),
	('Rose1'               , 'しろいバラ'),
	('Rose2'               , 'きいろいバラ'),
	('Rose3'               , 'ピンクのバラ'),
	('Rose4'               , 'オレンジのバラ'),
	('Rose5'               , 'むらさきのバラ'),
	('Rose6'               , 'くろいバラ'),
	('Rose7'               , 'あおいバラ'),
	('GoldenRose'          , '金のバラ'),
	('Cosmos0'             , 'しろいコスモス'),
	('Cosmos1'             , 'あかいコスモス'),
	('Cosmos2'             , 'きいろいコスモス'),
	('Cosmos3'             , 'ピンクのコスモス'),
	('Cosmos4'             , 'オレンジのコスモス'),
	('Cosmos5'             , 'くろいコスモス'),
	('Turip0'              , 'あかいチューリップ'),
	('Turip1'              , 'しろいチューリップ'),
	('Turip2'              , 'きいろいチューリップ'),
	('Turip3'              , 'ピンクのチューリップ'),
	('Turip4'              , 'むらさきチューリップ'),
	('Turip5'              , 'くろいチューリップ'),
	('Pansi0'              , 'しろいパンジー'),
	('Turip6'              , 'オレンジチューリップ'),
	('Pansi1'              , 'きいろいパンジー'),
	('Pansi2'              , 'あかいパンジー'),
	('Pansi3'              , 'むらさきのパンジー'),
	('Pansi4'              , 'あかきいろパンジー'),
	('Pansi5'              , 'あおいパンジー'),
	('Yuri0'               , 'しろいユリ'),
	('Yuri1'               , 'きいろいユリ'),
	('Yuri2'               , 'あかいユリ'),
	('Yuri3'               , 'オレンジのユリ'),
	('Yuri4'               , 'ピンクのユリ'),
	('Yuri5'               , 'くろいユリ'),
	('Anemone0'            , 'しろいアネモネ'),
	('Anemone1'            , 'あかいアネモネ'),
	('Anemone2'            , 'オレンジのアネモネ'),
	('Anemone3'            , 'ピンクのアネモネ'),
	('Anemone4'            , 'むらさきのアネモネ'),
	('Anemone5'            , 'あおいアネモネ'),
	('Hyacinth0'           , 'しろいヒヤシンス'),
	('Hyacinth1'           , 'きいろいヒヤシンス'),
	('Hyacinth2'           , 'あかいヒヤシンス'),
	('Hyacinth3'           , 'オレンジのヒヤシンス'),
	('Hyacinth4'           , 'ピンクのヒヤシンス'),
	('Hyacinth5'           , 'むらさきのヒヤシンス'),
	('Hyacinth6'           , 'あおいヒヤシンス'),
	('Mum0'                , 'しろいキク'),
	('Mum1'                , 'きいろいキク'),
	('Mum2'                , 'あかいキク'),
	('Mum3'                , 'ピンクのキク'),
	('Mum4'                , 'みどりのキク'),
	('Mum5'                , 'むらさきのキク'),
	('PltRose0'            , 'あかいバラのかぶ'),
	('PltRose1'            , 'しろいバラのかぶ'),
	('PltRose2'            , 'きいろいバラのかぶ'),
	('PltRose3'            , 'ピンクのバラのかぶ'),
	('PltRose4'            , 'オレンジのバラのかぶ'),
	('PltRose5'            , 'むらさきのバラのかぶ'),
	('PltRose6'            , 'くろいバラのかぶ'),
	('PltRose7'            , 'あおいバラのかぶ'),
	('PltGoldenRose'       , '金のバラのかぶ'),
	('PltCosmos0'          , 'しろいコスモスのかぶ'),
	('PltCosmos1'          , 'あかいコスモスのかぶ'),
	('PltCosmos2'          , 'きいろいコスモスのかぶ'),
	('PltCosmos3'          , 'ピンクのコスモスのかぶ'),
	('PltCosmos4'          , 'オレンジのコスモスのかぶ'),
	('PltCosmos5'          , 'くろいコスモスのかぶ'),
	('PltTurip0'           , 'あかいチューリップのかぶ'),
	('PltTurip1'           , 'しろいチューリップのかぶ'),
	('PltTurip2'           , 'きいろいチューリップのかぶ'),
	('PltTurip3'           , 'ピンクのチューリップのかぶ'),
	('PltTurip4'           , 'むらさきチューリップのかぶ'),
	('PltTurip5'           , 'くろいチューリップのかぶ'),
	('PltTurip6'           , 'オレンジのチューリップのかぶ'),
	('PltPansi0'           , 'しろいパンジーのかぶ'),
	('PltPansi1'           , 'きいろいパンジーのかぶ'),
	('PltPansi2'           , 'あかいパンジーのかぶ'),
	('PltPansi3'           , 'むらさきのパンジーのかぶ'),
	('PltPansi4'           , 'あかきいろパンジーのかぶ'),
	('PltPansi5'           , 'あおいパンジーのかぶ'),
	('PltYuri0'            , 'しろいユリのかぶ'),
	('PltYuri1'            , 'きいろいユリのかぶ'),
	('PltYuri2'            , 'あかいユリのかぶ'),
	('PltYuri3'            , 'オレンジのユリのかぶ'),
	('PltYuri4'            , 'ピンクのユリのかぶ'),
	('PltYuri5'            , 'くろいユリのかぶ'),
	('PltAnemone0'         , 'しろいアネモネのかぶ'),
	('PltAnemone1'         , 'あかいアネモネのかぶ'),
	('PltAnemone2'         , 'オレンジのアネモネのかぶ'),
	('PltAnemone3'         , 'ピンクのアネモネのかぶ'),
	('PltAnemone4'         , 'むらさきのアネモネのかぶ'),
	('PltAnemone5'         , 'あおいアネモネのかぶ'),
	('PltHyacinth0'        , 'しろいヒヤシンスのかぶ'),
	('PltHyacinth1'        , 'きいろいヒヤシンスのかぶ'),
	('PltHyacinth2'        , 'あかいヒヤシンスのかぶ'),
	('PltHyacinth3'        , 'オレンジのヒヤシンスのかぶ'),
	('PltHyacinth4'        , 'ピンクのヒヤシンスのかぶ'),
	('PltHyacinth5'        , 'むらさきのヒヤシンスのかぶ'),
	('PltHyacinth6'        , 'あおいヒヤシンスのかぶ'),
	('PltMum0'             , 'しろいキクのかぶ'),
	('PltMum1'             , 'きいろいキクのかぶ'),
	('PltMum2'             , 'あかいキクのかぶ'),
	('PltMum3'             , 'ピンクのキクのかぶ'),
	('PltMum4'             , 'みどりのキクのかぶ'),
	('PltMum5'             , 'むらさきのキクのかぶ'),
	('PltSuzuran'          , 'スズランのかぶ'),
	('Seedling'            , '木の苗'),
	('PltOak'              , '広葉樹'),
	('SeedlingConifer'     , '針葉樹の苗'),
	('PltConifer'          , '針葉樹'),
	('PltBamboo'           , '竹'),
	('PltPalm'             , 'ヤシの木'),
	('PltApple'            , 'リンゴの木'),
	('PltOrange'           , 'オレンジの木'),
	('PltPear'             , 'ナシの木'),
	('PltPeach'            , 'モモの木'),
	('PltCherry'           , 'さくらんぼの木'),
	('PltMoney'            , '金のなる木'),
	('Weed'                , 'ざっそう'),
	('EggGround'           , 'じめんのたまご'),
	('EggRock'             , 'いわのたまご'),
	('EggLeaf'             , 'はっぱのたまご'),
	('EggForest'           , 'もりのたまご'),
	('EggSky'              , 'そらとぶたまご'),
	('EggFish'             , 'サカナのたまご'),
	('MessageBottleEgg'    , 'たまごのメッセージボトル'),
)

enum_5fe6f47ed555_cd0b35a4b9fb = (
	('Player'     , 'プレイヤ家'),
	('Npc'        , 'NPC家'),
	('PhotoStudio', '撮影スタジオ'),
)

enum_60ad9adbd84b_bd137f5ee888 = (
	('NoChange', '変更なし'),
	('CliffAll', '平地 -> 崖平地'),
)

enum_60d7f7443dea_ced5321a8793 = (
	('None'                , 'なし'),
	('Series_Cute'         , 'キュート'),
	('Series_TOY'          , 'TOY'),
	('Series_Rattan'       , 'ラタン'),
	('Series_Oriental'     , 'オリエンタル'),
	('Series_AmericanRetro', 'アメリカンレトロ'),
	('Series_Antique'      , 'アンティーク'),
	('Series_Mom'          , '母'),
	('Set_Hero'            , 'ヒーローロボ'),
	('Set_Chinese'         , '中華テーブル'),
	('Set_Outdoortable'    , 'アウトドアテーブル'),
	('Set_School'          , '学校'),
	('Set_Collage'         , '講義室'),
	('Set_Study'           , '学習机'),
	('Set_Japaneseroom'    , '和室'),
	('Set_Boxsofa'         , 'ボックスソファ'),
	('Set_Shower'          , 'シャワーセット'),
	('Set_Flamingo'        , 'フラミンゴ'),
	('Tool_Outdoor'        , '道具アウトドア'),
	('Tool_Colorful'       , '道具カラフル'),
)

enum_62e4c6f51ad1_474f8f35cfdc = (
	('None', 'なし'),
	('1x1' , '1x1'),
	('3x3' , '3x3'),
)

enum_6375519ed254_5b8e07b717c6 = (
	('None' , 'クリアしない'),
	('Pre'  , '日またぎ成長処理前（経過日数が0以外）'),
	('Start', '起動時、日またぎ成長処理前'),
	('All'  , 'すべての成長処理（おすそわけ人数変更時を含む）'),
	('Plus' , '日が進んだときの日またぎ成長処理前（経過日数がプラス時）'),
)

enum_639356d46fa4_639356d46fa4 = (
	('No' , 'No'),
	('Yes', 'Yes'),
)

enum_63bab5a95741_093e393915f9 = (
	('TestSoft', 'testやわらかいくつ'),
	('Naked'   , 'はだし'),
	('Socks'   , 'くつした'),
	('Bird'    , 'トリ'),
	('Soft'    , 'やわらかい靴'),
	('Hard'    , 'かたい靴'),
	('None'    , 'なし'),
	('Geta'    , 'げた'),
	('Pumps'   , 'パンプス'),
)

enum_666520d79fd1_c1f7ed2fb38f = (
	('Overwrite' , '上書き'),
	('Sequential', '累積'),
)

enum_67d8f9fad662_3c4e63ce8503 = (
	('None' , 'なし'),
	('Scale', 'あり'),
)

enum_69eaeee0564d_950b97c5042a = (
	('N_convexity' , 'N凸'),
	('N_flat'      , 'N平'),
	('N_concavity' , 'N凹'),
	('NE_convexity', 'NE凸'),
	('NE_flat'     , 'NE平'),
	('NE_concavity', 'NE凹'),
	('E_convexity' , 'E凸'),
	('E_flat'      , 'E平'),
	('E_concavity' , 'E凹'),
	('SE_convexity', 'SE凸'),
	('SE_flat'     , 'SE平'),
	('SE_concavity', 'SE凹'),
	('S_convexity' , 'S凸'),
	('S_flat'      , 'S平'),
	('S_concavity' , 'S凹'),
	('SW_convexity', 'SW凸'),
	('SW_flat'     , 'SW平'),
	('SW_concavity', 'SW凹'),
	('W_convexity' , 'W凸'),
	('W_flat'      , 'W平'),
	('W_concavity' , 'W凹'),
	('NW_convexity', 'NW凸'),
	('NW_flat'     , 'NW平'),
	('NW_concavity', 'NW凹'),
)

enum_6adf97f83acf_3609f958a376 = (
	('None', 'なし'),
)

enum_6bc751394207_9a22cc494738 = (
	('Disable'               , 'デモ不可'),
	('EnableToDemoNetLock'   , 'デモネットロック可'),
	('EnableToDemoAll'       , 'デモ全部可'),
	('EnableToDemoStandSpeak', 'デモ立ちSpeak可'),
	('EnableToDemoSitSpeak'  , 'デモ座りSpeak可'),
	('EnableToDemoBedSpeak'  , 'デモベッドSpeak可'),
	('EnableToDemoSwimSpeak' , 'デモ泳ぎSpeak可'),
	('IsDemo'                , 'デモ状態'),
)

enum_6f6d6ff1098e_dbf69e6d0415 = (
	('None'     , 'なし'),
	('MakeFall' , '崖 -> 滝'),
	('BreakFall', '滝 -> 崖'),
)

enum_70471eeaa222_c602c1a479c5 = (
	('NoChange'     , '変更なし'),
	('AddCliffLevel', '崖レベル加算'),
	('RemoveHistory', '最終履歴削除'),
)

enum_717e8e90873e_eb9d94566e11 = (
	('Base'        , '地面'),
	('River'       , '川'),
	('RoadStone'   , '石道'),
	('Cliff'       , '崖'),
	('None'        , 'なし'),
	('Invalid'     , '無効値'),
	('Soil'        , '土'),
	('Brick'       , 'レンガ'),
	('DarkSoil'    , '黒土'),
	('StonePattern', '石畳'),
	('Sand'        , '砂'),
	('Tile'        , 'タイル'),
	('Wood'        , '木'),
)

enum_719f8c5ace1e_9dc2d1c92509 = (
	('Invalid', '無効値'),
	('Tent'   , 'テント'),
	('Level00', '成長段階00'),
	('Level01', '成長段階01'),
	('Level02', '成長段階02'),
	('Level03', '成長段階03'),
	('Level04', '成長段階04'),
)

enum_71a6eb72125d_4959f0d2a68c = (
	('Continue'               , '前ステート引継ぎ'),
	('Putaway'                , 'しまう'),
	('IfNotDemoDraw'          , 'デモでなければ表示'),
	('GiveOverKeepPutawayFlag', 'PlayerKeepFlagに従う'),
	('StageIn'                , 'ステージイン'),
)

enum_7797cc9a6dbe_5f875c1a6730 = (
	('Global'  , 'グローバル'),
	('Region'  , 'リージョン'),
	('Other'   , 'その他（誕生日等）'),
	('Totakeke', 'とたけけライブ'),
	('None'    , 'なし'),
	('Term'    , '期間型'),
)

enum_784cf9486925_255fffffb8d5 = (
	('No0', 'レイヤ0'),
	('No1', 'レイヤ1'),
)

enum_794b88fd5d5e_eaf8e9c36279 = (
	('None'                     , 'なし'),
	('ShopDefault'              , '店_初期'),
	('ShopMiscGoods'            , '店_雑貨'),
	('ShopLargeGoods'           , '店_大型'),
	('ShopHighClass'            , '店_高級'),
	('ShopLv1'                  , '店_店舗小'),
	('ShopLv2'                  , '店_店舗大'),
	('ShopSeasonSale'           , '店_季節限定'),
	('MarketAlways'             , '店_固定'),
	('DefaultFtr'               , '初期支給家具'),
	('MarketingRouteA'          , '店_流通A(家具設定不可)'),
	('MarketingRouteC'          , '店_流通C(家具設定不可)'),
	('MarketingRouteB'          , '店_流通B(家具設定不可)'),
	('MarketingRouteD'          , '店_流通D(家具設定不可)'),
	('ShopUmbrellaLv1'          , '店_カサ小'),
	('ShopUmbrellaLv2'          , '店_カサ大'),
	('ShopWrappingPaper'        , '店_ラッピングペーパー'),
	('ShopCracker'              , '店_クラッカー'),
	('ShopTimer'                , '店_店舗大固定'),
	('ShopVarietyFishingRod'    , '店_店売り：つりざお'),
	('ShopVarietyNet'           , '店_店売り：あみ'),
	('ShopVarietyShovel'        , '店_店売り：スコップ'),
	('ShopVarietyWatering'      , '店_店売り：ジョウロ'),
	('ShopVarietySlingShot'     , '店_店売り：パチンコ'),
	('Shop_EnableShovel'        , '店_スコップ解禁'),
	('Shop_EnableAxe'           , '店_オノ解禁'),
	('ShopRecipeBook2'          , '店_レシピブック2'),
	('ShopRemakeKit'            , '店_リメイクキット'),
	('Shop_EnableRecipeWatering', '店_レシピ解禁(ジョウロ)'),
	('Shop_EnableRecipeScoop'   , '店_レシピ解禁(スコップ高跳び)'),
	('Shop_EnableRecipeLadder'  , '店_レシピ解禁(ハシゴ)'),
	('SonkatsuRewardTent'       , 'マイル交換_初期'),
	('SonkatsuRewardShop'       , 'マイル交換_プラス'),
	('MileExchangeOnce'         , 'マイル交換_プラス(買い切り)'),
	('SonkatsuReward2'          , 'マイル交換_案内所'),
	('MileExchangePhoneCase'    , 'マイル交換_スマホケース'),
	('MileExchangeLicense'      , 'マイル交換_工事ライセンス(買い切り)'),
	('MileExchangePocket40'     , 'マイル交換_持ち物欄40(買い切り)'),
	('MileExchangeRecipe1'      , 'マイル交換_家具レシピ800'),
	('MileExchangeRecipe2'      , 'マイル交換_家具レシピ1500'),
	('MileExchangeRecipe3'      , 'マイル交換_家具レシピ2000'),
	('MileExchangeRecipe4'      , 'マイル交換_家具レシピ3000'),
	('MileExchangeRecipe5'      , 'マイル交換_家具レシピ5000'),
	('MileExchangeNsoPresent'   , 'マイル交換_NSO加入特典'),
	('Bridge'                   , '案内所_橋'),
	('Slope'                    , '案内所_坂'),
	('OnlineShoppingOnly'       , '通信販売のみ'),
	('Tailor'                   , '仕立て屋'),
	('TailorMarketOnly'         , '仕立て屋_店舗'),
	('TailorXmas'               , '仕立て屋_クリスマス'),
	('TailorMarketOnlyXmas'     , '仕立て屋_店舗_クリスマス'),
	('RugS'                     , 'ローラン_S'),
	('RugM'                     , 'ローラン_M'),
	('RugL'                     , 'ローラン_L'),
	('LaurentWallFloor'         , 'ローラン壁床'),
	('ShoesBagShop'             , 'シャンク'),
	('HgcQuestReward'           , 'ことの報酬'),
	('TkkGood'                  , 'とたけけ_ゴキゲン！'),
	('TkkBad'                   , 'とたけけ_フキゲン'),
	('TkkRelax'                 , 'とたけけ_まったり'),
	('TkkBlue'                  , 'とたけけ_ブルーかも'),
	('TkkUnsure'                , 'とたけけ_よくわからない'),
	('TkkHidden'                , 'とたけけ_隠し曲'),
	('TkkMiss'                  , 'とたけけ_はずれ曲'),
	('TkkBirthday'              , 'とたけけ_誕生日曲'),
	('TkkFirst'                 , 'とたけけ_初ライブ曲'),
	('TkkNewGood'               , 'とたけけ新曲_ゴキゲン！'),
	('TkkNewBad'                , 'とたけけ新曲_フキゲン'),
	('TkkNewRelax'              , 'とたけけ新曲_まったり'),
	('TkkNewBlue'               , 'とたけけ新曲_ブルーかも'),
	('TkkNewUnsure'             , 'とたけけ新曲_よくわからない'),
	('TkkNew'                   , 'とたけけ_新曲'),
	('TreasureQuest'            , '宝探しクエスト'),
	('TreasureQuestDust'        , '宝探しクエストごみ'),
	('SnowmanReward'            , 'ゆきだるま'),
	('PcBday'                   , 'PC誕生日'),
	('JohnnyQuest'              , 'ジョニークエスト'),
	('JohnnyQuestDust'          , 'ジョニークエストごみ'),
	('JohnnyQuestReward'        , 'ジョニークエスト報酬'),
	('TournamentFishing'        , 'つり大会'),
	('TournamentInsect'         , 'ムシとり大会'),
	('CountDown'                , 'カウントダウン'),
	('BeyDailyFishModel'        , 'ジャスティン(来訪)'),
	('ChyDailyInsectModel'      , 'レオン(来訪)'),
	('RecycleBox'               , 'リサイクルBOX'),
	('ShopSeed_Chrysanthemum'   , '販売種_菊'),
	('ShopSeed_Lily'            , '販売種_ユリ'),
	('ShopSeed_Cosmos'          , '販売種_コスモス'),
	('ShopSeed_Hyacinth'        , '販売種_ヒヤシンス'),
	('ShopSeed_Rose'            , '販売種_バラ'),
	('ShopSeed_Anemone'         , '販売種_アネモネ'),
	('ShopSeed_Tulip'           , '販売種_チューリップ'),
	('ShopSeed_Pansy'           , '販売種_パンジー'),
	('FruitApple'               , '<フルーツ>リンゴ'),
	('FruitOrange'              , '<フルーツ>オレンジ'),
	('FruitPear'                , '<フルーツ>ナシ'),
	('FruitPeach'               , '<フルーツ>モモ'),
	('FruitCherry'              , '<フルーツ>サクランボ'),
	('Insect'                   , '生き物：ムシ'),
	('Fish'                     , '生き物：サカナ'),
	('Fossil'                   , '化石'),
	('Flower'                   , '植物：花'),
	('Bromide'                  , 'ブロマイド'),
	('Poster'                   , 'ポスター'),
	('HHAGift'                  , 'HHA報酬'),
	('Trophy'                   , 'トロフィー'),
	('Mother'                   , 'はは'),
	('AirportNovelty'           , '飛行場記念品'),
	('ShopDIY'                  , '<DIY素材>'),
	('DIYNormal'                , '<DIY>汎用'),
	('Fence'                    , '<DIY>柵'),
	('DIY_Mushroom'             , '<DIY>きのこ'),
	('DIYZodiac'                , '<DIY>12星座'),
	('DIYSpringBamboo'          , '<DIY>春の若竹'),
	('DIYSummerShell'           , '<DIY>夏の貝がら'),
	('DIYAutmnNuts'             , '<DIY>秋の木の実'),
	('DIYOrnament'              , '<DIY>オーナメント'),
	('DIYMapleLeaf'             , '<DIY>もみじのはっぱ'),
	('DIYCherryBrossom'         , '<DIY>桜の花びら'),
	('DIYSnowCrystal'           , '<DIY>雪の結晶'),
	('DIYEasterEgg'             , '<DIY>イースターのたまご'),
	('DeliveryPocketCamp'       , '<永続配信>ポケ森コラボ'),
	('Easter'                   , 'イースター'),
	('FutureItem'               , '■アップデート向け■'),
	('NotAvailable'             , '◆入手不可◆'),
)

enum_79fc030d2ca5_3b8dd86eef4f = (
	('None'             , 'なし'),
	('Pet'              , '生き物'),
	('Audio'            , 'オーディオ'),
	('MusicalInstrument', '楽器'),
	('Plant'            , '観葉植物'),
	('Trash'            , 'ゴミ箱'),
	('SmallGoods'       , '小物'),
	('Lighting'         , '照明'),
	('TV'               , 'テレビ'),
	('Clock'            , '時計'),
	('AC'               , '冷暖房'),
	('Dresser'          , 'ドレッサー'),
	('Appliance'        , '家電'),
	('Doll'             , '人形'),
)

enum_7a531090c8c0_d059b6858b92 = (
	('River'         , '川'),
	('RiverCliffTop' , '川：崖上'),
	('Pond'          , '池'),
	('BrackishWater' , '汽水池'),
	('Sea'           , '海'),
	('Anywhere'      , 'どこでも'),
	('SeaBeachBridge', '海：桟橋'),
)

enum_7a6babece06f_675c7f6d8dcb = (
	('DisableOnlyLowerBody'     , '下半身再生不可'),
	('EnableOnlyLowerBody_Sit'  , '下半身再生可(座り系)'),
	('EnableOnlyLowerBody_Bed'  , '下半身再生可(寝る系)'),
	('EnableOnlyLowerBody_Stand', '下半身再生可(立ち系)'),
)

enum_7f4abdaa06e5_875003339aa7 = (
	('Orange'   , 'オレンジ'),
	('Red'      , 'レッド'),
	('Pink'     , 'ピンク'),
	('Purple'   , 'パープル'),
	('Blue'     , 'ブルー'),
	('LightBlue', 'みずいろ'),
	('Green'    , 'グリーン'),
	('Yellow'   , 'イエロー'),
	('Beige'    , 'ベージュ'),
	('Brown'    , 'ブラウン'),
	('Black'    , 'ブラック'),
	('Gray'     , 'グレー'),
	('White'    , 'ホワイト'),
	('Colorful' , 'カラフル'),
	('None'     , 'なし'),
)

enum_7fc56270e7a7_413dac6d2d4f = (
	('A', 'タイプA'),
)

enum_80fe2e01edeb_a0944789ee2d = (
	('WhitishFlower'        , '白系の花'),
	('RedPinkFlower'        , '赤・桃系の花'),
	('BluePurpleBlackFlower', '青・紫・黒系の花'),
	('YellowFlower'         , '黄色系の花'),
	('MatureTreeOak'        , '広葉樹（成木）'),
	('MatureTreeCedar'      , '針葉樹（成木）'),
	('MatureTreePalm'       , 'ヤシの木（成木）'),
	('MatureTreeBamboo'     , '竹（成木）'),
	('TreeOakStump'         , '広葉樹：切り株'),
	('TreeCedarStump'       , '針葉樹：切り株'),
	('TreePalmStump'        , 'ヤシの木：切り株'),
	('TreeBambooStump'      , '竹：切り株'),
	('Trash'                , 'ゴミ（ハエ用）'),
	('TurnipExpired'        , '腐ったカブ'),
	('Candy'                , '飴（アリ用）'),
	('TreeAdhereHoneycomb'  , '蜂の巣付きの木'),
	('Stone'                , '岩'),
	('None'                 , 'なし'),
)

enum_8660a424ddf9_da4e1de32164 = (
	('None'      , '×'),
	('Sometimes' , '△'),
	('Relatively', '〇'),
	('Always'    , '◎'),
)

enum_870fe161ccb7_b6b6458365a4 = (
	('None'         , 'なし'),
	('Iron'         , 'アイアン'),
	('IronWood'     , 'アイアンウッド'),
	('AmericanRetro', 'ダイナー'),
	('Antique'      , 'アンティーク'),
	('Gold'         , 'おうごん'),
	('Oriental'     , 'オリエンタル'),
	('Shell'        , 'かいがら'),
	('Mushroom'     , 'キノコ'),
	('Cute'         , 'キュート'),
	('Bamboo'       , 'たけ'),
	('Block'        , 'つみき'),
	('Halloween'    , 'ハロウィン'),
	('Fruit'        , 'フルーツ'),
	('Log'          , 'まるた'),
	('Wooden'       , 'もくせい'),
	('Rattan'       , 'ラタン'),
	('Rock'         , 'TOY'),
	('Ice'          , 'こおり'),
	('Star'         , 'ほし'),
	('Flower'       , 'はな'),
	('Nut'          , 'きのみ・おちば'),
	('CherryBlossom', 'さくら'),
	('Cardboard'    , 'ダンボール'),
	('Mother'       , 'はは'),
	('Christmas'    , 'クリスマス'),
	('Easter'       , 'イースター'),
)

enum_872b31abf9f9_cc7475a100e8 = (
	('Undefined', '未設定'),
	('Low'      , '低'),
	('Normal'   , '中'),
	('High'     , '高'),
)

enum_876f2a44aa3e_ea533d18da76 = (
	('None'                   , '※未設定'),
	('Shop'                   , 'お店'),
	('SeqRcoAlbeit'           , 'たぬきちアルバイト中'),
	('Sequence1'              , 'シーケンス専用1'),
	('Sza001'                 , 'しずえ1'),
	('Owl001'                 , 'フータ1'),
	('Slo001'                 , 'レイジ1'),
	('TV'                     , 'DIYテレビ番組'),
	('Sza002'                 , 'しずえ2(役場建設準備)'),
	('TownmakeLicenceLv5'     , '崖造成解禁時'),
	('NnpcHA000'              , '初期HA'),
	('NnpcAN000'              , '初期AN'),
	('DIYtutorial1'           , 'DIY体験会'),
	('DIYtutorial2'           , 'DIY体験会報酬'),
	('TrashRecipeTires'       , 'ゴミレシピ＜タイヤ＞'),
	('RcoDonationRewardA'     , 'たぬきち虫魚報酬A'),
	('Snowman'                , 'ゆきだるま'),
	('DIYbook1'               , 'DIYレシピブック1'),
	('DIYbook2'               , 'DIYレシピブック2'),
	('DIYbook3'               , 'DIYレシピブック3'),
	('DIYbookVariety'         , 'DIYレシピパーティグッズ'),
	('DIYbookFence1'          , 'DIYレシピ柵：木1'),
	('DIYbookFence2'          , 'DIYレシピ柵：木2'),
	('WoodBridge'             , 'まるたのはし(シーケンス)'),
	('CampSite'               , 'キャンプ場(シーケンス)'),
	('Ows01'                  , 'フーコ（星素材）'),
	('Ows02'                  , 'フーコ（12星座）'),
	('DIYbookNormalTools'     , 'DIYレシピいっぱし道具'),
	('DIYbookFence3'          , 'DIYレシピ柵：バラエティ'),
	('DIYbookFence4'          , 'DIYレシピ柵：鉄と石'),
	('SeasonSakura'           , '季節：桜の花びら'),
	('SeasonSpringBamboo'     , '季節：春のわかたけ'),
	('SeasonSummerShell'      , '季節：夏のかいがら'),
	('SeasonAutumnNuts'       , '季節：どんぐり'),
	('SeasonMomiji'           , '季節：紅葉の葉っぱ'),
	('SeasonChristmasOrnament', '季節：オーナメント'),
	('SeasonMushroom'         , '季節：きのこ'),
	('SeasonSnowCrystal'      , '季節：ゆきのけっしょう'),
	('RcoDonationRewardB'     , 'たぬきち虫魚報酬B'),
	('ImmigrationQuest'       , '移住クエスト'),
	('RemakeTutorial'         , 'リメイク体験'),
	('MileExchange'           , '＜マイル交換＞'),
	('Market'                 , '＜店売り＞'),
	('Inspire'                , '＜ひらめき＞'),
	('GoldTool'               , '＜金の道具＞'),
	('Broadcast'              , '＜島内放送＞'),
	('EasterPyn'              , 'イースター：ぴょんたろう会話'),
	('EasterNpc'              , 'イースター：アプローチ会話'),
	('EasterRand'             , 'イースター：風船・ボトル'),
	('EasterGround'           , 'イースター：ひらめき：じめん'),
	('EasterRock'             , 'イースター：ひらめき：いわ'),
	('EasterLeaf'             , 'イースター：ひらめき：はっぱ'),
	('EasterForest'           , 'イースター：ひらめき：もり'),
	('EasterSky'              , 'イースター：ひらめき：そらとぶ'),
	('EasterFish'             , 'イースター：ひらめき：サカナ'),
	('EasterCapHat'           , 'イースター：ひらめき：からコンプ'),
	('EasterTops'             , 'イースター：ひらめき：ふくコンプ'),
)

enum_8bcffcdc34f9_75d5da8d5621 = (
	('None'  , '無し'),
	('Square', '四角'),
	('Circle', '丸'),
	('Arch'  , 'アーチ'),
)

enum_8d64dd844b09_8d64dd844b09 = (
	('Player', 'Player'),
	('Npc'   , 'Npc'),
)

enum_8f4bdb1e73c6_3c4e63ce8503 = (
	('None' , 'なし'),
	('Valid', 'あり'),
)

enum_8fe44c9d797f_aa6d915eb9ed = (
	('Prefer', '好む'),
	('Normal', '気にせず'),
	('Avoid' , '避ける'),
)

enum_8ffbd0e14173_94fb029812b4 = (
	('NoRiver'  , '河口なし'),
	('WestRiver', '西河口'),
	('EastRiver', '東河口'),
)

enum_917e0a06d70e_917e0a06d70e = (
	('OFF', 'OFF'),
	('ON' , 'ON'),
)

enum_93cb28c3569f_1cf1287084ce = (
	('NoSelect'           , '指定無し'),
	('SelectRecipeSeason' , 'レシピ用季節'),
	('SelectCalendarEvent', 'カレンダーイベント'),
)

enum_9601b1ddc20d_b837359c7300 = (
	('None' , 'なし'),
	('Num'  , '数'),
	('Money', '金額'),
)

enum_960b44c579bc_90f80471d9f2 = (
	('Normal', '通常'),
)

enum_9cef5ff8f2fc_3c4e63ce8503 = (
	('None' , 'なし'),
	('UseAO', 'あり'),
)

enum_a099ed9ed7e6_1fc5597471f3 = (
	('Unknown'     , '未設定'),
	('MailBoxTypeA', 'ポスト：タイプA'),
	('MailBoxTypeB', 'ポスト：タイプB'),
	('MailBoxTypeC', 'ポスト：タイプC'),
	('MailBoxTypeD', 'ポスト：タイプD'),
	('MailBoxTypeE', 'ポスト：タイプE'),
)

enum_a28161dd393f_a28161dd393f = (
	('SS' , 'SS'),
	('S'  , 'S'),
	('M'  , 'M'),
	('L'  , 'L'),
	('LL' , 'LL'),
	('LLL', 'LLL'),
	('U'  , 'U'),
	('J'  , 'J'),
	('K'  , 'K'),
)

enum_a382e5214fd4_31aae64bf1ea = (
	('None'            , '未設定'),
	('DirectionOutdoor', '屋外向き'),
	('DirectionIndoor' , '屋内向き'),
)

enum_a397999fca4b_a59ff2e96b38 = (
	('FtrNoneUser'  , 'ユーザなし'),
	('FtrUniqueUser', '個別ユーザ'),
	('FtrCommonUser', '共通ユーザ'),
)

enum_a3c5bfa601e4_a3c5bfa601e4 = (
	('Make' , 'Make'),
	('Break', 'Break'),
)

enum_a3f2105dc205_cf3454689058 = (
	('None'         , '未設定'),
	('Mushroom'     , 'きのこ'),
	('Ice'          , 'こおり'),
	('Japanese'     , '和風'),
	('Block'        , 'つみき'),
	('Antique'      , 'アンティーク'),
	('School'       , '学校'),
	('Resort'       , 'リゾート'),
	('Office'       , 'オフィス'),
	('Log'          , 'まるた'),
	('Cute'         , 'キュート'),
	('Fruit'        , 'フルーツ'),
	('AmericanRetro', 'アメリカンレトロ'),
	('Toy'          , 'TOY'),
	('Shell'        , 'かいがら'),
	('IronWood'     , 'アイアンウッド'),
	('Easter'       , 'イースター'),
)

enum_a55023d0faad_4d2a3ca36fe8 = (
	('MannequinPause01', 'ポーズ1'),
	('MannequinPause02', 'ポーズ2'),
	('MannequinPause03', 'ポーズ3'),
	('MannequinPause04', 'ポーズ4'),
	('MannequinPause05', 'ポーズ5'),
	('MannequinPause06', 'ポーズ6'),
)

enum_a579ed29f896_c3ff5ecc7a5b = (
	('AllDay' , '一日中'),
	('Morning', '朝'),
	('Daytime', '昼'),
	('Night'  , '夜'),
)

enum_a68bce6af69b_92745feba3f9 = (
	('Undefined', '未設定'),
	('Play'     , 'あそび'),
	('Music'    , '音楽'),
	('Fitness'  , 'フィットネス'),
	('Fashion'  , 'ファッション'),
	('Education', '教養'),
	('Nature'   , '自然愛'),
)

enum_a7030bb7fc9b_fc546f9fbb31 = (
	('BO'     , 'ぼんやり男'),
	('HA'     , 'ハキハキ男'),
	('KO'     , 'コワイ男'),
	('ZK'     , 'キザ男'),
	('FU'     , 'ふつう女'),
	('GE'     , 'ゲンキ女'),
	('OT'     , 'オトナ女'),
	('AN'     , 'アネキ女'),
	('ALL_NPC', 'NPC共通'),
	('NO_TAKE', '入手不可'),
)

enum_a8722b855893_f7ee7d2a5a4e = (
	('None'             , 'なし'),
	('MyDesign'         , 'マイデザ'),
	('CommonAndMyDesign', '汎用&マイデザ'),
)

enum_a97c5a371180_d749edee2750 = (
	('Normal'   , '通常楽器'),
	('Drum'     , '打楽器'),
	('DrumSet'  , 'ドラムセット'),
	('FourHands', '連弾楽器'),
)

enum_aa288b7299e1_ae503b12cd83 = (
	('None'       , '未設定'),
	('FtrAccess'  , '家具アクセス'),
	('FtrSwitchOn', '家具スイッチ'),
	('RhythmSound', 'ノる'),
	('SingSong'   , '歌う'),
	('PlayMusic'  , '演奏する'),
)

enum_af770d1cdd34_208c036ec702 = (
	('None'            , 'なし'),
	('Smartphone'      , '撮影'),
	('Switch'          , '駆動'),
	('RhythmSound'     , 'ノる'),
	('SingSong'        , '歌う'),
	('PlayMusicBoth'   , '演奏する（両手）'),
	('PlayMusic'       , '演奏する（片手）'),
	('SwitchWind'      , '駆動（扇風機）'),
	('SwitchWarm'      , '駆動（温まる）'),
	('SwitchSomen'     , '駆動（そうめん）'),
	('SwitchTakenAback', '駆動（ビックリ）'),
	('Watch'           , 'まじまじ見る'),
	('WatchWall'       , 'まじまじ見る（壁掛）'),
	('MirrorPosing'    , '鏡の前でポーズ'),
	('WaterSpray'      , '霧吹き'),
	('SmellFood'       , '匂いをかぐ'),
	('SwitchSmellFood' , '駆動（匂いをかぐ）'),
)

enum_b0f707938ca8_32e4190d51a4 = (
	('Invalid'   , 'なし'),
	('UpperLeft' , '左上三角'),
	('LowerLeft' , '左下三角'),
	('LowerRight', '右下三角'),
	('UpperRight', '右上三角'),
)

enum_b22a0f29d59e_f465b9e811ce = (
	('Season'     , '季節'),
	('MinorSeries', '裏シリーズ'),
	('Purpose'    , '目的'),
	('None'       , 'なし'),
)

enum_b308e10c72b9_c2aae04b2493 = (
	('0', '1'),
	('1', '2'),
	('2', '3'),
	('3', '4'),
	('4', '5'),
)

enum_b4a495c4cd73_f919b604a1f1 = (
	('None'      , 'なし'),
	('Ftr'       , '家具'),
	('Tool'      , '道具'),
	('Smartphone', 'スマホ'),
)

enum_b4fc6363b59e_18efb227c4c9 = (
	('None'  , 'なし'),
	('Chair' , 'イス'),
	('Bed'   , 'ベッド'),
	('Closet', 'クローゼット'),
	('Chest' , 'タンス'),
)

enum_ba0d1303781b_38e4e433d05a = (
	('Ant'         , 'アリ'),
	('Beetle'      , '甲虫'),
	('Butterfly'   , 'チョウ'),
	('CastOffSkin' , 'セミノヌケガラ'),
	('Cicada'      , 'セミ'),
	('Dragonfly'   , 'トンボ'),
	('Feather'     , '羽'),
	('Firefly'     , 'ホタル'),
	('Flea'        , 'ノミ'),
	('Flower'      , '花の虫'),
	('Fly'         , 'ハエ'),
	('HermitCrab'  , 'ヤドカリ'),
	('HoneyBee'    , 'ミツバチ'),
	('Hornet'      , 'スズメバチ'),
	('Leaf'        , 'コノハムシ'),
	('Locust'      , 'バッタ'),
	('MoleCricket' , 'オケラ'),
	('Mosquito'    , 'カ'),
	('Moth'        , 'ガ'),
	('PillBug'     , 'ダンゴムシ'),
	('Scorpion'    , 'サソリ'),
	('SeaSlater'   , 'フナムシ'),
	('SnowCrystal' , '雪の結晶'),
	('Spider'      , 'クモ'),
	('Stump'       , '切り株'),
	('TigerBeetle' , 'ハンミョウ'),
	('Tumblebug'   , 'フンコロガシ'),
	('WaterBeetle' , 'ゲンゴロウ'),
	('WaterStrider', 'アメンボ'),
	('Wisp'        , '魂'),
	('Petal'       , '花弁'),
	('AutumnLeaf'  , '紅葉'),
)

enum_c1ee150f0e21_f567104db912 = (
	('Male'  , '男性'),
	('Female', '女性'),
)

enum_c247708f9bb1_67b0834c6103 = (
	('None'                , '（なし）'),
	('MileCard'            , 'たぬきマイルカード'),
	('Leaf'                , '葉っぱ'),
	('LeafYellow'          , '葉っぱ：黄'),
	('RoomWall'            , '壁紙'),
	('RoomFloor'           , '床板'),
	('Rug'                 , 'ラグ'),
	('Tops'                , '装：トップス'),
	('Bottoms'             , '装：ボトムス'),
	('Socks'               , '装：くつした'),
	('Shoes'               , '装：くつ'),
	('Cap'                 , '装：ぼうし'),
	('Helmet'              , '装：かぶりもの'),
	('Accessory'           , '装：アクセサリ'),
	('Bag'                 , '装：バッグ'),
	('Umbrella'            , '装：カサ'),
	('FishingRod'          , '道具：つりざお'),
	('Stick'               , '変身ステッキ'),
	('Fence'               , '柵'),
	('TentSet'             , 'テントセット'),
	('HousingKit'          , 'ハウジングキット'),
	('FossilUnknown'       , '化石：未鑑定'),
	('FossilKnown'         , '化石：鑑定済み'),
	('Pitfall'             , 'おとしあなのタネ'),
	('Music'               , 'ミュージック'),
	('Medicine'            , 'おくすり'),
	('RemakeKit'           , 'リメイクキット'),
	('SmartphoneCase'      , 'スマホケース'),
	('Timer'               , 'タイマー'),
	('Honeycomb'           , 'ハチの巣'),
	('Weed'                , '雑草'),
	('Turnip'              , 'カブ'),
	('TurnipExpired'       , 'カブ腐れ'),
	('MessageBottle'       , 'メッセージボトル'),
	('Recipe'              , 'レシピ'),
	('FishBait'            , 'サカナのまきエサ'),
	('AirTicket'           , 'マイル航空券'),
	('TailorTicket'        , 'したてやひきかえけん'),
	('RollanTicket'        , 'ローランひきかえけん'),
	('BellExchangeTicket'  , 'ベルひきかえかん'),
	('PresentBoxRed'       , 'プレゼントBOX赤'),
	('PresentBoxGreen'     , 'プレゼントBOX青'),
	('Insect'              , '生物：ムシかご'),
	('Fish'                , '生物：サカナ'),
	('TrushTire'           , 'ゴミ：タイヤ'),
	('TrushCan'            , 'ゴミ：あきカン'),
	('TrushBoot'           , 'ゴミ：ながぐつ'),
	('Coin'                , 'コイン'),
	('MoneyBag'            , 'ベル袋'),
	('Parts'               , 'ジョニーのパーツ'),
	('PartsDust'           , 'さびたパーツ'),
	('LostQuestPouch'      , '落し物：袋'),
	('LostQuestBook'       , '落し物：本（読み物）'),
	('LostQuestNote'       , '落し物：本（書き物）'),
	('CupCake'             , 'バースデーカップケーキ'),
	('PinataStick'         , 'ピニャータぼう'),
	('Apple'               , 'リンゴ'),
	('Orange'              , 'オレンジ'),
	('Pear'                , 'ナシ'),
	('Peach'               , 'モモ'),
	('Cherry'              , 'サクランボ'),
	('Coconut'             , 'ヤシの実'),
	('Bambooshoot'         , 'タケノコ'),
	('SeedlingOak'         , '広葉樹の苗'),
	('PltOak'              , '広葉樹'),
	('SeedlingCedar'       , '針葉樹の苗'),
	('PltCedar'            , '針葉樹'),
	('PltPalm'             , 'ヤシの木'),
	('PltBamboo'           , '竹'),
	('SeedPaperbag'        , '花の種袋'),
	('Seed'                , '花の種'),
	('DIYBranch'           , 'D：枝'),
	('DIYWoodNormal'       , 'D：木材'),
	('DIYWoodSoft'         , 'D：木材（柔らかい）'),
	('DIYWoodHard'         , 'D：木材（硬い）'),
	('DIYBamboo'           , 'D：竹材'),
	('DIYBambooSpring'     , 'はるのわかたけ'),
	('ShellSummer'         , 'なつのかいがら'),
	('DIYAcorn'            , 'どんぐり'),
	('DIYPinecone'         , 'まつぼっくり'),
	('Sakurapetal'         , 'さくらのはなびら'),
	('AutumnLeaf'          , 'もみじのはっぱ'),
	('SnowCrystalLarge'    , 'ゆきのだいけっしょう'),
	('SnowCrystal'         , 'ゆきのけっしょう'),
	('DIYOrnamentRed'      , 'オーナメントあか'),
	('DIYOrnamentBlue'     , 'オーナメントあお'),
	('DIYOrnamentGold'     , 'オーナメントきん'),
	('MushSplendid'        , 'りっぱなキノコ'),
	('MushRound'           , 'まるいキノコ'),
	('MushSlender'         , 'ほそいキノコ'),
	('MushFlat'            , 'ひらたいキノコ'),
	('MushRare'            , 'めずらしいキノコ'),
	('DIYStone'            , 'D：石'),
	('DIYClay'             , 'D：粘土'),
	('DIYIron'             , 'D：鉄鉱石'),
	('DIYGold'             , 'D：金鉱石'),
	('ShellSnail'          , '貝：巻き貝'),
	('ShellBivalve'        , '貝：二枚貝'),
	('ShellCoral'          , '貝：サンゴ'),
	('SmartPhone'          , 'スマホ'),
	('Paper'               , '紙きれ1まい'),
	('Map'                 , '地図'),
	('GeneralBox'          , '汎用アイコン：箱'),
	('GeneralSack'         , '汎用アイコン：袋'),
	('Starpiece'           , 'ほしのかけら'),
	('StarpieceRare'       , 'ねがいのけっしょう'),
	('StarpieceCapricornus', 'やぎざのかけら'),
	('StarpieceAquarius'   , 'みずがめざのかけら'),
	('StarpiecePisces'     , 'うおざのかけら'),
	('StarpieceAries'      , 'おひつじざのかけら'),
	('StarpieceTaurus'     , 'おうしざのかけら'),
	('StarpieceGemini'     , 'ふたござのかけら'),
	('StarpieceCancer'     , 'かにざのかけら'),
	('StarpieceLeo'        , 'ししざのかけら'),
	('StarpieceVirgo'      , 'おとめざのかけら'),
	('StarpieceLibra'      , 'てんびんざのかけら'),
	('StarpieceScorpio'    , 'さそりざのかけら'),
	('StarpieceSagittarius', 'いてざのかけら'),
	('WPaperYellow'        , 'ラッピングペーパー：イエロー'),
	('WPaperPink'          , 'ラッピングペーパー：ピンク'),
	('WPaperOrange'        , 'ラッピングペーパー：オレンジ'),
	('WPaperLightGreen'    , 'ラッピングペーパー：キミドリ'),
	('WPaperGreen'         , 'ラッピングペーパー：ミドリ'),
	('WPaperMint'          , 'ラッピングペーパー：ミント'),
	('WPaperLightBlue'     , 'ラッピングペーパー：ライトブルー'),
	('WPaperPurple'        , 'ラッピングペーパー：パープル'),
	('WPaperNavy'          , 'ラッピングペーパー：ネイビー'),
	('WPaperBlue'          , 'ラッピングペーパー：ブルー'),
	('WPaperWhite'         , 'ラッピングペーパー：ホワイト'),
	('WPaperRed'           , 'ラッピングペーパー：レッド'),
	('WPaperGold'          , 'ラッピングペーパー：ゴールド'),
	('WPaperBrown'         , 'ラッピングペーパー：ブラウン'),
	('WPaperGray'          , 'ラッピングペーパー：グレー'),
	('WPaperBlack'         , 'ラッピングペーパー：ブラック'),
	('WParcelYellow'       , 'ラッピング袋：イエロー'),
	('WParcelPink'         , 'ラッピング袋：ピンク'),
	('WParcelOrange'       , 'ラッピング袋：オレンジ'),
	('WParcelLightGreen'   , 'ラッピング袋：キミドリ'),
	('WParcelGreen'        , 'ラッピング袋：ミドリ'),
	('WParcelMint'         , 'ラッピング袋：ミント'),
	('WParcelLightBlue'    , 'ラッピング袋：ライトブルー'),
	('WParcelPurple'       , 'ラッピング袋：パープル'),
	('WParcelNavy'         , 'ラッピング袋：ネイビー'),
	('WParcelBlue'         , 'ラッピング袋：ブルー'),
	('WParcelWhite'        , 'ラッピング袋：ホワイト'),
	('WParcelRed'          , 'ラッピング袋：レッド'),
	('WParcelGold'         , 'ラッピング袋：ゴールド'),
	('WParcelBrown'        , 'ラッピング袋：ブラウン'),
	('WParcelGary'         , 'ラッピング袋：グレー'),
	('WParcelBlack'        , 'ラッピング袋：ブラック'),
	('FlwTulip'            , '花：チューリップ'),
	('FlwPansy'            , '花：パンジー'),
	('FlwCosmos'           , '花：コスモス'),
	('FlwRose'             , '花：バラ'),
	('FlwRoseGold'         , '花：バラ金'),
	('FlwLily'             , '花：ユリ'),
	('FlwAnemone'          , '花：アネモネ'),
	('FlwMum'              , '花：キク'),
	('FlwHyacinth'         , '花：ヒヤシンス'),
	('EggGround'           , 'じめんのたまご'),
	('EggRock'             , 'いわのたまご'),
	('EggLeaf'             , 'はっぱのたまご'),
	('EggForest'           , 'もりのたまご'),
	('EggSky'              , 'そらとぶたまご'),
	('EggFish'             , 'サカナのたまご'),
	('MessageBottleEgg'    , 'たまごのメッセージボトル'),
)

enum_c2f1120003e9_c2f1120003e9 = (
	('Default'          , 'Default'),
	('MainField'        , 'MainField'),
	('PlayerHouse'      , 'PlayerHouse'),
	('NpcHouse'         , 'NpcHouse'),
	('MysteryTourIsland', 'MysteryTourIsland'),
	('PhotoStudioIsland', 'PhotoStudioIsland'),
	('PhotoStudioHouse' , 'PhotoStudioHouse'),
)

enum_c3ddc88645a5_d774c8361500 = (
	('DisableAccess'  , '×参照×書き込み'),
	('EnableReadOnly' , '○参照×書き込み'),
	('EnableReadWrite', '○参照○書き込み'),
)

enum_c4b640ed3760_e8e603be0f51 = (
	('Normal'         , '普通'),
	('StoneMaterial'  , '素材岩'),
	('StoneCoin'      , 'コイン岩'),
	('StoneGold'      , 'きんこうせきの岩'),
	('Bamboo'         , '竹とタケノコ'),
	('TreeMoney'      , '小銭つきの木'),
	('TreeSisterFruit', '姉妹フルーツの木'),
	('FlowerRare'     , 'レアな花'),
)

enum_c6e92aae9ffa_253fcc4534a4 = (
	(''                       , '未設定'),
	('FtrTVProgramSandstorm'  , 'サンドストーム'),
	('FtrTVProgramColorbars'  , 'カラーバー'),
	('FtrTVProgramNews1'      , 'ニュース'),
	('FtrTVProgramWeather'    , '天気予報'),
	('FtrTVProgramDrama'      , 'ドラマ'),
	('FtrTVProgramMusic'      , '音楽番組'),
	('FtrTVProgramQuiz'       , 'クイズ'),
	('FtrTVProgramDocumentary', 'ドキュメンタリー'),
	('FtrTVProgramKids'       , '子ども番組'),
	('FtrTVProgramVariety'    , 'バラエティ'),
	('FtrTVProgramMovie'      , '映画'),
	('FtrTVProgramSports'     , 'スポーツ'),
	('FtrTVProgramTalk'       , '対談番組'),
	('FtrTVProgramAnime'      , 'アニメ'),
	('FtrTVProgramCooking'    , '料理番組'),
	('FtrTVProgramExercise'   , 'エクササイズ'),
	('FtrTVProgramCMCar'      , '季節のCM'),
	('FtrTVProgramCMOyatsu'   , 'おやつCM'),
	('FtrTVProgramCMCompany'  , '企業CM'),
	('FtrTVProgramCMFruits'   , 'フルーツCM'),
	('FtrTVProgramCMShopping' , 'ショッピングCM'),
	('FtrTVProgramSecret'     , '？'),
)

enum_cbce559724ee_944b062ad6d6 = (
	('Normal'       , '通常'),
	('ForceOriginal', 'オリジナル強制'),
)

enum_ccc3fdb6f890_062ac98e2307 = (
	('None'         , 'なし'),
	('Outdoor'      , 'アウトドア'),
	('Sea'          , 'うみ'),
	('Office'       , 'オフィス'),
	('Shop'         , 'おみせ'),
	('Music'        , 'おんがく'),
	('School'       , 'がっこう'),
	('Garage'       , 'ガレージ'),
	('Kitchen'      , 'キッチン'),
	('ChildrensRoom', 'こどもべや'),
	('Facility'     , 'しせつ'),
	('Study'        , 'しょさい'),
	('Oriental'     , 'とうようふう'),
	('Party'        , 'パーティー'),
	('BathAndToilet', 'バス・トイレ'),
	('Fitness'      , 'フィットネス'),
	('SnowAndIce'   , 'ごっかん'),
	('Concert'      , 'ライブ'),
	('LivingRoom'   , 'リビング'),
	('Space'        , 'うちゅう'),
	('FolkFcraft'   , 'みんげい'),
	('Horror'       , 'ホラー'),
	('Garden'       , 'にわ'),
	('Rich'         , 'リッチ'),
	('Fancy'        , 'ファンシー'),
)

enum_d15aca83378a_00ef512c69e8 = (
	('N_Stone'      , 'N岩場'),
	('N_Tsunekiti'  , 'Nつねきち'),
	('NW_Stone'     , 'NW岩場'),
	('NE_Stone'     , 'NE岩場'),
	('W_Beach'      , 'W砂浜'),
	('W_UpEnd_Entry', 'W島(上)'),
	('W_DownEnd'    , 'W島(下)'),
	('W_River'      , 'W汽水地'),
	('W_Stone'      , 'W岩場'),
	('W_Promontory' , 'W岬'),
	('E_Beach'      , 'E砂浜'),
	('E_UpEnd_Entry', 'E島(上)'),
	('E_DownEnd'    , 'E島(下)'),
	('E_River'      , 'E汽水地'),
	('E_Stone'      , 'E岩場'),
	('E_Promontory' , 'E岬'),
	('S_Beach'      , 'S砂浜'),
	('S_River'      , 'S汽水地'),
	('S_Airport_L'  , 'S空港(左)'),
	('S_Airport_R'  , 'S空港(右)'),
	('SW_Beach'     , 'SW砂浜'),
	('SW_Jetty'     , 'SW砂浜桟橋'),
	('SE_Beach'     , 'SE砂浜'),
	('SE_Jetty'     , 'SE砂浜桟橋'),
	('OutsideSea'   , '外周海'),
	('S_Isolated'   , 'S離島桟橋'),
	('PhotoStudio'  , '撮影スタジオ'),
	('Dummy'        , 'ダミー'),
)

enum_d1e01a5880ce_45c1b601c21a = (
	('3B_S2', '南中州'),
	('3B_SE', '南東中州'),
	('3B_SW', '南西中州'),
)

enum_d213af309f1d_10d5d2b786dc = (
	('03'         , '橋03'),
	('04'         , '橋04'),
	('05'         , '橋05'),
	('Diagonal025', '斜め橋025'),
	('Diagonal030', '斜め橋030'),
	('Diagonal035', '斜め橋035'),
)

enum_d6b51049aa8c_eb2a552f77d1 = (
	('None'                               , 'なし'),
	('NpcSpTopsSzaTshirtsL'               , 'NpcSpTopsSzaTshirtsL'),
	('NpcSpBottomsRcmApronNS'             , 'NpcSpBottomsRcmApronNS'),
	('PlayerTopsOnepieceSalopetteN'       , 'PlayerTopsOnepieceSalopetteN'),
	('PlayerTopsOnepieceSalopetteH'       , 'PlayerTopsOnepieceSalopetteH'),
	('PlayerTopsOnepieceSalopetteL'       , 'PlayerTopsOnepieceSalopetteL'),
	('PlayerTopsTopPuffH'                 , 'PlayerTopsTopPuffH'),
	('PlayerTopsOnepieceAlinemydesign3dsL', 'PlayerTopsOnepieceAlinemydesign3dsL'),
	('NpcSpTopsRcoTshirtsL'               , 'NpcSpTopsRcoTshirtsL'),
	('NpcSpTopsRcmOuterL'                 , 'NpcSpTopsRcmOuterL'),
	('NpcSpTopsRcmYshirtsH'               , 'NpcSpTopsRcmYshirtsH'),
	('PlayerTopsTopYshirtsmydesignN'      , 'PlayerTopsTopYshirtsmydesignN'),
	('NpcSpTopsRcmYshirtsapronH'          , 'NpcSpTopsRcmYshirtsapronH'),
	('NpcSpTopsSzaYshirtsH'               , 'NpcSpTopsSzaYshirtsH'),
	('NpcSpTopsSzaOuterL'                 , 'NpcSpTopsSzaOuterL'),
	('PlayerTopsOnepieceKimonomydesignL'  , 'PlayerTopsOnepieceKimonomydesignL'),
	('PlayerTopsOnepieceRibmydesignN'     , 'PlayerTopsOnepieceRibmydesignN'),
	('PlayerTopsOnepieceBoxmydesignN'     , 'PlayerTopsOnepieceBoxmydesignN'),
	('PlayerTopsOnepieceDressmydesignL'   , 'PlayerTopsOnepieceDressmydesignL'),
	('PlayerTopsOnepieceBalloonmydesignH' , 'PlayerTopsOnepieceBalloonmydesignH'),
	('PlayerTopsTopCoatmydesignL'         , 'PlayerTopsTopCoatmydesignL'),
	('PlayerTopsTopTshirtsmydesignH'      , 'PlayerTopsTopTshirtsmydesignH'),
	('PlayerTopsTopTshirtsmydesignN'      , 'PlayerTopsTopTshirtsmydesignN'),
	('PlayerTopsTopOutermydesignL'        , 'PlayerTopsTopOutermydesignL'),
	('PlayerTopsOnepieceRobeL'            , 'PlayerTopsOnepieceRobeL'),
	('PlayerTopsTopTshirtsH'              , 'PlayerTopsTopTshirtsH'),
	('PlayerTopsTopOuterL'                , 'PlayerTopsTopOuterL'),
	('PlayerTopsTopCoatL'                 , 'PlayerTopsTopCoatL'),
	('PlayerTopsOnepieceBalloonN'         , 'PlayerTopsOnepieceBalloonN'),
	('PlayerBottomsPantsNormal'           , 'PlayerBottomsPantsNormal'),
	('PlayerTopsTopTshirtsL'              , 'PlayerTopsTopTshirtsL'),
	('PlayerTopsTopTshirtsN'              , 'PlayerTopsTopTshirtsN'),
	('PlayerTopsOnepieceBalloonH'         , 'PlayerTopsOnepieceBalloonH'),
	('PlayerTopsOnepieceBalloonL'         , 'PlayerTopsOnepieceBalloonL'),
	('PlayerTopsOnepieceAlineN'           , 'PlayerTopsOnepieceAlineN'),
	('PlayerTopsOnepieceAlineH'           , 'PlayerTopsOnepieceAlineH'),
	('PlayerTopsOnepieceAlineL'           , 'PlayerTopsOnepieceAlineL'),
	('PlayerTopsOnepieceBoxN'             , 'PlayerTopsOnepieceBoxN'),
	('PlayerTopsOnepieceBoxH'             , 'PlayerTopsOnepieceBoxH'),
	('PlayerTopsOnepieceBoxL'             , 'PlayerTopsOnepieceBoxL'),
	('PlayerTopsTopOuterN'                , 'PlayerTopsTopOuterN'),
	('PlayerTopsTopYshirtsL'              , 'PlayerTopsTopYshirtsL'),
	('PlayerTopsTopYshirtsH'              , 'PlayerTopsTopYshirtsH'),
	('PlayerTopsTopYshirtsN'              , 'PlayerTopsTopYshirtsN'),
	('PlayerTopsTopCoatH'                 , 'PlayerTopsTopCoatH'),
	('PlayerTopsTopCoatN'                 , 'PlayerTopsTopCoatN'),
	('PlayerTopsOnepieceRibN'             , 'PlayerTopsOnepieceRibN'),
	('PlayerTopsOnepieceRibH'             , 'PlayerTopsOnepieceRibH'),
	('PlayerTopsOnepieceRibL'             , 'PlayerTopsOnepieceRibL'),
	('PlayerTopsOnepieceDressN'           , 'PlayerTopsOnepieceDressN'),
	('PlayerTopsOnepieceDressH'           , 'PlayerTopsOnepieceDressH'),
	('PlayerTopsOnepieceDressL'           , 'PlayerTopsOnepieceDressL'),
	('PlayerBottomsSkirtAline'            , 'PlayerBottomsSkirtAline'),
	('PlayerBottomsPantsWide'             , 'PlayerBottomsPantsWide'),
	('PlayerTopsOnepieceOverallN'         , 'PlayerTopsOnepieceOverallN'),
	('PlayerTopsOnepieceOverallH'         , 'PlayerTopsOnepieceOverallH'),
	('PlayerTopsOnepieceOverallL'         , 'PlayerTopsOnepieceOverallL'),
	('PlayerTopsOnepieceAlongN'           , 'PlayerTopsOnepieceAlongN'),
	('PlayerTopsOnepieceAlongH'           , 'PlayerTopsOnepieceAlongH'),
	('PlayerTopsOnepieceAlongL'           , 'PlayerTopsOnepieceAlongL'),
	('PlayerTopsOnepieceBlongN'           , 'PlayerTopsOnepieceBlongN'),
	('PlayerTopsOnepieceBlongH'           , 'PlayerTopsOnepieceBlongH'),
	('PlayerTopsOnepieceBlongL'           , 'PlayerTopsOnepieceBlongL'),
	('PlayerTopsOnepieceKimonoL'          , 'PlayerTopsOnepieceKimonoL'),
	('PlayerBottomsSkirtBox'              , 'PlayerBottomsSkirtBox'),
	('PlayerBottomsSkirtLong'             , 'PlayerBottomsSkirtLong'),
	('PlayerBottomsPantsHalf'             , 'PlayerBottomsPantsHalf'),
	('PlayerBottomsPantsHot'              , 'PlayerBottomsPantsHot'),
	('NpcSpTopsRcoYshirtsH'               , 'NpcSpTopsRcoYshirtsH'),
	('NpcSpBottomsRcoPantsHalf'           , 'NpcSpBottomsRcoPantsHalf'),
	('NpcSpTopsSzaTshirtsH'               , 'NpcSpTopsSzaTshirtsH'),
	('NpcSpBottomsSzaSkirtBox'            , 'NpcSpBottomsSzaSkirtBox'),
	('NpcSpBottomsRcoPantsNormal'         , 'NpcSpBottomsRcoPantsNormal'),
	('NpcSpTopsRcoOuterL'                 , 'NpcSpTopsRcoOuterL'),
	('PlayerTopsOnepieceAlinemydesignH'   , 'PlayerTopsOnepieceAlinemydesignH'),
	('PlayerTopsTopYshirtsmydesignL'      , 'PlayerTopsTopYshirtsmydesignL'),
	('PlayerTopsOnepieceAlinemydesign3dsN', 'PlayerTopsOnepieceAlinemydesign3dsN'),
	('PlayerTopsOnepieceAlinemydesign3dsH', 'PlayerTopsOnepieceAlinemydesign3dsH'),
	('PlayerTopsTopTshirtsmydesign3dsH'   , 'PlayerTopsTopTshirtsmydesign3dsH'),
	('PlayerTopsTopTshirtsmydesign3dsL'   , 'PlayerTopsTopTshirtsmydesign3dsL'),
	('PlayerTopsTopTshirtsmydesign3dsN'   , 'PlayerTopsTopTshirtsmydesign3dsN'),
)

enum_d7d32a028b49_2a813eb9cd7a = (
	('None'                      , 'なし'),
	('Chair'                     , 'イス：通常'),
	('ChairSp'                   , 'イス：SP'),
	('ChairAll'                  , 'イス：丸イス'),
	('ChairFL2Way'               , 'イス：前左2方向'),
	('ChairFB'                   , 'イス：前後'),
	('ChairLeftFB'               , 'イス：前後：左半分'),
	('ChairCenterF'              , 'イス：前：中央のみ'),
	('ChairFLRTouchSwitch'       , 'イス：SP：接触スイッチ'),
	('Bed'                       , 'ベッド：通常'),
	('BedSwitch'                 , 'ベッド：スイッチ'),
	('ChestPull'                 , 'タンス'),
	('ChestSingle'               , 'クローゼット：片開き'),
	('ChestDouble'               , 'クローゼット：両開き'),
	('ChestDoubleCenter'         , 'クローゼット：両開き：中央のみ'),
	('ChestFlip'                 , 'クローゼット：フリップ'),
	('Dresser'                   , 'ドレッサー'),
	('Audio'                     , 'オーディオ'),
	('RandomAudio'               , 'ラジオ'),
	('MusicalInstrument'         , '楽器'),
	('TV'                        , 'テレビ'),
	('Clock'                     , '時計：ノーマル'),
	('ClockPendulum'             , '時計：振り子'),
	('ClockPigeon'               , '時計：ハト'),
	('ClockDigital'              , '時計：デジタル'),
	('ClockSwitch'               , '時計：スイッチ'),
	('WorkBench'                 , '作業台'),
	('LoopAuto'                  , 'ループ'),
	('LoopSwitch'                , 'ループ：スイッチ'),
	('LoopOnOffFade'             , 'ループ：フェード'),
	('LoopTrigger'               , 'ループ：トリガー'),
	('LoopAutoOnOff'             , 'ループ：オンオフ'),
	('LoopTriggerOnOff'          , 'ループ：トリガー：オンオフ'),
	('TriggerOnce'               , 'トリガー'),
	('TriggerOnOff'              , 'トリガー：オンオフ'),
	('TriggerRestart'            , 'トリガー：上書き'),
	('TriggerOnOffAndLoop'       , 'トリガー：toループ オンオフ'),
	('TriggerOnOffAndLoopWaitEnd', 'トリガー：toループ終了待ちオンオフ'),
	('Pass'                      , '通過'),
	('Touch'                     , '接触'),
	('TouchTriggerWaitEndOnKeep' , '接触：ループ終了待ち：トリガー'),
	('GrabHoldLoopWaitEnd'       , '掴みホールド：ループ終了待ちオンオフ'),
	('GrabHold'                  , '掴みホールド'),
	('LightSensorSwitch'         , '外灯（明るさセンサー）'),
	('MailBoxTypeA'              , 'ポスト：タイプA'),
	('MailBoxTypeB'              , 'ポスト：タイプB'),
	('MailBoxTypeC'              , 'ポスト：タイプC'),
	('MailBoxTypeD'              , 'ポスト：タイプD'),
	('MailBoxTypeE'              , 'ポスト：タイプE'),
	('TrashBox'                  , 'ゴミ箱'),
	('SingInsect'                , '鳴くムシ'),
	('MoveBox'                   , '初期支給プレゼントBOX'),
	('MyDesignRug'               , 'マイデザインラグ'),
	('MusicJacket'               , 'ミュージックジャケット'),
	('Bromide'                   , 'ブロマイド'),
)

enum_daac3d573f2d_daac3d573f2d = (
	('99_Dummy'          , '99_Dummy'),
	('00_Ftr'            , '00_Ftr'),
	('01_Art'            , '01_Art'),
	('02_Dishes'         , '02_Dishes'),
	('10_Tops'           , '10_Tops'),
	('11_OnePiece'       , '11_OnePiece'),
	('12_Bottoms'        , '12_Bottoms'),
	('13_Socks'          , '13_Socks'),
	('14_Shoes'          , '14_Shoes'),
	('15_Cap'            , '15_Cap'),
	('16_Accessory'      , '16_Accessory'),
	('17_Helmet'         , '17_Helmet'),
	('18_Bag'            , '18_Bag'),
	('19_Umbrella'       , '19_Umbrella'),
	('20_Tool'           , '20_Tool'),
	('30_Insect'         , '30_Insect'),
	('31_Fish'           , '31_Fish'),
	('33_Shell'          , '33_Shell'),
	('34_Fossil'         , '34_Fossil'),
	('40_Plant'          , '40_Plant'),
	('41_Turnip'         , '41_Turnip'),
	('52_RoomRug'        , '52_RoomRug'),
	('61_HouseDoorDeco'  , '61_HouseDoorDeco'),
	('62_HousePost'      , '62_HousePost'),
	('70_Craft'          , '70_Craft'),
	('80_Etc'            , '80_Etc'),
	('81_Event'          , '81_Event'),
	('82_Music'          , '82_Music'),
	('83_Fence'          , '83_Fence'),
	('90_Money'          , '90_Money'),
	('50_RoomWall'       , '50_RoomWall'),
	('51_RoomFloor'      , '51_RoomFloor'),
	('84_Bromide'        , '84_Bromide'),
	('91_PhotoStudioList', '91_PhotoStudioList'),
	('85_BridgeSlope'    , '85_BridgeSlope'),
	('86_Poster'         , '86_Poster'),
	('36_InsectToy'      , '36_InsectToy'),
	('37_FishToy'        , '37_FishToy'),
)

enum_de3dece1349b_9af5c41bec95 = (
	('AccessoryOneEye'               , 'アクセサリ：片目'),
	('AccessoryMouth'                , 'アクセサリ：口'),
	('AccessoryMouthInvisibleNose'   , 'アクセサリ：口(鼻なし)'),
	('AccessoryMouthEarJaw'          , 'アクセサリ：口耳アゴ'),
	('AccessoryEye'                  , 'アクセサリ：目'),
	('AcceEyeMouth'                  , 'アクセサリ：目/口'),
	('AccessoryEyeMouthInvisibleNose', 'アクセサリ：目/口(鼻なし)'),
	('HeadFace'                      , '頭：お面'),
	('Headgear_HasBang'              , '頭：被り物(前髪あり)'),
	('Headgear_HasEar'               , '頭：被り物(耳あり)'),
	('Headgear_NoEar'                , '頭：被り物(耳なし)'),
	('Headgear_NoEarNoJaw'           , '頭：被り物(耳なし/アゴなし)'),
	('HeadHairOrnament_Front'        , '頭：髪飾り(おでこ)'),
	('HeadHairOrnament_Back'         , '頭：髪飾り(後頭部)'),
	('HeadHairOrnament_Top'          , '頭：髪飾り(頭上)'),
	('HeadHairOrnament_Peak'         , '頭：髪飾り(頂上)'),
	('HeadHairOrnament_Left'         , '頭：髪飾り(左頭)'),
	('HeadHairOrnament_Right'        , '頭：髪飾り(右頭)'),
	('HeadFullFace'                  , '頭：フルフェイス'),
	('HeadCap'                       , '頭：帽子'),
	('BagShoulder'                   , 'カバン：ショルダー'),
	('BagBackpack'                   , 'カバン：バックパック'),
	('ShoesHard'                     , '靴：かたい'),
	('ShoesSlippers'                 , '靴：スリッパ'),
	('ShoesGeta'                     , '靴：げた'),
	('ShoesPumps'                    , '靴：パンプス'),
	('ShoesSoft'                     , '靴：やわらかい'),
	('Socks'                         , '靴下'),
	('Tops'                          , 'トップス'),
	('Onepiece'                      , 'ワンピース'),
	('None'                          , 'なし'),
	('Bottoms'                       , 'ボトムス'),
	('Ocarina'                       , 'オカリナ'),
	('Tambourine'                    , 'タンバリン'),
	('Panpipe'                       , 'パンフルート'),
	('CliffMaker'                    , '崖造成キット'),
	('RiverMaker'                    , '川造成キット'),
	('FenceMaker'                    , '柵造成キット'),
	('GroundMaker'                   , '道造成キット'),
	('Net'                           , 'アミ：下位'),
	('NetMiddleLevel'                , 'アミ：中位'),
	('NetUpperLevel'                 , 'アミ：上位'),
	('Axe'                           , 'オノ：下位'),
	('AxeMiddleLevel'                , 'オノ：中位'),
	('AxeUpperLevel'                 , 'オノ：上位'),
	('AxeDull'                       , '切れないオノ：下位'),
	('AxeDullMiddleLevel'            , '切れないオノ：中位'),
	('Watering'                      , 'ジョウロ：下位'),
	('WateringMiddleLevel'           , 'ジョウロ：中位'),
	('WateringUpperLevel'            , 'ジョウロ：上位'),
	('ScoopHandMade'                 , 'スコップ：てづくり'),
	('Scoop'                         , 'スコップ：下位'),
	('ScoopMiddleLevel'              , 'スコップ：中位'),
	('ScoopUpperLevel'               , 'スコップ：上位'),
	('FishingRod'                    , 'つりざお：下位'),
	('FishingRodMiddleLevel'         , 'つりざお：中位'),
	('FishingRodUpperLevel'          , 'つりざお：上位'),
	('FishingRodAndFloat'            , 'つりざお：一体型'),
	('Slingshot'                     , 'パチンコ：下位'),
	('SlingshotMiddleLevel'          , 'パチンコ：中位'),
	('SlingshotUpperLevel'           , 'パチンコ：上位'),
	('JumpStick'                     , 'ジャンプ棒'),
	('Ladder'                        , 'はしご'),
	('ChangeStick'                   , '変身ステッキ'),
	('PaperFan'                      , 'うちわ'),
	('Umbrella'                      , 'カサ'),
	('Umbrella_NoUseToolCommonAnim'  , 'カサ（自前アニメ）'),
	('Umbrella_NoSound'              , 'カサ_開閉音無し'),
	('Umbrella_Leaf'                 , 'カサ_葉っぱ'),
	('Umbrella_Flower'               , 'カサ_花'),
	('Windmill'                      , 'かざぐるま'),
	('Cracker'                       , 'クラッカー'),
	('SoapBubble'                    , 'シャボン玉'),
	('StickLight'                    , 'スティックライト'),
	('Spanner'                       , 'スパナとかなづち'),
	('SmartPhone'                    , 'スマホ'),
	('Brush'                         , 'はけ'),
	('Fireworks'                     , '手持ち花火'),
	('PinataStick'                   , 'ピニャータ割り棒'),
	('Balloon'                       , 'ふうせん'),
	('Blowouts'                      , 'ふきもどし'),
	('Ice'                           , 'アイス'),
	('Branch'                        , 'えだ'),
	('Hammer'                        , 'かなづち'),
	('Canister'                      , '缶'),
	('Candy'                         , 'キャンディ'),
	('Sprayer'                       , 'きりふき'),
	('FruitBasket'                   , '果物カゴ'),
	('Coffee'                        , 'コーヒー'),
	('Cop'                           , 'コップ'),
	('Sandwich'                      , 'サンドウィッチ'),
	('Sketchbook'                    , 'スケッチブック'),
	('Smoothie'                      , 'スムージー'),
	('Dumbbell'                      , 'ダンベル'),
	('LightDumbbell'                 , 'ダンベル(軽い)'),
	('RcmTourFlag'                   , 'つぶまめツアー旗'),
	('BagHand'                       , '手提げカバン'),
	('CuteBagHand'                   , '手提げかばん(キュート)'),
	('CoolBagHand'                   , '手提げかばん(クール)'),
	('HighBagHand'                   , '手提げかばん(生活度高)'),
	('LowBagHand'                    , '手提げかばん(生活度低)'),
	('Doughnut'                      , 'ドーナッツ'),
	('TkkGuitar'                     , 'とたけけギター'),
	('Duster'                        , 'はたき'),
	('Broom'                         , 'ほうき'),
	('Book'                          , '本'),
	('SmallBook'                     , '本(小)'),
	('Firewood'                      , '薪'),
	('HandLens'                      , '虫眼鏡'),
)

enum_ded670ccf8f3_2f430bbb6124 = (
	('NoEffect', 'なし'),
	('Phono'   , 'ちくおんき'),
	('Retro'   , 'レトロ'),
	('Cheap'   , 'チープ'),
	('Hifi'    , 'ハイファイ'),
)

enum_e046ae7fa48d_57a924bf70f4 = (
	('None'             , 'なし'),
	('Kitchen'          , 'キッチン'),
	('Display'          , '上物_飾り'),
	('Food'             , '上物_飲食物'),
	('Insect'           , 'ムシ'),
	('Fish'             , 'サカナ'),
	('WorkStuff'        , '上物_作業用'),
	('Base_Desk'        , '台_机'),
	('Base_Table'       , '台_テーブル'),
	('Base_Display'     , '台_飾り棚'),
	('Base_Sp'          , '台_特殊'),
	('Base_Disable'     , '台_不可'),
	('Utility'          , 'ユーティリティ'),
	('Item_ForBase'     , '上物_原則床置'),
	('Bed'              , 'ベッド'),
	('Chair'            , 'イス・ソファ'),
	('Cushion'          , 'クッション'),
	('Closet'           , '収納'),
	('MusicalInstrument', '楽器系'),
	('DIYworkbench'     , 'DIY作業台'),
	('Fixed'            , '入替不可'),
)

enum_e7b08d8a83f9_27581a65a7ae = (
	('None'      , 'なし'),
	('RainActive', '雨可'),
)

enum_e88a63f4642d_4d2cf72813b3 = (
	('None'      , 'なし'),
	('Variation1', 'Variation1'),
	('Variation2', 'Variation2'),
	('Variation4', 'Variation4'),
)

enum_ea6867159088_b5057bd5784d = (
	('Pad'     , '肉球'),
	('Circle'  , 'まる'),
	('Oval'    , '長まる'),
	('ThinOval', '細長まる'),
	('Bird'    , 'トリ'),
	('Bird2'   , 'トリ（太）'),
	('Hoof'    , 'ヒヅメ'),
	('None'    , 'なし'),
	('Pumps'   , 'パンプス'),
)

enum_eac1ccc130ff_55f087e18a44 = (
	('None' , '-'),
	('Limit', '限'),
)

enum_eb74bd2dde24_eaeb657f44bf = (
	('None'  , 'なし'),
	('Up'    , '上'),
	('Middle', '中'),
	('Down'  , '下'),
)

enum_effe5979565a_894d134b30b9 = (
	('All'  , '全方位'),
	('Front', '正面'),
	('Back' , '背面'),
)

enum_f18e5565c112_ab0466cfcd5a = (
	('None'       , '無し'),
	('SquareCross', 'SquareCross'),
	('SquareHang' , 'SquareHang'),
	('Arch'       , 'Arch'),
	('Circle'     , 'Circle'),
)

enum_f20a1de8eac2_4485ac08bc53 = (
	('None'               , 'なし'),
	('Bells'              , 'お金'),
	('Turnip'             , 'カブ'),
	('Timer'              , 'タイマー'),
	('LostProperty'       , '落とし物'),
	('Present'            , 'プレゼント'),
	('Fassion'            , 'ファッション'),
	('HandyGoods'         , '手持ち品'),
	('Rug'                , 'ラグ'),
	('Medicine'           , 'おくすり'),
	('Insect'             , 'ムシ'),
	('Fish'               , 'サカナ・海の幸'),
	('HousingKit'         , 'ハウジングキット'),
	('UnknownFossil'      , '未鑑定化石'),
	('FishBait'           , '撒き餌'),
	('SnowCrystal'        , '雪の結晶'),
	('WallPaper'          , '壁紙'),
	('FloorBoard'         , '床板'),
	('TreasureCapsule'    , '宝探しカプセル'),
	('DoorDeco'           , 'ドア飾り'),
	('MessageBottle'      , 'メッセージボトル'),
	('DIYRecipe'          , 'レシピ'),
	('WrappingPaper'      , 'ラッピング'),
	('Fence'              , '柵'),
	('PlantKeepItemWindow', '植えるで持ち物閉じない'),
)

enum_f3c18336bb2d_2196d32cce4c = (
	('PermanentObj'    , '常設オブジェ'),
	('CalendarEvent'   , 'カレンダーイベント'),
	('NpcGroupActivity', 'NPC集団行動'),
	('VisitorNpc'      , '来訪NPC'),
)

enum_f5a85f4bb42c_b173422234a3 = (
	('Ftr'               , '家具'),
	('RoomWall'          , '内装：壁紙'),
	('RoomFloor'         , '内装：床板'),
	('Rug'               , 'ラグ'),
	('RugMyDesign'       , 'ラグマイデザイン'),
	('TopsDefault'       , '装備品：トップスデフォルト'),
	('Tops'              , '装備品：トップス'),
	('OnePiece'          , '装備品：ワンピース'),
	('BottomsDefault'    , '装備品：ボトムスデフォルト'),
	('Bottoms'           , '装備品：ボトムス'),
	('Socks'             , '装備品：くつした'),
	('Shoes'             , '装備品：くつ'),
	('Cap'               , '装備品：ぼうし'),
	('Helmet'            , '装備品：かぶりもの'),
	('Accessory'         , '装備品：アクセサリ'),
	('Bag'               , '装備品：バッグ'),
	('Umbrella'          , '装備品：かさ'),
	('FishingRod'        , '道具：つりざお'),
	('Net'               , '道具：あみ'),
	('Shovel'            , '道具：スコップ'),
	('Axe'               , '道具：オノ'),
	('Watering'          , '道具：じょうろ'),
	('Slingshot'         , '道具：パチンコ'),
	('ChangeStick'       , '道具：変身ステッキ'),
	('WoodenStickTool'   , '道具：川越えツール'),
	('Ladder'            , '道具：ハシゴ'),
	('GroundMaker'       , '道具：道造成キット'),
	('RiverMaker'        , '道具：川造成キット'),
	('CliffMaker'        , '道具：崖造成キット'),
	('PartyPopper'       , 'サブ道具：クラッカー'),
	('Ocarina'           , 'サブ道具：オカリナ'),
	('Panflute'          , 'サブ道具：パンフルート'),
	('Tambourine'        , 'サブ道具：タンバリン'),
	('FierworkHand'      , 'サブ道具：手持ち花火'),
	('StickLight'        , 'サブ道具：スティックライト'),
	('Uchiwa'            , 'サブ道具：うちわ'),
	('BlowBubble'        , 'サブ道具：シャボン玉'),
	('Partyhorn'         , 'サブ道具：ふきもどし'),
	('Timer'             , 'タイマー'),
	('TreeSeedling'      , '植物：木の苗'),
	('Tree'              , '植物：木'),
	('Vegetable'         , '植物：野菜'),
	('Weed'              , '植物：雑草'),
	('FlowerSeed'        , '植物：花の種'),
	('FlowerBud'         , '植物：花の茎、蕾、株'),
	('Flower'            , '植物：花'),
	('Fruit'             , 'フルーツ'),
	('Mushroom'          , 'キノコ'),
	('Turnip'            , 'カブ'),
	('TurnipExpired'     , 'カブ（くさったカブ）'),
	('FishBait'          , '撒き餌'),
	('PitFallSeed'       , 'おとしあなのタネ'),
	('Medicine'          , 'おくすり'),
	('CraftMaterial'     , '素材：DIY'),
	('CraftRemake'       , '素材：リメイクキット'),
	('Ore'               , '素材：鉱石'),
	('CraftPhoneCase'    , '素材：スマホケース'),
	('Honeycomb'         , 'ハチの巣'),
	('Trash'             , 'ゴミ'),
	('SnowCrystal'       , '雪の結晶'),
	('AutumnLeaf'        , '紅葉'),
	('Sakurapetal'       , '桜の花びら'),
	('XmasDeco'          , 'クリスマスオーナメント'),
	('StarPiece'         , '星のかけら'),
	('Insect'            , '生き物：ムシ'),
	('Fish'              , '生き物：サカナ'),
	('ShellDrift'        , '漂着貝'),
	('ShellFish'         , '生き物：潮干狩り貝'),
	('FishToy'           , 'サカナ模型'),
	('InsectToy'         , 'ムシ模型'),
	('Fossil'            , '化石'),
	('FossilUnknown'     , '化石（未鑑定）'),
	('Music'             , 'ミュージック'),
	('MusicMiss'         , 'ミュージック(入手不可)'),
	('Bromide'           , 'ブロマイド'),
	('Poster'            , 'ポスター'),
	('HousePost'         , '家パーツポスト'),
	('DoorDeco'          , 'ドア飾り'),
	('Fence'             , '柵'),
	('DummyRecipe'       , '陳列用：レシピブック'),
	('DummyDIYRecipe'    , '陳列用：単品DIYレシピ'),
	('DummyHowtoBook'    , '陳列用：ハウツー本'),
	('LicenseItem'       , '陳列用：工事ライセンス'),
	('BridgeItem'        , '陳列用：橋'),
	('SlopeItem'         , '陳列用：坂'),
	('DIYRecipe'         , 'DIYレシピ'),
	('MessageBottle'     , 'メッセージボトル'),
	('WrappingPaper'     , 'ラッピングペーパー'),
	('HousingKit'        , 'ハウジングキット'),
	('HousingKitRcoQuest', 'ハウジングキット：移住クエスト'),
	('HousingKitBirdge'  , 'ハウジングキット：橋用'),
	('Money'             , 'ベル（お金）'),
	('BdayCupcake'       , 'バースデーカップケーキ'),
	('YutaroWisp'        , 'ゆうたろうのたましい'),
	('JohnnyQuest'       , 'ジョニークエスト'),
	('JohnnyQuestDust'   , 'ジョニークエストごみ'),
	('QuestWrapping'     , 'クエスト配達プレゼントBOX'),
	('LostQuest'         , 'おとしもの'),
	('LostQuestDust'     , 'おとしものゴミ'),
	('TailorTicket'      , '仕立て屋クーポン'),
	('TreasureQuest'     , '宝探しカプセル'),
	('TreasureQuestDust' , '宝探しカプセルごみ'),
	('MilePlaneTicket'   , 'マイル航空券'),
	('RollanTicket'      , 'ローラン引換券'),
	('EasterEgg'         , 'イースターのたまご'),
	('Giftbox'           , '初期支給プレゼントBOX'),
	('PinataStick'       , '装備専用：ピニャータ割り棒'),
	('NpcOutfit'         , '装備品：NPC専用'),
	('PlayerDemoOutfit'  , '装備品：プレイヤ演出専用'),
	('SmartPhone'        , 'スマホ'),
	('DummyFtr'          , 'ダミー家具'),
	('SequenceOnly'      , 'シーケンス専用'),
	('MyDesignObject'    , 'マイデザインオブジェクト'),
	('MyDesignTexture'   , 'マイデザインテクスチャ'),
	('None'              , 'なし'),
	('DummyWrapping'     , 'ダミーラッピング済アイテム'),
	('DummyPresentbox'   , 'ダミープレゼントBOX'),
	('DummyCardboard'    , 'ダミーダンボール入りアイテム'),
	('EventObjFtr'       , 'イベントオブジェ家具'),
	('NnpcRoomMarker'    , 'NPC部屋マーカー'),
	('PhotoStudioList'   , '撮影スタジオ用アイテム'),
)

enum_f659111fbd89_a8479914e95b = (
	('None'       , 'なし'),
	('C_Normal'   , '帽子・普通'),
	('C_Brim'     , '帽子・つば(横)'),
	('C_BrimUnder', '帽子・つば(横下)'),
	('C_Bandana'  , '帽子・バンダナ'),
	('C_Knit'     , '帽子・ニット帽'),
	('C_Mask'     , '帽子・おめん'),
	('C_Crown'    , '帽子・わっか'),
	('C_Forehead' , '帽子・おでこ'),
	('C_Top'      , '帽子・後頭部'),
	('C_LeftBig'  , '帽子・左(大)'),
	('C_Left'     , '帽子・左'),
	('C_Right'    , '帽子・右'),
	('G_Normal'   , 'メガネ・普通'),
	('G_Down'     , 'メガネ・普通(下)'),
	('G_UP'       , 'メガネ・普通(上)'),
	('G_Fit'      , 'メガネ・近い(強)'),
	('G_FitLittle', 'メガネ・近い(弱)'),
	('G_Left'     , 'メガネ・片目(左)'),
	('G_Beard'    , 'メガネ・ひげメガネ'),
)

enum_f6bb6e7f3141_66cb3d119f1c = (
	('IdrMuseumFish_0'  , '[サカナ]沿岸の部屋'),
	('IdrMuseumFish_1'  , '[サカナ]沖と深海の部屋'),
	('IdrMuseumFish_2'  , '[サカナ]淡水の部屋'),
	('IdrMuseumInsect_0', '[ムシ]大温室'),
	('IdrMuseumInsect_1', '[ムシ]バタフライガーデン'),
	('IdrMuseumInsect_2', '[ムシ]ラボ'),
	('IdrMuseumFossil_0', '[かせき]古生代の部屋'),
	('IdrMuseumFossil_1', '[かせき]中生代の部屋'),
	('IdrMuseumFossil_2', '[かせき]新生代の部屋'),
)

enum_f924f1356c8c_64c17a17e85b = (
	('Bamboo'     , 'はるのわかたけ'),
	('SakuraPetal', 'さくらのはなびら'),
	('Shell'      , 'なつのかいがら'),
	('Nut'        , 'どんぐり・まつぼっくり'),
	('Mushroom'   , 'きのこ'),
	('Maple'      , 'もみじ'),
	('XmasDeco'   , 'クリスマスオーナメント'),
	('SnowCrystal', 'ゆきのけっしょう'),
)

class AITag(Row):
	AITagCategory = Enum(0xa8eacf70, enum_b22a0f29d59e_f465b9e811ce)
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class AmiiboData(Row):
	CharacterId = U32(0xc7ad2fdf)
	SpNpcCloth = S16(0xf6b34c16)
	NumberingId = U16(0x04a47035)
	NpcType = U8(0x81a43e76)
	NfpType = U8(0xac4a3345)
	NpcLabel = String(0x34c8eed5) # string8
	SeriesId = U8(0x5b7ca0b2)
	Reaction = U8(0xdca79149)
	Studio = U8(0x1d99c513) # size is 4, could this be an array?

class BgmPropertyControlParam(Row):
	UniqueID = U16(0x54706054)
	Value = U16(0x46c45907)
	PropertyID = U16(0x4e46c669)
	Name = String(0x85cf1615) # string128

class BgmPropertyParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x13ab5198) # string64

class CalendarEventParam(Row):
	_8c2aec6a = Enum(0x8c2aec6a, enum_322263f6b5a3_7a83210f041c)
	EventType = Enum(0x70703269, enum_7797cc9a6dbe_5f875c1a6730)
	_52c75c1e = Enum(0x52c75c1e, enum_322263f6b5a3_7a83210f041c)
	UniqueID = U16(0x54706054)
	Month2041 = U8(0x12ed4e02)
	NameShort = String(0x3c835e2c) # string128
	NameLong = String(0x1144c9a1) # string128
	EventBegin = U8(0x8d58a3bf)
	EventHalf = S8(0xac69956e)
	EventEnd = S8(0x73a932ae)
	NpcBegin = U8(0xd605c40d)
	NpcEnd = U8(0x69834ab9)
	LabelLong = String(0x443c0fb7) # string64
	WeatherPattern = String(0x062ec6cf) # string32
	Announce = U8(0x32c643e6)
	RegionJp = U8(0xff468c5f)
	RegionUs = U8(0x0f4323e2)
	RegionEu = U8(0x4ac8ebbc)
	RegionAsia = U8(0xfe807868)
	MsgFile = String(0xa425d8a5) # string64
	TalkFlowName = String(0xc6ddbf67) # string64
	_b92288a3 = U8(0xb92288a3)
	ReadyDays = U8(0xba007e4f)
	MainDays = U8(0xc17c7ca8)
	BbsDays = U8(0x952cf32e)
	BoardDesign = U8(0xceb81aff)
	Output = U8(0x87ff95cc)
	WeekNorth = U8(0x4c8935ec)
	WdayNorth = U8(0x06da20a1)
	MonthNorth = U8(0x026c5579)
	DayNorth = U8(0xd8f76b76)
	WeekSouth = U8(0xb63221ae)
	WdaySouth = U8(0xfc6134e3)
	MonthSouth = U8(0xf8d7413b)
	DaySouth = U8(0x224c7f34)
	Month2000 = U8(0x5fd18fa7)
	Day2000 = U8(0xa45750cc)
	Month2001 = U8(0xe76de8c2)
	Day2001 = U8(0x1ceb37a9)
	Month2002 = U8(0xf5d8472c)
	Day2002 = U8(0x0e5e9847)
	Month2003 = U8(0x4d642049)
	Day2003 = U8(0xb6e2ff22)
	Month2004 = U8(0xd0b318f0)
	Day2004 = U8(0x2b35c79b)
	Month2005 = U8(0x680f7f95)
	Day2005 = U8(0x9389a0fe)
	Month2006 = U8(0x7abad07b)
	Day2006 = U8(0x813c0f10)
	Month2007 = U8(0xc206b71e)
	Day2007 = U8(0x39806875)
	Month2008 = U8(0x9a65a748)
	Day2008 = U8(0x61e37823)
	Month2009 = U8(0x22d9c02d)
	Day2009 = U8(0xd95f1f46)
	Month2010 = U8(0x62b1a617)
	Day2010 = U8(0x9937797c)
	Month2011 = U8(0xda0dc172)
	Day2011 = U8(0x218b1e19)
	Month2012 = U8(0xc8b86e9c)
	Day2012 = U8(0x333eb1f7)
	Month2013 = U8(0x700409f9)
	Day2013 = U8(0x8b82d692)
	Month2014 = U8(0xedd33140)
	Day2014 = U8(0x1655ee2b)
	Month2015 = U8(0x556f5625)
	Day2015 = U8(0xaee9894e)
	Month2016 = U8(0x47daf9cb)
	Day2016 = U8(0xbc5c26a0)
	Month2017 = U8(0xff669eae)
	Day2017 = U8(0x04e041c5)
	Month2018 = U8(0xa7058ef8)
	Day2018 = U8(0x5c835193)
	Month2019 = U8(0x1fb9e99d)
	Day2019 = U8(0xe43f36f6)
	Month2020 = U8(0x2511dcc7)
	Day2020 = U8(0xde9703ac)
	Month2021 = U8(0x9dadbba2)
	Day2021 = U8(0x662b64c9)
	Month2022 = U8(0x8f18144c)
	Day2022 = U8(0x749ecb27)
	Month2023 = U8(0x37a47329)
	Day2023 = U8(0xcc22ac42)
	Month2024 = U8(0xaa734b90)
	Day2024 = U8(0x51f594fb)
	Month2025 = U8(0x12cf2cf5)
	Day2025 = U8(0xe949f39e)
	Month2026 = U8(0x007a831b)
	Day2026 = U8(0xfbfc5c70)
	Month2027 = U8(0xb8c6e47e)
	Day2027 = U8(0x43403b15)
	Month2028 = U8(0xe0a5f428)
	Day2028 = U8(0x1b232b43)
	Month2029 = U8(0x5819934d)
	Day2029 = U8(0xa39f4c26)
	Month2030 = U8(0x1871f577)
	Day2030 = U8(0xe3f72a1c)
	Month2031 = U8(0xa0cd9212)
	Day2031 = U8(0x5b4b4d79)
	Month2032 = U8(0xb2783dfc)
	Day2032 = U8(0x49fee297)
	Month2033 = U8(0x0ac45a99)
	Day2033 = U8(0xf14285f2)
	Month2034 = U8(0x97136220)
	Day2034 = U8(0x6c95bd4b)
	Month2035 = U8(0x2faf0545)
	Day2035 = U8(0xd429da2e)
	Month2036 = U8(0x3d1aaaab)
	Day2036 = U8(0xc69c75c0)
	Month2037 = U8(0x85a6cdce)
	Day2037 = U8(0x7e2012a5)
	Month2038 = U8(0xddc5dd98)
	Day2038 = U8(0x264302f3)
	Month2039 = U8(0x6579bafd)
	Day2039 = U8(0x9eff6596)
	Month2040 = U8(0xaa512967)
	Day2040 = U8(0x51d7f60c)
	LabelShort = String(0xbb66edcb) # string128
	Day2041 = U8(0xe96b9169)
	Month2042 = U8(0x0058e1ec)
	Day2042 = U8(0xfbde3e87)
	Month2043 = U8(0xb8e48689)
	Day2043 = U8(0x436259e2)
	Month2044 = U8(0x2533be30)
	Day2044 = U8(0xdeb5615b)
	Month2045 = U8(0x9d8fd955)
	Day2045 = U8(0x6609063e)
	Month2046 = U8(0x8f3a76bb)
	Day2046 = U8(0x74bca9d0)
	Month2047 = U8(0x378611de)
	Day2047 = U8(0xcc00ceb5)
	Month2048 = U8(0x6fe50188)
	Day2048 = U8(0x9463dee3)
	Month2049 = U8(0xd75966ed)
	Day2049 = U8(0x2cdfb986)
	Month2050 = U8(0x973100d7)
	Day2050 = U8(0x6cb7dfbc)
	Month2051 = U8(0x2f8d67b2)
	Day2051 = U8(0xd40bb8d9)
	Month2052 = U8(0x3d38c85c)
	Day2052 = U8(0xc6be1737)
	Month2053 = U8(0x8584af39)
	Day2053 = U8(0x7e027052)
	Month2054 = U8(0x18539780)
	Day2054 = U8(0xe3d548eb)
	Month2055 = U8(0xa0eff0e5)
	Day2055 = U8(0x5b692f8e)
	Month2056 = U8(0xb25a5f0b)
	Day2056 = U8(0x49dc8060)
	Month2057 = U8(0x0ae6386e)
	Day2057 = U8(0xf160e705)
	Month2058 = U8(0x52852838)
	Day2058 = U8(0xa903f753)
	Month2059 = U8(0xea394f5d)
	Day2059 = U8(0x11bf9036)
	Month2060 = U8(0xd0917a07)
	Day2060 = U8(0x2b17a56c)

class CharaMakeCheekTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x977adfce) # string32
	TexName = String(0xc05200e1) # string32

class CharaMakeEyeColorParam(Row):
	BaseColorB = Float(0x68bed0ef)
	BaseColorG = Float(0xa05e5f9f)
	BaseColorR = Float(0x085e476d)
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class CharaMakeEyeTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x977adfce) # string32
	ResName = String(0xdcfb52e8) # string32
	StungResName = String(0xdfa56cb9) # string32

class CharaMakeHairColorParam(Row):
	HighlightColorB = Float(0x16c95acc)
	HighlightColorG = Float(0xde29d5bc)
	HighlightColorR = Float(0x7629cd4e)
	BaseColorR = Float(0x085e476d)
	BaseColorB = Float(0x68bed0ef)
	BaseColorG = Float(0xa05e5f9f)
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class CharaMakeHairStyleParam(Row):
	PeakRotateOffsetZ = Float(0x5d966107)
	PeakRotateOffsetY = Float(0x1a361bd7)
	PeakRotateOffsetX = Float(0x27563267)
	PeakTransOffsetZ = Float(0x3a1f9e56)
	PeakTransOffsetY = Float(0x7dbfe486)
	PeakTransOffsetX = Float(0x40dfcd36)
	FrontRotateOffsetZ = Float(0xb35e860e)
	BackTransOffsetX = Float(0x866b76fe)
	BackTransOffsetY = Float(0xbb0b5f4e)
	BackTransOffsetZ = Float(0xfcab259e)
	BackRotateOffsetX = Float(0xb22fcc5e)
	BackRotateOffsetY = Float(0x8f4fe5ee)
	BackRotateOffsetZ = Float(0xc8ef9f3e)
	TopTransOffsetX = Float(0x19eec64f)
	TopTransOffsetY = Float(0x248eefff)
	TopTransOffsetZ = Float(0x632e952f)
	TopRotateOffsetX = Float(0x0ed6caf4)
	TopRotateOffsetY = Float(0x33b6e344)
	TopRotateOffsetZ = Float(0x74169994)
	LeftTransOffsetX = Float(0x43d2fb34)
	LeftTransOffsetY = Float(0x7eb2d284)
	FrontRotateOffsetY = Float(0xf4fefcde)
	LeftRotateOffsetX = Float(0xc95b5e7d)
	LeftRotateOffsetY = Float(0xf43b77cd)
	LeftRotateOffsetZ = Float(0xb39b0d1d)
	RightTransOffsetX = Float(0x0a2d6f3e)
	RightTransOffsetY = Float(0x374d468e)
	RightTransOffsetZ = Float(0x70ed3c5e)
	RightRotateOffsetX = Float(0x29c748f7)
	RightRotateOffsetY = Float(0x14a76147)
	RightRotateOffsetZ = Float(0x53071b97)
	FrontTransOffsetX = Float(0x8659e834)
	FrontTransOffsetY = Float(0xbb39c184)
	FrontTransOffsetZ = Float(0xfc99bb54)
	FrontRotateOffsetX = Float(0xc99ed56e)
	LeftTransOffsetZ = Float(0x3912a854)
	UniqueID = U16(0x54706054)
	ResName = String(0xdcfb52e8) # string32
	CapResName = String(0x683b0a91) # string32
	InvisibleEarR = U8(0xd1b1b453)
	Label = String(0x87bf00e8) # string32
	Name = String(0x977adfce) # string32
	InvisibleEarL = U8(0x617794ff)

class CharaMakeMouthTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x977adfce) # string32
	ResName = String(0xdcfb52e8) # string32

class CharaMakeNoseTypeParam(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x977adfce) # string32
	NodeName = String(0x3a14deea) # string32

class CharaMakeSkinColorParam(Row):
	CheekOrangeColorB = Float(0xc25cdc73)
	CheekOrangeColorG = Float(0x0abc5303)
	CheekOrangeColorR = Float(0xa2bc4bf1)
	SkinBaseColorR = Float(0x4d4e9d26)
	SkinBaseColorG = Float(0xe54e85d4)
	SkinBaseColorB = Float(0x2dae0aa4)
	SkinEdgeColorR = Float(0x3ab25276)
	CheekPinkColorB = Float(0x384e882c)
	SkinEdgeColorB = Float(0x5a52c5f4)
	CheekPinkColorR = Float(0x58ae1fae)
	CheekPinkColorG = Float(0xf0ae075c)
	SkinEdgeColorG = Float(0x92b24a84)
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class ColEffectAttributeParam(Row):
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32

class ColGroundAttributeParam(Row):
	UniqueID = U16(0x54706054)
	SoundAttribute = U16(0x2e17a0a7)
	EffectAttribute = U16(0x6ab4b6fb)
	ViewSortID = U16(0xb99c565a)
	WaterCheck = U8(0x58da05ed)
	CanBury = U8(0x472724ed)
	_0254bd05 = U8(0x0254bd05)
	DebugName = String(0xab51a3cf) # string32
	PlayerNoEntry = U8(0xe7e965db)
	NpcNoEntry = U8(0x5baf48a0)
	FtrPlace = U8(0x3e78dc38)
	_2e1e45c3 = String(0x2e1e45c3) # size 16
	_bd859433 = String(0xbd859433) # size 16
	Sand = U8(0x9cb82a1e) # size is 2, could this be an array?

class ColSoundAttributeParam(Row):
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32

class DuckingParam(Row):
	UniqueID = U16(0x54706054)
	Name = String(0x85cf1615) # string128

class EventFlagsHouseParam(Row):
	DefaultValue = U32(0x4c24f1cf)
	MaxValue = U32(0x344b17d7)
	UniqueID = U16(0x54706054)
	_fa93f14b = U8(0xfa93f14b)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	_5140e4b4 = U8(0x5140e4b4) # possible string size 1

class EventFlagsLandParam(Row):
	_93f49ec4 = Enum(0x93f49ec4, enum_10c129883403_814d6adbca21)
	MaxValue = U32(0x344b17d7)
	DefaultValue = U32(0x4c24f1cf)
	_fca0adb0 = Enum(0xfca0adb0, enum_c3ddc88645a5_d774c8361500)
	_fdb1f290 = Enum(0xfdb1f290, enum_6375519ed254_5b8e07b717c6)
	UniqueID = U16(0x54706054)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	SendPlayReport = U8(0xe2bff7f5) # size is 2, could this be an array?

class EventFlagsLandTempParam(Row):
	UniqueID = U16(0x54706054)
	MaxValue = U16(0x0110b14c)
	DefaultValue = U16(0x797f5754)
	_4f7333fd = U8(0x4f7333fd)
	_fa93f14b = U8(0xfa93f14b)
	_5140e4b4 = U8(0x5140e4b4)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	_3c7fb88f = U16(0x3c7fb88f)

class EventFlagsLifeSupportAchievementParam(Row):
	WaitFrame = U32(0x5971a42e)
	LifeSupportStamp = Enum(0x95cc0f22, enum_2c27ffe999d6_e4da0c79dac6)
	FlagLand = S32(0x3fe43170)
	MaxValue1 = U32(0xce0933fc)
	MaxValue2 = U32(0x89a9492c)
	MaxValue3 = U32(0xb4c9609c)
	MaxValue4 = U32(0x06e9bc8c)
	MaxValue5 = U32(0x3b89953c)
	FlagPlayer = S32(0x4171a41d)
	Reward1 = U32(0x4e7f3849)
	Reward6 = U32(0xfc5fe459)
	Reward3 = U32(0x34bf6b29)
	Reward4 = U32(0x869fb739)
	Reward5 = U32(0xbbff9e89)
	Reward2 = U32(0x09df4299)
	UniqueID = U16(0x54706054)
	Key = String(0x45f320f2) # string64
	Name = String(0x85cf1615) # string128
	IsSpecial = U8(0x895442dc)
	MaxLevel = U8(0x1be772f0)

class EventFlagsLifeSupportDailyParam(Row):
	WaitFrame = U32(0x5971a42e)
	_b5761610 = Enum(0xb5761610, enum_9601b1ddc20d_b837359c7300)
	AppearValue = U16(0x8792265f)
	GenreID = U16(0x7eabefae)
	UniqueID = U16(0x54706054)
	ItemNameUniqueID = U16(0xc33a894e)
	MsID = U16(0x74f1f060)
	MaxValue = U16(0x0110b14c)
	Reward = U16(0x127ccfd9)
	Weighting = U8(0xf163e8be)
	_fa93f14b = U8(0xfa93f14b)
	Key = String(0x45f320f2) # string64
	CountOtherVillage = U8(0xafb1f366)
	NetPlaySelect = U8(0x60da5fef)
	SpecialSelect = U8(0xe07863ab)
	BonusFive = U8(0x0329d696)
	Name = String(0x85cf1615) # string128

class EventFlagsNpcMemoryParam(Row):
	UniqueID = U16(0x54706054)
	DefaultValue = U8(0xd55938bd)
	Name = String(0x85cf1615) # string128
	_fa93f14b = U8(0xfa93f14b)
	Key = String(0x45f320f2) # string64
	MaxValue = U8(0xbd7682f5)
	_5140e4b4 = U8(0x5140e4b4)
	_5f77b61a = U8(0x5f77b61a)
	_8d401df7 = U8(0x8d401df7)

class EventFlagsNpcSaveParam(Row):
	MaxValue = U32(0x344b17d7)
	DefaultValue = U32(0x4c24f1cf)
	UniqueID = U16(0x54706054)
	Name = String(0x85cf1615) # string128
	_5140e4b4 = U8(0x5140e4b4)
	Key = String(0x45f320f2) # string64
	_fa93f14b = U8(0xfa93f14b)

class EventFlagsNpcTempParam(Row):
	UniqueID = U16(0x54706054)
	MaxValue = U16(0x0110b14c)
	DefaultValue = U16(0x797f5754)
	_fa93f14b = U8(0xfa93f14b)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	_5f77b61a = U8(0x5f77b61a) # possible string size 1
	_8d401df7 = U32(0x8d401df7)

class EventFlagsPlayerActivityParam(Row):
	UniqueID = U16(0x54706054)
	MessageLabel = U16(0x110a7053)
	_e6317726 = U16(0xe6317726)
	_ccd4c25f = U16(0xccd4c25f)
	MaxValue = U16(0x0110b14c)
	_fa93f14b = U8(0xfa93f14b) # possible string size 1
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64

class EventFlagsPlayerParam(Row):
	DefaultValue = U32(0x4c24f1cf)
	MaxValue = U32(0x344b17d7)
	UniqueID = U16(0x54706054)
	_fa93f14b = U8(0xfa93f14b)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	_5140e4b4 = U8(0x5140e4b4)
	_bed25a86 = U8(0xbed25a86)
	SendPlayReport = U8(0xe2bff7f5) # size is 3, could this be an array?

class EventFlagsPlayerTempParam(Row):
	UniqueID = U16(0x54706054)
	MaxValue = U16(0x0110b14c)
	DefaultValue = U16(0x797f5754)
	_fa93f14b = U8(0xfa93f14b)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	_3c7fb88f = U8(0x3c7fb88f)

class EventFlagsPlayerVisitParam(Row):
	UniqueID = U16(0x54706054)
	DefaultValue = U16(0x797f5754)
	MaxValue = U16(0x0110b14c)
	Name = String(0x85cf1615) # string128
	Key = String(0x45f320f2) # string64
	_fa93f14b = U16(0xfa93f14b)

class EventPlazaFtrParam(Row):
	EventFtrSwitch = Enum(0x24726310, enum_917e0a06d70e_917e0a06d70e)
	EventFtrDirection = Enum(0xc150fba5, enum_4547a8a48a03_a84b967e0ad7)
	ItemNameUniqueID = U16(0xc33a894e)
	UniqueID = U16(0x54706054)

class EventPlazaGround(Row):
	UniqueID = U16(0x54706054)
	ModelName = String(0x39b5a93d) # string32

class EventPlazaObjModelParam(Row):
	DemoDistance = Float(0x158a4c61)
	_a9c1118b = Enum(0xa9c1118b, enum_44bd12ada204_11a50a2b435c)
	UniqueID = U16(0x54706054)
	ResourceName = String(0xdf881359) # string32
	FlowFileName = String(0x364c173e) # string32
	NearCulling = U8(0xb418fb3b) # size is 2, could this be an array?

class EventPlazaPlacementParam(Row):
	_24e5b19d = U32(0x24e5b19d)
	_036dd90c = U32(0x036dd90c)
	PlacementKind = Enum(0x65a97fab, enum_5174da149586_78f560476764)
	EventType = Enum(0x70703269, enum_f3c18336bb2d_2196d32cce4c)
	UniqueID = U16(0x54706054)
	EventObjUniqueID = U16(0x26db5137)
	OffsetZ = S16(0x3b94564c)
	OffsetX = S16(0x4154052c)
	EventFtrUniqueID = U16(0x20dd4435)
	NpcSpLabel = String(0x5ba37406) # string32
	PlacementKey = String(0xe2d0ac54) # string32
	CalendarEventKey = String(0x52f0badd) # string32
	VisitorNpcLabel = String(0x7e322ef0) # string32
	_7215b154 = String(0x7215b154) # size 32
	_e6c63c5c = String(0xe6c63c5c) # size 34

class FgFlowerHeredity(Row):
	Kind = Enum(0x9b7aa0a0, enum_282b3f1c6bd6_e34f70824d5a)
	_753336dd = U16(0x753336dd) # possible string size 2
	Name = U16(0x6aa33bf0)
	HeredityD = U8(0xf0fe7aec)
	HeredityC = U8(0x6d294255)
	HeredityB = U8(0xd5952530)
	HeredityA = U8(0xc7208ade)
	DefaultHeredity = U8(0x08d23365) # size is 4, could this be an array?

class FgMainParam(Row):
	Kind = Enum(0x9b7aa0a0, enum_282b3f1c6bd6_e34f70824d5a)
	CollisionHeight = Float(0x0c315945)
	_123efcf1 = Float(0x123efcf1)
	InsectParam = Enum(0x360b721a, enum_80fe2e01edeb_a0944789ee2d)
	UniqueID = U16(0x54706054)
	NutItem = U16(0xbe17c845)
	PicItem = U16(0xb7a46956)
	DigItem = U16(0xf4678f13)
	BuryItem = U16(0x6ac5a6df)
	BuryItem2 = U16(0xd59ff85e)
	BuryItem3 = U16(0xe8ffd1ee)
	GrowupFg = U16(0x2c6a189e)
	EffectAttribute = U16(0x6ab4b6fb)
	SoundAttribute = U16(0x2e17a0a7)
	ChangeFg = U16(0x76e7fe08)
	ModelName = String(0x39b5a93d) # string32
	_a4b2d66d = RawData(0xa4b2d66d, 1)
	Nature = RawData(0x623dc307, 2)
	Grow = U8(0xf5a73337)
	ColorIndex = S8(0x64b8fff8)
	DebugName = String(0x3f45f2bf) # string64
	Label = String(0x87bf00e8) # string32
	ResName = String(0x48ef0398) # string64

class FieldCreateParam(Row):
	PhotoStudioRoomNo = Enum(0x65d009e1, enum_30e2684ee89a_599636c94afd)
	RoomType = Enum(0x897261e3, enum_42f04d307ef8_30984578ef41)
	FactoryType = Enum(0x6654378d, enum_c2f1120003e9_c2f1120003e9)
	ItemLayer = U8(0xaf3beca5)
	StaticField = U8(0x46e8c73e)
	StageName = String(0xd069f90c) # string32

class FieldDistantViewParam(Row):
	UniqueID = U16(0x54706054)
	ResName = String(0xdcfb52e8) # string32

class FieldLandMakingActionParam(Row):
	ActionRange = Enum(0x59485fad, enum_0e2adceecdfa_0e2adceecdfa)
	Layer = Enum(0xef79de0f, enum_784cf9486925_255fffffb8d5)
	SuccessResult = Enum(0x4932f93e, enum_a3c5bfa601e4_a3c5bfa601e4)
	_75fee4b0 = Enum(0x75fee4b0, enum_70471eeaa222_c602c1a479c5)
	MeshEdgeDirType = Enum(0x0bcf172f, enum_5bb07f38004e_feaae8200c31)
	PlaneChangeType = Enum(0xe421a842, enum_60ad9adbd84b_bd137f5ee888)
	FallActionType = Enum(0x281f90a8, enum_6f6d6ff1098e_dbf69e6d0415)
	_7674c4d6 = Enum(0x7674c4d6, enum_62e4c6f51ad1_474f8f35cfdc)
	UpdateParts = U8(0x926d7dd8)
	_f9a37bdc = U8(0xf9a37bdc)
	MainType = U8(0x31450aa2)
	_7c8e7f81 = U8(0x7c8e7f81)

class FieldLandMakingError(Row):
	UniqueID = U16(0x54706054)
	_0b3be609 = U8(0x0b3be609) # possible string size 1
	Label = String(0x69b161c4) # string30
	Name = String(0x04034aa7) # string60
	CliffCreate = U8(0xf8a892fc)
	AsCommand = String(0x7703d2dd) # string50
	EventFlowEntryName = String(0xb92c3183) # string40

class FieldLandMakingRoadKindParam(Row):
	GroundAttributeUniqueID = U16(0x2df085cc)
	InnerType = U8(0xaf88956b)
	MessageLabel = String(0xf68a2366) # string32

class FieldLandMakingUnitModelParam(Row):
	CornerType = Enum(0x9dfa9b39, enum_06495113f123_3d33eb822663)
	_d943e2bd = Enum(0xd943e2bd, enum_4270b8b74b46_c144e90289f3)
	InnerType000 = Enum(0xeb4430c7, enum_717e8e90873e_eb9d94566e11)
	TriangleType = Enum(0x59d78633, enum_b0f707938ca8_32e4190d51a4)
	EdgePatternType = Enum(0x0d54d810, enum_e88a63f4642d_4d2cf72813b3)
	StepLevel = Enum(0xc7f82afd, enum_2a04dcc2be18_4ae6d2210ecb)
	ModelType = Enum(0xc01e47a7, enum_555bb220c90f_a5afdf39ebc3)
	UniqueID = U16(0x54706054)
	Variation = U16(0xc733aa77)
	InnerType130 = U8(0xcc1cafc4)
	InnerType002 = U8(0xeae9ce3a)
	InnerType012 = U8(0xd789e78a)
	InnerType022 = U8(0x90299d5a)
	InnerType032 = U8(0xad49b4ea)
	InnerType003 = U8(0x5255a95f)
	InnerType013 = U8(0x6f3580ef)
	InnerType023 = U8(0x2895fa3f)
	InnerType033 = U8(0x15f5d38f)
	InnerType100 = U8(0x8bbcd514)
	InnerType110 = U8(0xb6dcfca4)
	InnerType120 = U8(0xf17c8674)
	InnerType031 = U8(0xbffc1b04)
	InnerType101 = U8(0x3300b271)
	InnerType111 = U8(0x0e609bc1)
	InnerType121 = U8(0x49c0e111)
	InnerType131 = U8(0x74a0c8a1)
	InnerType102 = U8(0x21b51d9f)
	InnerType112 = U8(0x1cd5342f)
	InnerType122 = U8(0x5b754eff)
	InnerType132 = U8(0x6615674f)
	InnerType103 = U8(0x99097afa)
	InnerType113 = U8(0xa469534a)
	InnerType123 = U8(0xe3c9299a)
	InnerType133 = U8(0xdea9002a)
	InnerType021 = U8(0x829c32b4)
	InnerType011 = U8(0xc53c4864)
	InnerType001 = U8(0xf85c61d4)
	InnerType030 = U8(0x07407c61)
	InnerType020 = U8(0x3a2055d1)
	InnerType010 = U8(0x7d802f01)
	ModelName = String(0x39b5a93d) # string32
	FishPoint = S8(0xa4f6da11)

class FieldMainFieldParam(Row):
	UniqueID = U16(0x54706054)
	FieldData = String(0x6e1ac981) # string32
	OutsideTemplateKind = U8(0x948eb946)
	Label = String(0x87bf00e8) # string32
	StructureData = String(0xecffb7c6) # string32
	ItemData = String(0xcad74e4e) # string32

class FieldMysteryTourFieldParam(Row):
	MysteryTourFieldOutside = U32(0xe8fa8b93)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class FieldMysteryTourItemParam(Row):
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class FieldMysteryTourParam(Row):
	ItemPlacementKind = U32(0xdd59b554) # possible string size 4
	UniqueID = U16(0x54706054)
	MysteryTourItemUniqueID = U16(0x7a09986c)
	MysteryTourFieldUniqueID = U16(0x72573f73)
	InsectPattern = S16(0xe23c6453)
	FishPattern = S16(0xb1f384dc)
	SelectWeight = U8(0xd89a0db0) # size is 2, could this be an array?

class FieldOutsideParts(Row):
	ReefType = Enum(0xb5a652fa, enum_69eaeee0564d_950b97c5042a)
	PartsKind = Enum(0x493eed57, enum_d15aca83378a_00ef512c69e8)
	UniqueID = U16(0x54706054)
	ModelName = String(0x39b5a93d) # string32

class FieldOutsideTemplate(Row):
	WindDirection = Enum(0x6971370a, enum_09c40b1f72c1_d8cf6e1a81aa)
	SeaType = Enum(0x714d3f2e, enum_009fa2d460ce_286d6aa2ee6b)
	TemplateKind = Enum(0x29346c33, enum_d1e01a5880ce_45c1b601c21a)
	NWParts = Enum(0xd094759a, enum_d15aca83378a_00ef512c69e8)
	N0Parts = Enum(0x1ed42314, enum_d15aca83378a_00ef512c69e8)
	N1Parts = Enum(0x7bb31852, enum_d15aca83378a_00ef512c69e8)
	N2Parts = Enum(0xd41a5598, enum_d15aca83378a_00ef512c69e8)
	N3Parts = Enum(0xb17d6ede, enum_d15aca83378a_00ef512c69e8)
	N4Parts = Enum(0x5039c84d, enum_d15aca83378a_00ef512c69e8)
	NEParts = Enum(0xfa9ca833, enum_d15aca83378a_00ef512c69e8)
	W0Parts = Enum(0xef18bb10, enum_d15aca83378a_00ef512c69e8)
	W1Parts = Enum(0x8a7f8056, enum_d15aca83378a_00ef512c69e8)
	W2Parts = Enum(0x25d6cd9c, enum_d15aca83378a_00ef512c69e8)
	SEParts = Enum(0x19a9348c, enum_d15aca83378a_00ef512c69e8)
	E0Parts = Enum(0x4038a881, enum_d15aca83378a_00ef512c69e8)
	E1Parts = Enum(0x255f93c7, enum_d15aca83378a_00ef512c69e8)
	E2Parts = Enum(0x8af6de0d, enum_d15aca83378a_00ef512c69e8)
	E3Parts = Enum(0xef91e54b, enum_d15aca83378a_00ef512c69e8)
	SWParts = Enum(0x33a1e925, enum_d15aca83378a_00ef512c69e8)
	S0Parts = Enum(0xfde1bfab, enum_d15aca83378a_00ef512c69e8)
	S1Parts = Enum(0x988684ed, enum_d15aca83378a_00ef512c69e8)
	S2Parts = Enum(0x372fc927, enum_d15aca83378a_00ef512c69e8)
	S3Parts = Enum(0x5248f261, enum_d15aca83378a_00ef512c69e8)
	S4Parts = Enum(0xb30c54f2, enum_d15aca83378a_00ef512c69e8)
	W3Parts = Enum(0x40b1f6da, enum_d15aca83378a_00ef512c69e8)
	UniqueID = U16(0x54706054)
	EnglishName = String(0xdadfa19a) # string32

class FishAppearRiverParam(Row):
	ItemID = U16(0x20cb67bc)
	ProbDecNight = U16(0x9217f8b8)
	ProbJanMorningAndEvening = U16(0x51bcedfa)
	ProbJanDaytime = U16(0xb3f1a70f)
	ProbJanNight = U16(0x3e01d394)
	ProbFebMorningAndEvening = U16(0x0f095b88)
	ProbFebDaytime = U16(0x5cb71135)
	ProbFebNight = U16(0x91ee0d19)
	ProbMarMorningAndEvening = U16(0x2cb125cc)
	ProbMarDaytime = U16(0xdf2eadb2)
	ProbMarNight = U16(0x770b5b7d)
	ProbAprMorningAndEvening = U16(0x0dbbebb5)
	ProbAprDaytime = U16(0x9c4a43c0)
	ProbAprNight = U16(0x1d790df7)
	ProbMayMorningAndEvening = U16(0xac8aae8c)
	ProbMayDaytime = U16(0xaebc09bc)
	ProbMayNight = U16(0x8feba08a)
	ProbJunMorningAndEvening = U16(0x5092ca25)
	ProbJunDaytime = U16(0xc74f6b43)
	ProbDecDaytime = U16(0x267c99f7)
	ProbJulMorningAndEvening = U16(0x7ec203a5)
	ProbJulDaytime = U16(0x2b74f5dc)
	ProbJulNight = U16(0x24dbb4e0)
	ProbAugMorningAndEvening = U16(0x74ea1d73)
	ProbAugDaytime = U16(0x15de6a3f)
	ProbAugNight = U16(0xada9eb19)
	ProbSepMorningAndEvening = U16(0x1fe65c0c)
	ProbSepDaytime = U16(0x5e853057)
	ProbSepNight = U16(0x260ec620)
	ProbOctMorningAndEvening = U16(0x6aed60aa)
	ProbOctDaytime = U16(0xb12179b4)
	ProbOctNight = U16(0xce420c64)
	ProbNovMorningAndEvening = U16(0xc57d2eb8)
	ProbNovDaytime = U16(0x5aafbfa6)
	ProbNovNight = U16(0x5b0802f1)
	ProbDecMorningAndEvening = U16(0xc11af347)
	ProbJunNight = U16(0x202e64dd)
	AppearArea = U8(0x137dd804) # size is 2, could this be an array?

class FishAppearSeaParam(Row):
	ItemID = U16(0x20cb67bc)
	ProbDecNight = U16(0x9217f8b8)
	ProbJanMorningAndEvening = U16(0x51bcedfa)
	ProbJanDaytime = U16(0xb3f1a70f)
	ProbJanNight = U16(0x3e01d394)
	ProbFebMorningAndEvening = U16(0x0f095b88)
	ProbFebDaytime = U16(0x5cb71135)
	ProbFebNight = U16(0x91ee0d19)
	ProbMarMorningAndEvening = U16(0x2cb125cc)
	ProbMarDaytime = U16(0xdf2eadb2)
	ProbMarNight = U16(0x770b5b7d)
	ProbAprMorningAndEvening = U16(0x0dbbebb5)
	ProbAprDaytime = U16(0x9c4a43c0)
	ProbAprNight = U16(0x1d790df7)
	ProbMayMorningAndEvening = U16(0xac8aae8c)
	ProbMayDaytime = U16(0xaebc09bc)
	ProbMayNight = U16(0x8feba08a)
	ProbJunMorningAndEvening = U16(0x5092ca25)
	ProbJunDaytime = U16(0xc74f6b43)
	ProbDecDaytime = U16(0x267c99f7)
	ProbJulMorningAndEvening = U16(0x7ec203a5)
	ProbJulDaytime = U16(0x2b74f5dc)
	ProbJulNight = U16(0x24dbb4e0)
	ProbAugMorningAndEvening = U16(0x74ea1d73)
	ProbAugDaytime = U16(0x15de6a3f)
	ProbAugNight = U16(0xada9eb19)
	ProbSepMorningAndEvening = U16(0x1fe65c0c)
	ProbSepDaytime = U16(0x5e853057)
	ProbSepNight = U16(0x260ec620)
	ProbOctMorningAndEvening = U16(0x6aed60aa)
	ProbOctDaytime = U16(0xb12179b4)
	ProbOctNight = U16(0xce420c64)
	ProbNovMorningAndEvening = U16(0xc57d2eb8)
	ProbNovDaytime = U16(0x5aafbfa6)
	ProbNovNight = U16(0x5b0802f1)
	ProbDecMorningAndEvening = U16(0xc11af347)
	ProbJunNight = U16(0x202e64dd)
	AppearArea = U8(0x137dd804) # size is 2, could this be an array?

class FishBeyQuestParam(Row):
	UniqueID = U16(0x54706054)
	_c44b9674 = U8(0xc44b9674)
	_fb867bc1 = U8(0xfb867bc1)
	_748db6d8 = U32(0x748db6d8)

class FishStatusParam(Row):
	EscapeScale = Float(0xb7c9dd05)
	_4108715d = U32(0x4108715d)
	FishMuseumAction = Enum(0x132dd5b9, enum_01016811d685_37fe72043e75)
	AppearArea = Enum(0x64330cb0, enum_3bcfd82ce180_8ccc4bd385f8)
	AppearType = Enum(0x0de2a3be, enum_7a531090c8c0_d059b6858b92)
	ShadowType = Enum(0xac0ebe24, enum_a28161dd393f_a28161dd393f)
	BuoyLv = Enum(0x770288fd, enum_b308e10c72b9_c2aae04b2493)
	SearchRadius = Enum(0x7ec9ada7, enum_b308e10c72b9_c2aae04b2493)
	UniqueID = U16(0x54706054)
	ItemID = U16(0x20cb67bc)
	ToyItemID = U16(0xdaaf8ba0)
	OpenDonatedNum = U16(0xeac6a012)
	_0e91fc27 = U8(0x0e91fc27)
	DebugName = String(0xab51a3cf) # string32
	Label = String(0x87bf00e8) # string32
	IsCreateBait = U8(0x3dc49bc2)
	_1f875d3d = String(0x1f875d3d) # size 32
	ResNameMuseum = String(0x1c8856db) # string32
	ResName = String(0x48ef0398) # string64

class GmoFootprintParam(Row):
	Sound = Enum(0x0fd26913, enum_63bab5a95741_093e393915f9)
	Effect = Enum(0x6d4bd7da, enum_ea6867159088_b5057bd5784d)
	UniqueID = U16(0x54706054)
	Name = String(0x85cf1615) # string128

class HumanAnimParam(Row):
	LowerSetting = Enum(0x0b69ec1a, enum_7a6babece06f_675c7f6d8dcb)
	UniqueID = U16(0x54706054)
	_2fe593c3 = U16(0x2fe593c3)
	_9f5123d4 = U8(0x9f5123d4)
	_d5217761 = U8(0xd5217761)
	AsCommand = String(0x2c447591) # string65
	Comment = String(0x96ba28fe) # string64
	MoveAs = U8(0x49803457)
	_84761fb6 = U8(0x84761fb6)
	CancelFootprint = U8(0xfc3116b5)
	ToolAsCommand = String(0x26911c10) # string30
	Misc = RawData(0x42ad246a, 3)

class IndoorIdrParam(Row):
	UniqueID = U16(0x54706054)
	FossilObjNum = U16(0x707e79ff)
	DecorationObjNum = U16(0x91b7e30b)
	ResourceName = String(0x4b9c4229) # string64

class IndoorPhotoStudioItemParam(Row):
	Dir = Enum(0xd5a8bf7e, enum_4547a8a48a03_a84b967e0ad7)
	PosX = S16(0x374d00da)
	RoomIndex = S16(0x7d016b27)
	UniqueID = U16(0x54706054)
	ItemID = U16(0x20cb67bc)
	PosZ = S16(0x4d8d53ba)
	ReBody = S16(0xc61c279a)
	ReFabric = S16(0xb5980451) # size is 4, could this be an array?

class InsectAppearParam(Row):
	UniqueID = U16(0x54706054)
	ItemID = U16(0x20cb67bc)
	ProbDecemberNight = U16(0xdd1caee7)
	ProbJanuaryMidnight = U16(0x40104a6c)
	ProbJanuaryMorning = U16(0x93d99c53)
	ProbJanuaryDaytime = U16(0x65270095)
	ProbJanuaryEvening1 = U16(0x600d479e)
	ProbJanuaryEvening2 = U16(0x27ad3d4e)
	ProbJanuaryNight = U16(0x3a737394)
	ProbFebruayMidnight = U16(0x175dfeb2)
	ProbFebruayMorning = U16(0xb6d86727)
	ProbFebruayDaytime = U16(0x4026fbe1)
	ProbFebruayEvening1 = U16(0x3740f340)
	ProbFebruayEvening2 = U16(0x70e08990)
	ProbFebruayNight = U16(0x78a12603)
	ProbMarchMidnight = U16(0xb8117ffd)
	ProbMarchMorning = U16(0xf042648e)
	ProbMarchDaytime = U16(0x06bcf848)
	ProbMarchEvening1 = U16(0x980c720f)
	ProbMarchEvening2 = U16(0xdfac08df)
	ProbMarchNight = U16(0x7c00c111)
	ProbAprilMidnight = U16(0x77c808ae)
	ProbAprilMorning = U16(0x93a0aeb8)
	ProbAprilDaytime = U16(0x655e327e)
	ProbAprilEvening1 = U16(0x57d5055c)
	ProbAprilEvening2 = U16(0x10757f8c)
	ProbAprilNight = U16(0xd420d79d)
	ProbMayMidnight = U16(0x02694909)
	ProbMayMorning = U16(0x5842957a)
	ProbMayDaytime = U16(0xaebc09bc)
	ProbMayEvening1 = U16(0x227444fb)
	ProbMayEvening2 = U16(0x65d43e2b)
	ProbMayNight = U16(0x8feba08a)
	ProbJuneMidnight = U16(0x8027726f)
	ProbJuneMorning = U16(0x1e8d322c)
	ProbJuneDaytime = U16(0xe873aeea)
	ProbJuneEvening1 = U16(0xa03a7f9d)
	ProbJuneEvening2 = U16(0xe79a054d)
	ProbJuneNight = U16(0x2a93682f)
	ProbJulyMidnight = U16(0x4ff4a9e3)
	ProbJulyMorning = U16(0x77c3271a)
	ProbJulyDaytime = U16(0x813dbbdc)
	ProbJulyEvening1 = U16(0x6fe9a411)
	ProbJulyEvening2 = U16(0x2849dec1)
	ProbJulyNight = U16(0x4f6db088)
	ProbAugustMidnight = U16(0xc888bffa)
	ProbAugustMorning = U16(0x0376ec8b)
	ProbAugustDaytime = U16(0xf588704d)
	ProbAugustEvening1 = U16(0xe895b208)
	ProbAugustEvening2 = U16(0xaf35c8d8)
	ProbAugustNight = U16(0x8d40260e)
	ProbSeptemberMidnight = U16(0xc7e37192)
	ProbSeptemberMorning = U16(0x6841b0c2)
	ProbSeptemberDaytime = U16(0x9ebf2c04)
	ProbSeptemberEvening1 = U16(0xe7fe7c60)
	ProbDecemberEvening2 = U16(0x98812c3b)
	ProbSeptemberNight = U16(0x339772b5)
	ProbOctoberMidnight = U16(0xb96c2db5)
	ProbOctoberMorning = U16(0x56612acf)
	ProbOctoberDaytime = U16(0xa09fb609)
	ProbOctoberEvening1 = U16(0x99712047)
	ProbOctoberEvening2 = U16(0xded15a97)
	ProbOctoberNight = U16(0xdac2c157)
	ProbNovemberMidnight = U16(0x1f65ddac)
	ProbNovemberMorning = U16(0xe3c6546a)
	ProbNovemberDaytime = U16(0x1538c8ac)
	ProbNovemberEvening1 = U16(0x3f78d05e)
	ProbNovemberEvening2 = U16(0x78d8aa8e)
	ProbNovemberNight = U16(0x6c66ea56)
	ProbDecemberMidnight = U16(0xff3c5b19)
	ProbDecemberMorning = U16(0x6fa9ff60)
	ProbDecemberDaytime = U16(0x995763a6)
	ProbDecemberEvening1 = U16(0xdf2156eb)
	ProbSeptemberEvening2 = U16(0xa05e06b0)
	AppearArea = U8(0x137dd804) # size is 4, could this be an array?

class InsectBattleParam(Row):
	UniqueID = U16(0x54706054)
	Level = U16(0x36083c78)
	Strength = U8(0x4d9888d3) # size is 4, could this be an array?

class InsectStatusParam(Row):
	AppearArea = Enum(0x64330cb0, enum_3bcfd82ce180_8ccc4bd385f8)
	GetScale = Float(0x27450132)
	WaitScale = Float(0xda0b5c29)
	Kind = Enum(0x9b7aa0a0, enum_ba0d1303781b_38e4e433d05a)
	AppearWeather = Enum(0xa103c985, enum_48fbbb9e63e7_c771014390e5)
	UniqueID = U16(0x54706054)
	ToyItemID = U16(0xdaaf8ba0)
	_5d4ef312 = U16(0x5d4ef312)
	ItemID = U16(0x20cb67bc)
	AppearFg = RawData(0xbace6554, 3)
	Label = String(0x87bf00e8) # string32
	_e4b73f7d = String(0xe4b73f7d) # size 32
	DebugName = String(0x3f45f2bf) # string64
	ResNameField = String(0x11b0b143) # string32
	Property = U8(0x0909f3d4)
	_4c777e9e = String(0x4c777e9e) # size 32

class ItemAct(Row):
	AsName = Enum(0xea6a09cc, enum_156e850c7e27_b09d6477c3b6)
	CategoryName = Enum(0xa0839d12, enum_b4fc6363b59e_18efb227c4c9)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x036e8ebe) # string64
	Collision = U8(0x31cb6b0a) # size is 2, could this be an array?

class ItemClothGroup(Row):
	ItemShopSeasonality = Enum(0xe83c30be, enum_5ba0e3fef915_f4a390fc627b)
	UniqueID = U16(0x54706054)
	ParentItemName = U16(0x65503f9f)
	FashionThemeOutdoor = U8(0x811b386c)
	Name = String(0x036e8ebe) # string64
	FashionThemeParty = U8(0x93ddc6d7)
	FashionThemeSport = U8(0x1e996a76)
	FashionThemeWork = U8(0x8048a3a7)
	FashionThemeRelax = U8(0x0cd7f9c5)
	Label = String(0x13ab5198) # string64
	FashionThemeFairyland = U8(0x47f8f099)
	FashionThemeHorror = U8(0x97eba4fc)
	FashionThemeStage = U8(0x9079071d)
	FashionThemeVacation = U8(0xbaa1115f)
	FashionThemeFomal = U8(0x44718a37)
	FashionThemeDaily = U8(0x52add71d)
	_83ccbe0f = String(0x83ccbe0f) # size 64
	_8d7f40e5 = U8(0x8d7f40e5)

class ItemColor(Row):
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class ItemFilter(Row):
	UniqueID = U16(0x54706054)
	ItemKind15 = U16(0x1ea2c2c4)
	ItemKind14 = U16(0x23c2eb74)
	ItemKind13 = U16(0x91e23764)
	ItemKind1 = U16(0xab9b88d6)
	ItemKind2 = U16(0xec3bf206)
	ItemKind3 = U16(0xd15bdbb6)
	ItemKind4 = U16(0x637b07a6)
	ItemKind5 = U16(0x5e1b2e16)
	ItemKind12 = U16(0xac821ed4)
	ItemKind7 = U16(0x24db7d76)
	ItemKind8 = U16(0xa68beaa7)
	ItemKind9 = U16(0x9bebc317)
	ItemKind10 = U16(0xd6424db4)
	ItemKind11 = U16(0xeb226404)
	ItemKind6 = U16(0x19bb54c6)
	CheckDonation = U8(0xffe069a3)
	ItemNum = S8(0x8771aa09)
	Label = String(0x87bf00e8) # string32

class ItemFrom(Row):
	UniqueID = U16(0x54706054)
	_d62525d0 = U16(0xd62525d0)
	Name = String(0x036e8ebe) # string64
	Label = String(0x87bf00e8) # string32

class ItemKind(Row):
	ItemKindUIType = Enum(0xd606a6c4, enum_f20a1de8eac2_4485ac08bc53)
	_1b936128 = Enum(0x1b936128, enum_56ee1b9c32d0_341e9128ff85)
	ItemRemakeType = Enum(0x6b749e8a, enum_b4a495c4cd73_f919b604a1f1)
	MessageKind = Enum(0x29c41a0d, enum_daac3d573f2d_daac3d573f2d)
	SLinkType = Enum(0x4d655154, enum_a397999fca4b_a59ff2e96b38)
	MultiHoldMaxNum = S16(0x4c9ba961)
	SaveCountMaxNum = U16(0x0ce69142)
	UniqueID = U16(0x54706054)
	CanEat = U8(0x9b433dd5)
	CanSell = U8(0x3d4f3f42)
	CanSellSimple = U8(0xb52fe52e)
	CanPlant = U8(0xd4697ff8)
	CanBury = U8(0x472724ed)
	CanGift = U8(0x06012035)
	CanPut = U8(0x5d389fbf)
	CanFtr = U8(0x90bc0855)
	CanSetCloset = U8(0x1bcd4858)
	CanSetChest = U8(0xdae27694)
	CanSetItem = U8(0x49129b27)
	CanNpcPresent = U8(0x0732bb98)
	CanNpcBirthdayPresent = U8(0x2c1b3b5b)
	_c37a683c = U8(0xc37a683c)
	Label = String(0x87bf00e8) # string32
	_d223f25c = U8(0xd223f25c)
	Name = String(0x036e8ebe) # string64
	CanSetInTrashBox = U8(0xc8a5a762)
	IsCollectAchievement = U8(0xfd3b7c9a)
	CanUsePhotoStudio = U8(0x5218c48c)

class ItemMailAttachCategoryGroup(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x3febc642) # string50
	Name = String(0x036e8ebe) # string64
	_e4361c86 = String(0xe4361c86) # size 540

class ItemMenuIcon(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x036e8ebe) # string64
	ResName = String(0xdcfb52e8) # string32

class ItemNpcFtrActionParam(Row):
	NpcFtrActionHoldTime = S32(0xae63cef0)
	NpcFtrActionInterest = Enum(0xb422539e, enum_aa288b7299e1_ae503b12cd83)
	UniqueID = U16(0x54706054)
	NpcFtrActionTool = U16(0x2ca34410)
	Name = String(0x977adfce) # string32
	NpcFtrActionAsName = String(0x6c6fdb31) # string64
	Label = String(0x87bf00e8) # string32

class ItemNpcOutfitInfo(Row):
	UniqueID = U16(0x54706054)
	Label = String(0x13ab5198) # string64
	Name = String(0x977adfce) # string32
	_e5c221d5 = U8(0xe5c221d5)
	_8e07b21e = U8(0x8e07b21e) # possible string size 1

class ItemNpcRoomReplaceCategory(Row):
	UniqueID = U16(0x54706054)
	CanPutInsect = U8(0xef1f311c)
	CanPutKitchen = U8(0x84432956)
	CanPutDisplay = U8(0x8a647661)
	CanPutFood = U8(0xa604b7cf)
	Label = String(0x87bf00e8) # string32
	CanPutFish = U8(0x9f9b91e9)
	CanPutWorkStuff = U8(0x3594f417)
	CanPutUtility = U8(0xaa4f6b89)
	CanPutForBase = U8(0xb2ac5428) # size is 3, could this be an array?

class ItemNpcTopsForm(Row):
	OuterLNormalScaleMaskA = Float(0x89dfed0e)
	OuterLNormalScaleMaskB = Float(0xce7f97de)
	OuterLNormalScaleMaskG = Float(0x069f18ae)
	TshirtsHNormalScaleMaskR = Float(0xf504bb4c)
	TshirtsHNormalScaleMaskG = Float(0x5d04a3be)
	TshirtsHNormalScaleMaskB = Float(0x95e42cce)
	TshirtsHNormalScaleMaskA = Float(0xd244561e)
	TshirtsLNormalScaleMaskR = Float(0xe7fdbff7)
	TshirtsLNormalScaleMaskG = Float(0x4ffda705)
	TshirtsLNormalScaleMaskB = Float(0x871d2875)
	TshirtsLNormalScaleMaskA = Float(0xc0bd52a5)
	TshirtsNNormalScaleMaskR = Float(0x0339be8a)
	TshirtsNNormalScaleMaskG = Float(0xab39a678)
	TshirtsNNormalScaleMaskB = Float(0x63d92908)
	TshirtsNNormalScaleMaskA = Float(0x247953d8)
	OuterLNormalScaleMaskR = Float(0xae9f005c)
	OnepieceHNormalScaleMaskG = Float(0x20e74524)
	OnepieceHNormalScaleMaskB = Float(0xe807ca54)
	OnepieceHNormalScaleMaskA = Float(0xafa7b084)
	OnepieceLNormalScaleMaskR = Float(0x9a1e596d)
	OnepieceLNormalScaleMaskG = Float(0x321e419f)
	OnepieceLNormalScaleMaskB = Float(0xfafeceef)
	OnepieceLNormalScaleMaskA = Float(0xbd5eb43f)
	OnepieceNNormalScaleMaskR = Float(0x7eda5810)
	OnepieceNNormalScaleMaskG = Float(0xd6da40e2)
	OnepieceNNormalScaleMaskB = Float(0x1e3acf92)
	OnepieceNNormalScaleMaskA = Float(0x599ab542)
	OnepieceHNormalScaleMaskR = Float(0x88e75dd6)
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x2f1b930d) # string8

class ItemOutfitCategory(Row):
	UniqueID = U16(0x54706054)
	Misc = RawData(0x42ad246a, 2)
	Label = String(0x87bf00e8) # string32
	HandToolAsName = String(0x03b7f760) # string32
	_f71bffe7 = String(0xf71bffe7) # size 32
	_1b93daa9 = String(0x1b93daa9) # size 32
	Name = String(0x977adfce) # string32
	ToolRightModelName = String(0x4ec849ec) # string20
	UseToolLeft = U8(0x42739ab0)
	ToolLeftModelName = String(0x6ce1d85c) # string20
	_555442aa = U8(0x555442aa)
	_7eb53ebb = U16(0x7eb53ebb)

class ItemOutfitInfo(Row):
	WallScale = Float(0x9f253177)
	FloorScale = Float(0x5195e4bd)
	RotateOffsetZ = Float(0xc8848b74)
	RotateOffsetY = Float(0x8f24f1a4)
	Category = Enum(0x90466afd, enum_2c1ecb54c4b5_fa9288c80a2d)
	TransOffsetX = Float(0xed7f3cfe)
	TransOffsetY = Float(0xd01f154e)
	TransOffsetZ = Float(0x97bf6f9e)
	RotateOffsetX = Float(0xb244d814)
	UniqueID = U16(0x54706054)
	BreakDamage = U16(0x68db76c2)
	SpecialELink = U8(0x04ac1bea)
	SpecialSLink = U8(0xbe782346)
	Label = String(0x87bf00e8) # string32
	Name = String(0x036e8ebe) # string64
	Storage = RawData(0xc89fb7af, 2)

class ItemParam(Row):
	ItemUICategory = Enum(0x28297660, enum_3b7b05ca4a0a_52b2ca6f0581)
	ItemHHAPart = Enum(0x16a66e06, enum_0ed369abe447_b58ba6b527fb)
	ItemPriorityPlace = Enum(0x510f21dc, enum_a382e5214fd4_31aae64bf1ea)
	ItemKind = Enum(0x5270eb75, enum_f5a85f4bb42c_b173422234a3)
	ItemSize = Enum(0xe06fb090, enum_52e1af9ea232_bc050e1554c9)
	RideHeight = Float(0xb662662c)
	Height = Float(0xc187c516)
	ItemHHASeason = Enum(0x05639ab0, enum_10d294d5ba3c_9f0b7bd1cc21)
	ItemUnitIcon = Enum(0x010d74a6, enum_c247708f9bb1_67b0834c6103)
	ItemMenu = Enum(0x348d7b06, enum_5db8059c5629_f2952caee23e)
	ItemFrom = Enum(0xdb1a2f07, enum_794b88fd5d5e_eaf8e9c36279)
	Price = S32(0x718b024d)
	ItemCatalogType = Enum(0xdaf0238c, enum_064edb92c317_a4705285e5f1)
	ItemOutfitInfo = Enum(0x7724bf93, enum_de3dece1349b_9af5c41bec95)
	ItemAct = Enum(0xf1246e5f, enum_d7d32a028b49_2a813eb9cd7a)
	ItemHHASituation2 = Enum(0xb6bafdfd, enum_ccc3fdb6f890_062ac98e2307)
	CarpetMaterial = S32(0x9c32cf82)
	OutfitSE = Enum(0x041c3234, enum_6adf97f83acf_3609f958a376)
	WallPlaceType = Enum(0xe1bf0894, enum_eb74bd2dde24_eaeb657f44bf)
	Depth = Float(0xf8316716)
	ItemLayout = Enum(0x9dcea17e, enum_478bafec288f_571514e8ca3c)
	_85c63b71 = Float(0x85c63b71)
	ItemNpcFtrWatchType = Enum(0xd9855b4e, enum_effe5979565a_894d134b30b9)
	ItemNpcFtrActionType = Enum(0xaa6a39c6, enum_af770d1cdd34_208c036ec702)
	Seasonality = Enum(0x0e6ca0d4, enum_5ba0e3fef915_f4a390fc627b)
	ItemGender = Enum(0xf80e9fee, enum_046a2d7d535d_d28a72f9a4ec)
	NpcGender = Enum(0x8392798c, enum_046a2d7d535d_d28a72f9a4ec)
	NpcOutfit = Enum(0x60c99a5e, enum_f659111fbd89_a8479914e95b)
	ItemHHASituation1 = Enum(0xa7c79784, enum_ccc3fdb6f890_062ac98e2307)
	ItemHHACategory = Enum(0xf17f8753, enum_79fc030d2ca5_3b8dd86eef4f)
	ItemHHASet = Enum(0x059d1682, enum_41a82db5b173_65380129188a)
	ItemHHATheme = Enum(0xd61205d0, enum_870fe161ccb7_b6b6458365a4)
	ClothGroup = Enum(0x690e3379, enum_2d78bfb5905f_6f798aada062)
	_9ba040c2 = U32(0x9ba040c2)
	_164a5f24 = Enum(0x164a5f24, enum_0571932eb060_3c22bd5c3fdd)
	Color1 = Enum(0xa6b1a7fd, enum_7f4abdaa06e5_875003339aa7)
	Color2 = Enum(0xb7cccd84, enum_7f4abdaa06e5_875003339aa7)
	ItemPlayerTopsBottomsForm = Enum(0x9feb9da6, enum_d6b51049aa8c_eb2a552f77d1)
	DragSE = Enum(0x43507f0d, enum_017c76af34f4_35ed35a1a2a5)
	FossilSet = Enum(0xd7f212ea, enum_3fa655858099_cae6208225e0)
	_0e0acf95 = Enum(0x0e0acf95, enum_6adf97f83acf_3609f958a376)
	LocalWindType = Enum(0x9a3fb47c, enum_4db76367118c_3ca2ed9ace4f)
	_5504464e = Enum(0x5504464e, enum_60d7f7443dea_ced5321a8793)
	AudioPreset = Enum(0x2654be7c, enum_ded670ccf8f3_2f430bbb6124)
	LampType = Enum(0xd65f862b, enum_19d95e13020f_5e46daa0967c)
	ItemNpcReactionGenreType = Enum(0xa812e496, enum_34f1ef8cdbcc_52861a019f72)
	ItemLightColor = Enum(0xa69385c1, enum_41b98234401e_b5f5ba492fa2)
	ItemMailAttachCategory = Enum(0x70e19913, enum_5c6b871e086e_81d76143976e)
	ItemNpcRoomReplaceCategory = Enum(0xead62c46, enum_e046ae7fa48d_57a924bf70f4)
	ItemNpcRoomLayoutLimit = Enum(0xbf80f575, enum_8f4bdb1e73c6_3c4e63ce8503)
	_ba4fd546 = Enum(0xba4fd546, enum_639356d46fa4_639356d46fa4)
	ItemMessageCategory = Enum(0x5032ef59, enum_53801c2056ab_77e4c99ac56b)
	ItemNpcReactionThemeType = Enum(0xeffadab6, enum_a3f2105dc205_cf3454689058)
	ItemHobbyType = Enum(0x7b2fdfc1, enum_07d126e46327_fafea373c976)
	ItemUIFurnitureCategory = Enum(0x8221388c, enum_1dbcb57b21ff_7eb8e52a5bb1)
	ItemRegionFilter = Enum(0xea9fc92a, enum_07500acb2a20_c4ab2d74d5ad)
	_7dcd5be1 = Enum(0x7dcd5be1, enum_07d126e46327_fafea373c976)
	FakeArtConvertId = U16(0xbee071da)
	WallTableId = U16(0x0f9f6747)
	FloorTableId = U16(0xc833b068)
	SlopeTableId = U16(0xbfba247c)
	BridgeTypeId = U16(0x5c1c3044)
	SewingRecipeID = S16(0x88a6501c)
	RemakeID = S16(0xcb5eb33f)
	DiyRecipeID = S16(0xbcf5d17a)
	CookingRecipeID = U16(0xc353ef20)
	_9ec34ed4 = U16(0x9ec34ed4)
	ItemShareTextureUniqueID = U16(0x9bd046a2)
	_02169dc7 = U16(0x02169dc7)
	UniqueID = U16(0x54706054)
	AITagBitRankA = RawData(0xe8c448b2, 4)
	ValidEffect = U8(0x49cc96d0)
	CapturePreset = String(0xfc275e86) # string32
	AITagBitRankC = RawData(0x42cd8039, 4)
	AITagBitRankB = RawData(0xfa71e75c, 4)
	ItemHHADirection = U8(0x3cda3274)
	AITagBitRankS = RawData(0x12d4d7a6, 4)
	IsSwingFtr = U8(0xbea3e8b8)
	_4b97cdab = U8(0x4b97cdab)
	CaptureFtrIcon = U8(0xe65df243)
	CaptureClosetIcon = U8(0xe4697080)
	CaptureDiyIcon = U8(0xe24d9b0e)
	_f179f796 = U8(0xf179f796)
	NpcDefaultSwitch = U8(0xdeb3f8dc)
	DefaultSwitch = U8(0xd862189a)
	HasJmp = U8(0xa4db9685)
	TouchRumble = U8(0x7404ebb3)
	RumbleForEdit = U8(0x86efa036)
	FrontSwitch = U8(0x147e658d)
	ResName = String(0x48ef0398) # string64
	CanNotLookFace = U8(0xfd415a4c)
	Label = String(0x3febc642) # string50
	ItemName = String(0xb8cc232c) # string64
	ItemReleaseVersion = U8(0x805cdabb)

class ItemPlayerInitialOutfitBoyAWParam(Row):
	UniqueID = U16(0x54706054)
	Shoes = U16(0xce827d47)
	Cap = U16(0x291a1b04)
	AcceEye = U16(0x2b57b24a)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	Bottoms = U16(0xcc136eb5)
	AcceMouth = U16(0x9403c267)
	Label = String(0x87bf00e8) # string32

class ItemPlayerInitialOutfitBoySSParam(Row):
	UniqueID = U16(0x54706054)
	Shoes = U16(0xce827d47)
	Cap = U16(0x291a1b04)
	AcceEye = U16(0x2b57b24a)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	Bottoms = U16(0xcc136eb5)
	AcceMouth = U16(0x9403c267)
	Label = String(0x87bf00e8) # string32

class ItemPlayerInitialOutfitGirlAWParam(Row):
	UniqueID = U16(0x54706054)
	Shoes = U16(0xce827d47)
	Cap = U16(0x291a1b04)
	AcceEye = U16(0x2b57b24a)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	Bottoms = U16(0xcc136eb5)
	AcceMouth = U16(0x9403c267)
	Label = String(0x87bf00e8) # string32

class ItemPlayerInitialOutfitGirlSSParam(Row):
	UniqueID = U16(0x54706054)
	Shoes = U16(0xce827d47)
	Cap = U16(0x291a1b04)
	AcceEye = U16(0x2b57b24a)
	Socks = U16(0x39ed7f5a)
	Tops = U16(0x870f1e29)
	Bottoms = U16(0xcc136eb5)
	AcceMouth = U16(0x9403c267)
	Label = String(0x87bf00e8) # string32

class ItemPlayerTopsForm(Row):
	NormalScaleMaskR = Float(0x1e4ff55f)
	NormalScaleMaskA = Float(0x390f180d)
	NormalScaleMaskG = Float(0xb64fedad)
	NormalScaleMaskB = Float(0x7eaf62dd)
	UniqueID = U16(0x54706054)
	NpcSpResName = String(0xdf7ab4c3) # string64
	NpcResName = String(0x4e3ee3de) # string64
	ResName = String(0x48ef0398) # string64
	Label = String(0x13ab5198) # string64
	Name = String(0x036e8ebe) # string64
	TorsoResName = String(0x15d08d9a) # string32

class ItemRemake(Row):
	ItemReFabricType = Enum(0x35917e05, enum_a8722b855893_f7ee7d2a5a4e)
	_c54eaad9 = Enum(0xc54eaad9, enum_41b98234401e_b5f5ba492fa2)
	_924c8d08 = U32(0x924c8d08)
	_0239d7bc = U32(0x0239d7bc) # possible string size 4
	_bbc20c54 = U32(0xbbc20c54) # possible string size 4
	_aabf662d = U32(0xaabf662d) # possible string size 4
	_1344bdc5 = U32(0x1344bdc5) # possible string size 4
	_8845b2df = U32(0x8845b2df) # possible string size 4
	_31be6937 = U32(0x31be6937) # possible string size 4
	_20c3034e = U32(0x20c3034e) # possible string size 4
	_8331e771 = U32(0x8331e771)
	_b0b659fa = U32(0xb0b659fa)
	_094d8212 = U32(0x094d8212)
	_1830e86b = U32(0x1830e86b)
	_a1cb3383 = U32(0xa1cb3383)
	_3aca3c99 = U32(0x3aca3c99)
	_9938d8a6 = U32(0x9938d8a6)
	RemakeKitNum = U16(0x29ecb129)
	ItemUniqueID = U16(0xfd9af1e1)
	UniqueID = U16(0x54706054)
	ReFabricPattern2Color1 = U8(0xe8163031)
	ReBodyPattern7Color0 = U8(0xf944e681)
	ReFabricPattern0VisibleOff = U8(0x62c23ed0)
	ReFabricPattern0Color0 = U8(0x545f8769)
	ReFabricPattern0Color1 = U8(0xece3e00c)
	ReFabricPattern1Color0 = U8(0xbb9dec57)
	ReFabricPattern1Color1 = U8(0x03218b32)
	ReFabricPattern2Color0 = U8(0x50aa5754)
	ReBodyPattern7Color1 = U8(0x41f881e4)
	ReFabricPattern3Color0 = U8(0xbf683c6a)
	ReFabricPattern3Color1 = U8(0x07d45b0f)
	ReFabricPattern4Color0 = U8(0x5db42713)
	ReFabricPattern4Color1 = U8(0xe5084076)
	ReFabricPattern5Color0 = U8(0xb2764c2d)
	ReFabricPattern5Color1 = U8(0x0aca2b48)
	ReFabricPattern6Color0 = U8(0x5941f72e)
	ReFabricPattern6Color1 = U8(0xe1fd904b)
	ReFabricPattern7Color0 = U8(0xb6839c10)
	ReFabricPattern7Color1 = U8(0x0e3ffb75)
	ReBodyPattern6Color1 = U8(0xae3aeada)
	ReBodyPattern6Color0 = U8(0x16868dbf)
	ReBodyPattern5Color1 = U8(0x450d51d9)
	ReBodyPattern5Color0 = U8(0xfdb136bc)
	ReBodyPattern4Color1 = U8(0xaacf3ae7)
	ReBodyPattern4Color0 = U8(0x12735d82)
	ReBodyPattern3Color1 = U8(0x4813219e)
	ReBodyPattern3Color0 = U8(0xf0af46fb)
	ReBodyPattern2Color1 = U8(0xa7d14aa0)
	ReBodyPattern2Color0 = U8(0x1f6d2dc5)
	ReBodyPattern1Color1 = U8(0x4ce6f1a3)
	ReBodyPattern1Color0 = U8(0xf45a96c6)
	ReBodyPattern0Color1 = U8(0xa3249a9d)
	ReBodyPattern0Color0 = U8(0x1b98fdf8)
	ReFabricPatternNum = S8(0x0cb402a3)
	ReBodyPatternNum = S8(0xb0304b0d)
	_d4f43b0b = U16(0xd4f43b0b)

class ItemRemakeCommonPattern(Row):
	Color2 = Enum(0xb7cccd84, enum_7f4abdaa06e5_875003339aa7)
	Color1 = Enum(0xa6b1a7fd, enum_7f4abdaa06e5_875003339aa7)
	SortID = U32(0x8fb1ed85)
	Category = Enum(0x90466afd, enum_1e2429734a5c_ee729020db58)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	TextureResName = String(0x5aebbfb5) # string64

class ItemRemakeCommonPatternCategory(Row):
	SortID = U32(0x8fb1ed85)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class ItemSeasonalityParam(Row):
	UniqueID = U16(0x54706054)
	StartMonthNorth = U16(0xf16b7305)
	StartDayNorth = U16(0x5fad728f)
	EndMonthNorth = U16(0x859c3e3e)
	EndDayNorth = U16(0xa9b28820)
	StartMonthSouth = U16(0x6943e8ad)
	StartDaySouth = U16(0xc785e927)
	EndMonthSouth = U16(0x1db4a596)
	EndDaySouth = U16(0x319a1388) # size is 4, could this be an array?

class ItemShareTexture(Row):
	UniqueID = U16(0x54706054)
	ResName = String(0xdcfb52e8) # string32

class ItemSize(Row):
	_801351e6 = U32(0x801351e6)
	PolygonLimit = U16(0x3cf05708)
	MemoryUnitNum = U16(0x09b64264)
	UniqueID = U16(0x54706054)
	HalfUnitSizeX = U8(0x16b8f524)
	Label = String(0x87bf00e8) # string32
	Name = String(0x977adfce) # string32
	HalfUnitSizeZ = U8(0xbcb13daf)

class ItemStrSort(Row):
	UniqueID = U16(0x54706054)
	StrSortIdJPja = U16(0x8ff6331b)
	StrSortIdUSen = U16(0x68832f05)
	StrSortIdEUen = U16(0x77e82b14)
	StrSortIdEUde = U16(0xcb64c9a0)
	StrSortIdEUfr = U16(0x546c2339)
	StrSortIdUSfr = U16(0x4b072728)
	StrSortIdEUes = U16(0xef987827)
	StrSortIdUSes = U16(0xf0f37c36)
	StrSortIdEUit = U16(0x2a7a644c)
	StrSortIdEUnl = U16(0x67ef88b7)
	StrSortIdEUru = U16(0x7e0bbfa4)
	StrSortIdKRko = U16(0xa0af4f68)
	StrSortIdCNzh = U16(0xa99eaf49)
	StrSortIdTWzh = U16(0x2da64e66) # size is 4, could this be an array?

class ItemUIContextMenu(Row):
	UniqueID = U16(0x54706054)
	Priority = U16(0x200dd382)
	Label = String(0x87bf00e8) # string32
	Name = String(0x036e8ebe) # string64
	MSLabel = String(0x026f0892) # string32
	AutoDisappear = U8(0xf2ce6e17) # size is 4, could this be an array?

class ItemUnitIcon(Row):
	ScaleOffset = Float(0x68460c05)
	UniqueID = U16(0x54706054)
	CatalogItemUniqueID = U16(0xfc86133a)
	ResName = String(0x48ef0398) # string64
	Label = String(0x87bf00e8) # string32
	ColorIndex = S8(0x64b8fff8)
	Name = String(0x036e8ebe) # string64
	ModelName = String(0x39b5a93d) # string32

class LocalizeNameConvertParam(Row):
	UniqueID = U16(0x54706054)
	EUen = U8(0x1f301724)
	LocalizeModel = U8(0x9ff07c89)
	LocalizeTexture = U8(0x086f5f3a)
	LocalizeAnim = U8(0xc70be94f)
	JPja = U8(0x638671f9)
	USen = U8(0xaeb768f7)
	USfr = U8(0xf3d8fa00)
	USes = U8(0x0cc4e7b5)
	BaseName = String(0x50edd045) # string32
	EUfr = U8(0x425f85d3)
	EUes = U8(0xbd439866)
	EUde = U8(0xf551b995)
	EUit = U8(0xe5644dde)
	EUnl = U8(0xc2e9eebe)
	EUru = U8(0x4ae88c28)
	KRko = U8(0x558685c5)
	CNzh = U8(0xd22a8fc9)
	TWzh = U8(0x548a7eda) # size is 2, could this be an array?

class MannequinCoodinate(Row):
	MannequinPose = Enum(0x1c73934d, enum_a55023d0faad_4d2a3ca36fe8)
	Seasonality = U32(0xb44dbf73)
	Cap = U16(0x291a1b04)
	Socks = U16(0x39ed7f5a)
	Shoes = U16(0xce827d47)
	Bottoms = U16(0xcc136eb5)
	AccEye = U16(0x395b7795)
	AccMouth = U16(0x79ad3f84)
	Tops = U16(0x870f1e29)
	UniqueID = U16(0x54706054)

class MaterialType(Row):
	UniqueID = U16(0x54706054)
	SoundAttribute = U16(0x2e17a0a7)
	DebugName = String(0xab51a3cf) # string32

class MessageCardBoardDesignParam(Row):
	UniqueID = U16(0x54706054)
	_84818e10 = U16(0x84818e10) # possible string size 2
	HeadColor = U16(0x32c0c064)
	BodyColor = U16(0x41afe839)
	FootColor = U16(0x57c98e5b)
	PenColor1 = U16(0x990406a9)
	TextLotId = S16(0x5f384120)
	PenColor3 = U16(0xe3c455c9)
	PenColor4 = U16(0x51e489d9)
	BackColor = U16(0xa2fe7f71)
	RuleColor = U16(0x94d6cb5d)
	PenColor2 = U16(0xdea47c79)
	ResourceName = String(0x4b9c4229) # string64

class MessageCardColorParam(Row):
	Color = U32(0xf0cf80ff)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class MessageCardDesignParam(Row):
	UniqueID = U16(0x54706054)
	_ea031e9a = U16(0xea031e9a)
	_d299f964 = U16(0xd299f964)
	HeadColor = U16(0x32c0c064)
	BodyColor = U16(0x41afe839)
	FootColor = U16(0x57c98e5b)
	PenColor1 = U16(0x990406a9)
	PenColor2 = U16(0xdea47c79)
	PenColor3 = U16(0xe3c455c9)
	PenColor4 = U16(0x51e489d9)
	_953983b4 = U16(0x953983b4)
	RuleColor = U16(0x94d6cb5d)
	TextLotId = S16(0x5f384120)
	_84818e10 = U16(0x84818e10) # possible string size 2
	_63a46970 = U16(0x63a46970) # possible string size 2
	_ada3644a = U16(0xada3644a)
	BackColor = U16(0xa2fe7f71)
	SelectableSeason = U8(0xaa738fed)
	UnlockTrigger = U8(0x7a6965c5)
	ResourceName = String(0x4b9c4229) # string64
	Kind = U8(0x24da7ada) # size is 4, could this be an array?

class MessageCardSelectDesign(Row):
	_37571146 = U32(0x37571146)
	DesignSpring2 = U16(0xcb625ad7)
	DesignAlways2 = U16(0xa326fa8c)
	DesignAlways3 = U16(0x9e46d33c)
	DesignAlways4 = U16(0x2c660f2c)
	DesignSpring1 = U16(0x8cc22007)
	DesignAlways1 = U16(0xe486805c)
	DesignSummer1 = U16(0xccc4afcb)
	DesignSummer2 = U16(0x8b64d51b)
	DesignAutumn1 = U16(0xd29880f2)
	DesignAutumn2 = U16(0x9538fa22)
	DesignWinter1 = U16(0x1bf6abea)
	DesignWinter2 = U16(0x5c56d13a)

class MessageCardSelectDesignSp(Row):
	_37571146 = U32(0x37571146)
	DesignSpring2 = U16(0xcb625ad7)
	DesignAlways2 = U16(0xa326fa8c)
	DesignAlways3 = U16(0x9e46d33c)
	DesignAlways4 = U16(0x2c660f2c)
	DesignSpring1 = U16(0x8cc22007)
	DesignAlways1 = U16(0xe486805c)
	DesignSummer1 = U16(0xccc4afcb)
	DesignSummer2 = U16(0x8b64d51b)
	DesignAutumn1 = U16(0xd29880f2)
	DesignAutumn2 = U16(0x9538fa22)
	DesignWinter1 = U16(0x1bf6abea)
	DesignWinter2 = U16(0x5c56d13a)

class MessageCardSelectPresent(Row):
	_37571146 = U32(0x37571146)
	ItemCategory = U32(0x368210c4)
	ItemCategoryGroup = U32(0x128a3d9b)
	_e060d3cd = U16(0xe060d3cd)
	ItemRemakeType = U8(0xc233727b) # size is 2, could this be an array?

class MessageCardSelectPresentSp(Row):
	_37571146 = U32(0x37571146)
	ItemCategory = U32(0x368210c4)
	ItemCategoryGroup = U32(0x128a3d9b)
	_e060d3cd = U16(0xe060d3cd)
	ItemRemakeType = U8(0xc233727b) # size is 2, could this be an array?

class MuseumFossilDonateInfo(Row):
	StageName = Enum(0xbe776e71, enum_f6bb6e7f3141_66cb3d119f1c)
	UniqueID = U16(0x54706054)
	WatchItem = U16(0xb76b7d37)
	ModelID = U16(0xfdeed09c)
	CameraParamName = String(0xb16c3035) # string33

class MuseumNPCLayoutInfo(Row):
	UniqueID = U16(0x54706054)
	WatchPointID = U16(0x4765b463)
	WatchItem = U16(0xb76b7d37)
	ReactionTalkKey = String(0x60e4e478) # string25
	_97be8767 = U32(0x97be8767) # possible string size 4
	BalloonTalkKey = String(0xe9812e07) # string25
	_b434805d = U32(0xb434805d) # possible string size 4

class MuseumNPCSilhouette(Row):
	SilhouettePosZ = Float(0x75e35e54)
	SilhouettePosY = Float(0x32432484)
	MuseumNpcRace = U32(0x110ca7b2)
	SilhouettePosX = Float(0x0f230d34)
	UniqueID = U16(0x54706054)
	SilhouetteName = String(0x7c6429ea) # string65

class MuseumNPCSpotTalk(Row):
	StageName = Enum(0xbe776e71, enum_f6bb6e7f3141_66cb3d119f1c)
	UniqueID = U16(0x54706054)
	SpotTalkName = String(0xb10b6bc8) # string65
	SpotTalkKey = String(0x8e768bd8) # string25
	_9d9b3598 = U32(0x9d9b3598) # possible string size 4

class MuseumNameboardInfo(Row):
	NameboardAngleY = Float(0x2c40799e)
	StageName = Enum(0xbe776e71, enum_f6bb6e7f3141_66cb3d119f1c)
	NameboardPosZ = Float(0xa5f3bd28)
	NameboardPosX = Float(0xdf33ee48)
	NameboardPosY = Float(0xe253c7f8)
	UniqueID = U16(0x54706054)
	DonateItemFifth = U16(0x1ef061dd)
	DonateItemFirst = U16(0x3574933b)
	DonateItemSecond = U16(0x50650a2b)
	DonateItemFourth = U16(0xdfacc347)
	DonateItemThird = U16(0xb58d7541)
	ModelResName = String(0xfad4ff78) # string65

class MuseumWatchPoint(Row):
	_65f8c085 = Float(0x65f8c085)
	_2258ba55 = Float(0x2258ba55)
	WatchPosX = Float(0x2633f2c1)
	WatchPosY = Float(0x1b53db71)
	WatchPosZ = Float(0x5cf3a1a1)
	WatchAngleY = Float(0xd200ffd3)
	StageName = Enum(0xbe776e71, enum_f6bb6e7f3141_66cb3d119f1c)
	SilhouetteID = U32(0x3e884a6d)
	_1f3893e5 = Float(0x1f3893e5)
	_35ac2c17 = Enum(0x35ac2c17, enum_23f7dd8d5dc1_9e5af7814467)
	UniqueID = U16(0x54706054)
	PointName = String(0x85fb9dd5) # string65
	BattlePoint = U8(0x91eaeedd)
	SilhouettePoint = U8(0xf58109f5) # size is 4, could this be an array?

class MysteryTourFieldParam(Row):
	MysteryTourFieldOutside = Enum(0xe8fa8b93, enum_8ffbd0e14173_94fb029812b4)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class MysteryTourFishParam(Row):
	UniqueID = U16(0x54706054)
	TargetShadow = RawData(0xc35f78ed, 2)

class MysteryTourInsectParam(Row):
	UniqueID = U16(0x54706054)
	TargetInsect = RawData(0xd086a528, 14)

class MysteryTourItemParam(Row):
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class MysteryTourParam(Row):
	ItemPlacementKind = Enum(0xdd59b554, enum_c4b640ed3760_e8e603be0f51)
	UniqueID = U16(0x54706054)
	MysteryTourItemUniqueID = U16(0x7a09986c)
	MysteryTourFieldUniqueID = U16(0x72573f73)
	InsectPattern = S16(0xe23c6453)
	FishPattern = S16(0xb1f384dc)
	MustItem0 = U16(0xbc5f2a7b)
	MustItem1 = U16(0x813f03cb)
	_8f2f4bf9 = String(0x8f2f4bf9) # size 32
	_4e5cd9f3 = String(0x4e5cd9f3) # size 32
	_88bd09c2 = String(0x88bd09c2) # size 32
	_7215b154 = String(0x7215b154) # size 32
	SelectWeight = U8(0xd89a0db0) # size is 2, could this be an array?

class NmlNpcParam(Row):
	_e2efe82d = U32(0xe2efe82d)
	_5ef86f1f = U32(0x5ef86f1f)
	NpcLooks = Enum(0x04f52f6a, enum_3db89b93b3c4_1360cab183ed)
	VmPauseType = Enum(0x0e7ab6a6, enum_4608a26bdcad_ba6d01a90298)
	Hobby = Enum(0x9eea1288, enum_a68bce6af69b_92745feba3f9)
	Social = Enum(0xaa4403ea, enum_872b31abf9f9_cc7475a100e8)
	VmRhythmType = Enum(0xdd2d2adc, enum_04c6f73235ef_eb1f48d30352)
	_195815cf = U32(0x195815cf)
	_bea84522 = Enum(0xbea84522, enum_8fe44c9d797f_aa6d915eb9ed)
	_a54f92fd = U32(0xa54f92fd)
	UniqueID = U16(0x54706054)
	Umbrella = U16(0xbb9c816e)
	RainWare = U16(0x1d69405f)
	Tops = U16(0x870f1e29)
	RainHat = U16(0x03200971)
	SmartphoneRemakePattern = U16(0xf8be7f94)
	SmartphoneRemakeCommonPattern = S16(0x57e889b2)
	PosterItemID = S16(0x0f640691)
	BromideItemID = S16(0x71bf253b)
	AccentWall = U16(0x08238405)
	WallType = U16(0xda63a0cc)
	FloorType = U16(0x0b52f5bb)
	_566f1d31 = U8(0x566f1d31)
	Color2 = U8(0x265ef22d)
	Color1 = U8(0x34eb5dc3)
	_e52f0037 = U8(0xe52f0037)
	_42f255d5 = U8(0x42f255d5)
	_21c5bbd6 = U8(0x21c5bbd6)
	NpcColor = U8(0x41977699)
	HelperBoneResName = String(0xc1fb0035) # string64
	SpecialSLink = U8(0xbe782346)
	SpecialELink = U8(0x04ac1bea)
	HavokResName = String(0x4ce98793) # string64
	ResName = String(0x48ef0398) # string64
	BirthMDay = U8(0x919ea52a)
	BirthMonth = U8(0x9456b6a3)
	InitLive = U8(0x454b2adc)
	NpcTalkType = U8(0x33af13e1)
	Label = String(0x2f1b930d) # string8

class NmlNpcRaceParam(Row):
	Label = String(0x2f1b930d) # string8
	AnimeTypeFishingRod = String(0x7c6fde34) # string64
	AnimeTypeNet = String(0xfca98253) # string64
	AnimeTypeWateringCan = String(0x09b714f9) # string64
	AnimeTypeBloom = String(0x9916cf87) # string64
	AnimeTypeFirewood = String(0x55c343c4) # string64
	AnimeTypeSmartPhone = String(0xd06d98dc) # string64
	AnimeTypeBook = String(0x41935ae1) # string64
	AnimeTypeBag = String(0x85e386bb) # string64
	AnimeTypeBasket = String(0xcb358e51) # string64
	AnimeTypeFood = String(0x70216bfa) # string64
	AnimeTypeDrink = String(0x0c98243c) # string64
	AnimeTypeUmbrella = String(0x5e2aa87d) # string64
	AnimeTypeSitDown = String(0xb109a778) # string64
	AnimeTypeHandGlass = String(0x9951a44b) # string64

class NpcCastLabelData(Row):
	CastType = U8(0xb7a6c4a8)
	AIFlowName = String(0xf37316e6) # string64
	AIFlowEntryName = String(0x02c2ac67) # string32
	AppearStage = U8(0x378b2f14) # size is 3, could this be an array?

class NpcCastScheduleData(Row):
	EventName = String(0x7d740fa4) # string32
	CastLabel = U8(0x69a9bb3c)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd)
	EndHour = U8(0x675ca211)
	EndMinute = U8(0x2b09d942)
	NeglectSleep = U8(0xa78d0cc5)
	_d507df3e = U8(0xd507df3e)
	_e76db92f = U8(0xe76db92f)
	ApplyNeedActivity = U8(0xaaae3a0f)
	CanDoze = U8(0xac0593cc) # size is 3, could this be an array?

class NpcEquipRule(Row):
	ScoreMultiplier = Float(0xcbbe9d2d)
	_b219374f = Enum(0xb219374f, enum_eac1ccc130ff_55f087e18a44)
	_68d62ca8 = Enum(0x68d62ca8, enum_3f8ad7b8db09_a7b5a46a35b6)
	PurposeScore = S32(0x1f401b52)
	PurposeTag = U32(0xe765b554)
	SeasonScore = S32(0x79be959d)
	TasteScore = S32(0xa3dc7c4c)
	_423d1c4d = Enum(0x423d1c4d, enum_8660a424ddf9_da4e1de32164)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32
	Name = String(0x036e8ebe) # string64
	_2c2a379e = U8(0x2c2a379e)
	_a4396b29 = U8(0xa4396b29)
	_74275e7a = U8(0x74275e7a) # possible string size 1
	_cc198281 = U8(0xcc198281) # possible string size 1
	_14767df7 = U8(0x14767df7) # possible string size 1
	_744b3452 = U8(0x744b3452)
	_a073aa81 = U8(0xa073aa81)
	_fdf8907b = U8(0xfdf8907b)
	_f9cf603a = U16(0xf9cf603a)

class NpcInterest(Row):
	Offset = Float(0xecf95b05)
	ItemUniqueID = U16(0xfd9af1e1)
	ContinuousTime = U16(0xb694c63b)
	TimeZoneIndoorEveningLevel = U8(0xd2ab4a8f)
	TimeZoneOutdoorEarlyMorningLevel = U8(0xfa3b3608)
	TimeZoneOutdoorMorningLevel = U8(0x2ae7c830)
	TimeZoneOutdoorNoonLevel = U8(0x8d3bad84)
	TimeZoneOutdoorEveningLevel = U8(0xe4fe6719)
	TimeZoneOutdoorNightLevel = U8(0x1b6eaa53)
	TimeZoneOutdoorMidnightLevel = U8(0xb9e9f361)
	TimeZoneIndoorEarlyMorningLevel = U8(0x154eee75)
	TimeZoneIndoorMorningLevel = U8(0x1cb2e5a6)
	TimeZoneIndoorNoonLevel = U8(0x92827ae7)
	IntervalTime = U8(0xa0d9d29e)
	TimeZoneIndoorNightLevel = U8(0xcfca2366)
	TimeZoneIndoorMidnightLevel = U8(0xa0b3903d)
	RainActive = U8(0xa9de0384)
	VillageDevelopmentLevel = U8(0xee0961fa)
	BehaviorType = U8(0x40876b17)
	ConditionType = U8(0xa8644472)
	MoveConditionType = U8(0xa0efadac)
	_6bcf870d = U8(0x6bcf870d)
	MoveASType = String(0x604df507) # string32
	WaitASType = String(0x8eabc257) # string32
	NeedType = U8(0xd6b82305)
	LabelType = U8(0xd7ded52a)
	FlagType = U8(0x430dbf65) # size is 3, could this be an array?

class NpcLife(Row):
	ArriveDist = Float(0x3b27f030)
	SatisfyMinute = U16(0x76e5e67a)
	ItemUniqueID = U16(0xfd9af1e1)
	TimeZoneIndoorMidnightLevel = U8(0xa0b3903d)
	HobbyMusicLevel = U8(0x1eb65d06)
	HobbyFitnessLevel = U8(0x54ab2c62)
	HobbyFashionLevel = U8(0x9fbbc76b)
	HobbyEducationLevel = U8(0xcd61ce25)
	HobbyNatureLevel = U8(0xebd71bbd)
	TimeZoneOutdoorEarlyMorningLevel = U8(0xfa3b3608)
	TimeZoneOutdoorMorningLevel = U8(0x2ae7c830)
	TimeZoneOutdoorNoonLevel = U8(0x8d3bad84)
	TimeZoneOutdoorEveningLevel = U8(0xe4fe6719)
	TimeZoneOutdoorNightLevel = U8(0x1b6eaa53)
	TimeZoneOutdoorMidnightLevel = U8(0xb9e9f361)
	TimeZoneIndoorEarlyMorningLevel = U8(0x154eee75)
	TimeZoneIndoorMorningLevel = U8(0x1cb2e5a6)
	TimeZoneIndoorNoonLevel = U8(0x92827ae7)
	TimeZoneIndoorEveningLevel = U8(0xd2ab4a8f)
	TimeZoneIndoorNightLevel = U8(0xcfca2366)
	HobbyPlayLevel = U8(0x630a25b4)
	RainActive = U8(0xa9de0384)
	RainEquipment = U8(0x67850558)
	SeasonSpringLevel = U8(0xeaadf252)
	SeasonSummerLevel = U8(0x2760bc87)
	SeasonAutumnLevel = U8(0x7c1b4734)
	SeasonWinterLevel = U8(0xb2540403)
	LifeMotif = U8(0x38954eb6)
	VillageDevelopmentLevel = U8(0xee0961fa)
	NetPlay = U8(0xf196e054)
	BehaviorType = U8(0x40876b17)
	MoveASType = String(0x604df507) # string32
	WaitASType = String(0x8eabc257) # string32
	EquipRule = String(0xd941db12) # string32
	LiveMotif = U8(0x1f3bcf5e)
	HobbyMotif = U8(0xa42b13ce)
	LookAtType = U8(0x35c78d62)
	SpotType = RawData(0x9bc85bd0, 3)
	FlagType = U8(0x430dbf65)
	GroupActivityPlacementType = U8(0xbdd4dc0f) # size is 2, could this be an array?

class NpcLooksParam(Row):
	Speciality2 = U32(0xaf58956d)
	Speciality1 = U32(0xe8f8efbd)
	Music0 = U32(0xeffe09fe)
	Music1 = U32(0xd29e204e)
	Music2 = U32(0x953e5a9e)
	Book0 = U32(0x6ffec71e)
	Book1 = U32(0x529eeeae)
	Book2 = U32(0x153e947e)
	Comic0 = U32(0xa1e8d2bb)
	Comic1 = U32(0x9c88fb0b)
	Comic2 = U32(0xdb2881db)
	Movie0 = U32(0x48a92c68)
	Movie1 = U32(0x75c905d8)
	Movie2 = U32(0x32697f08)
	TvProgram0 = U32(0x6f9dd83d)
	TvProgram1 = U32(0x52fdf18d)
	TvProgram2 = U32(0x155d8b5d)
	Speciality0 = U32(0xd598c60d)
	Sports1 = U32(0xd6597c9d)
	Sports2 = U32(0x91f9064d)
	Drink0 = U32(0xb305defd)
	Drink1 = U32(0x8e65f74d)
	Drink2 = U32(0xc9c58d9d)
	Food0 = U32(0xc34424c7)
	Food1 = U32(0xfe240d77)
	Food2 = U32(0xb98477a7)
	Dream0 = U32(0xc4bb5846)
	Dream1 = U32(0xf9db71f6)
	Dream2 = U32(0xbe7b0b26)
	Hobby0 = U32(0x20624ee7)
	Hobby1 = U32(0x1d026757)
	Hobby2 = U32(0x5aa21d87)
	Sports0 = U32(0xeb39552d)
	UniqueID = U16(0x54706054)
	Label = String(0x87bf00e8) # string32

class NpcMoveRoomTemplate(Row):
	RoomType = U32(0xd9a1f501)
	_ef0088e8 = U8(0xef0088e8)
	Size = S8(0x0b6d59d2)
	GroupIndex = S8(0xb12e26da)
	_8f5c3da3 = U8(0x8f5c3da3)
	Direction = S8(0x3a1fca06) # size is 4, could this be an array?

class NpcMsgBullfestParam(Row):
	NpcMsgBullfestCondition = Enum(0xddf1f8bf, enum_47e581a0f3c1_94306367028d)
	_5ef56066 = U16(0x5ef56066)
	CapID = U16(0x8ff469e1)
	AccessoryID = U16(0x478dd182)
	TopsID = U16(0xdfb46994)
	BottomsID = U16(0x524596a2)
	SocksID = U16(0xe113ac8d)
	ShoesID = U16(0xf07156d2)
	_c35c5af7 = U16(0xc35c5af7)
	_286be1f4 = U16(0x286be1f4) # possible string size 2
	_7b1d9990 = U16(0x7b1d9990)
	_902a2293 = U16(0x902a2293) # possible string size 2
	UniqueID = U16(0x54706054)
	_b5c2db65 = U16(0xb5c2db65) # possible string size 2
	_7991b277 = U16(0x7991b277)
	_92a60974 = U16(0x92a60974) # possible string size 2
	_8c03fdc7 = U16(0x8c03fdc7)
	_673446c4 = U16(0x673446c4) # possible string size 2
	_b9507563 = U16(0xb9507563)
	_5267ce60 = U16(0x5267ce60) # possible string size 2
	_d0241896 = U16(0xd0241896)
	_3b13a395 = U16(0x3b13a395) # possible string size 2
	_754c57c7 = U16(0x754c57c7)
	_9e7becc4 = U32(0x9e7becc4) # possible string size 4

class NpcRoomTemplate(Row):
	RoomType = U32(0xd9a1f501)
	_ef0088e8 = U8(0xef0088e8)
	Size = S8(0x0b6d59d2)
	GroupIndex = S8(0xb12e26da)
	_8f5c3da3 = U8(0x8f5c3da3)
	Direction = S8(0x3a1fca06) # size is 4, could this be an array?

class NpcSpClothSetParam(Row):
	UniqueID = U16(0x54706054)
	Tool = U16(0x973fae34)
	Shoes = U16(0xce827d47)
	SpNpcID = U16(0x0207a2af)
	Cap = U16(0x291a1b04)
	Bottoms = U16(0xcc136eb5)
	Tops = U16(0x870f1e29)
	AcceEye = U16(0x2b57b24a)
	Label = String(0x87bf00e8) # string32
	Name = String(0x036e8ebe) # string64

class NpcSpModelScale(Row):
	_c7a5b572 = U32(0xc7a5b572)
	_8005cfa2 = U32(0x8005cfa2) # possible string size 4
	_48e540d2 = U32(0x48e540d2) # possible string size 4
	NormalScaleNR = Float(0x60edacd3)
	NormalScaleNG = Float(0xc8edb421)
	NormalScaleNB = Float(0x000d3b51)
	NormalScaleNA = Float(0x47ad4181)
	NormalScaleHR = Float(0xb6b44fce)
	NormalScaleHG = Float(0x1eb4573c)
	_e0e55820 = U32(0xe0e55820) # possible string size 4
	NormalScaleHA = Float(0x91f4a29c)
	NormalScaleLR = Float(0x2d250dd8)
	NormalScaleLG = Float(0x8525152a)
	NormalScaleLB = Float(0x4dc59a5a)
	NormalScaleLA = Float(0x0a65e08a)
	NormalScaleHB = Float(0xd654d84c)
	UniqueID = U16(0x54706054)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class NpcSpServiceMotionRandom(Row):
	UniqueID = U16(0x54706054)
	SelectSecond = U16(0x1abe6e96)
	EndHour = U8(0x675ca211)
	StartHour = U8(0x8ae48661)
	ASCommand = String(0x9bee16d1) # string66
	Label = String(0x87bf00e8) # string32
	SelectRate = U8(0x1e7ef977)
	Type = U8(0xd1f6dae0) # size is 3, could this be an array?

class NpcSpServiceMotionWork(Row):
	UniqueID = U16(0x54706054)
	Rate4 = U8(0xa3cfc752)
	ASCommand1 = String(0xcd16f843) # string66
	Rate1 = U8(0x94113760)
	ASCommand2 = String(0x26214340) # string66
	Rate2 = U8(0x86a4988e)
	ASCommand3 = String(0xc9e3287e) # string66
	Rate3 = U8(0x3e18ffeb)
	ASCommand4 = String(0x2b3f3307) # string66
	Label = String(0x87bf00e8) # string32
	ASCommand5 = String(0xc4fd5839) # string66
	Rate5 = U8(0x1b73a037)
	ASCommand6 = String(0x2fcae33a) # string66
	Rate6 = U8(0x09c60fd9)
	ASCommand7 = String(0xc0088804) # string66
	Rate7 = U8(0xb17a68bc)
	ASCommand8 = String(0x3103d389) # string66
	Rate8 = U8(0xe91978ea) # size is 3, could this be an array?

class NpcSpServiceMotionWorkSp(Row):
	UniqueID = U16(0x54706054)
	StartHour = U8(0x8ae48661)
	ASCommand = String(0x9bee16d1) # string66
	EndHour = U8(0x675ca211)
	SelectRate = U8(0x1e7ef977) # size is 2, could this be an array?

class PlayerStateParam(Row):
	PacketType = Enum(0xf9dcdec7, enum_666520d79fd1_c1f7ed2fb38f)
	ToolState = Enum(0xf299f7fc, enum_71a6eb72125d_4959f0d2a68c)
	ObjCheckRate = Float(0x38762eaa)
	ObjCheckType = Enum(0xc5567172, enum_4cb47c29b213_bcb1c15d0dcc)
	ChangeDemo = Enum(0xccf68ebe, enum_6bc751394207_9a22cc494738)
	BgCheckType = Enum(0x4045796c, enum_0a0cce2b4f07_e7b3e2de0566)
	RemoteChase = Enum(0x838b098c, enum_10a6294998ff_537c16dab4e8)
	ForbidOverwrite = U8(0x35fd6466)
	WaitType = U8(0x9067bb0e)
	DemoNetLockState = U8(0xae3add79)
	_ede0a8ca = U8(0xede0a8ca)
	_87438100 = U8(0x87438100)
	_a84507aa = U8(0xa84507aa)
	_16e483f0 = U8(0x16e483f0)
	_5b6d5751 = U8(0x5b6d5751)
	StateName = String(0x2ae273e3) # string48
	_497ac4d6 = U8(0x497ac4d6)
	BeesRunAway = U8(0x730cefc8)
	_63f77486 = U8(0x63f77486)
	_65fd6b0d = U8(0x65fd6b0d)
	HideHUD = U8(0x5681a1c3)
	_e550abdf = U8(0xe550abdf)
	_1aaaddc1 = U8(0x1aaaddc1)
	StopAutoSave = U8(0xfce7d916)
	EnableStageChange = U8(0xecfe9ddb)
	BgmEnd = U8(0xa9f6fac2)
	_833e2942 = U8(0x833e2942)
	AcceptAccess = U8(0xa6324d34)
	_f413acd2 = U8(0xf413acd2)
	PoseTrans = U8(0xfbb451bf)
	_68daf155 = U8(0x68daf155)
	NpcLookAction = U8(0xa1b074dd)
	_5dcf7b24 = U8(0x5dcf7b24)
	_aa0070b7 = U8(0xaa0070b7)
	_95798f28 = U8(0x95798f28)
	_2b6186a0 = U8(0x2b6186a0)

class RadioCM(Row):
	SelectRate = Float(0x293ee089)
	MusicNo = U16(0x0f30a50e)
	UniqueID = U16(0x54706054)
	Frames = U16(0x45ffea9a)
	BeforeDays = U8(0x00244ce4)
	Timezone = U8(0x627277e6)
	EventLabelShort = String(0x806cfd72) # string128

class RadioJingle(Row):
	SelectRate = Float(0x293ee089)
	Timezone = Enum(0xfc7a1955, enum_a579ed29f896_c3ff5ecc7a5b)
	MusicNo = U16(0x0f30a50e)
	UniqueID = U16(0x54706054)
	Frames = U16(0x45ffea9a)
	BeforeDays = U8(0x00244ce4)
	EventLabelShort = String(0x806cfd72) # string128

class RecipeCraftParam(Row):
	VillagerOpenNum = U32(0x3711677b)
	BoardColorID = U32(0x5f405bfb)
	NPCUnlock = Enum(0xcde5164f, enum_a7030bb7fc9b_fc546f9fbb31)
	CraftUnlock = Enum(0x34a742ad, enum_876f2a44aa3e_ea533d18da76)
	Amount4 = U16(0xdb46d805)
	Amount2 = U16(0x54062da5)
	Material3 = U16(0x617ff43e)
	Amount3 = U16(0x69660415)
	Material4 = U16(0xd35f282e)
	Material2 = U16(0x5c1fdd8e)
	Material5 = U16(0xee3f019e)
	Amount5 = U16(0xe626f1b5)
	Material6 = U16(0xa99f7b4e)
	Amount6 = U16(0xa1868b65)
	Amount1 = U16(0x13a65775)
	Material1 = U16(0x1bbfa75e)
	Item = U16(0x89a3482c)
	SerialID = S16(0x39dede36)
	UniqueID = U16(0x54706054) # size is 4, could this be an array?

class ReleaseVersionParam(Row):
	UniqueID = U16(0x54706054)
	ReleaseKey = U16(0x76c190b2)
	Name = String(0x977adfce) # string32
	Label = String(0x87bf00e8) # string32

class RoomArchParam(Row):
	UniqueID = U16(0x54706054)
	ResourceName = String(0x4b9c4229) # string64

class RoomCeilingParam(Row):
	UniqueID = U16(0x54706054)
	ResourceName = String(0x4b9c4229) # string64

class RoomCurtainParam(Row):
	UniqueID = U16(0x54706054)
	Name = String(0x036e8ebe) # string64
	ResourceName = String(0x4b9c4229) # string64

class RoomCurtainTexParam(Row):
	UniqueID = U16(0x54706054)
	Name = String(0x036e8ebe) # string64
	ResourceName = String(0x4b9c4229) # string64

class RoomFloorParam(Row):
	Act = Enum(0xf74f3d2c, enum_0caaf5f51cb7_b79133e4ebb1)
	Price = S32(0x718b024d)
	_b117eb21 = Enum(0xb117eb21, enum_67d8f9fad662_3c4e63ce8503)
	Scale = Enum(0x49295020, enum_67d8f9fad662_3c4e63ce8503)
	UniqueID = U16(0x54706054)
	LandingUniqueID = U16(0x8fced711)
	Floorboards = U16(0xab771eae)
	ItemTableId = U16(0x58aff4fb)
	Rotatable = U8(0x8ed948dd)
	ResourceName = String(0x4b9c4229) # string64
	Horizon = U8(0x3543c34a)
	Reverberation = S8(0x05836619)
	ItemName = String(0xb8cc232c) # string64
	HasJmp = U8(0xa4db9685)

class RoomLandingParam(Row):
	UniqueID = U16(0x54706054)
	Floorboards = U16(0xab771eae)
	LandingName = String(0x05038516) # string64
	ResourceName = String(0x4b9c4229) # string64

class RoomWallParam(Row):
	Price = S32(0x718b024d)
	AO = Enum(0x8a377042, enum_9cef5ff8f2fc_3c4e63ce8503)
	Light = Enum(0x85ed8743, enum_1be25fe2a516_ddd20c924fed)
	Act = Enum(0xf74f3d2c, enum_0caaf5f51cb7_b79133e4ebb1)
	WindowUniqueID = U16(0xe3a28616)
	UniqueID = U16(0x54706054)
	CurtainUniqueID = U16(0xa0e569dc)
	CeilingUniqueID = U16(0x947875dd)
	ItemTableId = U16(0x58aff4fb)
	ArchUniqueID = U16(0x499e42f9)
	CurtainTexUniqueID = U16(0xaa9bfc6e)
	TextureWindow = U8(0x318ebbf2)
	Reverberation = S8(0x05836619)
	ResourceName = String(0x4b9c4229) # string64
	ItemName = String(0xb8cc232c) # string64

class RoomWindowParam(Row):
	RoomWindowModelType = Enum(0xc90ab4c4, enum_f18e5565c112_ab0466cfcd5a)
	RoomWindowWallType = Enum(0xcbc01f0d, enum_8bcffcdc34f9_75d5da8d5621)
	UniqueID = U16(0x54706054)
	ResourceName = String(0x4b9c4229) # string64
	WindowName = String(0x9b0b7ce4) # string64

class SeasonCalendar(Row):
	Month = U8(0x287db05d)
	Day = U8(0xd5692bff)
	Season_N = U8(0x185d9096)
	Snow_N = U8(0x80e1de38)
	Cloud_N = U8(0x8b21a26b)
	SPWeather_N = U8(0x66b4a4c1)
	Bush_N = U8(0x4875e383)
	Shop_N = U8(0x5b8be707)
	Weed_N = U8(0xa155bc19)
	Fog_N = U8(0x61501334)
	Sakura_N = U8(0xb5a8fc2e)
	Season_S = U8(0xba2e1fd4)
	Snow_S = U8(0x2292517a)
	Cloud_S = U8(0x29522d29)
	SPWeather_S = U8(0xc4c72b83)
	Bush_S = U8(0xea066cc1)
	Shop_S = U8(0xf9f86845)
	Weed_S = U8(0x0326335b)
	Fog_S = U8(0xc3239c76)
	Sakura_S = U8(0x17db736c)

class ShopItemRouteFlags(Row):
	FlagLand = S32(0x3fe43170)
	FlagPlayer = S32(0x4171a41d)
	ShopType = Enum(0xd3d4284e, enum_05496a929e72_1987c9f2e67f)
	ItemFrom = String(0x46e66708) # string32
	AttrCollectBit = U8(0x74b2eb78) # size is 4, could this be an array?

class SoundAttributeForGround(Row):
	UniqueID = U16(0x54706054)
	_5e7a33b5 = U16(0x5e7a33b5)

class SoundAttributeForPlacement(Row):
	UniqueID = U16(0x54706054)
	_5e7a33b5 = U16(0x5e7a33b5)

class SoundAudioMusic(Row):
	UniqueID = U16(0x54706054)
	RefItemUniqueID = U16(0x3637ebb9)
	AudioMusicID = S16(0xd4892d19)
	Label = String(0x87bf00e8) # string32
	_32bc8d59 = U16(0x32bc8d59) # possible string size 2

class SoundInstruments(Row):
	InstrumentsType = Enum(0x64bc65e7, enum_a97c5a371180_d749edee2750)
	RefItemUniqueID = U16(0x3637ebb9)
	UniqueID = U16(0x54706054)
	Name = String(0x85cf1615) # string128
	Label = String(0x87bf00e8) # string32

class SoundMaterialType(Row):
	UniqueID = U16(0x54706054)
	SoundAttribute = U16(0x2e17a0a7)
	DebugName = String(0xab51a3cf) # string32

class SpNpcParam(Row):
	GenderUsEu = Enum(0x86ad0ce1, enum_c1ee150f0e21_f567104db912)
	GenderAsia = Enum(0xdda5d566, enum_c1ee150f0e21_f567104db912)
	Social = U32(0x23e7c2a0)
	PacketId = S32(0x3ce2e8d8)
	NpcSpClothSet = U16(0x9611c929)
	Umbrella = U16(0xbb9c816e)
	PosterItemID = S16(0x0f640691)
	Smartphone = U16(0x3f858678)
	UniqueID = U16(0x54706054)
	VmRhythmType = U8(0x9d1d8e45)
	VmPauseType = U8(0xe7534ab5)
	_42f255d5 = U8(0x42f255d5)
	_21c5bbd6 = U8(0x21c5bbd6)
	NpcColor = U8(0x41977699)
	SpecialSLink = U8(0xbe782346)
	SpecialELink = U8(0x04ac1bea)
	HavokResName = String(0x4ce98793) # string64
	ResName = String(0x48ef0398) # string64
	BirthMonth = U8(0x9456b6a3)
	BirthMDay = U8(0x919ea52a)
	Label = String(0x2f1b930d) # string8
	_e52f0037 = U8(0xe52f0037)

class StructureBridgeParam(Row):
	BridgePattern = Enum(0x74be6041, enum_d213af309f1d_10d5d2b786dc)
	BridgeTypeUniqueID = U16(0xee9ce68d)
	UniqueID = U16(0x54706054)
	ModelName = String(0x39b5a93d) # string32

class StructureBridgeTypeParam(Row):
	_904611f3 = U32(0x904611f3)
	UniqueID = U16(0x54706054)
	ItemNameUniqueID = U16(0xc33a894e)
	BridgeTypeNameJp = String(0x5c28c4db) # string32
	BridgeTypeName = String(0x68cf5938) # string32

class StructureDoorParam(Row):
	_98a65efb = U32(0x98a65efb) # possible string size 4
	_a1def3bb = U32(0xa1def3bb) # possible string size 4
	_b6f6977b = U32(0xb6f6977b) # possible string size 4
	_498a840d = U32(0x498a840d) # possible string size 4
	_5ea2e0cd = U32(0x5ea2e0cd)
	_8238f88d = U32(0x8238f88d)
	_95109c4d = U32(0x95109c4d) # possible string size 4
	_ac68310d = U32(0xac68310d)
	_bb4055cd = U32(0xbb4055cd)
	_de996b8d = U32(0xde996b8d)
	_c9b10f4d = U32(0xc9b10f4d)
	_f0c9a20d = U32(0xf0c9a20d)
	_e7e1c6cd = U32(0xe7e1c6cd)
	UniqueID = U16(0x54706054)
	Stage11 = String(0xfd606cac) # string32
	Stage10 = String(0x12a20792) # string32
	Stage9 = String(0x4122941d) # string32
	Stage8 = String(0xaee0ff23) # string32
	Stage7 = String(0x5feba4ae) # string32
	Stage6 = String(0xb029cf90) # string32
	Stage5 = String(0x5b1e7493) # string32
	Stage4 = String(0xb4dc1fad) # string32
	Stage3 = String(0x560004d4) # string32
	Stage2 = String(0xb9c26fea) # string32
	Stage1 = String(0x52f5d4e9) # string32
	Stage0 = String(0xbd37bfd7) # string32
	Name = String(0x977adfce) # string32
	Stage12 = String(0x1657d7af) # string32

class StructureFacilityModel(Row):
	_85a0fa49 = U32(0x85a0fa49)
	FloorHeight = Float(0x6efc082c)
	FacilityModelVariation = Enum(0xdd9617a2, enum_7fc56270e7a7_413dac6d2d4f)
	Door0Angle = Float(0x88ff5893)
	StructureInfoUniqueID = U16(0x00c1577d)
	Door0 = U16(0x0d664b5c)
	_9c2d6dc6 = U16(0x9c2d6dc6)
	RoofMaterial = U16(0x83b54e59)
	DoorMaterial = U16(0x42bdd56f)
	UniqueID = U16(0x54706054)
	UseChimneySmoke = U8(0x397b2b54)
	HasNightLight = U8(0x42e82ded)
	HasEigyoLight = U8(0x43d8a434)
	UseMyDesign = U8(0x89be1d8f)
	Construction = U8(0x9c8a400b)
	GrowLevel = U8(0x35ac1bb4)
	ModelName = String(0x39b5a93d) # string32
	HasDoorEigyoLight = U8(0x23e16936) # size is 2, could this be an array?

class StructureHouseDoorParam(Row):
	_b619ba5c = U32(0xb619ba5c)
	HouseDoorAnim = Enum(0x712c43a7, enum_4a1ca0237618_2589c82f75a6)
	HouseDoorShape = Enum(0x0aa76edd, enum_4bb482986734_fd8d6be18496)
	UniqueID = U16(0x54706054)
	CustomizeSortID = U16(0x37d4e515)
	Material = U16(0x39cb9646)
	LatchBolt = U8(0x960a51fe)
	DecoForbidden = U8(0xc93db65a)
	HasDoorWindow = U8(0xf489f3c5)
	ModelName = String(0x39b5a93d) # string32
	Dummy = U8(0xf75ddf51) # size is 3, could this be an array?

class StructureHouseRoofParam(Row):
	HouseColor = Enum(0xa9424a50, enum_17a769bfe354_791918aecc14)
	HouseShapeUniqueID = U16(0xb6f501d2)
	UniqueID = U16(0x54706054)
	CustomizeSortID = U16(0x37d4e515)
	Material = U16(0x39cb9646)
	Dummy = U8(0xf75ddf51)
	ModelName = String(0x39b5a93d) # string32

class StructureHouseShapeParam(Row):
	AppearanceLevel = Enum(0x10dbd8bb, enum_719f8c5ace1e_9dc2d1c92509)
	_e6fc6624 = U16(0xe6fc6624)
	UniqueID = U16(0x54706054)
	DefaultWallUniqueID = U16(0xd8727d7d)
	DefaultDoorUniqueID = U16(0xc86e60d5)
	DefaultRoofUniqueID = U16(0x0966fbe3)
	Name = String(0x977adfce) # string32
	DoorBellName = String(0xe3a73129) # string32

class StructureHouseWallParam(Row):
	HouseDoorStep = Enum(0x60680c93, enum_106465ec3a51_1268c2c082da)
	UniqueID = U16(0x54706054)
	_9c2d6dc6 = U16(0x9c2d6dc6)
	HouseShapeUniqueID = U16(0xb6f501d2)
	CustomizeSortID = U16(0x37d4e515)
	ModelName = String(0x39b5a93d) # string32
	UseExteriorLight = U8(0x0424930f)
	UseCurtain = U8(0x9e19c94c)
	LightParamName = String(0xd2c59675) # string32

class StructureInfoParam(Row):
	_fec3548b = U32(0xfec3548b)
	StructureInfoType = Enum(0xd6704d8b, enum_3f984d1a17ec_8f1bbc952a3f)
	ModelType = Enum(0xc01e47a7, enum_3f984d1a17ec_8f1bbc952a3f)
	_1ff4093d = Enum(0x1ff4093d, enum_8d64dd844b09_8d64dd844b09)
	StructureInfoHouseType = Enum(0xcc24374e, enum_5fe6f47ed555_cd0b35a4b9fb)
	Door0 = U16(0x0d664b5c)
	UniqueID = U16(0x54706054)

class StructureSlopeParam(Row):
	UniqueID = U16(0x54706054)
	ItemNameUniqueID = U16(0xc33a894e)
	ModelName = String(0x39b5a93d) # string32
	JpName = String(0x08462f85) # string32

class TVProgram(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	EndMoS3 = U8(0x584d684a)
	_01481890 = U8(0x01481890)
	ResourceNameSp1 = String(0x7834d5db) # string33
	StartMoN1 = U8(0x878cd782)
	StartDayN1 = U8(0x13b9f45c)
	EndMoN1 = U8(0x6a34f3f2)
	EndDayN1 = U8(0x43513d44)
	StartMoS1 = U8(0x1ffc84b1)
	StartDayS1 = U8(0x8bc9a76f)
	EndMoS1 = U8(0xf244a0c1)
	EndDayS1 = U8(0xdb216e77)
	ResourceNameSp2 = String(0x93036ed8) # string33
	StartMoN2 = U8(0x9539786c)
	StartDayN2 = U8(0x010c5bb2)
	EndMoN2 = U8(0x78815c1c)
	EndDayN2 = U8(0x51e492aa)
	StartMoS2 = U8(0x0d492b5f)
	StartDayS2 = U8(0x997c0881)
	EndMoS2 = U8(0xe0f10f2f)
	EndDayS2 = U8(0xc994c199)
	ResourceNameSp3 = String(0x7cc105e6) # string33
	StartMoN3 = U8(0x2d851f09)
	StartDayN3 = U8(0xb9b03cd7)
	EndMoN3 = U8(0xc03d3b79)
	EndDayN3 = U8(0xe958f5cf)
	StartMoS3 = U8(0xb5f54c3a)
	StartDayS3 = U8(0x21c06fe4)
	ResourceName = String(0xa88f23cf) # string33
	EndDayS3 = U8(0x7128a6fc)
	ResourceNameSp4 = String(0x9e1d1e9f) # string33
	StartMoN4 = U8(0xb05227b0)
	StartDayN4 = U8(0x2467046e)
	EndMoN4 = U8(0x5dea03c0)
	EndDayN4 = U8(0x748fcd76)
	StartMoS4 = U8(0x28227483)
	StartDayS4 = U8(0xbc17575d)
	EndMoS4 = U8(0xc59a50f3)
	EndDayS4 = U8(0xecff9e45)
	ResourceNameSp5 = String(0x71df75a1) # string33
	StartMoN5 = U8(0x08ee40d5)
	StartDayN5 = U8(0x9cdb630b)
	EndMoN5 = U8(0xe55664a5)
	EndDayN5 = U8(0xcc33aa13)
	StartMoS5 = U8(0x909e13e6)
	StartDayS5 = U8(0x04ab3038)
	EndMoS5 = U8(0x7d263796)
	EndDayS5 = U8(0x5443f920)
	ResourceNameSp6 = String(0x9ae8cea2) # string33
	StartMoN6 = U8(0x1a5bef3b)
	StartDayN6 = U8(0x8e6ecce5)
	EndMoN6 = U8(0xf7e3cb4b)
	EndDayN6 = U8(0xde8605fd)
	StartMoS6 = U8(0x822bbc08)
	StartDayS6 = U8(0x161e9fd6)
	EndMoS6 = U8(0x6f939878)
	EndDayS6 = U8(0x46f656ce)

class TVProgramFriday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramMonday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramSaturday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramSunday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramThursday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramTuesday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class TVProgramWednesday(Row):
	TVProgramName = Enum(0xa988063c, enum_c6e92aae9ffa_253fcc4534a4)
	StartHour = U8(0x8ae48661)
	StartMinute = U8(0x3835a9dd) # size is 3, could this be an array?

class VMMultistepNPC(Row):
	UniqueID = U16(0x54706054)
	NPCLabel = String(0x091b46f5) # string128

lookup = {
	'AITag.bcsv': AITag,
	'AmiiboData.bcsv': AmiiboData,
	'BgmPropertyControlParam.bcsv': BgmPropertyControlParam,
	'BgmPropertyParam.bcsv': BgmPropertyParam,
	'CalendarEventParam.bcsv': CalendarEventParam,
	'CharaMakeCheekTypeParam.bcsv': CharaMakeCheekTypeParam,
	'CharaMakeEyeColorParam.bcsv': CharaMakeEyeColorParam,
	'CharaMakeEyeTypeParam.bcsv': CharaMakeEyeTypeParam,
	'CharaMakeHairColorParam.bcsv': CharaMakeHairColorParam,
	'CharaMakeHairStyleParam.bcsv': CharaMakeHairStyleParam,
	'CharaMakeMouthTypeParam.bcsv': CharaMakeMouthTypeParam,
	'CharaMakeNoseTypeParam.bcsv': CharaMakeNoseTypeParam,
	'CharaMakeSkinColorParam.bcsv': CharaMakeSkinColorParam,
	'ColEffectAttributeParam.bcsv': ColEffectAttributeParam,
	'ColGroundAttributeParam.bcsv': ColGroundAttributeParam,
	'ColSoundAttributeParam.bcsv': ColSoundAttributeParam,
	'DuckingParam.bcsv': DuckingParam,
	'EventFlagsHouseParam.bcsv': EventFlagsHouseParam,
	'EventFlagsLandParam.bcsv': EventFlagsLandParam,
	'EventFlagsLandTempParam.bcsv': EventFlagsLandTempParam,
	'EventFlagsLifeSupportAchievementParam.bcsv': EventFlagsLifeSupportAchievementParam,
	'EventFlagsLifeSupportDailyParam.bcsv': EventFlagsLifeSupportDailyParam,
	'EventFlagsNpcMemoryParam.bcsv': EventFlagsNpcMemoryParam,
	'EventFlagsNpcSaveParam.bcsv': EventFlagsNpcSaveParam,
	'EventFlagsNpcTempParam.bcsv': EventFlagsNpcTempParam,
	'EventFlagsPlayerActivityParam.bcsv': EventFlagsPlayerActivityParam,
	'EventFlagsPlayerParam.bcsv': EventFlagsPlayerParam,
	'EventFlagsPlayerTempParam.bcsv': EventFlagsPlayerTempParam,
	'EventFlagsPlayerVisitParam.bcsv': EventFlagsPlayerVisitParam,
	'EventPlazaFtrParam.bcsv': EventPlazaFtrParam,
	'EventPlazaGround.bcsv': EventPlazaGround,
	'EventPlazaObjModelParam.bcsv': EventPlazaObjModelParam,
	'EventPlazaPlacementParam.bcsv': EventPlazaPlacementParam,
	'FgFlowerHeredity.bcsv': FgFlowerHeredity,
	'FgMainParam.bcsv': FgMainParam,
	'FieldCreateParam.bcsv': FieldCreateParam,
	'FieldDistantViewParam.bcsv': FieldDistantViewParam,
	'FieldLandMakingActionParam.bcsv': FieldLandMakingActionParam,
	'FieldLandMakingError.bcsv': FieldLandMakingError,
	'FieldLandMakingRoadKindParam.bcsv': FieldLandMakingRoadKindParam,
	'FieldLandMakingUnitModelParam.bcsv': FieldLandMakingUnitModelParam,
	'FieldMainFieldParam.bcsv': FieldMainFieldParam,
	'FieldMysteryTourFieldParam.bcsv': FieldMysteryTourFieldParam,
	'FieldMysteryTourItemParam.bcsv': FieldMysteryTourItemParam,
	'FieldMysteryTourParam.bcsv': FieldMysteryTourParam,
	'FieldOutsideParts.bcsv': FieldOutsideParts,
	'FieldOutsideTemplate.bcsv': FieldOutsideTemplate,
	'FishAppearRiverParam.bcsv': FishAppearRiverParam,
	'FishAppearSeaParam.bcsv': FishAppearSeaParam,
	'FishBeyQuestParam.bcsv': FishBeyQuestParam,
	'FishStatusParam.bcsv': FishStatusParam,
	'GmoFootprintParam.bcsv': GmoFootprintParam,
	'HumanAnimParam.bcsv': HumanAnimParam,
	'IndoorIdrParam.bcsv': IndoorIdrParam,
	'IndoorPhotoStudioItemParam.bcsv': IndoorPhotoStudioItemParam,
	'InsectAppearParam.bcsv': InsectAppearParam,
	'InsectBattleParam.bcsv': InsectBattleParam,
	'InsectStatusParam.bcsv': InsectStatusParam,
	'ItemAct.bcsv': ItemAct,
	'ItemClothGroup.bcsv': ItemClothGroup,
	'ItemColor.bcsv': ItemColor,
	'ItemFilter.bcsv': ItemFilter,
	'ItemFrom.bcsv': ItemFrom,
	'ItemKind.bcsv': ItemKind,
	'ItemMailAttachCategoryGroup.bcsv': ItemMailAttachCategoryGroup,
	'ItemMenuIcon.bcsv': ItemMenuIcon,
	'ItemNpcFtrActionParam.bcsv': ItemNpcFtrActionParam,
	'ItemNpcOutfitInfo.bcsv': ItemNpcOutfitInfo,
	'ItemNpcRoomReplaceCategory.bcsv': ItemNpcRoomReplaceCategory,
	'ItemNpcTopsForm.bcsv': ItemNpcTopsForm,
	'ItemOutfitCategory.bcsv': ItemOutfitCategory,
	'ItemOutfitInfo.bcsv': ItemOutfitInfo,
	'ItemParam.bcsv': ItemParam,
	'ItemPlayerInitialOutfitBoyAWParam.bcsv': ItemPlayerInitialOutfitBoyAWParam,
	'ItemPlayerInitialOutfitBoySSParam.bcsv': ItemPlayerInitialOutfitBoySSParam,
	'ItemPlayerInitialOutfitGirlAWParam.bcsv': ItemPlayerInitialOutfitGirlAWParam,
	'ItemPlayerInitialOutfitGirlSSParam.bcsv': ItemPlayerInitialOutfitGirlSSParam,
	'ItemPlayerTopsForm.bcsv': ItemPlayerTopsForm,
	'ItemRemake.bcsv': ItemRemake,
	'ItemRemakeCommonPattern.bcsv': ItemRemakeCommonPattern,
	'ItemRemakeCommonPatternCategory.bcsv': ItemRemakeCommonPatternCategory,
	'ItemSeasonalityParam.bcsv': ItemSeasonalityParam,
	'ItemShareTexture.bcsv': ItemShareTexture,
	'ItemSize.bcsv': ItemSize,
	'ItemStrSort.bcsv': ItemStrSort,
	'ItemUIContextMenu.bcsv': ItemUIContextMenu,
	'ItemUnitIcon.bcsv': ItemUnitIcon,
	'LocalizeNameConvertParam.bcsv': LocalizeNameConvertParam,
	'MannequinCoodinate.bcsv': MannequinCoodinate,
	'MaterialType.bcsv': MaterialType,
	'MessageCardBoardDesignParam.bcsv': MessageCardBoardDesignParam,
	'MessageCardColorParam.bcsv': MessageCardColorParam,
	'MessageCardDesignParam.bcsv': MessageCardDesignParam,
	'MessageCardSelectDesign.bcsv': MessageCardSelectDesign,
	'MessageCardSelectDesignSp.bcsv': MessageCardSelectDesignSp,
	'MessageCardSelectPresent.bcsv': MessageCardSelectPresent,
	'MessageCardSelectPresentSp.bcsv': MessageCardSelectPresentSp,
	'MuseumFossilDonateInfo.bcsv': MuseumFossilDonateInfo,
	'MuseumNPCLayoutInfo.bcsv': MuseumNPCLayoutInfo,
	'MuseumNPCSilhouette.bcsv': MuseumNPCSilhouette,
	'MuseumNPCSpotTalk.bcsv': MuseumNPCSpotTalk,
	'MuseumNameboardInfo.bcsv': MuseumNameboardInfo,
	'MuseumWatchPoint.bcsv': MuseumWatchPoint,
	'MysteryTourFieldParam.bcsv': MysteryTourFieldParam,
	'MysteryTourFishParam.bcsv': MysteryTourFishParam,
	'MysteryTourInsectParam.bcsv': MysteryTourInsectParam,
	'MysteryTourItemParam.bcsv': MysteryTourItemParam,
	'MysteryTourParam.bcsv': MysteryTourParam,
	'NmlNpcParam.bcsv': NmlNpcParam,
	'NmlNpcRaceParam.bcsv': NmlNpcRaceParam,
	'NpcCastLabelData.bcsv': NpcCastLabelData,
	'NpcCastScheduleData.bcsv': NpcCastScheduleData,
	'NpcEquipRule.bcsv': NpcEquipRule,
	'NpcInterest.bcsv': NpcInterest,
	'NpcLife.bcsv': NpcLife,
	'NpcLooksParam.bcsv': NpcLooksParam,
	'NpcMoveRoomTemplate.bcsv': NpcMoveRoomTemplate,
	'NpcMsgBullfestParam.bcsv': NpcMsgBullfestParam,
	'NpcRoomTemplate.bcsv': NpcRoomTemplate,
	'NpcSpClothSetParam.bcsv': NpcSpClothSetParam,
	'NpcSpModelScale.bcsv': NpcSpModelScale,
	'NpcSpServiceMotionRandom.bcsv': NpcSpServiceMotionRandom,
	'NpcSpServiceMotionWork.bcsv': NpcSpServiceMotionWork,
	'NpcSpServiceMotionWorkSp.bcsv': NpcSpServiceMotionWorkSp,
	'PlayerStateParam.bcsv': PlayerStateParam,
	'RadioCM.bcsv': RadioCM,
	'RadioJingle.bcsv': RadioJingle,
	'RecipeCraftParam.bcsv': RecipeCraftParam,
	'ReleaseVersionParam.bcsv': ReleaseVersionParam,
	'RoomArchParam.bcsv': RoomArchParam,
	'RoomCeilingParam.bcsv': RoomCeilingParam,
	'RoomCurtainParam.bcsv': RoomCurtainParam,
	'RoomCurtainTexParam.bcsv': RoomCurtainTexParam,
	'RoomFloorParam.bcsv': RoomFloorParam,
	'RoomLandingParam.bcsv': RoomLandingParam,
	'RoomWallParam.bcsv': RoomWallParam,
	'RoomWindowParam.bcsv': RoomWindowParam,
	'SeasonCalendar.bcsv': SeasonCalendar,
	'ShopItemRouteFlags.bcsv': ShopItemRouteFlags,
	'SoundAttributeForGround.bcsv': SoundAttributeForGround,
	'SoundAttributeForPlacement.bcsv': SoundAttributeForPlacement,
	'SoundAudioMusic.bcsv': SoundAudioMusic,
	'SoundInstruments.bcsv': SoundInstruments,
	'SoundMaterialType.bcsv': SoundMaterialType,
	'SpNpcParam.bcsv': SpNpcParam,
	'StructureBridgeParam.bcsv': StructureBridgeParam,
	'StructureBridgeTypeParam.bcsv': StructureBridgeTypeParam,
	'StructureDoorParam.bcsv': StructureDoorParam,
	'StructureFacilityModel.bcsv': StructureFacilityModel,
	'StructureHouseDoorParam.bcsv': StructureHouseDoorParam,
	'StructureHouseRoofParam.bcsv': StructureHouseRoofParam,
	'StructureHouseShapeParam.bcsv': StructureHouseShapeParam,
	'StructureHouseWallParam.bcsv': StructureHouseWallParam,
	'StructureInfoParam.bcsv': StructureInfoParam,
	'StructureSlopeParam.bcsv': StructureSlopeParam,
	'TVProgram.bcsv': TVProgram,
	'TVProgramFriday.bcsv': TVProgramFriday,
	'TVProgramMonday.bcsv': TVProgramMonday,
	'TVProgramSaturday.bcsv': TVProgramSaturday,
	'TVProgramSunday.bcsv': TVProgramSunday,
	'TVProgramThursday.bcsv': TVProgramThursday,
	'TVProgramTuesday.bcsv': TVProgramTuesday,
	'TVProgramWednesday.bcsv': TVProgramWednesday,
	'VMMultistepNPC.bcsv': VMMultistepNPC,
}
