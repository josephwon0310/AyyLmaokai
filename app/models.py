from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String(25), index=True, unique=True)
    password = db.Column(db.String(256), index=True, unique=True)
    rank = db.Column(db.Integer, index=True)

    #false if we wanna troll people lmao
    @property
    def is_authenticated(self):
        return True

    #false if we deleted accounts
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous
        return False

    def __repr__(self):
        return '{User #%d: SummonerName: %s, Rank: %d}\n' % \
        (self.id, self.league_name, self.rank)

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
