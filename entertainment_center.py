# -*- coding: cp1252 -*-
import media
import fresh_tomatoes

# Criando instancias da classe Movie

toy_story = media.Movie("Toy Story",
                        "Um garoto tem brinquedos que ganham vida",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/"
                        "Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Um oficial em um planeta alien",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

rplayer_one = media.Movie("Ready Player One",
                          "A virtual reality game that changes the world",
                          "https://upload.wikimedia.org/wikipedia/pt/d/d4/"
                          "Ready_Player_One_%28filme%29.png",
                          "https://www.youtube.com/watch?v=cSp1dM2Vj48")

ratatouille = media.Movie("Ratatouille",
                          "Um rato que é chefe em Paris",
                          "https://upload.wikimedia.org/wikipedia/pt/8/82/"
                          "Ratatouille_p%C3%B4ster.jpg",
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")

school_of_rock = media.Movie("Escola do Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/pt/1/1b/"
                             "Schoolrockposter.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

harry_potter = media.Movie("Harry Potter e a Pedra Filosofal",
                           "Um jovem bruxo que entra no mundo da magia",
                           "http://br.web.img3.acsta.net/c_215_290/medias/nmedia"
                           "/18/95/59/60/20417256.jpg",
                           "https://www.youtube.com/watch?v=CLJv2Qi98jU")

# Criando lista de filmes
movies = [toy_story, avatar, rplayer_one, ratatouille,
          school_of_rock, harry_potter]
# Chamando a funcao que abre a pagina html referente a minha lista de filmes
fresh_tomatoes.open_movies_page(movies)
