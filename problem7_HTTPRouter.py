"""
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.


First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
"""

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        
        curr_node = self.root
        for p in path:
            if p not in curr_node.children:
                curr_node.insert(p)
            curr_node = curr_node.children[p]
        
        curr_node.handler = handler
        
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr_node = self.root

        for p in path:
            if p not in curr_node.children:
                curr_node.insert(p)
            curr_node = curr_node.children[p]
        if curr_node.handler:
            return curr_node.handler
        else:
            return "Not found handler"

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}
    
    def insert(self, sub_path):
        # Insert the node as before
        self.children[sub_path] = RouteTrieNode()
    
    def __repr__(self):
        return str(self.children)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        sub_paths = self.split_path(path)
        self.route_trie.insert(sub_paths , handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        sub_paths = self.split_path(path)
        return  self.route_trie.find(sub_paths)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == "/":
            return []
        #removing "/" from both ends
        path = path.strip('/')
        sub_paths = path.split('/')

        return sub_paths


# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/test/case/one", "test case one handler")  # add a route
router.add_handler("/test/case/one/nested/", "test case one nested handler")  # add a route
router.add_handler("/test/case/two", "test case two handler")  # add a route
router.add_handler("/test/case/three", "test case three handler")  # add a route


# Regular test cases
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/test")) # should print 'Not found handler' or None if you did not implement one
print(router.lookup("/test/case/one")) # should print 'test case one handler'
print(router.lookup("/home/about")) # should print 'Not found handler' or None if you did not implement one
print(router.lookup("/test/case/one/nested")) # should print 'test case one nested handler' or None if you did not implement one


# Edge test cases

# Extra slashes
print(router.lookup("/test/")) #should print 'Not found handler' or None if you did not implement one
print(router.lookup("/test/case/one/nested/")) # should print 'test case one nested handler' or None if you did not implement one

# Empty path
print(router.lookup("")) #should print 'Not found handler' or None if you did not implement one