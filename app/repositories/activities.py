from app.domain.dtos import ActivityDto, MapDto, AthleteDto

class ActivitiesRepository:
  def __init__(self, db_connection):
    self.connection = db_connection
    
  def _select_all_by_user_id(self, user_id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT 
      id, user_id, name, start_date, start_date_local, type_id, distance, moving_time, average_speed, max_speed, total_elevation_gain,
      average_heartrate, max_heartrate, map_id, intensity_score, target
      FROM activities
      WHERE user_id = %s
      ORDER BY start_date DESC;
      """,
      (user_id, )
    )
    return cursor.fetchall()
    
  def _select_from_activities(self, id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT 
      id, user_id, name, start_date, start_date_local, type_id, distance, moving_time, average_speed, max_speed, total_elevation_gain,
      average_heartrate, max_heartrate, map_id, intensity_score, target
      FROM activities
      WHERE id = %s LIMIT 1;
      """,
      (id, )
    )
    return cursor.fetchone()
  
  def _select_from_activities_by_id_and_user_id(self, user_id, id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT 
      id, user_id, name, start_date, start_date_local, type_id, distance, moving_time, average_speed, max_speed, total_elevation_gain,
      average_heartrate, max_heartrate, map_id, intensity_score, target
      FROM activities
      WHERE id = %s AND user_id = %s LIMIT 1;
      """,
      (id, user_id, )
    )
    return cursor.fetchone()
  
  def _select_from_types(self, id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT 
      id, type
      FROM types
      WHERE id = %s LIMIT 1;
      """,
      (id, )
    )
    return cursor.fetchone()
  
  def _select_from_maps(self, id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT 
      id, summary_polyline
      FROM maps
      WHERE id = %s LIMIT 1;
      """,
      (id, )
    )
    return cursor.fetchone()
  
  def _mapping_records_to_dto(self, activity_record, type_record, map_record):
    return ActivityDto(
      id=activity_record[0],
      athlete=AthleteDto(id=activity_record[1]),
      name=activity_record[2],
      start_date=activity_record[3],
      start_date_local=activity_record[4],
      type=type_record[1],
      distance=activity_record[6],
      moving_time=activity_record[7],
      average_speed=activity_record[8],
      max_speed=activity_record[9],
      total_elevation_gain=activity_record[10],
      average_heartrate=activity_record[11],
      max_heartrate=activity_record[12],
      map=MapDto(id=map_record[0], summary_polyline=map_record[1]),
      intensity_score=activity_record[14],
      target=activity_record[15],
    )
    
  def fetch(self, id):
    activity_record = self._select_from_activities(id)
    if activity_record:
      type_record = self._select_from_types(activity_record[5])
      map_record = self._select_from_maps(activity_record[13])
      return self._mapping_records_to_dto(activity_record, type_record, map_record)
    
  def fetch_by_id_and_user_id(self, user_id, id):
    activity_record = self._select_from_activities_by_id_and_user_id(user_id, id)
    if activity_record:
      type_record = self._select_from_types(activity_record[5])
      map_record = self._select_from_maps(activity_record[13])
      return self._mapping_records_to_dto(activity_record, type_record, map_record)
    
  def fetch_all_by_user_id(self, user_id):
    activities_records = self._select_all_by_user_id(user_id)
    activities = []
    for activity_record in activities_records:
      type_record = self._select_from_types(activity_record[5])
      map_record = self._select_from_maps(activity_record[13])
      activities.append(
        self._mapping_records_to_dto(activity_record, type_record, map_record)
      )
    return activities
  
  def fetch_last_start_date_by_user_id(self, user_id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT start_date FROM activities 
      WHERE user_id = %s
      ORDER BY start_date DESC 
      LIMIT 1;
      """,
      (user_id, )
    )
    last_start_date_record = cursor.fetchone()
    if last_start_date_record:
      return last_start_date_record[0]
    
  def _save_map(self, map_dto):
    cursor = self.connection.cursor()
    try:
      cursor.execute("BEGIN")
      cursor.execute(
        """
        INSERT INTO maps (id, summary_polyline) 
        VALUES (%s, %s);
        """,
        (
          map_dto.id,
          map_dto.summary_polyline,
        )
      )
      self.connection.commit()
    except Exception as e:
      self.connection.rollback()
      raise e

  def _save_activity(self, activity_dto):
    cursor = self.connection.cursor()
    try:
      cursor.execute("BEGIN")
      cursor.execute(
        """
        INSERT INTO activities (id, user_id, name, start_date, start_date_local, type_id, distance, moving_time, average_speed, max_speed, total_elevation_gain,
        average_heartrate, max_heartrate, map_id, intensity_score, target) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
        (
          activity_dto.id,
          activity_dto.athlete.id,
          activity_dto.name,
          activity_dto.start_date,
          activity_dto.start_date_local,
          activity_dto.type,
          activity_dto.distance,
          activity_dto.moving_time,
          activity_dto.average_speed,
          activity_dto.max_speed,
          activity_dto.total_elevation_gain,
          activity_dto.average_heartrate,
          activity_dto.max_heartrate,
          activity_dto.map.id,
          activity_dto.intensity_score,
          activity_dto.target,
        )
      )
      self.connection.commit()
    except Exception as e:
      self.connection.rollback()
      raise e
    
  def save_with_map(self, activity_dto):
    self._save_map(activity_dto.map)
    self._save_activity(activity_dto)
    
  def update_intensity_score_and_target(self, id, intensity_score, target):
    cursor = self.connection.cursor()
    try:
      cursor.execute("BEGIN")
      cursor.execute(
        """
        UPDATE activities
        SET intensity_score = %s, target = %s
        WHERE id = %s;
        """,
        (
          intensity_score,
          target,
          id,
        )
      )
      self.connection.commit()
    except Exception as e:
      self.connection.rollback()
      raise e
