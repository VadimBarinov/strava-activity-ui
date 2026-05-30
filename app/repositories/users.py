from app.domain.dtos import AthleteDto

class UsersRepository:
  def __init__(self, db_connection):
    self.connection = db_connection
    
  def fetch(self, id):
    cursor = self.connection.cursor()
    cursor.execute(
      """
      SELECT 
      id, username, firstname, lastname
      FROM users
      WHERE id = %s LIMIT 1;
      """,
      (id, )
    )
    user_record = cursor.fetchone()
    if user_record:
      user_dto = AthleteDto(
        id=user_record[0],
        username=user_record[1],
        firstname=user_record[2],
        lastname=user_record[3],
      )
      return user_dto
    
  def save(self, user_dto):
    cursor = self.connection.cursor()
    try:
      cursor.execute("BEGIN")
      cursor.execute(
        """
        INSERT INTO users (id, username, firstname, lastname) 
        VALUES (%s, %s, %s, %s);
        """,
        (
          user_dto.id,
          user_dto.username,
          user_dto.firstname,
          user_dto.lastname, 
        )
      )
      self.connection.commit()
    except Exception as e:
      self.connection.rollback()
      raise e