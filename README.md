# fledger 
A software library for the retrieval of public social Facebook data.

### Citing this software
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1310932.svg)](https://doi.org/10.5281/zenodo.1310932)  

## Usage
A Facebook API token is necessary to use the Facebook API.  
Put this token (or multiple tokens, one per line) inside a file and name the file `.tokens.txt`. This token will allow access to data on Facebook, including your personal Facebook data if you created a personal token. Beware of accidentally sharing the token.  

### Fetch a post
```
import fledger  

post = fledger.fetch_post(post_id)
```

### Fetch all comments on a post
```
import fledger

post = fledger.fetch_post(post_id)
post["comments"] = fledger.extract_comments_for_post(post)
```

#### Note
The structure of the objects returned by calls to `fetch_post` are highly similar to the `json` response from the Facebook API.
