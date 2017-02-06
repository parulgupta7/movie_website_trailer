import media
import fresh_tomatoes

# Function to get direct information of Movie details like
# title , rating , poster etc.
ZNMD = media.Movie("Zindagi Na Milegi Dobara",
                   "A story of three friends who just want to enjoy every" +
                   "single moment of their life..",
                   "http://www.minority-review.com/wp-content/uploads/2011" +
                   "/12/zindagi1.jpg",
                   "https://www.youtube.com/watch?v=ifIBOKCfjVs"
                   )

rockstar = media.Movie("Rockstar",
                       "A story of two people who loved each other uncondit" +
                       "ionally and boundlessly",
                       "http://harryjerry.com/wp-content/uploads/2011/10/" +
                       "rockstar-review.png",
                       "https://www.youtube.com/watch?v=bD5FShPZdpw"
                       )

three_idiots = media.Movie("3 Idiots",
                           "A story of three engineering students who gave" +
                           "the real meaning of education and life",
                           "http://www.media.glamsham.com/download/poster/" +
                           "images/3_idiots/3-idiots-05.jpg",
                           "https://www.youtube.com/watch?v=DHPuTiF9vdA"
                           )

fast_furious = media.Movie("Fast and Furious 8",
                           "A car racing movie.. Another chapter in fast and" +
                           "furious series",
                           "https://awesomemovieideas.files.wordpress.com/" +
                           "2015/07/furious8posterfinal.png",
                           "https://www.youtube.com/watch?v=uisBaTkQAEs"
                           )

punjabi = media.Movie("Goreyan Nu Daffa Karo",
                      "A comedian love story of a canadian girl and a" +
                      "punjabi boy",
                      "http://www.impawards.com/intl/india/2014/" +
                      "posters/goreyan_nu_daffa_karo_ver2.jpg",
                      "https://www.youtube.com/watch?v=fxV0bzCqrkM"
                      )

jab_we_met = media.Movie("Jab We Met",
                         "A story of a naughty punjabi girl and a serious" +
                         "boy who fell in love with each other in a train",
                         "https://www.movieposter.com/posters/archive/main" +
                         "/147/MPW-73729",
                         "https://www.youtube.com/watch?v=CnIQbVjLu84"
                         )

# Array of Movie objects is Created
movies = [ZNMD, rockstar, three_idiots, fast_furious, punjabi, jab_we_met]

# HTML page is requested
fresh_tomatoes.open_movies_page(movies)
