# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Q

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    
    #print type(post_list)
    #print post_list
    
    return HttpResponse(post_list )
    #return HttpResponse.Post


def post_detail(request, id, showComments=False):
    one_entry= Post.objects.get(id = id)
    comment= Comment.objects.get(id = id)#Comment.object.filter()
     
    allcontent = '<h1>'+one_entry.title +'</h1>' +'</br>'+ one_entry.body + '<p>'+ comment.body + '</p>'
    
    return HttpResponse(allcontent)
'''
   
    if showComments is not False:
	return HttpResponse(showComments)
    else:
	return HttpResponse("<h1> has no comments</h1>" % post_list)
    pass
'''
def post_search(request, term):
    search = Post.objects.filter(
	Q(title__icontains= term)|
	Q(body__icontains = term)
	Q(created__icontains = term))
    return HttpResponse(search)
'''
    term= request.GET.get('term')
    if term is not None:
	results = Post.objects.filter(
	    Q(title=term)|
            Q(body = term)).order_by('title')
	return render_to_response('results.html', {'results': results,}
    
context_instance = RequestContext( request ) )   
'''
def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 

