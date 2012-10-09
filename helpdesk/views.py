from django.shortcuts import render_to_response

def newticket( request ):
	return render_to_response( 'newticket.html' )

