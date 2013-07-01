
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from message.models import message
from message.forms import messageform
from django.core.urlresolvers import reverse


from django.core.context_processors import csrf
def message_view(request):	
 		message_all = message.objects.all()
		if request.method == 'POST':
       			form = messageform(request.POST or None)
			if form.is_valid():
   				m=form.save()  
				m.save()
				return HttpResponseRedirect('')
		else:
       			 form = messageform()
		return render_to_response('message.html',{'body_message':form,'all_entries': message_all},context_instance=RequestContext(request))
		



