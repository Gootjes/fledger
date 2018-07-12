from fledger.access import AccessManager
from fledger.options import *
from fledger.data import complete, Page

access_manager = AccessManager()

from fledger.logger import *


def fetch_posts(page_id, amount = 99999999, post_options=PostOptions(), reaction_options=ReactionOptions(), comment_options=CommentOptions(), subreaction_options=ReactionOptions(), subcomment_options=CommentOptions()):
    
    url=build_url(page_id+"/posts", post_options, reaction_options, comment_options, subreaction_options, subcomment_options)
    result = access_manager.make_request(url)

    #posts = []

    if result.code != 200:
        raise Exception("Error: {}".format(result.code))

    return result.content
    
    #return posts

def extract_posts(posts, amount = 99999999):
    count = 0

    page=result.content

    while count < amount:

        for post in page["data"]:
            #debug(post["id"])
            if "data" in post:
                for key in post["data"].keys():
                    complete(post["data"][key], access_manager) #["comments"]
            count+=1
            yield post
            if count > amount - 1:
                return
            #posts.append(post)
            #if len(posts) > amount - 1:
                #return posts

        p = Page(page)
        if p.has_next():
            page = p.next(access_manager).page
        else:
            debug("No more posts")
            break    

import json

def fetch_post(post_id, post_options=PostOptions(), reaction_options=ReactionOptions(), comment_options=CommentOptions(), subreaction_options=ReactionOptions(), subcomment_options=CommentOptions()):
    
    url=build_url(post_id, post_options, reaction_options, comment_options, subreaction_options, subcomment_options)
    result = access_manager.make_request(url)

    if result.code != 200:
        raise Exception("Error: " + result.code)

    return result.content

### Not finished yet.
def fetch_object(obj_id, options={}):
    pass

def extract(obj, key, limit=pow(2,31), recurse = True):

    count = 0

    page = obj[key]

    if not "data" in page:
        raise Exception("Not a paging type")

    while count < limit:

        for item in page["data"]:
            if recurse:
                if isinstance(item, dict):
                    if key in item.keys():
                        extract(item, key, limit, recurse)
            count+=1
            yield item

            if count > limit - 1:
                return

        p = Page(page)
        if p.has_next():
            page = p.next(access_manager).page
        else:
            debug("No more pages")
            break

def extract_comments_for_post(post, amount=pow(2,31), include_subcomments=True):

    count = 0

    page = post["comments"]

    while count < amount:

        for comment in page["data"]:
            #debug(comment["id"])
            if "comments" in comment:
                #complete(comment["comments"], access_manager)
                comment["comments"]=list(extract_subcomments_for_comment(comment))
                    
            count+=1
            yield comment
            if count > amount - 1:
                return

        p = Page(page)
        if p.has_next():
            page = p.next(access_manager).page
        else:
            debug("No more comments")
            break    

def extract_subcomments_for_comment(post, amount=pow(2,31)):
    
    count = 0

    page = post["comments"]

    while count < amount:

        for comment in page["data"]:
            #debug(comment["id"])
            #if "comments" in comment:
                #complete(comment["comments"], access_manager)
                    
            count+=1
            yield comment
            if count > amount - 1:
                return

        p = Page(page)
        if p.has_next():
            page = p.next(access_manager).page
        else:
            debug("No more comments")
            break  
