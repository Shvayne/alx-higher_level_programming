$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(response){
        response.results.forEach(function(film) {
            $('<li></li>').text(film.title).appendTo('#list_movies');
        });
    }
});