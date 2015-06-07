import media
import fresh_tomatoes

#Instances of the movie class where each instance corresponds to my favorite movie
dial_m_for_murder = media.Movie("Dial M for Murder",
                                "An ex-tennis pro who wants to have his wealthy wife murdered",
                                "http://upload.wikimedia.org/wikipedia/commons/4/48/Dial_M_For_Murder.jpg",
                                "https://www.youtube.com/watch?v=y1oPtCA2PWg")

good_bad_ugly = media.Movie("The Good the Bad and the Ugly",
                            "A mysterious stranger, a Mexican outlaw and a sadistic criminal on the hunt for a hidden treasure",
                            "http://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                            "https://www.youtube.com/watch?v=WCN5JJY_wiA")

lawrence_of_arabia = media.Movie("Lawrence of Arabia",
                                 "The adventure of British Lieutenant T.E. Lawrence in Arabia",
                                 "http://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Lawrence_of_arabia_ver3_xxlg.jpg/640px-Lawrence_of_arabia_ver3_xxlg.jpg",
                                 "https://www.youtube.com/watch?v=zmr1iSG3RTA")

back_to_the_future = media.Movie("Back to the Future",
                                 "A young man is accidentally sent 30 years int the past in a time-travelling car",
                                 "http://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

hotel_rwanda = media.Movie("Hotel Rwanda",
                           "The true story of a hotel manager who housed over a thousand refugees during the Rwandan genocide",
                           "http://upload.wikimedia.org/wikipedia/en/d/d5/Hotel_Rwanda_movie.jpg",
                           "https://www.youtube.com/watch?v=4dd8rX5Dy_Q")

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook and his accomplice in a Parisian restaurant",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=87q0RD5R4Us")

the_dark_knight = media.Movie("The Dark Knight",
                              "Batmans fight against a vile criminal called the Joker to protect Gotham city",
                              "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

fury_road = media.Movie("Mad Max: Fury Road",
                        "A warrior and a loner who try to outrun a tyrant and his army through the apocalyptic wasteland",
                        "http://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
                        "https://www.youtube.com/watch?v=hEJnMQG9ev8")

#Create a list of my favorite movies
my_movies = [dial_m_for_murder, good_bad_ugly, lawrence_of_arabia, back_to_the_future, toy_story, hotel_rwanda, ratatouille, the_dark_knight, fury_road]

#Open the list of my favorite movies in a HTML page
fresh_tomatoes.open_movies_page(my_movies)

