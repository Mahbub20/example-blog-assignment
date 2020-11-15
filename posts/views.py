from django.shortcuts import render
from django.http import response
import requests
import json

# POSTS VIEW ENDPOINT
def posts(request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    #print('response:',response[0])
    context = {'response':response}
    return render(request, 'blog-listing.html', context)

# POST DETAILS VIEW ENDPOINT
def post_details(request, post_id):
    response = requests.get("https://jsonplaceholder.typicode.com/posts/{}".format(post_id)).json()
    comments = requests.get("https://jsonplaceholder.typicode.com/posts/{}/comments".format(post_id)).json()
    #print('comments', comments)
    #print('response:',response[post_id ])
    #context = {'response':response[post_id-1]}
    context = {'response':response, 'comments':comments}
    return render(request, 'blog-post.html', context)
