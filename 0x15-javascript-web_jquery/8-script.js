$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    const movieTitles = data.results.map(function (movie) {
      return movie.title;
    });

    const listElement = $('UL#list_movies');

    $.each(movieTitles, function (index, title) {
      const listitem = $('<li>' + title + '</li>');
      listElement.append(listitem);
    });
  }
});
