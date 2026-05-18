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
    "distance":convert_distance(3000),
    "moving_time": convert_moving_time(100),
    "average_speed": convert_speed(6.7), 
    "total_elevation_gain": 300, 
    "average_heartrate": 140,
    "max_heartrate" : 178,
    "map": { # будет отдельной сущностью в бд
      "id": "456",
      "summary_polyline": "i{wjI{xhfHHWPM~@CZFZd@Pd@Jj@APsClDiDvCu@x@[n@UjAu@dAYjAe@r@Ql@?PTp@Lv@vAnFBLANe@AkA_@mAQUDyC|Di@l@iB`CKTCV?fAGvBQnD_@bFGZMb@KN_@VWXk@\\u@FcAAi@^u@IKBKHK\\m@pCe@zAa@|@oAhBc@|@Or@]xCS~@s@xB{AxCm@dDmAdDOVi@l@sBlBwCvCoA~Ay@h@QPUj@SjBQp@wFxJQNe@LaABKHCP?rAEz@DpAMl@g@~@K^CXBvAAl@IlBOfBEfBGj@O|@mAbFUn@cA~A[`A_AjFOhBI`@BB{@~AUnAYr@CVFp@CL_B`CqBnBiApBgD|AkAz@QTI^Kp@BlAIbFKr@OXcCdCsAv@y@j@y@fAa@dAW\\eAr@aA`@g@j@aAr@n@a@z@aAz@e@nA}@PYX_AJQfBaBjAo@|@iArAoAJYF_@N{ABgBIkBP{AFDFNEOxAgA`@g@`Bc@f@URY`@aAPQh@{@zA_B|@}ADWCe@@]Vs@LgAbAiBNk@NwBJy@TmANuAn@aBn@m@f@y@`@aBn@iDN{AR_DJiD?oBLg@d@_ANs@CiA@u@CkABa@NKzACLEPQnByDjAmB\\a@Vo@L[He@VeCPc@x@a@dA{@xAcBhA_A`@g@n@k@^Yn@{@b@u@n@eBj@yBHECA@MLu@\\s@`@mAv@kBf@}BVcCLm@f@eArAaB\\o@j@aBr@gDL[HIJAx@ZP@FGHc@FI~@@l@Ix@i@P[d@a@Zo@EJFm@VmFLsADcCL}BH]`BgCxBaCvAkBNAp@HdBf@n@@wAgFk@_CC_@DSJYh@w@ZgAr@{@RqAVk@PWtEcFvCmClJsJdA_Ar@w@J[Hw@Ao@WkAo@sAa@oAEWBK\\a@Fi@f@o@n@o@HAPHNGhAqAlBkB|AyBt@q@bBkBvAcAd@m@zBwBh@o@rCmCj@YBISYEUGgAFY`@{@p@eAd@gAVa@TOjAUZMPWB][dAQLy@XkA|@qAzBYt@Gd@@bADLLR?Pe@JmHxHcEvD_BbB_AjAoExEQJk@AYXo@~@Ox@[b@APT~@t@xAf@nB?RCVIh@KTqI~ImBfBMBMEIQKe@MQ[_AIIMDSXCJ?LTx@FDEaBdCeAB@TY?c@E^",
      "resource_state": 2
    },
    "intensity_score": 0.57,
    "target": 2,
  },
  {
    "athlete": {
      "id": 123,
      "name": "Вадим Баринов",
    },
    "id": 2,
    "name": "Тренировка (после обеда)",
    "start_date_local": convert_date("2025-09-22T17:54:39Z"),
    "type": "Run",
    "distance":convert_distance(3000),
    "moving_time": convert_moving_time(100),
    "average_speed": convert_speed(6.7), 
    "total_elevation_gain": 300, 
    "average_heartrate": 140,
    "max_heartrate" : 178,
    "map": {
      "id": "123",
      "summary_polyline": "i{wjI{xhfHHWPM~@CZFZd@Pd@Jj@APsClDiDvCu@x@[n@UjAu@dAYjAe@r@Ql@?PTp@Lv@vAnFBLANe@AkA_@mAQUDyC|Di@l@iB`CKTCV?fAGvBQnD_@bFGZMb@KN_@VWXk@\\u@FcAAi@^u@IKBKHK\\m@pCe@zAa@|@oAhBc@|@Or@]xCS~@s@xB{AxCm@dDmAdDOVi@l@sBlBwCvCoA~Ay@h@QPUj@SjBQp@wFxJQNe@LaABKHCP?rAEz@DpAMl@g@~@K^CXBvAAl@IlBOfBEfBGj@O|@mAbFUn@cA~A[`A_AjFOhBI`@BB{@~AUnAYr@CVFp@CL_B`CqBnBiApBgD|AkAz@QTI^Kp@BlAIbFKr@OXcCdCsAv@y@j@y@fAa@dAW\\eAr@aA`@g@j@aAr@n@a@z@aAz@e@nA}@PYX_AJQfBaBjAo@|@iArAoAJYF_@N{ABgBIkBP{AFDFNEOxAgA`@g@`Bc@f@URY`@aAPQh@{@zA_B|@}ADWCe@@]Vs@LgAbAiBNk@NwBJy@TmANuAn@aBn@m@f@y@`@aBn@iDN{AR_DJiD?oBLg@d@_ANs@CiA@u@CkABa@NKzACLEPQnByDjAmB\\a@Vo@L[He@VeCPc@x@a@dA{@xAcBhA_A`@g@n@k@^Yn@{@b@u@n@eBj@yBHECA@MLu@\\s@`@mAv@kBf@}BVcCLm@f@eArAaB\\o@j@aBr@gDL[HIJAx@ZP@FGHc@FI~@@l@Ix@i@P[d@a@Zo@EJFm@VmFLsADcCL}BH]`BgCxBaCvAkBNAp@HdBf@n@@wAgFk@_CC_@DSJYh@w@ZgAr@{@RqAVk@PWtEcFvCmClJsJdA_Ar@w@J[Hw@Ao@WkAo@sAa@oAEWBK\\a@Fi@f@o@n@o@HAPHNGhAqAlBkB|AyBt@q@bBkBvAcAd@m@zBwBh@o@rCmCj@YBISYEUGgAFY`@{@p@eAd@gAVa@TOjAUZMPWB][dAQLy@XkA|@qAzBYt@Gd@@bADLLR?Pe@JmHxHcEvD_BbB_AjAoExEQJk@AYXo@~@Ox@[b@APT~@t@xAf@nB?RCVIh@KTqI~ImBfBMBMEIQKe@MQ[_AIIMDSXCJ?LTx@FDEaBdCeAB@TY?c@E^",
      "resource_state": 2
    },
    "intensity_score": 0.77,
    "target": 1,
  }
]

class StravaFetchAllActivities:
  def __init__(self, strava_api_cls=StravaAPI):
    self.strava_api_cls = strava_api_cls
    
  def call(self, athlete_id):
    # только пользователь с таким id может перейти к своим тренировкам
    
    # получать тренировки из базы
    
    StravaSyncLastActivities().call()
    
    # еще на странице должна быть кнопка синхронизации (тянет данные со strava api и подсчитывает target)
    # это будет асинхронная джоба
    # так же ее запускать при каждом заходе на страницу (не забываем про ограничения по запросам в strava api)
    return activities
  
class StravaSyncLastActivities:
  def call(self):
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