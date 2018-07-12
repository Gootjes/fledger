import fledger

oi = "pageID_postID"

#Fetch a post based on the post's identifier
post = fledger.fetch_post(oi)

#Fetch all comments
post["comments"] = list(fledger.extract_comments_for_post(post))

