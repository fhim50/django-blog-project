# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response


from models import Post, Comment 


def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))


def post_detail(request, id, showComments=False):
    post = Post.objects.get(id = id)
    comments = post.comment_set.all()
    return render_to_response('blog/post_detail.html',{'post':post,'comments':comments})
'''
    one_entry= Post.objects.get(id = id)
    comment= Comment.objects.get(id = id)#Comment.object.filter()
    comments = one_entry.comment_set.all()
     
    allcontent = '<title>blog</title>'+'<h1>'+one_entry.title +'</h1>' +'</br>'+ one_entry.body + '<p>'+ comment.body + '</p>' 
    new_comments=[]
    for i in comments:
	new_comments+=i.body
    return HttpResponse(new_comments)
    #return HttpResponse(allcontent)
    

g
   
    if showComments is not False:
	return HttpResponse(showComments)
    else:
	return HttpResponse("<h1> has no comments</h1>" % post_list)
    pass
'''
def post_search(request, term):
    search = Post.objects.filter(
	Q(title__icontains= term)|
	Q(body__icontains = term))
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
   return render_to_response('blog/base.html',{})

