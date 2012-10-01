from django.db import models

class User( models.Model ):
	username = models.CharField( max_length = 80 )
	firstname = models.CharField( max_length = 80 )
	lastname = models.CharField( max_length = 80 )

	def __unicode__( self ):
		return self.username
	
class Status( models.Model ):
	statusdesc = models.CharField( max_length = 100 )

	def __unicode__( self ):
		return self.statusdesc
	
class Building( models.Model ):
	buildingdesc = models.CharField( max_length = 100 )

	def __unicode__( self ):
		return self.buildingdesc


class EventType( models.Model ):
	typedesc = models.CharField( max_length = 100 )

	def __unicode__( self ):
		return self.typedesc

class Ticket( models.Model ):
	name = models.CharField( max_length = 200 )
	room = models.CharField( max_length = 200 )
	building = models.ForeignKey( Building )
	probdesc = models.CharField( max_length = 5000 )
	submitdatetime = models.DateTimeField( auto_now_add = True )
	submitip = models.IPAddressField()
	status = models.ForeignKey( Status )
	assignee = models.ForeignKey( User )

class Comment( models.Model ):
	ticket = models.ForeignKey( Ticket )
	user = models.ForeignKey( User )
	date = models.DateTimeField( auto_now_add = True )
	comment = models.CharField( max_length = 5000 )
	
class Event( models.Model ):
	ticket = models.ForeignKey( Ticket )
	user = models.ForeignKey( User )
	date = models.DateTimeField( auto_now_add = True )
	type = models.ForeignKey( EventType )