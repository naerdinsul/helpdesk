from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

class TicketForm( forms.Form ):
	BUILDINGS = (
		('NA', '-- Select a building --'),
		('PWES', 'Portsmouth West Elementary School'),
		('PWMS', 'Portsmouth West Middle School'),
		('PWHS', 'Portsmouth West High School'),
		('BO', 'District Board Office'),
	)
	name = forms.CharField( label='Name:' )
	room = forms.CharField( label='Room Number:' )
	building = forms.ChoiceField( label='Building:', choices=BUILDINGS )
	problem = forms.CharField( label='Problem Description:', widget=forms.Textarea )

def newticket( request ):
	if request.method == 'POST':
		form = TicketForm( request.POST )
		if form.is_valid():
			#
			# Process and save ticket HERE
			#
			return HttpResponseRedirect( '/thanks/' )
	else:
		form = TicketForm()
	
	return render( request, 'newticket.html', {
		'form': form,
	})

def thanks( request ):
	return render( request, 'thanks.html', {} )