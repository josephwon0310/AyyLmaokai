from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), index=True, unique=True)
    league_name = db.Column(db.String(25), index=True, unique=True)
    rank = db.Column(db.Integer, index=True)
    password = db.Column(db.String(256))
    looking_for_lower = db.Column(db.Boolean)
    looking_for_equal = db.Column(db.Boolean)
    looking_for_greater = db.Column(db.Boolean)

    #false if we wanna troll people lmao
    @property
    def is_authenticated(self):
        return True

    #false if we deleted accounts
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __repr__(self):
        if self.league_name is None:
            self.league_name = "hi"
        if self.password is None:
            self.password = "hi"
        return '{User #%d: SummonerName: %s, Email: %s, Password: %s}\n' % \
        (self.id, self.league_name, self.email, self.password)

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

class Snapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    snap_time = db.Column(db.Date)
    division = db.Column(db.Integer)
