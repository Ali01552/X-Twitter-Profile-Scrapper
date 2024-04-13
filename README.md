# X-Twitter-Profile-Scrapper
Scrape the text from the latest 100 posts on any twitter profile

This script retrieves tweets from an API, possibly Twitter's API. It utilizes the `requests` library to make the request.

##It will request input of: 
1- The API-URL of the UserTweets request <you can find it from DevTools
2- The 'x-guest-token' of the UserTweets request <you can find it from DevTools in the headers
3- The 'x-client-transaction-id' of the UserTweets request <you can find it from DevTools in the headers

###it will output the results as a json file

###Then parse it to extract the information we need and ask as to choose a file name for the csv file it will put the data into
