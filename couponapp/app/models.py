#Models to be used in the application
from datetime import datetime
from app import mongo, Document

class User(Document):
	structure = {
		'id' : unicode,
		'name' : unicode,
		'email' : unicode,
		'created_dttime':datetime,
	}
	required_fields = ['id', 'name', 'email']
	default_values = {'created_dttime' : datetime.utcnow}
	use_dot_notation = True

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
	    return True

	@property
	def is_anonymous(self):
	    return False

	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)

	def __repr__(self):
		return '<User %r>' % (self.name)
