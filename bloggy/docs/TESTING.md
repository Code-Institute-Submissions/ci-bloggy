# Bloggy - The home of blogs you love

![Bloggy logo](../static/img/logo.svg "Bloggy logo Logo")

## Testing

### 🛠 Home page and posts displaying

Once home page loads, users are presented with all posts on Bloggy. First 6 posts are present on page with pagination displayed at the bottom of the page for navigation to more posts.

### 🛠 Home page and posts searching

MongoDB text search is utilised to search the database based on user's query. Indexes are set up for *title*, *description* & *body* fields - hence, users can search for posts based on title, description or tags. 

Note that MongoDB is automatically ignoring 'stop' words, more on which can be read [here](https://docs.mongodb.com/manual/reference/operator/query/text/#stop-words). These can be disabled by creating an index but I've chosen not to disable them.

### 🛠 Home page posts sorting

Users are able to sort posts by date created (Most recent first/Oldest first), alphabetically (A-Z/Z-A) & by popularity by clicking on dropdown select menu under search field.

If users chooses to sort by most recent first, filter on database query is utilised to filter it by *last_updated* in descending order.

Similarly for oldest first, database query is utilised to filter it by *last_updated* in ascending order.

To sort by popularity, database query is used to filter results by *views* which is also displaying on post cards next to read time.




