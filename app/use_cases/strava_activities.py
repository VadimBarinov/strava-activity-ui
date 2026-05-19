from datetime import datetime, timedelta
from app.api.strava_api import StravaAPI

def convert_date(iso_date: str):
  dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
  return dt.strftime("%d %B %Y г. в %H:%M")

def convert_distance(distance_in_metres):
  return distance_in_metres / 1000

def convert_moving_time(seconds):
  delta = timedelta(seconds=seconds)
  return str(delta)

def convert_speed(speed):
  return speed * 3.6

activities = [
  {
    "athlete": { # поменяется на user и будет отдельной сущностью в бд
      "id": 123,
      "name": "Вадим Баринов", # в api такого нет, нужно будет при синхронизации обновлять данные пользователя в бд
    },
    "id": 1,
    "name": "Тренировка (после обеда)",
    "start_date_local": convert_date("2025-09-22T17:54:39Z"),
    "type": "Ride", # будет отдельной сущностью в бд
    "distance": convert_distance(11819.9),
    "moving_time": convert_moving_time(3161),
    "average_speed": convert_speed(3.739), 
    "total_elevation_gain": 94, 
    "average_heartrate": 111,
    "max_heartrate": 150,
    "map": { # будет отдельной сущностью в бд
      "id": "456",
      "summary_polyline": "i{wjI{xhfHHWPM~@CZFZd@Pd@Jj@APsClDiDvCu@x@[n@UjAu@dAYjAe@r@Ql@?PTp@Lv@vAnFBLANe@AkA_@mAQUDyC|Di@l@iB`CKTCV?fAGvBQnD_@bFGZMb@KN_@VWXk@\\u@FcAAi@^u@IKBKHK\\m@pCe@zAa@|@oAhBc@|@Or@]xCS~@s@xB{AxCm@dDmAdDOVi@l@sBlBwCvCoA~Ay@h@QPUj@SjBQp@wFxJQNe@LaABKHCP?rAEz@DpAMl@g@~@K^CXBvAAl@IlBOfBEfBGj@O|@mAbFUn@cA~A[`A_AjFOhBI`@BB{@~AUnAYr@CVFp@CL_B`CqBnBiApBgD|AkAz@QTI^Kp@BlAIbFKr@OXcCdCsAv@y@j@y@fAa@dAW\\eAr@aA`@g@j@aAr@n@a@z@aAz@e@nA}@PYX_AJQfBaBjAo@|@iArAoAJYF_@N{ABgBIkBP{AFDFNEOxAgA`@g@`Bc@f@URY`@aAPQh@{@zA_B|@}ADWCe@@]Vs@LgAbAiBNk@NwBJy@TmANuAn@aBn@m@f@y@`@aBn@iDN{AR_DJiD?oBLg@d@_ANs@CiA@u@CkABa@NKzACLEPQnByDjAmB\\a@Vo@L[He@VeCPc@x@a@dA{@xAcBhA_A`@g@n@k@^Yn@{@b@u@n@eBj@yBHECA@MLu@\\s@`@mAv@kBf@}BVcCLm@f@eArAaB\\o@j@aBr@gDL[HIJAx@ZP@FGHc@FI~@@l@Ix@i@P[d@a@Zo@EJFm@VmFLsADcCL}BH]`BgCxBaCvAkBNAp@HdBf@n@@wAgFk@_CC_@DSJYh@w@ZgAr@{@RqAVk@PWtEcFvCmClJsJdA_Ar@w@J[Hw@Ao@WkAo@sAa@oAEWBK\\a@Fi@f@o@n@o@HAPHNGhAqAlBkB|AyBt@q@bBkBvAcAd@m@zBwBh@o@rCmCj@YBISYEUGgAFY`@{@p@eAd@gAVa@TOjAUZMPWB][dAQLy@XkA|@qAzBYt@Gd@@bADLLR?Pe@JmHxHcEvD_BbB_AjAoExEQJk@AYXo@~@Ox@[b@APT~@t@xAf@nB?RCVIh@KTqI~ImBfBMBMEIQKe@MQ[_AIIMDSXCJ?LTx@FDEaBdCeAB@TY?c@E^",
      "resource_state": 2
    },
    "intensity_score": 0.5612,
    "target": 2,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "name": "Тренировка (после обеда)",
    "distance": convert_distance(19487.9),
    "moving_time": convert_moving_time(6869),
    "total_elevation_gain": 122.9,
    "type": "Ride",
    "id": 15910747028,
    "start_date_local": convert_date("2025-09-13T15:23:35Z"),
    "map": {
      "id": "a15910747028",
      "summary_polyline": "{ywjI_~hfHv@KVPt@pEVXjMiM\\uA@u@mB{EMk@`@c@T}@nAuAh@BtHwIzBwB~@i@jCeDlGwFFSUy@DqApCaF`BYp@u@xB{A\\?`@^`AXz@Ux@uArDcEt@cCf@uER_@tAy@jAg@jD]|BtF`AvDb@PhAOTZ\\`Bd@P`@h@^HbCaC~B{CNe@Ce@t@KdA_AxOs@tJgALg@MqHHkCOcAE}JYiFpEmA~CsAPgAOmFPi@tHi@b@PzAbBfBKhAPfCkA~Dc@h@y@Lm@MsFLg@hI~@fBm@tHgAdC{@tDYpCd@`FhBh@Zv@jAfA`AnEdBjCODWIIc@h@eARwC_AuDaCOBI\\_AbKD`@Z\\a@hElKdG^n@mAtEI|AoApHOlBDl@x@dBDv@u@|AsANa@|A[d@o@nCYMeAcByAyAkBwEMu@a@^eApBmB~@UZyADm@XMV}@kHUmCH]GZYJIu@MKyG`F_HjDFSSrAkAAi@\\o@OSe@wBDiEbA{L`AwHZ_@Sw@@UeIBSXa@Kc@k@UYLHfCIx@Y^gFp@iMx@gDHsBzAgGhIm@\\w@i@uAwDk@Ce@h@c@UeB}GuAqCi@UuCj@yChB_@v@a@zDk@vByFbHm@DyB_Aq@ZiC`C{Ah@gBfCo@vACrAX~@AN{@TeIzIqCtBkDpE{EzEx@o@J_@}@qE}@iFI_AbAfHbApEcAhAi@Aq@n@o@vAa@l@Jt@bArB`@bBDl@Kz@Yl@oQdQwGrHMnAo@fAZdAb@xC|AdG{AzBE\\XzA`AfCjCf@z@d@hAs@LNPl@Oj@N~@xGhWxAjEfLh[f@dAb@fBfBtDHt@RBb@nAClBm@bAEz@|EbKhArDrAdD|@~Cl@vEMIJi@AQy@uDaC{FcAsEu@}AeAmAiB}DEi@Ho@j@y@ZaAHB}@{Bi@B@LUb@QhAaB~@c@e@QwAHJQWHR?[GHPEQL[Q[cBy@`@kCy@A[I?Bb@La@ET@_@?NOHVJCQUHFq@Hb@KIFFSATJGBDIGI@VBQKFDODZOC@TLAGu@V^tBv@nAy@Mf@Vx@lAvCZRdAg@l@yCIcBaCcG_IqTmAqE_AeB_B}Di@gDqFaSPw@Ke@QQcAp@aAq@_C_@c@q@Ca@vAw@Jk@{@qEwAuEoAqGb@m@z@qCbGcGjBgCs@{CQAU^XxAGBLaAGUwB_B",
      "resource_state": 2
    },
    "average_speed": convert_speed(2.837),
    "average_heartrate": 112,
    "max_heartrate": 135,
    "intensity_score": 0.558,
    "target": 2,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "name": "Тренировка (после обеда)",
    "distance": convert_distance(39620.0),
    "moving_time": convert_moving_time(10942),
    "total_elevation_gain": 443.1,
    "type": "Ride",
    "sport_type": "Ride",
    "id": 15910747780,
    "start_date_local": convert_date("2025-08-31T13:46:38Z"),
    "map": {
        "id": "a15910747780",
        "summary_polyline": "i}xjImphfHOpDVfI}AJmDhCu@_@Kb@HtAj@tCpG~Ql@hRO`@_B?{EyAgD}AwLg@iJH_jAjI_i@mCm[{BgIuIsDkFoA]yKpBSn@AhBqEhN_IaM_K_OgD}Ba@Au@`AiAf@sBX_A|FwOk@cBw@}AfAsD|GqBbB}ElHmBhEk@|B}@jCmBdCsArDqCbBu@vC_A|Aq@vC}AjAeBMa@`@iDlLgDbMOxD[z@_XbFqDzAeQrD{DfBqGvDqMvDmBrAiDr@UM{@eCwa@_b@yEsG_@_COeEL_[QyCaFgTuLgb@}CuRcCyIuAyLa@{QWs@XJBjFGqDU}@gB_@sAReAbBsBxJoB|@[_@a@eJJuFj@}DQa@PgDz@gEd@Eq@jA]nBOnEc@rDGpKvBb`@n@nQVv@EvCZlCAlAq@vBgCu@IjCZrB@~Bm@bC@lDDfBn@lDvBjDTfBrBfA~Dv@z@~@f@~CbAlAjBbAdAhB`HnDvA~CfBzGfC|@hBQ~@^l@lH|AhCne@hf@d@v@V|AB|q@y@dd@bD~d@?xIeMx~@qCb\\uAtF}Lpe@|@bB~[h\\bAtC|BlDrBdItAlRz@|@D~A[r@bF~u@hGvOjEtMdAfCRO}GnJa@tGsCbCpEtLIrBeTdMaAz@k@hBQ`DHvh@TnCJzMRrBOfCC|SjFQ?gAe@Ob@Lh@`BpB\\\\tBTpKL\\t@ENYIqBgAwGlAZTgALLKJJWMIPH]FJJXMURLBAc@}BT]k@Ts@lLo@f@]Jq@Pn@t@DvE[dAo@JqCk@yXZgCl`@yAh@[l@}A?_D?`D^^`GqAtBqDzBjACmBXsC~Ai@j@eAjBmHPuCdBaF~@cF|@sCv@`@\\yInD_JH{B`@mBtE{NjB}LvC}Gf@cDbDcKdAuBxCmL`BS`A`@`@~F@}ArAgAjDcB|AQ`BqAvMyDdDuBrN{R|TiYpA_AlEsAhBoBvFsIvEsE`DoBpEqAfB}BdFqR[uB@yKeAqM_Eu_AQ}XEwOf@eK_@wEeAiKfFuBhDE~LyH|CkC`EyAxEyFjByAzD_FrEiEpBiArAoCLLbAyA`GqFXqFIiBPeAlB}ArD_BpAwCnDeEEkA^s@NsAjAuBnAuJrBwEbB_Hd@yMdAsDMaGtCe@~FcKt@kEtMiMnAeDr@oDnC}G|@mGtCqEpBaHvCH~BgA`AiAViAf@}PNm@~HqJhEr@hCmA{CyNlA}DjFmFcA_HfCwBPdA]tAJd@b@`@",
        "resource_state": 2
    },
    "average_speed": convert_speed(3.621),
    "average_heartrate": 139,
    "max_heartrate": 169,
    "intensity_score": 0.7615,
    "target": 3,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "name": "Тренировка (вечер)",
    "distance": convert_distance(14925.8),
    "moving_time": convert_moving_time(4519),
    "total_elevation_gain": 94.9,
    "type": "Ride",
    "id": 15910746794,
    "start_date_local": convert_date("2025-08-26T18:18:22Z"),
    "map": {
        "id": "a15910746794",
        "summary_polyline": "_axjIcshfHMPq@ZKXL`BAxBH`ABHH@HIRu@NW`G{Fn@Of@J`A_@RBLLKGIAGQLCKq@A`@DTFPDWE@SaABYRm@`EsEpAgA|B_CPYTsAAm@qB{I{BoIyAcG]gB]iAC[HW\\]rAk@r@e@tAgAzCiBPi@?_Ah@k@VTJp@bBT~BElAe@\\?fGnCfAV~@b@\\Bn@m@p@]hAwAxA_@bBeARa@@YKeAQm@?OrAgARo@LSTEC?HPf@r@fAVh@?f@a@n@cAv@w@j@}@p@m@h@iAPm@Ju@V}CTq@d@c@lCkAfCa@\\F~AlCZ~AfAhEXN|@WN@LLl@`BZZ\\l@b@N\\OlCaDhA_Bx@u@|@kAb@_@nKu@rCCdIy@ZSNg@BsDj@ARHR^VBnAi@|Bk@hIwC^[bCeAt@M|A_AvCwA~EyAZAL\\LdBDdDHxARFf@KJIBISuA?kCIoBX`@IOADDjAe@KTg@Gs@PRCDWoAFSxO_GhCc@n@AfCg@l@Xr@CjDw@t@@FCFQh@@l@RBG?i@DK`AVLg@HGtDtB^KH@jDxBHIdAeIJyAf@{Cl@aDLQb@NzBhBjDjBlCjB|@\\jAjAf@ZT\\O^G~@Or@VoABm@IBB@BJGIJ?M@VEQHGGFK@SKa@qDaCc@EQWgA_AqAi@yFuDkAGSIWa@ICmB^k@GuBw@sBeAs@o@o@gAYSwCkAaBg@qAMcC@gCTiA\\yANoA`@eAD{Dv@qA?yB]aCMQVIn@F~GWC[h@m@ZaBHu@Ce@XkBb@q@QgBBqB}AYI}FVo@NOLEb@JnB@tB?dAEZ_Bj@w@NqBx@uALOLDrALdADfACdHNhEAdCH`D?dBM\\QN_Cd@qLr@kCh@_AMe@Nm@@s@Zq@ACSGEaAjCeA`AkDlE]PgAMw@kDQ_@U?y@^WMSc@cB_G_@q@UGm@j@u@lAoBjCoAtAuCpD_HbHe@XqAb@iJzDcAv@y@`@o@p@iBs@}Ae@gF}BOSSwACX[t@e@f@u@b@u@Dy@Sm@Aa@Q]]a@Ne@ESFU`@I^?tAERkAp@{E~CYTEVDb@r@tCvApF`D~NIV}@x@WBMIw@R[ElAKn@Db@e@NEx@fA^fBBh@QhA[j@mCvCmB|AoKzKiDdDm@~@K?Mw@AaCKgABQJUvA{AQLGKJBCJNJIDZk@^a@HU",
        "resource_state": 2
    },
    "average_speed": convert_speed(3.303),
    "average_heartrate": 105,
    "max_heartrate": 125,
    "intensity_score": 0.533,
    "target": 1,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "name": "Тренировка (после обеда)",
    "distance": convert_distance(21788.2),
    "moving_time": convert_moving_time(4019),
    "total_elevation_gain": 251.1,
    "type": "Ride",
    "id": 15910746494,
    "start_date_local": convert_date("2025-08-21T13:53:09Z"),
    "map": {
        "id": "a15910746494",
        "summary_polyline": "swniIyoifHLa@KaAiBaHqBmFo@eC_@KaAv@g@bAaAz@}J|EATZbD^pBTnDd@hC?`@STqDnA}ArAgCxAOXAV`@bAj@AzB_B`GiCVAL^ZfCtAzNh@xBpAdA|FnJ~GxJv@h@fEbArCCnD_A|@i@nBsBt@g@`Ee@vBuCj@WZZhDfInAlBTfABSW}@@eAj@uFzB}Jj@cBx@yA|AmBpAiAlCiDb@ObAT^YB[Oq@}MqXcBwCc@c@cDiFkIuN}DkFq@cBmA{Dd@qBz@{EdAmC`Da@`A]vD{B`DmAz@y@Do@QgA_H{SiBmGIu@vBqDjFqHdCwCxE{Gl@gBHiASoBi@mBE?@RTTh@zCIlBm@pB[n@gNvQqDrFOb@Ff@lKx\\Np@?r@c@h@gJdEuFxAYj@i@jByAfIhAbEb@bArAhB`CbCf@fAzCrEfAdCvDvF|@fBzIjOpF`MJh@A\\_@^w@Si@{B_BuCcGkLwDiFoAuBcBsA{DkHeA{CWg@uAwAi@UmBvJ{AnCe@dCO`Bc@nBg@tASbA_CxH[tBu@~HQXe@PaBNqAQQRw@zMq@bOGTO?yAaC_C{C}AgDmF_IpCwInD}I~D{M?iAc@{B_BwFeCiH]uBLq@rCwDh@aA`AkEDe@Ea@yDaGu@u@[FcBbBgBbAIZB^~AjFtApGXfCCn@MTcAp@s@rAg@b@{GtCwBrA?t@b@lCjAdK?x@{A~@gBt@aAz@cDnAMTAn@H\\RV|KwFhB_BhBgAdHoDX[FUCKMDeHfEeChAm@J_@Kk@qEe@kCuAaKkAeLk@cDDkAgAoH@s@`@sBNkGE_BUaCDWp@}@Jq@MeDS}AQ]QEWJS^Il@IfFQn@y@n@mBz@a@h@ChAb@zJLp@NPNAbBsAt@nBJAXe@ZeAFw@DyGYwD@UZq@C}AMGJVDC]DNCAYqBnCcDxAWd@Cr@\\lJNhAJVN@bBwARDlA`Df@nDp@nD\\jAN@dDeCxEuBnB{ATGLT|@`EbAfHM\\{@p@_AlAuL~FG\\\\jB`@jFn@hF?r@UT}Br@kCpBkCzAIb@Nl@`@FlCcBzC{ArE_DrDmB~CiAhAw@F]U@uDbBoGnDaACmA`@uBpAqEtBQX?t@F`@\\GjJ}EdBoAlJyErAcAHa@{DzAMAMY_BwK[kERo@dCyAj@{@t@i@\\CR\\~@tDHz@~@`CrBxGBx@e@pA",
        "resource_state": 2
    },
    "average_speed": convert_speed(5.421),
    "average_heartrate": 145,
    "max_heartrate": 176,
    "intensity_score": 0.778,
    "target": 3,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "name": "Вечерний забег",
    "distance": convert_distance(2713.4),
    "moving_time": convert_moving_time(1274),
    "total_elevation_gain": 19.3,
    "type": "Run",
    "id": 18567209351,
    "start_date_local": convert_date("2025-08-17T19:37:30Z"),
    "map": {
        "id": "a18567209351",
        "summary_polyline": "qvwjIq}hfH?`@l@UDROLERPp@BP@\\Qt@GLGDGNCAId@GFI?ADCZRh@?NIHB@OJwAfBy@f@UR[^Q`@a@ZSf@ILc@RMLKXSZQr@[VSZKh@AXDv@P~@@f@BLNPPN^h@Ph@Lp@f@n@LTHv@@\\Jp@Pj@PbADLVP^^m@OG@QLEA]oAGGI@c@XY^MDGE[[GMSUGQEc@Fi@AI[]{@aBYm@EEM?SXa@\\QRWPQV]Vi@p@IXYWU[WQKKGUg@o@Wc@AGBC?Ba@^An@DNN^FXGBb@f@XRZl@MDIFSVWj@KJEFEhAFnBYnBCdA?b@Bq@NkA@oAH{@DaAAi@DUPe@\\a@P_@h@c@d@s@x@}@jA}AHYBUAm@MgCCk@BUFKr@c@R]TI`@q@X[Py@PU\\u@\\WRYVi@Xa@j@oAPQn@_@^]RWf@Wn@o@DO@OEs@@KHYNQVWDMAQGUEw@Mk@QLAFVz@",
        "resource_state": 2
    },
    "average_speed": convert_speed(2.13),
    "average_heartrate": 165.1,
    "max_heartrate": 187.0,
    "intensity_score": 0.812,
    "target": 3,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "name": "Тренировка (после обеда)",
    "distance": convert_distance(3744.2),
    "moving_time": convert_moving_time(1511.0),
    "total_elevation_gain": 320.1,
    "type": "Ride",
    "id": 15910746495,
    "start_date_local": convert_date("2025-08-15T18:19:28Z"),
    "map": {
        "id": "a18567582378",
        "summary_polyline": "gzmiIkhifHNDFNJv@B`As@nIg@fFYdEMhAKvBIv@IvEBfBAnCDbBAHIN[R[f@UXo@^g@RqBVc@Jc@K_ABaBMw@OcAa@i@Ky@{@uBwDsAgBOO}@eBY]w@sAi@w@w@qAgAyAc@y@c@o@@MADm@aDY{CW_BSkB{@uFMuAM{@MgBW_CWwAGGOD?EAGBFDBLQb@iBFs@@cBCSMIOCK@GHAVAxFEn@EWCGEBAX@F@@BEJBMBD@M@?DB@HU@[@B@A@YCa@OoAKsAAw@m@iDOcBQ}@MsA[cCUiAU}@ASFSGcA_AmFSaGIaAAYFgAH[`@_@Tc@@QAkAKs@?WJUXSPSF_@GkCQoBOm@EIQIQJGHSh@ANIrCG~AG`@U\\_@\\aAXYL_@Vc@`@EJGVDf@RjBDdBFpA?n@NnANf@JDJC|@w@t@}@Na@?M?HEGDJFQIF@@",
        "resource_state": 2
    },
    "average_speed": convert_speed(5.1),
    "average_heartrate": 148.7,
    "max_heartrate": 176,
    "intensity_score": 0.913,
    "target": 4,
  },
]

class StravaFetchAllActivities:
  def __init__(self, strava_api_cls=StravaAPI):
    self.strava_api_cls = strava_api_cls
    
  def call(self, athlete_id):
    # только пользователь с таким id может перейти к своим тренировкам
    
    StravaSyncLastActivities().call()
    # получать тренировки из базы
    return activities
  
class StravaSyncLastActivities:
  def call(self):
    # получает из бд последнюю тренировку (либо если нет, то None)
    # получить токен из redis
    # отправляет запрос в strava на получение тренировок
      # туда отправляем промедуток времени (время последней тренировки в бд, текущее время)
      # все новые тренировки добавляем в бд
    self.predict_types()
    
  def predict_types(self):
    # отправляет запрос на api для классификации
    # обновляет записи в бд (добавляет target и intensity_score)
    pass
  
class StravaFetchOneActivity:
  def __init__(self, strava_api_cls=StravaAPI):
    self.strava_api_cls = strava_api_cls
    
  def call(self, athlete_id, activity_id):
    # только пользователь с таким id может перейти к своим тренировкам

    # получать данные из базы по конкретной тренировке 
    activity = [a for a in activities if str(a["id"]) == str(activity_id)].pop()
    return activity